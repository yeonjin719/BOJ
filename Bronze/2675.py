num=int(input()) #입력받을 총 경우를 알려주니 num으로 저장합니다
for i in range(num):
    N, word=input().split() 
		#공백을 기준으로 몇번 반복시킬 건지, 단어가 뭔지 알려주니 split으로 나누고 각각 N, word의 형태로 저장합니다.
    for j in word: 
        print(j*int(N), end='') 
				#아까 입력받을 몇번 반복시킬 건지와 word의 j번째 값을 곱하는 걸 반복하는데 공백 없이 출력해야해서 end=''로 지정해줍니다.
    print() 
		#케이스가 다를 경우 다른 줄로 프린트해야해서 공백을 프린트해줍니다
