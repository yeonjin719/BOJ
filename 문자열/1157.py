from itertools import count

words=input().lower() #단어를 입력받아 전부 소문자로 바꿔줍니다
ad_word=list(set(words)) #단어에서 중복되는 알파벳을 제거해줍니다
n_list=[]
for i in ad_word: 
    n=words.count(i) #리스트의 i번째 값의 알파벳의 개수를 세줍니다
    n_list.append(n) #그걸 리스트에 다시 저장합니다

if n_list.count(max(n_list))>=2: #n_list 중 최댓값의 개수가 n_list에서 2개 이상이면
    print('?') #최댓값에 해당하는 값 만큼을 가지고 있는 알파벳이 2개 이상이므로 문제에서 말한 ?를 출력해줍니다.
else:
    max_num=n_list.index(max(n_list)) #그 외의 경우는 최댓값에 해당하는 값의 위치를 리스트에서 찾아 max_num으로 저장합니다.
    print(ad_word[max_num].upper()) #그 값에 해당하는 알파벳을 출력합니다. 단 문제에서 대문자로 출력하래서 upper을 달아줍니다.