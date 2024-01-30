num=int(input())
Fibonacci=[0,1] #0과 1로 시작하기 때문에 기본 세팅
for i in range(num):
    Fibonacci.append(int(Fibonacci[i])+int(Fibonacci[i+1])) #피보나치 수열은 앞의 두 수의 합이 그 다음 수가 됨
print(Fibonacci[num])
