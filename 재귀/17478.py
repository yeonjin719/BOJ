num=int(input())
r=''
def say1(r): #같이 붙어서 나오는 문장을 분류 후  ____가 붙는 경우에 매개변수를 이용한다
    print('어느 한 컴퓨터공학과 학생이 유명한 교수님을 찾아가 물었다.')

def say2(r): 
    print('%s"재귀함수가 뭔가요?"'%r)
    print('%s"잘 들어보게. 옛날옛날 한 산 꼭대기에 이세상 모든 지식을 통달한 선인이 있었어.'%r)
    print("%s마을 사람들은 모두 그 선인에게 수많은 질문을 했고, 모두 지혜롭게 대답해 주었지."%r)
    print('%s그의 답은 대부분 옳았다고 하네. 그런데 어느 날, 그 선인에게 한 선비가 찾아와서 물었어."' %r)

def say3(r):
    print("%s라고 답변하였지."%r)

def answer1(r):
    print('%s"재귀함수가 뭔가요?"'%r)
    print('%s"재귀함수는 자기 자신을 호출하는 함수라네"'%r)
    print("%s라고 답변하였지."%r)

def answer2(r):
    print("%s라고 답변하였지."%r)

say1(r) #한 번만 말하는 문장은 for문에 포함 X
for i in range(num):
    say2(r)
    r='____'*(i+1)
answer1(r)
for j in range(num):
    r='____'*(num-j-1)
    answer2(r)