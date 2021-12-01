import os
import sys
import time

#import pymssql
#from machbaseAPI.machbaseAPI import machbase


def call_db_info():
    dbFileName = 'db/db.conf'

    try:
        db_obj = open(dbFileName, 'r')

        server = db_obj.readline().rstrip()
        database = db_obj.readline().rstrip()
        username = db_obj.readline().rstrip()
        password = db_obj.readline().rstrip()

        return server, database, username, password

    except Exception as e:
        print('Error: Failed to read db.conf')
        sys.exit()


def connect_to_database():
    # MSSQL 접속
    cnxn = #pymssql.connect(server, username, password, database)
    cur = cnxn.cursor()

    return cur


def show_tables(cursor):
    cursor.execute('select * from information_schema.tables;')

    while True:
        row = cursor.fetchone()

        if row:
            print('TABLE_CATALOG: ' + row[0])
            print('TABLE_SCHEMA: ' + row[1])
            print('TABLE_NAME: ' + row[2])
            print()

        else:
            break


def get_data_columns(cursor, tb_name):
    cursor.execute("SELECT LOWER(A.COLUMN_NAME) "
                   "FROM INFORMATION_SCHEMA.COLUMNS A WHERE A.TABLE_NAME = '{}'".format(tb_name))

    columns_list = []

    while True:
        row = cursor.fetchone()

        if row:
            columns_list.append(row[0])

        else:
            break

    return columns_list


def get_data_types(cursor, tb_name):
    cursor.execute("SELECT DATA_TYPE "
                   "FROM INFORMATION_SCHEMA.COLUMNS A WHERE A.TABLE_NAME = '{}'".format(tb_name))

    columns_list = []

    while True:
        row = cursor.fetchone()

        if row:
            columns_list.append(row[0])

        else:
            break

    return columns_list


def change_data_types(data_types):
    change_table = {'numeric': 'INTEGER', 'real': 'DOUBLE', 'smallint': 'INTEGER',
                    'varchar': 'VARCHAR(100)', 'int': 'INTEGER', 'bit': 'INTEGER',
                    'decimal': 'INTEGER'}
    changed_data_types = []

    for dt in data_types:
        if dt in change_table:
            changed_data_types.append(change_table[dt])

        else:
            changed_data_types.append(dt)

    return changed_data_types


def find_index(column_list, find_list):
    index_list = {}

    for col in find_list:
        index_list[col] = column_list.index(col)

    return index_list


def call_mdb_info():
    dbFileName = 'db/mach_db.conf'

    try:
        db_obj = open(dbFileName, 'r')

        server = db_obj.readline().rstrip()
        user_name = db_obj.readline().rstrip()
        user_pw = db_obj.readline().rstrip()
        port = db_obj.readline().rstrip()

        return server, user_name, user_pw, port

    except Exception as e:
        print('Error: Failed to read mach_db.conf')
        sys.exit()


def mach_connect(server, user_name, user_pw, port):
    db = #machbase()

    if db.openEx(server, user_name, user_pw, port, 'SHOW_HIDDEN_COLS=1;CONNECTION_TIMEOUT=30') == 0:
        print('Error: Failed to connect machbase')
        sys.exit()

    return db


def drop_mach_table(tb_name):
    db.execute('drop table {}'.format(tb_name))
    print(db.result())


def create_mach_table(tb_name, columns, data_types):
    query = 'create TABLE {} ('.format(tb_name)

    for col_name, data_type in zip(columns, data_types):
        query += col_name + ' ' + data_type + ','

    query = query[: -1] + ');'

    if db.execute(query) == 0:
        return db.result()
    db.result()


def data_insert_to_mach(insert_list):
    while True:
        for tb_name, time_stamp, columns, data_types in insert_list:
            if time_stamp:
                cursor.execute('select * from {} where {}=(select max({}) from {});'
                               .format(tb_name, time_stamp, time_stamp, tb_name))

            else:
                cursor.execute('select * from {}'.format(tb_name))
            # print(columns)
            # print(data_types)
            # print(len(data_types))
            row = cursor.fetchone()

            sql = "INSERT INTO {} VALUES (".format(tb_name)

            for data, data_type in zip(row, data_types):
                if data_type == 'datetime':
                    if data is None:
                        data = '2021-01-01 00:00:00'
                    else:
                        data = str(data)[:19]
                    sql += "TO_DATE('{}', 'YYYY-MM-DD HH24:MI:SS')".format(data)
                else:
                    if data_type not in ['INTEGER', 'DOUBLE']:
                        sql += "'"

                    if data is None:
                        sql += "0"

                    else:
                        if data in [True, False]:
                            sql += '1' if data else '0'
                        else:
                            sql += str(data)

                    if data_type not in ['INTEGER', 'DOUBLE']:
                        sql += "'"

                sql += ', '

            sql = sql[:-2]
            sql += ")"

            if db.execute(sql) == 0:
                print(tb_name, db.result())
                sys.exit()
            else:
                print(tb_name, db.result())

        time.sleep(5)


if __name__ == '__main__':
    server, database, username, password = call_db_info()
    cursor = connect_to_database()
    # show_tables(cursor)

    shot_data_columns = get_data_columns(cursor, 'shot_data')
    shot_data_rec_columns = get_data_columns(cursor, 'shot_data_rec')
    mct_tmp_data_columns = get_data_columns(cursor, 'TB_MC_MT_MECHIF_M_TMP')
    op_data_columns = get_data_columns(cursor, 'TB_MC_MT_MECHIF_NONOP')
    state_data_columns = get_data_columns(cursor, 'TB_MC_MT_MECHIF_STATE')
    pct_data_columns = get_data_columns(cursor, 'TB_FM_PCT')
    mct_data_columns = get_data_columns(cursor, 'TB_FM_MCT')

    shot_data_types = get_data_types(cursor, 'shot_data')
    shot_data_rec_types = get_data_types(cursor, 'shot_data_rec')
    mct_tmp_data_types = get_data_types(cursor, 'TB_MC_MT_MECHIF_M_TMP')
    op_data_types = get_data_types(cursor, 'TB_MC_MT_MECHIF_NONOP')
    state_data_types = get_data_types(cursor, 'TB_MC_MT_MECHIF_STATE')
    pct_data_types = get_data_types(cursor, 'TB_FM_PCT')
    mct_data_types = get_data_types(cursor, 'TB_FM_MCT')
    # print(set(shot_data_types + mct_data_types + op_data_types + mct_data_types))

    shot_data_types = change_data_types(shot_data_types)
    shot_data_rec_types = change_data_types(shot_data_rec_types)
    mct_tmp_data_types = change_data_types(mct_tmp_data_types)
    op_data_types = change_data_types(op_data_types)
    state_data_types = change_data_types(state_data_types)
    pct_data_types = change_data_types(pct_data_types)
    mct_data_types = change_data_types(mct_data_types)

    m_server, m_user_name, m_user_pw, m_port = call_mdb_info()
    db = mach_connect(m_server, m_user_name, m_user_pw, m_port)

    # drop_mach_table('shot_data')
    # drop_mach_table('shot_data_rec')
    # drop_mach_table('TB_MC_MT_MECHIF_M_TMP')
    # drop_mach_table('TB_MC_MT_MECHIF_NONOP')
    # drop_mach_table('TB_MC_MT_MECHIF_STATE')
    # drop_mach_table('TB_FM_PCT')
    # drop_mach_table('TB_FM_MCT')
    # create_mach_table('shot_data', shot_data_columns, shot_data_types)
    # create_mach_table('shot_data_rec', shot_data_rec_columns, shot_data_rec_types)
    # create_mach_table('TB_MC_MT_MECHIF_M_TMP', mct_tmp_data_columns, mct_tmp_data_types)
    # create_mach_table('TB_MC_MT_MECHIF_NONOP', op_data_columns, op_data_types)
    # create_mach_table('TB_MC_MT_MECHIF_STATE', state_data_columns, state_data_types)
    # create_mach_table('TB_FM_PCT', pct_data_columns, pct_data_types)
    # create_mach_table('TB_FM_MCT', mct_data_columns, mct_data_types)

    data_insert_to_mach([
        ['shot_data', 'timestamp', shot_data_columns, shot_data_types],
        ['shot_data_rec', 'timestamp', shot_data_rec_columns, shot_data_rec_types],
        ['TB_MC_MT_MECHIF_M_TMP', 'iftime', mct_tmp_data_columns, mct_tmp_data_types],
        ['TB_MC_MT_MECHIF_NONOP', 'iftime', op_data_columns, op_data_types],
        ['TB_MC_MT_MECHIF_STATE', '', state_data_columns, state_data_types],
        ['TB_FM_PCT', '', pct_data_columns, pct_data_types],
        ['TB_FM_MCT', '', mct_data_columns, mct_data_types]
    ])
