def buy(dic):
    item = input('상품명? ')
    if(item == ''):
        return False
    amount = int(input('수량은? '))
    dic[item] = amount
    print(f'장바구니에 {item} {amount}개가 담겼습니다.', end ='\n\n')

def show(dic):
    print('>>> 장바구니 보기 :',dic)

def find(dic):
    print('\n[검색]')
    serch = input('장바구니에서 확인하고자 하는 상품은? ')

    if serch in dic :
        print(f'{serch}은(는) {dic.get(serch)}개 담겨 있습니다.')
    else:
        print(f'장바구니에 {serch}는 없습니다.')
    

shopping_bag = {}
while True:
    if buy(shopping_bag) == False:
        break

show(shopping_bag)
find(shopping_bag)
