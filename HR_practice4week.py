#문자열 string

# 문자열 내부에 큰따옴표나 작은따옴표를 사용하기 위해서는?
# str1 = 'He said "I love you"'
# str2 = "It's so beautiful"
# str3 = """MY name is "goorm" """
# str4 = '''It's a apple'''
#
# print(str1)
# print(str2)
# print(str3)
# print(str4)


# 문자열에 엔터를 통해 줄바꿈을 하려면 '''''' 또는 """"""를 사용한다.

# str1 = "바로 실행하면서 배우는 \n파이썬" # 왼쪽처럼 \n 기호를 사용하면 엔터가 되지만 그냥 엔터를 치면 엔터입력이 안된다.
# str2 = '설치가 필요없는 클라우드 IDE 구름 IDE'
# str3 = '''이스케이프 시퀀스를
# 배워봅니다.'''
# str4 = """바로 실행해 보면서 배우는
# GO Lang"""
# str5 = "이렇게 하면" \
#        "안되는구나"

# print(str1)
# print(str2)
# print(str3)
# print(str4)
# print(str5)

#그런데 이렇게 이스케이프 시퀀스를 사용하다보면 코드가 지저분해질 가능성이 높은데 따라서 백슬래쉬 \ 를 이용해서 따옴표처리를 하기도 하는데 해당
#방법을 알아보도록 하자

#문자열도 간단한 덧셈 연산이 가능하다.
str1 = "Hello "
str2 = "goorm!"
result = str1 + str2
print(result)

#문자열 곱셈도 가능하다.
str3 = "떡볶이"
a=3
result1 = str3*a
print(result1)

#포맷을 사용해보자
name1= "허룡"
name2= "송민경"
age = 26
height = 168.725

print("저의 이름은{2} 입니다. 그리고 나이는 {1}살이고 키는 {0}cm입니다.".format(height,age, name1))
print("{1}의 나이 : {0}, {2}의 나이 : {0}".format(age,name1,name2))

str=" Hello goorm! I study Python.    "

num = str.count(' ') #빈칸의 개수를 세어라
print("빈칸의 개수는{} 입니다.".format(num))
print("빈칸의 개수는 %d입니다." %num)

print("처음 등장하는 'l'의 인덱스 값은 %d입니다." %str.find('l'))
print("Good day에서 처음 등장하는 'y'의 인덱스 값은 %d입니다." %"Good day".index('y'))

print(" ".join(str)) #join함수는 문자열 사이사이에 해당 문자열을 추가한다
print(str.upper())
print(str.lower())
print(str.lstrip())
print(str.rstrip())
print(str.replace('Python','C'))
print(str.split())

print(len(str))