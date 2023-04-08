#임의의 한자리 십진 정수에 대한 한글 문자열을 반환하는 함수
def read_single_digit(digit):
    if digit == 1:
        return '일'
    elif digit == 2:
        return '이'
    elif digit == 3:
        return '삼'
    elif digit == 4:
        return '사'
    elif digit == 5:
        return '오'
    elif digit == 6:
        return '육'
    elif digit == 7:
        return '칠'
    elif digit == 8:
        return '팔'
    elif digit == 9:
        return '구'
    else:
        return '잘못된 입력입니다'

#read_single_digit()을 이용해 임의의 세자리 십진 정수에 대한
#한글 문자열을 반환하는 함수
def read_number(number):
    number1 = number//100
    number = number%100
    
    number2 = number//10
    number = number%10
    if 0 < number1 < 10:
        return f'{read_single_digit(number1)} {read_single_digit(number2)} {read_single_digit(number)}'
    else:
        return read_single_digit(number1)
    
#주프로그램부
num = int(input('세 자리 정수 입력: '))
print(read_number(num))
