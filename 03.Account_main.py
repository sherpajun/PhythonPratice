import pickle,os
from  Account import Account

account_list=[]
# account_list 불러오기
dir = os.path.dirname(__file__)+'/account.pickle'
print(dir)

with open(dir,'rb') as f:
    account_list = pickle.load(f)

Account.account_count = account_list[-1].account_number

while True:
    display = '''
----------------------------------------------------------------------
1. 계좌개설  2. 입금  3. 출금  4. 계좌로그  5. 계좌정보  6. 종료   
----------------------------------------------------------------------
>>>  '''
    menu = input(display)
    if menu == '1':
        name=input('이름 >>> ')
        balance=''
        while not balance.isdecimal():
            balance= input("입금금액 >>>")
        balance = int(balance)
        account_list.append(Account(name,balance))
        print('-------------------')
        for item in account_list:
            print(item)
    elif menu =='2':
        account_num = int(input('계좌번호 입력하세요 >>> '))
        check = 0
        for acc in account_list:
            if acc.account_number == account_num:
                check = 1 
                amount =int(input('입금 금액 >>> '))
                acc.deposit(amount)
        if check == 0:
            print('계좌번호가 없습니다.')
    elif menu == '3':
        account_num = int(input('계좌번호 입력하세요 >>> '))
        check = 0
        for acc in account_list:
            if acc.account_number == account_num:
                check = 1 
                amount =int(input('출금 금액 >>> '))
                acc.withdraw(amount)
        if check == 0:
            print('계좌번호가 없습니다.')
    elif menu == '4':
        account_num = int(input('계좌번호를 입력하세요 >>> '))
        check = 0
        for acc in account_list:
            if acc.account_number ==account_num:
                check = 1
                for data in acc.total_log:
                    print(data[0],' : ',data[1])
        if check == 0:
            print('계좌번호가 없습니다.')
    elif menu == '5':
        for acc in account_list:
            print(acc)
        account_num = int(input('계좌번호를 입력하세요 >>> '))
        check = 0
        for acc in account_list:
            if acc.account_number ==account_num:
                check = 1
                print(acc)
        if check == 0:
            print('계좌번호가 없습니다.')
    elif menu =='6':
        ## account_list 저장
        with open(dir,'wb') as f:
            pickle.dump(account_list,f)
        print('프로그램 종료!')
        break
    
