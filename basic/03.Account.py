#은행 계좌를 클래스로 작성하시오
#클래스 변수를 이용하여 계좌가 개설된 건수를 체크하고 출력하는 클래스 함수를 작성합니다.
#아래의 내용은 인스턴스 함수와 변수로 작성합니다.
#계좌는 이름과 금액을 입력받고, 계좌번호는 자동으로 생성합니다.
#입금은 0보다 큰금액을 입력하며 로그에 입금내역을 기록합니다.
#입금 횟수에 따라 1%의 이자가 지급됩니다(5회마다)
#출금은 잔액보다 작을 경우에 처리됩니다. 로그에 출금 기록을 남깁니다.
#계좌 정보를 출력하는 함수는 은행이름, 예금주,계좌번호,잔고를 출력합니다.
#입금 내역과 출금 내역을 출력하는 함수


class Account:
    account_count = 0 #(class 변수)

    @classmethod
    def get_account_count(cls):
        print('계좌수:',cls.account_count)

    def __init__(self,name,balance):
        Account.account_count += 1
        self.name = name
        self.balance = balance
        self.deposit_count = 0
        self.total_log = []
        self.account_number = Account.account_count

    def deposit(self,amount):
        if amount >= 1:
            self.total_log.append(('입금처리',amount))
            self.balance+=amount
            print(f'{amount:,.1f}원이 입금처리되었습니다. 총 금액은{self.balance:,}입니다.')
            self.deposit_count += 1
            if self.deposit_count %5 ==0:
                interest = self.balance *0.01
                self.balance+=interest
                self.total_log.append(('이자지급',interest))
                print(interest,'원의 이자가 지급완료')




    def withdraw(self,amount):
        if self.balance>=amount:
            self.balance-=amount
            self.total_log.append(('출금',amount))
            print(amount,'원이 출금되었습니다.')
        else:
            print('잔액이 부족합니다.')



    def __str__(self):
        return f'예금주:{self.name},계좌번호:{self.account_number},잔고:{self.balance:,.0f}'

a = Account('aaa',1000)
b = Account('nnn',2000)


a.deposit(3000)
a.deposit(1000)
a.deposit(23000)
a.deposit(33000)
a.deposit(311000)
a.withdraw(400000)
a.withdraw(10000)

print(a.total_log)

b.deposit(3000)
b.deposit(1000)
b.deposit(23000)
b.deposit(33000)
b.deposit(311000)
b.withdraw(400000)
b.withdraw(10000)
print(b.total_log)

print(a)
print(b)
''' 
print(Account.get_account_count())
print(a.get_account_count())
print(b.get_account_count())
print(a.name)
print(b.name)
print(a.account_number)
print(b.account_number)
''' 