# input : 사용자가 직접 값을 입력하여 변수에 집어넣음
a = input("값을 입력하세요 : ")

print(a)

print("- input은 문자형으로 받으므로 두 숫자를 더하기 위해서는 형 변환 필요")
a = int(input("정수를 입력하세요 : "))
b = float(input("실수를 입력하세요 : "))

print("두 수를 더한 결과는 :", a+b, "입니다.")
print(type(a+b))

# 숫자형
print("- 숫자형")
a = 10
b = -2.5
c = 1 + 2j
d = 0o21 # 17
e = 0xDA # 128

print(a, type(a))
print(b, type(b))
print(c, c.real , c.imag, c.conjugate(), type(c))
print(d, type(d))
print(e, type(e))

print(a + b, type(a + b))
print(b + d, type(b + d))
print(d + e, type(d + e))
print(c + e, type(c + e))

# 간단한 콘솔 입력과 숫자형 실습
print("- 간단한 콘솔 입력과 숫자형 실습")
a = int(input())
b = float(input())
c = 2j
d = 0xDA

print(a+b, type(a+b))
print(c.real, c.imag)
print(c+d, type(c+d))

"""파이썬엔서는 주어진 조건에 대한 참/거짓뿐만 아니라 값의 존재 유무에 따라 참/거짓을 판별한다. 다른 언어에서는 보통 1과 0을 참/거짓으로 많이 사용하지만, 파이썬은 좀 더 범위를 넓혀 값 자체가 존재하면 참, 존재하지 않으면 거짓으로 판별한다."""
print("- 참/거짓")
a = "Hello goorm!"
if (a) : #만약 (a)의 값이 존재한다면 
    print("참")
else : #아니면
    print("거짓")

b = ""
if (b) : #만약 (b)의 값이 존재한다면
    print("참")
else : #아니면
    print("거짓")
    
c = 1
if (c) : #만약 (c)의 값이 존재한다면
    print("참")
else : #아니면
    print("거짓")
    
d = []
if (d) : #만약 (d)의 값이 존재한다면
    print("참")
else : #아니면
    print("거짓")
