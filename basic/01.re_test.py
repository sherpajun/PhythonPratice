# ctrl+alt++ 터미널 실행

import  json,pickle,os
import  re_func as func

file_json = os.path.dirname(__file__)+'/member.json'
file_pickle = os.path.dirname(__file__)+'/member.pickle'
member = {'jun1451': ['홍길동', '010-5555-1336', '931217-1123313', 'jun1985@naver.com']}
#with open(file_json,'w') as f:
    #1member = json.load(f) #저장한걸 불러와야한다.
while True:
    display = '''
    ------------------------------------------------
    1. 회원가입 2. 회원목록 3. 종료 4. pickle열기 5.pickle 저장
    ------------------------------------------------
    >>> '''
    menu = input(display)
    if menu == '1':
        member = func.signUp(member)
    elif menu =='2':
        print('회원목록')
        print(member)
    elif menu =='3':
        with open(file_json,'w') as f:
            json.dump(member,f,indent=4) #아래 주석 처리된 명령어와 같다. dump가 저장이라는 의미
        #f = open('member.json','w')
        #json.dump(member,f)
        #f.close()
        print('프로그램을 종료합니다.')
        break
    elif menu == '4':
        print('pickle 열기')
        with open(file_pickle,'rb')as f:
            member = pickle.load(f)
            print(member)
    elif menu == '5':
        print('pickle 저장')
        with open(file_pickle,'wb')as f:
            pickle.dump(member,f)




#signUp()