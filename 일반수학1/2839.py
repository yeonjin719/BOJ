N = int(input())
a = 0 #a는 5kg짜리 설탕 봉지 개수, b는 3kg짜리 설탕 봉지 개수
answer = [] #정확히 설탕 Nkg가 되는 봉지 개수 리스트
while 5*a <= N : 
    b = (N-(5*a))/3 #3kg짜리 봉지 개수는 Nkg에서 5kg 봉지 a개를 뺀 후 3으로 나눈 값
    if b == int(b) : #이 때 봉지 개수는 소수가 될 수 없으므로 예외처리해줌
        answer.append(a+b) #정수일 경우만 봉지 개수를 더해 answer 리스트에 추가
    else :
        pass
    a += 1 #a값이 하나씩 커지게 하여 대입하여 answer 구하기
if len(answer) == 0 : #만약 answer 리스트가 비었다면
    print('-1') #문제에서 -1 출력하라 했음
else:
    print(int(min(answer))) #이 외에는 가장 적은 봉지를 가져가는 경우이므로 answer 중 가장 작은 값 출력
