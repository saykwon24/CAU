# numpy는 수학 계산 함수 등을 모아 놓은 파이썬 라이브러리 (패키지)이며, 
# 기본 자료형은 n차원 배열(n-dimensional array = ndarray)
#
import numpy as np				# 대개 이 형태로 import함.

my_array = np.array( [[1, 2, 3], [7, 8, 9]] )
print(my_array)				    # [[1 2 3] (다음 줄에) [7 8 9]]
print(my_array.ndim)			# 2 (즉, 2차원 배열을 의미함)
print(my_array.shape)			# (2, 3)
print(my_array.size)			# 6 (= 2×3)
print(my_array.dtype)			# int32

print(type(123))				# <class 'int'>
print(type(123.456))			# <class 'float'>
print(type(my_array))			# <class 'numpy.ndarray'>


# 2D array
#
my_array = np.array( [[1, 2, 3], [7, 8, 9]] )
print( my_array.ndim )     # 2 (즉, 2차원 배열을 의미함)
print( my_array.shape )    # (2, 3)
print( my_array )          # [[1 2 3] \n [7 8 9]]

print( my_array[0][0] )	   # 1	참고로, my_array[0, 0]도 사용 가능.
print( my_array[0][1] )	   # 2
print( my_array[0][2] )	   # 3
print( my_array[0] )	   # [1 2 3]

print( my_array[1][0] )	   # 7
print( my_array[1][1] )	   # 8
print( my_array[1][2] )	   # 9
print( my_array[1] )	   # [7 8 9]


# 3D array
#
my_array = np.array( [[[1, 2], [3, 4]], [[5, 6], [7, 8]]] )
print( my_array.ndim )	  # 3 (즉, 3차원 배열을 의미함)
print( my_array.shape )	  # (2, 2, 2)
print( my_array )

print( my_array[0][0][0] )	# 1
print( my_array[0][1][1] )	# 4
print( my_array[1][0][1] )	# 6
print( my_array[0][0] ) 	# [1 2]
print( my_array[0][1] ) 	# [3 4]
print( my_array[0] )		# [[1 2] \n [3 4]]

print( my_array[1][0] )	    # [5 6]
print( my_array[1][1] )	    # [7 8]
print( my_array[1] )		# [[5 6] \n [7 8]]


# 1D and 0D arrays
#
my_array = np.array( [5, 6, 7, 8] )
print( my_array.ndim )	    # 1 (즉, 1차원 배열을 의미함)
print( my_array.shape )	    # (4,)
print( my_array )		    # [5 6 7 8]

print( my_array[0] )		# 5
print( my_array[1] )		# 6
print( my_array[2] )		# 7
print( my_array[3] )		# 8

my_array = np.array( 7 )
print( my_array.ndim )	    # 0 (즉, 0차원 배열을 의미함)
print( my_array.shape )	    # ()
print( my_array )		    # 7


# ones/zeros 함수 및 random 함수
# ones/zeros 함수: np.ones(shape, dtype) -> default dtype: float (numpy.float64)
# random 함수: np.random.rand(d0, d1, ..., dn)
#
print( np.ones((2, 2)) )		# (2, 2) 전체가 shape 인자를 나타냄.
print( np.zeros((3,), int) )

np.random.seed(999)		        # 결과 재현성이 필요할 경우 사용
print( np.random.rand(3, 2) )	# 구간 [0, 1) 사이의 uniform distribution
print( np.random.randn(2, 2) )	# 평균 0, 표준편차 1의 정규분포


# Multi-dimensional array
#
x=3, y=4, z=2
xx = np.ones((x, y, z))     # 또는... np.ones((x, y, z, w))
print(xx)


# Numpy basic operations
#
arr = np.array([[10, 20, 30], [40, 50, 60]])
print(arr[:, 1])		# [20 50]
print(arr[1, :])		# [40 50 60]

data = np.array([1, -2, 3, -4, 5])
mask = data > 0
print(mask)		                        # [True  False  True  False  True]
print(data[mask])		                # [1 3 5]
print(np.where(data > 0, data**2, 0))	# [1  0  9  0 25]

array1 = np.array([[1, 2], [3, 4]])
array2 = np.array([[2, 2], [2, 2]])
print(array1)	 # [[1 2] \n [3 4]]
print(array2)	 # [[2 2] \n [2 2]]

print( array1 + array2 )		    # 성분별 덧셈
print( array1 * array2 ) 		    # 성분별 곱셈
print( np.dot(array1, array2) )		# 행렬 (배열) 곱셈
print( array1 @ array2 ) 		    # 행렬 (배열) 곱셈 (Python 3.5 이후 버전만 가능)


# Broadcasting: 서로 다른 차원/형상을 갖는 배열 사이의 연산이 가능하도록 하는 파이썬 (numpy)의 기능
#
aa = np.array( [[2, 3]] )
bb = np.array( [[1, 2], [4, 5]] )

print(aa)			        # [[2 3]]
print(aa.transpose())	    # [[2] (다음 줄에) [3]]
print(aa+3)		            # [[5 6]]
print(bb*2)		            # [[2 4] (다음 줄에) [8 10]]
print(aa+bb)		        # [[3 5] (다음 줄에) [6 8]]
print(aa.transpose()+bb)	# [[3 4] (다음 줄에) [7 8]]


# arange 및 reshape method
#
print(np.arange(4))
print(np.arange(1, 2, 0.2))	    # (start, end, step)

print(np.arange(12))
print(np.arange(12).reshape(3, 4))
print(np.arange(12).reshape(2, -1))
print(np.arange(12).reshape(2, -1, 3))


# np.sum(xx, axis=n): n번 axis의 인덱스만 다른 항목들을 모두 더해 줌.
#
xx = np.array( [[4, 5, 6], [1, 2, 3]] )

print( xx )
print( np.sum(xx) )			    # 21
print( np.sum(xx, axis=0) )		# [5 7 9]
print( np.sum(xx, axis=1) )		# [15 6]

print( xx.shape )			        # (2, 3)
print( np.sum(xx, axis=0).shape )	# (3,)
print( np.sum(xx, axis=1).shape )	# (2,)

xx = np.array( [[[1, 2, 3], [4, 5, 6]], [[10, 20, 30], [40, 50, 60]]] )
print( xx )
print( np.sum(xx, axis = 0) )
print( np.sum(xx, axis = 1) )
print( np.sum(xx, axis = 2) )

print( xx.shape )                       # (2, 2, 3)
print( np.sum(xx, axis = 0).shape )     # (2, 3)
print( np.sum(xx, axis = 1).shape )     # (2, 3)
print( np.sum(xx, axis = 2).shape )     # (2, 2)


# np.argmax(xx, axis=n): n번 axis의 인덱스만 다른 항목들을 서로 비교함.
#
xx = np.array([10, 20, 30])
print(np.argmax(xx))		# 30에 대응하는 index인 2가 출력됨.

xx = np.array([[40, 20, 60], [10, 30, 10]])
print(np.argmin(xx))		# (첫번째) 10에 대응하는 index인 3이 출력됨.

print(np.argmax(xx, axis=0))		# [0 1 0]
print(np.argmax(xx, axis=1))		# [2 1]

print(xx.shape)			            # (2, 3)
print(np.argmax(xx, axis=0).shape)	# (3,)
print(np.argmax(xx, axis=1).shape)	# (2,)

xx = np.array([[[1, 8], [3, 1]], [[5, 2], [7, 4]], [[6, 5], [4, 9]]])
print(xx)
print(np.argmax(xx, axis=0))
print(np.argmax(xx, axis=1))
print(np.argmax(xx, axis=2))

print(xx.shape)			            # (3, 2, 2)
print(np.argmax(xx, axis=0).shape)	# (2, 2)
print(np.argmax(xx, axis=1).shape)	# (3, 2)
print(np.argmax(xx, axis=2).shape)	# (3, 2)
