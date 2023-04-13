def display_multiplation_table_form_end(f,e) :
    for n2 in range(1,10) :
        for n1 in range(f,e+1) :
            print(f'{n1} x {n2} = {n1*n2}', end='\t')
        print()
        
def display_all_multiplation_table() :
    display_multiplation_table_form_end(2,5)
    print()
    display_multiplation_table_form_end(6,9) 

display_all_multiplation_table()
