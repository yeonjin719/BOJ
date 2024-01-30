num=int(input())
groupword=num #그룹 단어 개수를 일단 단어 개수로 지정
for i in range(num): #넘버만큼 반복
    word=input() #단어 입력받고
    for j in range(0, len(word)-1): #단어 길이보다 하나 짧게 반복
        if word[j]==word[j+1]: #만약 단어의 j번째, j+1번째가 같다면
            pass #문제가 없으니 넘어가기
        elif word[j] in word[j+1:]: #만약 단어의 j번째랑 j+1번째가 다른데 j+1번째 이후로 단어의 j번째 문자가 존재한다면             
            groupword -= 1 #그룹단어개수에서 하나 빼기
            break #멈추기
print(groupword)
