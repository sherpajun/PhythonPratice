import re,sys
class Customer:
    custlist=[{'name': '홍길동', 'gender': 'M', 'email': 'hong123@gmail.com', 'birthyear': '2000'},
          {'name': '박철수', 'gender': 'M', 'email': 'park01@gmail.com', 'birthyear': '2002'},
          {'name': '김나리', 'gender': 'F', 'email': 'kim123@gmail.com', 'birthyear': '1999'} ]
    page = 2

    def insertData(self):
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
                for i in Customer.custlist:
                    if i['email'] == customer['email']:
                        check=1
                if check==0:
                    break
                print('중복되는 이메일이 있습니다.')

            while True:
                customer['birthyear'] = input('생년월일(4자리) >>> ')
                if len(customer['birthyear']) == 4 and customer['birthyear'].isdigit():
                    break

            Customer.custlist.append(customer)
            Customer.page =len(Customer.custlist)-1
            print(Customer.custlist)
            print(Customer.page)

    def curSearch(self):
        if Customer.page < 0:
            print('입력된 정보가 없습니다.')
        else:
            print(f'현재 페이지는 {Customer.page}페이지 입니다.')
            print(Customer.custlist[Customer.page])

    def preSearch(self):
        if Customer.page <= 0:
            print('첫번째 페이지입니다.')
            print(Customer.page)
        else:
            Customer.page -= 1
            print(f'현재 페이지는 {Customer.page}페이지 입니다.')
            print(Customer.custlist[Customer.page])   

    def nextSearch():
        if Customer.page >= len(Customer.custlist)-1:
            print('마지막 페이지입니다.')
            print(Customer.page)
        else:
            Customer.page += 1
            print(f'현재 페이지는 {Customer.page}페이지 입니다.')
            print(Customer.custlist[Customer.page])

    def updateData(self):
        while True:
            choice1 = input('수정하려는 이메일주소를 입력하세요 >>> ')
            idx =-1
            for i in range(len(Customer.custlist)):
                if Customer.custlist[i]['email'] == choice1:
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
                Customer.custlist[idx][choice2] = input('수정할 {}를 입력하세요 >>> '.format(choice2))
                print(Customer.custlist[idx])
                break
            elif choice2 == 'exit':
                break
            else:
                print('존재하지 않는 항목입니다.')
                break

    def deleteData(self):
        choice1 = input('삭제하려는 이메일주소를 입력하세요 >>> ')
        delok = 0
        for i in range(len(Customer.custlist)):
            if Customer.custlist[i]['email'] ==choice1:
                print('{} 고객님의 정보가 삭제되었습니다.'.format(Customer.custlist[i]['name']))
                del Customer.custlist[i]
                delok=1
                print(Customer.custlist)
                break

    def exe(self, choice):
        if choice=='I':
            self.insertData()
        elif choice=='C':
            self.curSearch()
        elif choice=='P':
            self.preSearch()
        elif choice=='N':
            self.nextSearch()
        elif choice=='U':
            self.updateData()
        elif choice=='D':
            self.deleteData()
        elif choice=='Q':
            sys.exit()


    def display(self):
        choice=input('''
    다음 중에서 하실 일을 골라주세요 :
    I - 고객 정보 입력
    C - 현재 고객 정보 조회
    P - 이전 고객 정보 조회
    N - 다음 고객 정보 조회
    U - 고객 정보 수정
    D - 고객 정보 삭제
    Q - 프로그램 종료
    ''').upper()
        return choice

    def __init__(self):
        while True:
            self.exe(self.display())

# 프로그램 실행
Customer()