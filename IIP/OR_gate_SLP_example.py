"""
OR gate 학습 신경망(SLP) 구현 예제
>>> 참고: https://docs.pytorch.org
"""

"""
import torch
import torch.nn as nn

#torch.manual_seed(999)    # 결과 재현성이 필요할 경우 사용 (seed 값 고정)
                           # 즉, 정해진 sequence의 random number를 사용하여 항상 같은 결과가 나오도록 함.


X = torch.tensor([[0, 0], [0, 1], [1, 0], [1, 1]]).float()	  # (4, 2) 형태의 입력 데이터. nn.Linear()가 float type data를 기대(expect)함.
target = torch.tensor([0, 1, 1, 1])		                      # For (softmax + CEL). (4,) 형태.
##target = torch.tensor([[0], [1], [1], [1]]).float()	      # For (sigmoid + BCEL). (4, 1) 형태.
                                                              # (sigmoid + BCEL) 방식을 사용하려면, ‘##’로 표시한 4곳을 수정해야 함.

model = nn.Linear(2, 2)		# For (softmax + CEL): 입력 데이터 수=2, 출력 데이터 수=2
##model = nn.Linear(2, 1)	# For (sigmoid + BCEL): 입력 데이터 수=2, 출력 데이터 수=1

loss_func = nn.CrossEntropyLoss() 			# (softmax 레이어) + (CEL 레이어)에 해당
##loss_func = nn.BCEWithLogitsLoss()		# (sigmoid 레이어) + (BCEL 레이어)에 해당

num_epochs = 200				                           # epoch(~=반복 횟수) 지정
optimizer = torch.optim.SGD(model.parameters(), lr=0.2)	   # 다양한 optimizer 중 'Stochastic Gradient Descent(확률적 경사 하강법, BS=1)' 방식 사용


### 학습(training) 모드
model.train()	                  	    # model.train()이 default 옵션이므로 생략 가능하지만, 명시 권장!!
for epoch in range(num_epochs+1):	    # 현재 코드는 (0번부터 200번까지) 201번 반복하도록 되어 있음. (terminal 창에서 10 epoch 별로 학습 결과를 확인하기 위함)
    logits = model(X)		            # (4, 2) (for (softmax + CEL)) 또는 (4, 1) (for (sigmoid + BCEL)) 형태.
                                        # 참고로, 현재 방식은 'Batch Gradient Descent Method(BS=N=전체 학습 데이터 수=4)' 방식에 해당.
    loss = loss_func(logits, target)	# 손실 함수 계산. (logits ~= scores)

    optimizer.zero_grad()               # 기울기값을 0으로 초기화
    loss.backward()		                # 기울기값 계산
    optimizer.step()		            # 가중치 업데이트

    if epoch % 10 == 0:		                                      # 특정 조건(epoch = 10의 배수)을 만족할 때마다 현재 진행 상태 표시
        print(f'Epoch: {epoch:4d}  loss = {loss.item():8.5f}')	  # epoch 넘버 및 현재의 손실값 표시
        print('logits =', logits.detach().squeeze().numpy())	  # (logits ~= scores)
        print()


### 추론(evaluation, reference) 모드
model.eval()           	# 현재 코드에서는 필요 없으나, Dropout, BatchNorm 등과 사용할 때에는 반드시 필요.
with torch.no_grad():	# 자동미분을 위한 계산 그래프를 생성하지 않음 (메모리 절감 및 추론 속도 향상 효과)
    logits = model(X)	# (4, 2) 또는 (4, 1) 형태.

prediction = torch.argmax(logits, dim=1)	# For (softmax + CEL). (torch의 dim) = (numpy의 axis). 형태 변화: (4, 2) -> (4,)
##prediction = (logits > 0).float()		    # For (sigmoid + BCEL). (확률이 아닌) score이므로 (0.5가 아닌) 0과 비교해야 함.

print('prediction =', prediction.detach().squeeze().numpy())	# 예측 결과
print('target     =', target.squeeze().numpy())		            # 정답값
accuracy = (prediction == target).float().mean()		        # 예측값과 정답값 비교
print('accuracy   =', accuracy.item()*100, '%')
"""