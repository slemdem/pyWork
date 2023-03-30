def rep_char(c, n):
    print(c*n)

def draw_line_greetings(name) :
    msg1 = f' Hello {name}, \n'
    msg2 = ' welcome to Seoul. '
    nstr = len(msg1) if (len(msg1) > len(msg2)) else len(msg2)
    rep_char('-',nstr)
    print(msg1 + msg2)
    rep_char('-',nstr)
    
welcome_name = input('Input his/her name:')
draw_line_greetings(welcome_name)
