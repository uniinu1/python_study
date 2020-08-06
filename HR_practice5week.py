#리스트에 대해 공부합니다.

#리스트 선언, 초기화
'''
oddnumber = [1,3,5,7,9]
cafes = ['star','bene','yoger','friends']
A = [1,5,'A','CC','B']

listINlist = [[1,3,5,6,7], cafes, oddnumber, 1,3,'Abc']

print(oddnumber)
print(cafes)
print(A)
print(listINlist)

#리스트 값에 인덱싱을 통해 접근이 가능하다.

a = oddnumber[3] #리스트도 항상 인덱스는 0부터 시작한다.
b = cafes[1]
c = A[2]
d = listINlist[0][1] #리스트 내부의 리스트값에 접근

print(a)
print(b)
print(c)
print(d)

print(a+d , oddnumber[4] * listINlist[4]) # 리스트 내부 값에 접근해서 바로 숫자 연산이 가능하기
print(b+c) #리스트 내부 문자열에 접근해서 바로 문자열 덧셈 연산이 가능

#리스트는 슬라이싱도 가능하다.
a1 = oddnumber[1:5]
b1 = cafes[1:]
c1 = A[:2]
d1 = listINlist[0][1:4]

print(a1)
print(b1)
print(c1)
print(d1)
'''
'''
evennumbers = [2, 4, 6, 8, 10]
oddnumbers = [1, 3, 5, 7, 9]

numbers = evennumbers + oddnumbers

numbers[4:5] = [80]
print(numbers)

numbers[2:6] = "hello"
print(numbers)

numbers[2:3] = ['a','b','c']
print(numbers)

numbers[8] = ['a', 'b', 'c'] #인덱스 8에 슬라이스 자체를 대입
print(numbers)

numbers[:] = [1]
print(numbers) #왜 numbers list의 전부가 1로 바뀌는게아니고 list 자체가 1 하나의 값만 가지는 list로 변경되는지?
'''

# list에 다양한 함수를 사용해보자
'''
evennumber = [2,4,6,8]
oddnumber = [1,3,5,7]

print(evennumber, oddnumber)

evennumber.append(10)
oddnumber.append(9)

print(evennumber, oddnumber)

numbers = evennumber + oddnumber
print(numbers) # 바로 정렬되어서 나오지 않음에 유의한다.

numbers.sort()
print(numbers)

numbers.reverse()
print(numbers)

numbers.insert(3, [11,12,13])
print(numbers)

numbers.remove(9)
print(numbers)
print(numbers.pop())
print(numbers)

#append와 extend의 차이
numbers.extend(['a','b','c'])
print(numbers)

numbers.append(['a','b','c'])
print(numbers)

print(numbers.index(6))
print(numbers.count(4))

print(len(numbers))
'''

#리스트 사용시 주의해야 할 것들

# 공백 리스트를 초기화하지 않은 상태에서 리스트 인덱스를 사용해 바로 값을 넣을 수 없다.
drawer =[] #공백 리스트 생성
# drawer[0]='양말' # 만들어지지 않은 0번 인덱스에 값을 할당?
print(drawer) #당연히 오류가 뜬다.

drawer.append("양말") # 먼저 list에 값을 넣을 수 있는 공간(index)를 만들어 준 뒤, 값을 넣어줘야하므로
#위와같이 append등의 index를 먼저 생성하는 함수를 이용해 값을 넣도록 한다.
print(drawer)

