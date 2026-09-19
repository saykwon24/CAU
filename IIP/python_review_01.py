a = 3+4		# 자료형 지정 필요 없음.
b = 7/4		# 참고로, 문장 끝에 ‘;’ 필요 없음.

print(a)		# 7
print(b)		# 1.75

print(type(a))	# <class 'int'>
print(type(b))	# <class 'float'>

z = float(a)	# 자료형 변환 (int -> float)
print(z)		# 7.0
print(type(z))	# <class 'float'>

b = 7/4		    # 부동 소수점 나누기
print(b)		# 1.75
print(7/4)	    # 1.75
print(7//4)	    # 1 -> (정수 나누기 후) 몫
print(7%4)	    # 3 -> (정수 나누기 후) 나머지
print (7%4)	    # 3 -> print와 ( 사이에 공백 넣어도 무방함.
print ( 7%4 )	# 3 -> (...) 내의 인자 앞 뒤로 공백 넣어도 무방함.

sum = 100 + \
      200 + \
      300	# 긴 라인의 경우, \를 사용함.	
print(sum)	# 600


a = True			    # True와 False는 reserved keywords임.
print(type(a))		    # <class 'bool'>이 출력됨.
#b = TRUE		        # Error. 파이썬은 대/소문자를 구별함.
c = a and (3>4)		    # False가 출력됨. 참고로, ‘&’ 기호를 사용할 수도 있음.
print(c)			    # False가 출력됨.
print(a or (3>4))		# True가 출력됨. 참고로, ‘|’ 기호를 사용할 수도 있음.
print((not a) or c)		# False가 출력됨.

d = 'hello'		    # "hello"도 사용 가능함. (그러나, ‘hello’, “hello”는 안됨)
print(d)			# hello 가 출력됨.
print(type(d))		# <class 'str'>이 출력됨.

z = 'abcdefg'
print(z[0])	    # a (1번째 문자 추출)
print(z[2])	    # c (3번째 문자 추출)
print(z[-1])	# g (끝에서 1번째 문자 추출)
print(z[-3])	# e (끝에서 3번째 문자 추출)

y = 'hijk'
x = y+z[1]+z	# 문자열 결합 (concatenation) (즉, 전체가 1개의 문자열)
print(x)		# hijkbabcdefg


xx = 5
yy = 3.2

print("%2d" %xx)		# ⊔5 가 출력됨. 단..., ⊔는 공백을 의미함. "%2d"와 %xx 사이에 comma 없음.
print("%3d" %xx) 		# ⊔⊔5 가 출력됨.
print("%6.2f" %yy) 		# ⊔⊔3.20이 출력됨.
print("%7.4f" %yy) 		# ⊔3.2000 이 출력됨.

print(f'{xx:2d}')		# ⊔5 가 출력됨. 단..., ⊔는 공백을 의미함.
print(f'{xx:3d}') 		# ⊔⊔5 가 출력됨.
print(f'{yy:6.2f}') 	# ⊔⊔3.20이 출력됨.
print(f'{yy:7.4f}')		# ⊔3.2000 이 출력됨.


z = 'abcdefghijk'
print(z[0:2])	# ab (end '직전' 원소까지만 포함함)
print(z[1:4])	# bcd (end '직전' 원소까지만 포함함)

print(z[:3])	# abc (start 생략하면 진행 방향의 1번째 원소부터 시작)
print(z[3:])	# defghijk (end 생략하면 진행 방향의 마지막 원소까지 포함)
print(z[:])	    # abcdefghijk (z[:]는 사실상 z와 같음)

print(z[-3:])	# ijk (끝에서 3번째 원소부터 시작함)
print(z[-4:-1])	# hij (end '직전' 원소까지만 포함함)


z = 'abcdefghijk'
print(z[::2])	    # acegik (step 값만큼 jump하면서 진행함) 
print(z[0:-1:2])	# acegi (step 값만큼 jump하면서 진행함) 
print(z[1:-1:3])	# beh (step 값만큼 jump하면서 진행함) 
print(z[-3::-2])	# igeca
print(z[-3:0:-2])	# igec


# List and Tuple
aa = [1, 2, 3]	# 리스트 생성/정의
bb = (1, 2, 3)	# 튜플 생성/정의 (괄호 생략 가능)
print(aa[1])	# 2
print(bb[2])	# 3

aa[1] = 5	    # 2가 5로 바뀜.
print(aa[1])	# 5
#bb[1] = 5	    # Error. 튜플의 경우, 항목의 추가, 삭제, 변경이 허용되지 않음.
		        # 튜플의 경우, 메모리 효율성이 더 좋으며, 처리 속도가 더 빠름.

aa = [1, 2, 3]
print(aa)		# [1, 2, 3]

aa.append(7)	# 리스트 끝에 항목을 추가함. [1, 2, 3, 7]이 됨.
aa.insert(1, 8)	# 원하는 위치에 항목을 추가함. [1, 8, 2, 3, 7]이 됨.
del aa[2]		# 원하는 위치의 항목을 삭제함. [1, 8, 3, 7]이 됨.
print(aa[1:3])	# slice 형태로 사용할 수 있음. [8, 3]이 출력됨.

# un-packing (for list, tuple, string, .....)
bb = (1, 2, 3)	    # 튜플 생성/정의 (괄호 생략 가능)
(b0, b1, b2)=bb	    # b0, b1, b2에 각각 1, 2, 3이 할당됨 (un-packing).
		            # 참고로, (b0, b1, b2)에서 괄호를 사용하지 않아도 무방함.
print(b0, b1, b2)	# 1 2 3


# Dictionary
aa = {42:'Tom', 20:'Jane', 23:'John'}	# 중괄호 (curly bracket) 안에 표시함. 
bb = {'Mike':65, 'Bob':80}			    # key:value 형태의 항목들로 구성됨.
print(aa[42])		                    # Tom
print(bb['Mike'])	                    # 65

for k in aa.keys( ):		    # k 대신 다른 문자 사용 가능.
    print(k)			        # 42, 20, 23...이 (서로 다른 줄에) 출력됨.
for v in aa.values( ):
    print(v) 			        # Tom, Jane, John...이 (서로 다른 줄에) 출력됨.
for key, value in aa.items():
    print(f"{key}: {value}")	# 42: Tom, 20: Jane, 23: John ...이 (서로 다른 줄에) 출력됨.


# if...else statement
x = 1
if x < 0:			    # if 라인 마지막에 ':' 필요함.
    print('abc')		# {...} 등의 기호를 사용하지 않고 공백(indentation)으로 구조를 표시하고, 대개 4칸의 공백을 사용함.
elif x == 0:		    # elseif가 아니고, elif를 사용함.
    print('defg')
else:
    if x > 2:
        print('hijk')	# nested 구조도 구현할 수 있음.
    else:
        print('lmn')	# x = 1일 경우, lmn이 출력됨.


# for [변수] in [iterable]: 형태로 사용하며,
# [iterable]의 예는 list, tuple, 문자열 (string), ... 등등 매우 다양함.
LLL = [1, 2, 5]
for aa in LLL:
    print(aa)		# 1, 2, 5가 (서로 다른 줄에) 출력됨.

S1 = 'hello'
for c in S1:
    print(c)		# h, e, l, l, o가 (서로 다른 줄에) 출력됨.


# for [변수] in [iterable]: 구문에서
# [iterable]의 예로 range( ) 함수를 사용하는 경우도 많으며, range( ) 함수의 사용법은 슬라이스 사용법과 비슷함.
for x in range(0, 3, 1):	# for 라인 끝에 콜론 잊지 말 것.
    print(x)		        # 0, 1, 2가 (서로 다른 줄에) 출력됨.

for x in range(3, 11, 2):
    print(x)		        # 3, 5, 7, 9가 (서로 다른 줄에) 출력됨.

for x in range(4):		    # default start 값은 0, stop 값은 생략할 수 없음.
    print(x)		        # 0, 1, 2, 3이 (서로 다른 줄에) 출력됨.


# while, break, continue 사용 방법은 C 언어에서와 같음.
x = 1
while (x<10):
    print(x)	# 1, 2, ..., 9가 (서로 다른 줄에) 출력됨.
    x = x+1

x = 1
while (x<10):
    if (x == 5):
        break		# while 문 종료
    print(x)		# 1, 2, 3, 4가 (서로 다른 줄에) 출력됨.
    x += 1		    # x=x+1 과 같은 효과임.

x = 0
while (x<10):
    x = x+1
    if (x%2 == 0):		# 짝수인 경우
        continue		# 잔여 코드는 생략하고 블록 처음으로 돌아감.
    print(x)		    # 1, 3, 5, 7, 9가 (서로 다른 줄에) 출력됨.



# enumerate는 (리스트, 튜플, 문자열 등의) iterable을 순회하면서 각 요소의 인덱스와 값을 동시에 얻을 수 있게 해주는 내장 함수임.
fruits = ["apple", "banana", "cherry"]
for index, fruit in enumerate(fruits):
    print(index, fruit)				# 0 apple\n 1 banana\n 2 cherry

names = ['Alice', 'Bob', 'Charlie', 'David']
for i, name in enumerate(names, start=11):		# 시작 인덱스를 11로 지정
    print(f"{i} --> {name}")			        # 11 --> Alice, 12 --> Bob, .....


# 기존의 리스트에서 조건을 만족하는 항목만 추출하여 새로운 리스트 구성
# (초보자 관점에서는) readability가 다소 떨어지나... (속도, 메모리 효율) 관점에서 유리함.
X = list(range(1, 21))			                        # [1, 2, 3, ..., 20]
Y1 = [x for x in X if (x%2 == 0)]		                # [2, 4, 6, ..., 20]
Y2 = [a for a in X if 5 < (a**2) < 50]	                # [3, 4, 5, 6, 7]
Y3 = [x if x%2 == 0 else x**2 for x in range(1, 11)]	# [1, 2, 9, 4, 25, 6, 49, 8, 81, 10]
print(Y1, Y2, Y3)

words = ['apple', 'banana', 'cherry', 'boat', 'camera']
long_words = [w for w in words if len(w) > 5]		    # ['banana', 'cherry', 'camera']
b_words = [w for w in words if w.startswith('b')]		# ['banana', 'boat']

print(long_words, b_words)
