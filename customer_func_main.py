import re,sys
import customer_func as cf

custlist=[{'name': '홍길동', 'gender': 'M', 'email': 'hong123@gmail.com', 'birthyear': '2000'},
          {'name': '박철수', 'gender': 'M', 'email': 'park01@gmail.com', 'birthyear': '2002'},
          {'name': '김나리', 'gender': 'F', 'email': 'kim123@gmail.com', 'birthyear': '1999'} ]
page = 2

def exe(choice,page):
    if choice=='I':
        cf.insertData(custlist)
    
    elif choice=='C':
        cf.curSearch(custlist,page)
    
    elif choice=='P':
        page = cf.preSearch(custlist,page)

    elif choice=='N':
        page = cf.nextSearch(custlist,page)

    elif choice=='U':
        cf.updateData(custlist)
    
    elif choice=='D':
        cf.deleteData(custlist)
    
    elif choice=='Q':
        sys.exit()
    return page
            
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
    page = exe(choice,page)