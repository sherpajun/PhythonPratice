# 은행 계좌를 클래스로 작성하시오
# 클래스 변수를 이용하여 계좌가 개설된 건수를 체크하고 출력하는 클래스함수를 작성합니다.
# 아래의 내용은 인스턴스 함수와 변수로 작성합니다.
# 계좌는 이름과 금액을 입력받고, 계좌번호는 자동으로 생성합니다.
# 입금은 0보다 큰금액을 입력해야하며 로그에 입금내역을 기록합니다.
# 입금 횟수에 따라 1%의 이자가 지급됩니다.(5회마다)
# 출금은 잔액보다 작을경우에 처리됩니다. 로그에 출금 기록을 남깁니다.
# 계좌정보를 출력하는 함수는 은행이름,예금주,계좌번호,잔고를 출력합니다.
# 입금내역과 출금내역을 출력하는 함수

class Account:
    account_count = 0 

    @classmethod
    def get_account_count():
        print('계좌수 : ',Account.account_count)
    
    def __init__(self,name,balance):
        Account.account_count += 1
        self.name =name
        self.balance = balance
        self.deposit_count = 0
        self.total_log = []
        self.account_number = Account.account_count

    def deposit(self,amount):
        if amount >= 1:
            self.total_log.append(('입금',amount))
            self.balance += amount
            print(f'{amount:,.1f}원이 입급처리되었습니다. 총 금액은 {self.balance:,}입니다.')
            self.deposit_count += 1
            if self.deposit_count % 5 == 0:
                interest = self.balance * 0.01
                self.balance  += interest
                self.total_log.append(('이자지급',interest))
                print(interest,'원의 이자가 지급되었습니다.')

    def withdraw(self,amount):
        if self.balance >= amount:
            self.balance -= amount
            self.total_log.append(('출금',amount))
            print(f'{amount:,}원이 출금되었습니다.')
        else:
            print('잔액이 부족합니다.')

    def __str__(self):
        return f'예금주 : {self.name}, 계좌번호 : {self.account_number}, 잔고 : {self.balance:,.0f} '


import pickle,os

account_list=[]
# account_list 불러오기
dir = os.path.dirname(__file__)+'/account.pickle'

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
        account_list.append( Account(name,balance))
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
    
