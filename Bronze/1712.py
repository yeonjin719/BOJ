a,b,c=map(int,input().split()) #문제에서 a,b,c를 지정해줬으니 받아오는데 int형으로 받아옵니다
if c==b: #만약 c랑 b랑 같으면 0으로 나누는 꼴이 되버리기 때문에 -1을 출력
    print('-1')
else: 
    n=int(a/(c-b)) #그 이외의 경우는 계산을 해주는데
    if n<0: #만약 n이 0보다 작으면 손익분기점이 존재x
        print('-1')
    else:
        print(n+1) #손익분기점은 총수입=총지출이 아니므로 총 지출을 넘기기 위해 +1을 해준다
