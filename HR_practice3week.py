# 변수에 값을 입력하고 출력하기 : input 함수


'''
a= input("값을 입력하세요 : ")
print(a);
'''

# 두 변수에 값을 입력하고 그 값을 더한 값을 출력하기
'''
a= input("a에 들어갈 값을 입력하세요 : ")
b= input("b에 들어갈 값을 입력하세요 : ")

print("a+b = ",a+b,' 입니다.') #결과 값이 a+b 문자열의 형태로 출력된다.
'''

# 두 변수의 형을 숫자형으로 변경하여 그 값을 더해보기
'''
a= int(input("a에 들어갈 값을 입력하세요 : "))
b= float(input("b에 들어갈 값을 입력하세요 : "))

print("두 수를 더한 결과는 ",a+b,"입니다.")
print(type(a+b))
'''

# 여러가지 형태의 숫자형을 사용해보기
'''
a=10
b=-2.5
c=1+2j
d=0o21
e=0xDA

print(a,b,c,d,e)
print(c, c.real, c.imag, c.conjugate())
print(type(a),type(b),type(c),type(d),type(e))

print(a + b, type(a + b))
print(b + d, type(b + d))
print(d + e, type(d + e))
print(c + e, type(c + e))
'''

# bool 형 (True,False) 사용해보기
'''a1=True
if(a1==True):
    print("참")
else:
    print("거짓")

a = "Hello goorm!"
if (a):  # 만약 (a)의 값이 존재한다면
    print("참")
else:  # 아니면
    print("거짓")

b = ""
if (b):  # 만약 (b)의 값이 존재한다면
    print("참")
else:  # 아니면
    print("거짓")

c = 1
if (c):  # 만약 (c)의 값이 존재한다면
    print("참")
else:  # 아니면
    print("거짓")

d = []
if (d):  # 만약 (d)의 값이 존재한다면
    print("참")
else:  # 아니면
    print("거짓")

a2="Hello world!"
if(a2==True):
    print("참")
else:
    print("거짓")

b2=""
if(b2==False):
    print("참")
else:
    print("거짓")

c2=True
if(c2==True):
    print("참")
else:
    print("거짓")
'''

#수식 연산자를 다뤄보기
'''
num1 = 17.5
num2 = 10
cpx1 = 3 + 3j
cpx2 = 1 - 2j
str1 = "Hello"
str2 = "goorm"

print(num1 + num2)
print(str1 + str2)
print(num1 - num2)
print(num1 * num2)
print(num2 ** num1)
print(num1 / num2)
print(num1 // num2)
print(num1 % num2)
print(cpx1 / cpx2)
'''

#논리 연산자 AND OR NOT
a=True
b=False

print('True and False : ',a and b);
print('True and True : ',a and a);
print('True or False : ',a or b);
print("False or False : ",b or b);
print("not True : ", not a);
print("not False : ",not b);
print("False and False : ",b and b)