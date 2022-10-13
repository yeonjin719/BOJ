X = int(input())
line = 0 #몇번 째 줄인가
M_num = 0 #최대 숫자가 몇인가
while X > M_num:
    line += 1 
    M_num += line
if line % 2 == 0: #짝수번째 줄이랑 홀수번째 줄이랑 방식이 다름
    print(line - M_num + X, end = '')
    print('/', end = '')
    print(M_num - X + 1)
else:
    print(M_num - X + 1, end='')
    print('/', end = '')
    print(line - M_num + X)