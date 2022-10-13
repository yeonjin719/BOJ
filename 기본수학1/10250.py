T = int(input())
for i in range(T):
    H, W, N = map(int, input().split())
    A= N % H # 층수 = n번째를 층수로 나눈 나머지
    B= N // H + 1 #호수는 n번째를 층수로 나눈 몫에 1을 더한 값(0호가 X)
    if A==0:#근데 N이 H의 배수일 경우 나머지가 0
        A=H #이 경우 층수는 총 층수에 해당
        B-=1 #호수도 하나 빼줘야함
    else:
        pass
    
    print(A*100+B)