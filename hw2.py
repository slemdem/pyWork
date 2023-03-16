#입력한 금액을 500, 100, 50, 10원의 동전으로 바꿔주는 함수
def exchange(cash) :
    #각 금액의 몫(동전개수) 계산
    ex_500 = cash // 500
    cash %= 500
    
    ex_100 = cash // 100
    cash %= 100
    
    ex_50 = cash // 50
    cash %= 50
    
    ex_10 = cash // 10

    #저장한 값의 출력
    print('500원 동전의 개수:',ex_500)
    print('100원 동전의 개수:',ex_100)
    print('50원 동전의 개수:',ex_50)
    print('10원 동전의 개수:',ex_10)

#숫자를 입력받아 int로 바꿔주는 함수 
def get_integer(prompt) :
    i = int(input(prompt))
    return i

money = get_integer('동전으로 교환하고자 하는 금액은?')
exchange(money)
