#정수를 입력받는 함수
def get_float(prompt):
    gf = float(input(prompt))
    return gf

#할인가와 할인율로 원래의 가격을 계산
def get_fixed_price(price,rate):
    origin_price = price/(1 - (rate/100))
    return origin_price
    

#주프로그램부
rate = get_float('할인율은? ')
price_A  = get_float('A상품의 할인된 가격은? ')
price_B  = get_float('B상품의 할인된 가격은? ')
print('A상품의 정가는 ',get_fixed_price(price_A, rate),'원')
print('B상품의 정가는 ',get_fixed_price(price_B, rate),'원')
