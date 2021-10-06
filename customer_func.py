import re
def insertData(custlist):
        customer={'name': '', 'gender': '', 'email': '', 'birthyear': ''}
        
        customer['name']=input('이름 >>> ')

        while True:
            customer['gender']=input('성별(M,F) >>> ').upper()
            if customer['gender'] in ('M','F'):
                break

        while True:
            email_p = re.compile('^[a-z][a-z0-9]{4,}@[a-z]{2,6}[.][a-z]{2,5}$')
            while True:
                customer['email'] = input('이메일 >>> ')
                if email_p.match(customer['email']):
                    break
                else:
                    print('이메일을 정확하게 입력해주세요!!')
            
            check = 0 
            for i in custlist:
                if i['email'] == customer['email']:
                    check=1
            if check==0:
                break
            print('중복되는 이메일이 있습니다.')

        while True:
            customer['birthyear'] = input('생년월일(4자리) >>> ')
            if len(customer['birthyear']) == 4 and customer['birthyear'].isdigit():
                break

        custlist.append(customer)
        page =len(custlist)-1
        print(custlist)
        print(page)

def curSearch(custlist,page):
    if page < 0:
        print('입력된 정보가 없습니다.')
    else:
        print(f'현재 페이지는 {page}페이지 입니다.')
        print(custlist[page])

def preSearch(custlist,page):
    if page <= 0:
        print('첫번째 페이지입니다.')
        print(page)
    else:
        page -= 1
        print(f'현재 페이지는 {page}페이지 입니다.')
        print(custlist[page])   
    return page

def nextSearch(custlist,page):
    if page >= len(custlist)-1:
        print('마지막 페이지입니다.')
        print(page)
    else:
        page += 1
        print(f'현재 페이지는 {page}페이지 입니다.')
        print(custlist[page])
    return page

def updateData(custlist):
    while True:
        choice1 = input('수정하려는 이메일주소를 입력하세요 >>> ')
        idx =-1
        for i in range(len(custlist)):
            if custlist[i]['email'] == choice1:
                idx = i
                break
        if idx == -1:
            print('등록되지 않은 이메일 입니다.')
            break
        choice2 = input('''
-------------------------------------------------------------------------
다음 중 수정할 항목을 선택하세요(수정할 정보가 없으면 exit 입력)
name,  gender,  birthyear 중 입력
-------------------------------------------------------------------------
>>> ''')
        if choice2 in ('name','gender','birthyear'):
            custlist[idx][choice2] = input('수정할 {}를 입력하세요 >>> '.format(choice2))
            print(custlist[idx])
            break
        elif choice2 == 'exit':
            break
        else:
            print('존재하지 않는 항목입니다.')
            break

def deleteData(custlist):
    choice1 = input('삭제하려는 이메일주소를 입력하세요 >>> ')
    delok = 0
    for i in range(len(custlist)):
        if custlist[i]['email'] ==choice1:
            print('{} 고객님의 정보가 삭제되었습니다.'.format(custlist[i]['name']))
            del custlist[i]
            delok=1
            print(custlist)
            break