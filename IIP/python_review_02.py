# 함수 정의는 def 키워드로 시작함.
#
def print_hello():		# (인자가 없는) 함수 정의
    print('hello')

print_hello()		    # 함수 호출 (hello 가 출력됨). 함수 정의를 먼저 해야 함.

def add_two(a, b):	    # (2개의 인자가 있는) 함수 정의
    return a+b

print(add_two(2, 3))	# 5
print(add_two(5, 4))	# 9


# Function Overloading: 같은 이름의 함수를 인자의 타입 또는 개수를 달리하여 여러 개 정의할 수 있는 기능
# C++의 경우, FO를 지원하므로 아래와 같이 사용할 수 있으나, C 언어의 경우, FO를 지원하지 않으므로 아래와 같이 정의하면 (컴파일) Error
#
"""
int add_two(int a, int b) {
    return a + b;
}
float add_two(float a, float b) {
    return a + b;
}

# 즉, C 언어의 경우, FO를 지원하지 않으므로 다음과 같이 사용해야 함.
int add_two_int(int a, int b) {
    return a + b;
}
float add_two_float(float a, float b) {
    return a + b;
}
"""

# Dynamic Typing: 변수의 타입이 컴파일 시점이 아니라 실행 시점에 결정되는 언어의 특성
# Duck Typing: 객체의 타입 자체를 따지지 않고 필요한 연산이나 메서드가 존재하면 그냥 실행하는 프로그래밍 방식
# 파이썬의 경우, dynamic typing (및 duck typing)의 특성을 가지므로 function overloading의 ‘효과’를 갖게 됨.
#
def add_two(a, b):	        # (2개의 인자가 있는) 함수 정의
    return a+b

print(add_two(2, 3))	    # 5
print(add_two(2.0, 3.0))	# 5.0


# (*args): 여러 개의 positional argument (위치 인자)를 tuple 형태로 전달
# (**kwargs): 여러 개의 keyword argument (키워드 인자)를 dict 형태로 전달
#
def print_args(*args):	    # 임의의 수의 인자를 받을 수도 있음.
    print(args)		        # 반드시 args 라는 이름을 사용해야 하는 것은 아님.

print_args(1, 2, 3, 4)	    # (1, 2, 3, 4)
print_args('a', 'b', 'c')	# ('a', 'b', 'c')

def add_args(*args):
    total = 0
    for n in args:		    # 참고로, args는 tuple 형태임.
        total += n
    return total

print(add_args(1, 2, 3, 4))     # 10
print(add_args(1.0, 2, 3))		# 6.0


def print_man(**kwargs):
    if kwargs.get('sex').upper() in ['M', 'MALE']:
        for key, value in kwargs.items():
            print(f"{key}: {value}")

print_man(name="Jane", sex="F", age=25, city="New York")
print_man(name="Mike", sex="Male", age=30, city="Los Angeles")
print_man(name="Sarah", sex="female", age=28, city="Chicago")
# name: Mike, sex: Male, age: 30, city: Los Angeles가 서로 다른 줄에 출력됨.


def print_two(A, B):
    print(A, B)

print_two("abc", "defg")		# (위치 인자 방식) abc defg
print_two("defg", "abc")		# (위치 인자 방식) defg abc
print_two(A="abc", B="defg")		# (키워드 인자 방식) abc defg
print_two(B="defg", A="abc")		# (키워드 인자 방식) abc defg

def print_two(A="abc", B="defg"):	# default 인자 지정
    print(A, B)

print_two( )			        # abc defg
print_two("hijk")			    # hijk defg
print_two(A="hijk")			    # hijk defg
print_two(B="hijk")			    # abc hijk
print_two(B="123", A="4567")	# 4567 123


# 외부 module 호출
#
import my_module		# 이 라인이 없을 경우, 아래 라인에서 에러 발생함.
my_module.do_it()		# hello가 출력됨.
#do_it()			    # Error

# module 이름이 길 경우, 다음과 같이 사용할 수도 있음.
import my_module as mm	# 또 다른 예: import numpy as np
mm.do_it2()		        # hello2

# 다음과 같이 필요한 함수만 import할 수도 있음.
from my_module import do_it
do_it()				# hello


# 현재 폴더 (즉, main.py 파일이 포함된 폴더) 아래의 ccc 폴더 내에 my_module.py 파일이 존재하는 경우에는 다음과 같이 사용함.
#
import ccc.my_module
ccc.my_module.do_it()		# hello

import ccc.my_module as mm
mm.do_it2()			# hello2

from ccc.my_module import do_it
do_it()				# hello


# 파일 입출력 (old ver.)
# 용례: file_obj = open(file_name, mode1, mode2)
# mode 1: r (read), a (append), x (해당 파일 없을 때에만 write), w (해당 파일 있어도 over-write)
# mode 2: t (text file), b (binary file). 단, default 옵션은 text 파일임.
#
f = open("D:/zTest/zTemp/test.txt", 'w')	# 파일 open
for i in range(1, 11):				        # 1부터 10까지.
    print(f'{i:2d}번째 줄입니다.', file=f) 	  # 파일 write
f.close()						            # 파일 close

f = open("D:/zTest/zTemp/test.txt", 'r')	# 파일 open
read_file = f.read()					    # 파일 read
print(read_file)					        # 파일 내용이 그대로 출력됨.
f.close()						            # 파일 close


# 파일 입출력 (new ver.)
# 용례는 앞 페이지 내용과 같음  file_obj = open(file_name, mode1, mode2)
# 새로운 방식에서는 file을 close하는 것이 (예외 상황에서도) 자동으로 처리됨.
#
with open("D:/zTest/zTemp/test.txt", 'w') as f:
    for i in range(1, 11):
        f.write(f'{i:2d}번째 줄입니다.\n')

with open("D:/zTest/zTemp/test.txt", 'r') as f:
    read_file = f.read()
    print(read_file)


# class 정의
#
class Student:			            # 클래스 정의
    def __init__(self, name, ID):   # 생성자(constructor) 멤버 함수(method)에 해당함.
        self.st_name = name		    # st_name은 멤버 변수(attribute)에 해당함.
        self.st_ID = ID		        # st_ID도 멤버 변수에 해당함.

    def print_st(self):		    # print_st()는 (일반) 멤버 함수에 해당함.
        print(self.st_name)		# 대개 멤버 함수의 1번째 인자는 self임.
        print(self.st_ID)

s1 = Student('Jane', 123)		# s1이라는 객체(object) 정의
s1.print_st()			        # Jane, 123이 (서로 다른 줄에) 출력됨.
s2 = Student('Tom', 567)		# s2라는 객체 (object) 정의
s2.print_st()			        # Tom, 567이 (서로 다른 줄에) 출력됨.


# class inheritance
#
class Person:
    def __init__(self, name):
        self.name = name
    
    def show1(self):
        print('Name:', self.name)

    def show3(self):
        print('Name of this person:', self.name)


class Student(Person):	            # 괄호 안에 base class의 이름을 써 줌.
    def __init__(self, name, ID):
        super().__init__(name)	    # base class의 초기화 함수 호출
        # super(Student, self).__init__(name)   	# 이것도 가능.
        self.ID = ID

    def show2(self):
        print('Name =', self.name)
        print('ID =', self.ID)

    def show3(self):
        print('Name of this student:', self.name)
        
    def show4(self):
        super().show3()
        self.show2()

p1 = Person('Jane')

p1.show1()	# Name: Jane
p1.show3()	# Name of this person: Jane

s1 = Student('Tom', 123)

s1.show1()	# Name: Tom
s1.show2()	# Name = Tom, ID = 123
s1.show3()	# Name of this student: Tom  “method over-riding”
s1.show4()	# Name of this person: Tom, Name = Tom, ID = 123
