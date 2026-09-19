"""
import numpy as np
import torch

def print_header(title):
    print(f"\n{'='*50}\n{title}\n{'='*50}")


## numpy array vs. pytorch tensor
print_header("1. numpy array vs. pytorch tensor")
X = np.array( [[1, 2, 3], [4, 5, 6]] )
Y = torch.tensor( [[1, 2, 3], [4, 5, 6]] )

print("numpy array:\n", X)			# [[1 2 3]\n[4 5 6]]
print("pytorch tensor:\n", Y)		# tensor([[1, 2, 3],\n[4, 5, 6]])
print()

print(type(X))		# <class 'numpy.ndarray'>
print(type(Y))		# <class 'torch.Tensor'>
print()

print(X.ndim)		# 2
print(Y.ndim)		# 2
print()

print(X.shape)		# (2, 3)
print(Y.shape)		# torch.Size([2, 3])
print()

print(np.array( [1, 2, 3] ).shape)		# (3,)
print(torch.tensor( [1, 2, 3] ).shape)	# torch.Size([3])
                                        # pytorch의 경우 shape이 1이면 생략
print()



## element 지정 방식: numpy array와 pytorch tensor는 element 지정 방식이 동일함.
print_header("2. element 지정 방식")

print("--- numpy array ---")
Y = np.array( [[1, 2, 3], [7, 8, 9]] )

print( Y.ndim )	    # 2 (즉, 2차원 배열을 의미함)
print( Y.shape )	# (2, 3)
print( Y )		    # [[1 2 3]\n[7 8 9]]
print()

print( Y[0][0] )	# 1
print( Y[0][1] )	# 2
print( Y[0][2] )	# 3
print( Y[0] )	    # [1 2 3]
print()

print( Y[1][0] )	# 7
print( Y[1][1] )	# 8
print( Y[1][2] )	# 9
print( Y[1] )	    # [7 8 9]
print()


print("--- pytorch tensor ---")
Z = torch.tensor( [[1, 2, 3], [7, 8, 9]] )

print( Z.ndim )	    # 2 (즉, 2차원 배열을 의미함)
print( Z.shape )	# torch.Size([2, 3])
print( Z )		    # tensor([[1, 2, 3],\n[7, 8, 9]])
print()

print( Z[0][0] )	# tensor(1)
print( Z[0][1] )	# tensor(2)
print( Z[0][2] )	# tensor(3)
print( Z[0] )	    # tensor([1, 2, 3])
print()

print( Z[1][0] )	# tensor(7)
print( Z[1][1] )	# tensor(8)
print( Z[1][2] )	# tensor(9)
print( Z[1] )	    # tensor([7, 8, 9])
print()



## numpy array -> pytorch tensor
print_header("3-1. numpy array -> pytorch tensor")
X = np.array( [[1, 2, 3], [4, 5, 6]] )

print('X =', X)		           # X = [[1 2 3]\n[4 5 6]]
print('type(X) =', type(X))	   # <class 'numpy.ndarray'>
print('X.shape =', X.shape)	   # (2, 3)
print()

Y = torch.from_numpy(X)	       # 방법 1) 메모리 공유 (X, Y가 서로의 변경 사항을 공유)
Y = torch.tensor(X)		       # 방법 2) 메모리 독립 복사본 생성 (Y 변경이 X에 영향을 주지 않음)
print('Y =', Y)		           # tensor([[1, 2, 3],\n[4, 5, 6]])
print('type(Y) =', type(Y))	   # <class 'torch.Tensor'>
print('Y.shape =', Y.shape)	   # torch.Size([2, 3])
print()


## pytorch tensor -> numpy array
print_header("3-2. pytorch tensor -> numpy array")
X = torch.tensor( [[1, 2, 3], [4, 5, 6]] ) 

print('X =', X)     		   # tensor([[1, 2, 3], (다음 줄에) [4, 5, 6]])
print('type(X) =', type(X))	   # <class 'torch.Tensor'>
print('X.shape =', X.shape)    # torch.Size([2, 3])
print()

Y = X.numpy()	               # 방법 1) 메모리 공유. 참고로, X가 GPU에 있는 경우, X.cpu().numpy() <- 권장!!
Y = X.numpy().copy()   	       # 방법 2) 메모리 독립 복사본 생성 (Y 변경이 X에 영향을 주지 않음)
print('Y =', Y)     		   # Y = [[1 2 3] (다음 줄에) [4 5 6]]
print('type(Y) =', type(Y))	   # <class 'numpy.ndarray'>
print('Y.shape =', Y.shape)	   # (2, 3)
print()



## detach(): requires_grad=True인 tensor는 .numpy()를 직접 호출할 수 없기 때문에 
#            detach() 를 사용하여 계산 그래프에서 분리한 후 변환해야 함.
print_header("4. detach()")
X = torch.zeros((2, 3), requires_grad=True)	   # 수동으로 requires_grad 속성을 설정하는 경우는 많지 않음. (default=True)

#Y = X.numpy()    # RuntimeError: Can't call numpy() on Tensor that requires grad. 
Y = X.detach()
Z = X.detach().numpy()

print(X), print(Y), print(Z)
print()



## squeeze(): 'dummy' dimension을 없애주는 function (dimension of size가 1인 것들 제거)
print_header("5. squeeze()")
X = torch.tensor([[1], [2], [3]])     # 2-D array
Y = torch.tensor([[[1, 2, 3, 4]]])    # 3-D array
X2 = X.squeeze()
Y2 = Y.squeeze()

print(X)     # tensor([[1],\n[2],\n[3]])
print(Y)     # tensor([[[1, 2, 3, 4]]])
print(X2)    # tensor([1, 2, 3])
print(Y2)    # tensor([1, 2, 3, 4])
print()

print(X.shape)		# torch.Size([3, 1])
print(Y.shape)		# torch.Size([1, 1, 4])
print(X2.shape)		# torch.Size([3])
print(Y2.shape)		# torch.Size([4])
print()



## unsqueeze(): squeeze()의 반대. 즉, 'dummy' dimension을 다시 표시해주는 function
print_header("6. unsqueeze()")
x = torch.tensor([1, 2, 3])
print(x)                 # torch.Size([3])
print(x.unsqueeze(0))    # 0차원에 추가: torch.Size([1, 3])
print(x.unsqueeze(1))    # 1차원에 추가: torch.Size([3, 1])
print()

x = torch.tensor( [[1, 2, 3], [4, 5, 6]] )
print(x)                 # torch.Size([2, 3])
print(x.unsqueeze(0))    # torch.Size([1, 2, 3])
print(x.unsqueeze(1))    # torch.Size([2, 1, 3])
print(x.unsqueeze(2))    # torch.Size([2, 3, 1])
print()
"""