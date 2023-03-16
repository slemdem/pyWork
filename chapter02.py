#+부호는 일반적으로 생략함
#-부호 연산자는 피 연산자 항의 부호를 반대로 바꾼 '결과값'을 지님
n = -10
print('+n =', +n)
print('-n =',-n)
print('n =', n)

print('|-2 + -3| =',-(-2+-3))

#덧셈 뺄셈 곱셈 나눗셈 나누셈의 몫, 나머지 거듭제곱
#   +    -    *      /          //      %        **

#실수의 경우 내부적으로 유효 자릿수와 지수값을 기반으로 근사화된 값으로 저장

#나눗셈의 몫과 나머지를 구하는 함수
def show_division(divided,divisor) :

    #나눗셈의 몫을 구하고 출력
    n = int(divided//divisor)
    print('몫 = ', n)
    
    #나눗셈의 나머지를 구하고 출력
    n = int(divided%divisor)
    print('나머지 = ', n) 

p = int(input('피젯수를 정수로 입력하세요: '))
j = int(input('젯수를 정수로 입력하세요: '))
show_division(p,j)

#대입연산자 - 우측 표현식의 결과값을 좌측 변수에 대입
#피연산자들의 순서를 바꿀 수 없고, 다른 연산자보다 낮은 우선순위를 가짐
#왼쪽항에는 새로운 값을 대입받을 수 있는 성질의 표현식만 올 수 있음
#왼쪽항에 올 수 있는 것들 = 객체를 참조하는 표현식, 단순 변수
n1 = 1 + 2
n2 = n1
n2 = n2 - 1
n3 = n1 + n2

#대입연산자는 오른쪽에서 왼쪽 방향으로 결합되며 결과값은 대입된 왼쪽항이 갖는 값
x = y = z = 1
z = 1; y = z; x = y;

#다중 대입문 - 좌변의 변수들에다가 순서대로 우변의 표현식의 값을 순차적으로 대입
x, y = 1, 2 # x = 1; y = 2;

#다중대입문으로 변수값을 쉽게 맞교환 할 수 있음
x, y = y, x # tmp = x; x = y; y = tmp;


#비트 연산자 - 각항을 구성하는 데이터의 비트들 간에 비트논리연산 혹은 시프트연산을 수행
# 단항  ~    비트부정              각 비트값을 반전한 결과값
# 이항  &    비트 논리곱           두 비트가 모두 1일 때만 1
#       |    비트 논리합           두 비트가 모두 0일 때만 0
#       ^    비트 배타적 논리합    두 비트가 값이 다를 때만 1
#       <<   비트 왼쪽으로 이동     각 비트를 왼쪽으로 이동
#       >>   비트 오른쪽으로 이동     각 비트를 오른쪽으로 이동

n1 = 0b10101101
n2 = 0b00001111 # n2 = 15

#내장함수 bin() 인수로 지정한 정수을 이진 비트열의 문자열로 변환해 반환
print(bin(n1 & n2))
print(n1 & n2)
print(bin(n1 | n2))
print(n1 | n2)
print(bin(n1 ^ n2))
print(n1 ^ n2)
print(bin(~n2))
print(~n2)


print(bin(n2 >> 2))
print(n2 >> 2) # 3 = 15 // (2**2)
print(bin(n2 << 2))
print(n2 << 2) # 60 = 15 * (2**2)

#총 구매금액과 지불금액을 입력받아 잔돈을 계산하고 잔돈으로 지불할 최소 지폐수 출력
def exchange(money):
    print('잔돈:',money,'원')
    exc_5000 = money // 5000
    money %= 5000
    exc_1000 = money // 1000
    print('5000원권', exc_5000,'장')
    print('1000원권', exc_1000,'장')

total_cost = int(input('구매한 물건의 총 구매 금액은? '))
payment = int(input('구매한 물건의 총 구매 금액은? '))
change = payment - total_cost
exchange(change)

#연산자의 우선순위 괄호 -> 산술 -> 비트 -> 논리 -> 대입

#사용자로부터 화씨온도를 입력받아 섭씨온도로 변환
def fahrenheit_to_celsius(f):
    c = 5/9*(f-32)
    return c

def get_real(prompt):
    gr = float(input(prompt))
    return gr
    
ftemp = get_real('변환하고자 하는 화씨온도?')
ctemp = fahrenheit_to_celsius(ftemp)
print('화씨',ftemp,'도는 섭씨',ctemp,'도')


#사용자로부터 초단위 시간을 입력받아 시 준 초로 변환
def convert_time(time):
    s = time
    h = s // 3600
    s %= 3600
    m = s//60
    s %= 60

    print(time,'초는', h,'시간',m,'분',s,'초이다')
    

def get_integer(prompt):
    gi = int(input(prompt))
    return gi

seconds = get_integer('변환하고자 하는 시간(초)?')
convert_time(seconds)



#n비트를 모두 1로 설정한 수를 10진수와 2진수로 표현
def set_all_bits(n):
    return (1<<n) - 1 

bits = get_integer('설정할 비트 수는?')
i = set_all_bits(bits)
print(bits,'비트를 모두 1로 설정한 수는', i,'(', bin(i),')이다')
