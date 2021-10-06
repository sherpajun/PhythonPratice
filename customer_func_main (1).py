import re
import customer_func as cf

custlist=[]
page=-1

def exe(choice):
    if choice=='I':
        cf.insertData()
    
    elif choice=='C':
        cf.curSearch()
    
    elif choice=='P':
        cf.preSearch()

    elif choice=='N':
        cf.nextSearch()

    elif choice=='U':
        cf.updateData()
    
    elif choice=='D':
        cf.deleteData()
    
    elif choice=='Q':
        quit()
            
while True:
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
    exe(choice)