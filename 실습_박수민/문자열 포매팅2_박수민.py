# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean

name = input()
age = input()
height = float(input())

print(f"제 이름은 {name}입니다.")
print("제 나이는 {0:0>10}입니다.".format(age))
print("제 키는 {0: <8.2f}cm입니다.".format(height))
