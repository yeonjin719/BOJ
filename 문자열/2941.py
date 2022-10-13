import re
word=input() #단어를 입력받는다
try:
    word=re.sub("c=","c",word) #크로아티아 문자에 해당하는 문자를 정규표현식을 이용하여 알파벳 하나짜리로 바꿔준다 단, 존재하지 않는 경우도 있기 때문에 try except문을 사용한다
except:
    pass
try:
    word=re.sub("c-","c",word)
except:
    pass
try:
    word=re.sub("dz=","d",word)
except:
    pass
try:
    word=re.sub("d-","d",word)
except:
    pass
try:
    word=re.sub("lj","l",word)
except:
    pass
try:
    word=re.sub("nj","n",word)
except:
    pass
try:
    word=re.sub("s=","s",word)
except:
    pass
try:
    word=re.sub("z=","z",word)
except:
    pass
print(len(word)) #문자열의 길이를 출력한다