numbers=input().split() #numbers라는 이름의 리스트로 두 수를 공백 기준으로 split하여 저장
num1=numbers[0] #numbers의 0번째 값을 num1로 저장
num2=numbers[1] #numbers의 1번째 값을 num2로 저장

new_num1=num1[2]+num1[1]+num1[0] #새로운 숫자는 백의 자리 숫자와 일의 자리 숫자만 바뀐 것이니 바꿔준다
new_num2=num2[2]+num2[1]+num2[0] #마찬가지

if new_num1 > new_num2: #이제 두 수를 비교
    print(new_num1) #큰 값을 출력
else:
    print(new_num2)