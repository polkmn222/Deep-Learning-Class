#!/usr/bin/env python
# coding: utf-8

# 다음주 즈음에 케라스를 활용한 선형회귀를 구현해 보겠지만 기본적인 케라스 모델을 구현하는 방식은 아래와 같이 이루어집니다. 
# 
# Sequential로 model이라는 이름의 모델을 생성하고, 그에 따른 add함수를 통해
# 입력과 출력 벡터의 차원과 같은 필요 정보들을 추가합니다.

# In[1]:


# ## 예시코드로써 실행이 되진 않습니다.
# model = Sequential()
# model.add(keras.layers.Dense(1, input_dim=1))


# In[2]:


import numpy as np
import matplotlib.pyplot as plt
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras import optimizers


# In[3]:


X = [1,2,3,4,5,6,7,8,9] # 공부하는 시간
y = [11,22,33,44,53,66,77,87,95] # 각 공부하는 시간에 매핑되는 성적

model = Sequential()

# 출력 y의 차원은 1. 입력 x의 차원(input_dim)은 1이다
# 선형회귀를 구현할 것이므로 activation(활성화 함수라고도)구현하려는 
# 함수를 의미한다. 

model.add(Dense(1, input_dim=1, activation='linear'))

# sgd는 경사 하강법을 의미. 학습률(Learing_rate, 이하 lr)은 0.01
sgd = optimizers.SGD(lr=0.01)

# 손실함수(loss function)은 평균제곱오차 mse를 사용한다.
model.compile(optimizer=sgd, loss='mse', metrics=['mse'])

# 주어진 x와 y데이터에 대해서 오차를 최소화하는 작업을 300번 시도해보자.
model.fit(X,y, epochs=2)


# In[4]:


plt.plot(X, model.predict(X), 'b', X,y, 'k.')


# In[5]:


# end of files

