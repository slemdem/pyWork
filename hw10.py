import os
import pickle


#score
def input_scores() :
    scores = []
    sco = 0
    count = 1
    print('[점수입력]')
    while sco >=0 :
        sco = int(input(f'#{count}? '))
        if sco < 0: break
        scores.append(sco)
        count +=1
        
    return scores

def get_average(lst) :
    total = 0
    for i in lst:
        total += i
    return total/len(lst)

def show_scores(lst) :
    print('[점수출력]')
    print('개인점수:',end = ' ')
    for i in lst:
        print(f'{i}',end = ' ')
    print()
    print(f'평균{get_average(lst):.1f}')

#save bin
def save_data(filepath,lists):
    with open(filepath, 'wb') as file:
        pickle.dump(lists,file)

def load_data(filepath):
    newlist = []
    with open(filepath, 'rb') as file:
        newlist = pickle.load(file)
              
    return newlist

#main
filename = 'score.bin'

if os.path.exists(filename):
    print('[파일 열기]')
    print()
    scores = load_data(filename)
    show_scores(scores)
    
else :
    score_list = input_scores()
    print()
    show_scores(score_list)
    save_data(filename,score_list)



