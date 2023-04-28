def add_to_shopping_bag(list_bag,items,count):
    list_bag[item] = count
    

shopping_bag = {}
while True:
    item = input('상품명? ')
    if(item == ''):
        print()
        break
    amount = int(input('수량은? '))
    add_to_shopping_bag(shopping_bag,item,amount)
    print(f'장바구니에 {item} {amount}개가 담겼습니다.', end ='\n\n')
    
print('>>> 장바구니 보기 :',shopping_bag)
print('\n[검색]')
serch = input('장바구니에서 확인하고자 하는 상품은? ')

if serch in shopping_bag :
    print(f'{serch}은(는) {shopping_bag.get(serch)}개 담겨 있습니다.')
else:
    print(f'{serch}는 장바구니에 없습니다.')
