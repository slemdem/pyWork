print("hello");print("world")
print("hello","world")

#정수 리터럴 표현
#10진수
print(-1+1)
#2진수 b
print(0b1010 + 1)
#8진수 o
print(0o17)
#16진수 x
print(0xf+1)

#소수점표기법 정수와 소수 부분을 .으로 분리해 표기 
print(15 + .12345)
print(15.+.12345)
#지수(과학적) 표기법 유효 숫자와 지수를 e로 분리해 표기
#아주 크거나 아주 작은 수를 상대적으로 간결하게 표현
print(3.14e-5 +1)

#논리 리터럴
print(not False)
print(True)
print(not True)
print(False)

#문자열 리터럴
#입출력을 위한 문자열을 나타내는 리터럴
#같은 종류의 따옴표로 감싼 문자들의 묶음
print('hello'+'!')

#인수로 하나의 문자열을 갖는 출력문 - 기본적으로 출력 후 줄바꿈 처리
print('hello world')
#다양한 유형의 리터럴을 인수로 가질 수 있음
print(3+2)
#하나의 인수도 갖지 않는 함수
#인수 없이 호출 시 출력내용이 없기에 줄바꿈 처리만 일어난다
print()
#print()는 가변개의 인수를 가질 수 있음 , 로 구분
print(2, '+', 3, '=', 2+3)

#식별자 = 함수의 이름
#알파벳 문자, 숫자문자, _ 로 이루어져야 함
#숫자문자로 시작 불가, 키워드와 동일하면 안됨
#키워드(예약어) = 특별히 정의하지 않아도 이미 문법적으로 특별한 의미가 있는 단어
#한글로 가능은 하지만 깨지거나 재 사용성이 낮아짐

#모든 함수는 호출되기 전에 미리 호출형태와 동작내용이 정의되어야 함
#함수의 식별자는 보통 그 동작을 나타낼 수 있는 동사구로 이름짓는 것이 좋음
#함수의 몸체는 반드시 1열보다 한 단계 들여써야 함

#사용자 정의 함수 부
def show_message() : #함수 헤더
    print('hello world!') #함수 몸체(스위트)
    print('good job')

#주 프로그램 부
print('시작')
show_message()
print('마침')

#변수 - 프로그램이 진행되는 동안 변할 수 있는 데이터
#어떤 값을 저장할 수 있는 메모리 공간
#변수에는 자료형에 상관없이 하나의 데이터만 유지 가능
# '=' (대입연산자) 기호는 같다가 아니라 오른쪽 표현식의 결과값을 왼쪽에 넣는다는 의미
#저장된 데이터는 무한히 참조가능 하지만 한번에 하나의 데이터만 저장가능
nStud, nProf = 9,3
print(nStud)
nStud = nProf
print(nStud)
nStud = "문자열"
print(nStud, nProf)

#변수의 자료형은 할당되는 값에 따라 자료형이 동적으로 결정됨
print(type(nStud))

#사실 파이썬 변수는 각 데이터에 대한 아이디를 가지는 것
#내장함수 id는 데이터의 아이디를 반환해 줌
id(123)
n = 123
id(n)
n= 'hi'
id(n)
id('hi')

#매개변수 - 함수 내에 선언된 변수로 함수 호출시 전달되는 인수를 받을 목적으로 사용되는 변수
#호출문의 각 인수를 순서대로 전달받음 개수 제한은 없
#함수 몸체에서 매개변수로 전달받는 값을 반드시 이용 (이용하지 않는다면 매개변수 없이 생성)
#동일한 함수가 인수로 전달된 다른 데이터에 대해 주어진 일을 처리할 수 있게 함

#사용자 정의 함수부
def show_messege(msg, name):
    print(msg, name, '님')

#주 프로그램 부
print('start')
show_messege('hi', '진상하')
show_messege('반가워','홍길동')
print('end')

#함수 호출시 매개변수의 이름을 명시하면 순서와 상관없이 인수를 전달 할 수 있음
print('start')
show_messege(msg = 'hi', name = '진상하')
show_messege(name = '홍길동', msg = '반가워')
print('end')


#함수 정의시 매개변수는 기본값을 지정할 수 있음 - 디폴트 인수라고 부름
#매개변수의 초기값은 반드시 뒤쪽 매개변수부터 지정되어야 함
def show_msg(msg='안녕하세요', name ='여러분'):
    print(msg, name, '님')
    
show_msg()
show_msg('안녕')
show_msg(name = '홍길동')

print('당신의 이름은?', end='')
name = input()
print('반가워요', name)

def make_message():
    name = input('당신의 이름은?')
    msg = input('하실 말씀은?') + ' ' + name
    print(msg)
    
print('start')
make_message()
print('end')

def make_message(name):
    msg = '반가워요' + name
    print(msg)
    
print('start')
input_name = input('이름')
make_message(input_name)
print('end')

def make_message(name):
    msg = '반가워요' + name
    return msg

print('start')
input_name = input('이름')
print(make_message(input_name))
print('end')
