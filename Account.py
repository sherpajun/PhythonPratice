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
