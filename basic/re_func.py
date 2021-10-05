
import re


def nameCheck():
    name_p = re.compile('^[ㄱ-ㅣ가-힣]{2,}$')#정규식 표현
    name_c = 0
    while not name_c:
        name = input('이름>>>')
        name_c=name_p.match(name)
    return name
#print(nameCheck())

def idCheck():
    id_p = re.compile('^[a-zA-Z][a-zA-z0-9]{4,11}$')
    id_c = 0
    while not id_c:
        id = input('아이디>>>')
        id_c = id_p.match(id)
    return id
#print(idCheck())


def telCheck():
    tel_p = re.compile('[0-9]{2,3}-[0-9]{3,4}-[0-9]{3,4}$')
    tel_c = 0
    while not tel_c:
        tel = input('전화번호>>>')
        tel_c = tel_p.match(tel)
    return tel
#print(telCheck())


def emailCheck():
    email_p = re.compile('[a-z][a-z0-9_]{4,}@[a-z]{2,}.[.][a-z]{2,}')
    email_c = 0
    while not email_c:
        email = input('이메일입력>>>')
        email_c = email_p.match(email)
    return email
#print(emailCheck())


def juminCheck():
    jumin_p = re.compile('[0-9]{6}-[1-8][0-9]{6}$')
    jumin_c = 0
    while not jumin_c:
        jumin = input('주민번호>>>')
        jumin_c = jumin_p.match(jumin)
    return jumin
#print(juminCheck())


def signUp(member):
    name = nameCheck()
    id= idCheck()
    tel= telCheck()
    jumin = juminCheck()
    email = emailCheck()
    member[id]=[name,tel,jumin,email]
    return member

#print(signUp())