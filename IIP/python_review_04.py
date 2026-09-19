import matplotlib.pyplot as plt
import numpy as np

x = np.array( [0, 1, 2, 3] )
y = np.array( [3, 2, 4, 1] )

plt.scatter(x, y)	# scattered(흩뿌려진) 점 형태의 그래프
plt.show()		    # 이 라인 생략하면 왼쪽과 같이 나옴.
plt.plot(x, y)	    # 이어진 직선 형태 (이 외에도 다양한 형태의 그래프 가능)
plt.show()		    # (대개) 이 명령을 수행해야 메모리에 있는 내용을 실제로 그림으로 그려 줌.



x = np.arange(0.001, 1.5, 0.001)	# (start, end, step)
y1 = np.log(x)                      # log10 (base: 10) vs log (base: e)
y2 = -10*x*np.log(x)

plt.plot(x, y1, label='graph_1')
plt.plot(x, y2, label='graph_2')
# plt.plot(x, y1, c='purple', linewidth=5.5, label='graph_1')
# plt.plot(x, y2, linestyle='--', label='graph_2')
# solid (-), dotted (:), dashed (--), dashdot (-.)

plt.legend()
plt.grid(True)
plt.title('My Title')
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.show()



names = ['R', 'G', 'B']
values = [1, 1.5, 4]

plt.figure(dpi=100)
plt.subplot(1, 3, 1)
plt.bar(names, values)
plt.title('aaa')

plt.subplot(1, 3, 2)
plt.scatter(names, values)
plt.title('bbb')

plt.subplot(1, 3, 3)
plt.plot(names, values)
plt.title('ccc')

plt.suptitle('My Title')
plt.show()
