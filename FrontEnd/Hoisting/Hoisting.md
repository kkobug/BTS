# 호이스팅

JavaScrpit 기준

### 호이스팅이란?

**스코프** 내부 어디서든 변수 선언은 최상위에 선언된 것처럼 행동



### 변수

let         const          var



### var

1. **한번 선언된 변수를 다시 선언할 수 있다.**

![image-20220811100438843](C:\Users\PARK\AppData\Roaming\Typora\typora-user-images\image-20220811100438843.png)

let은?

![image-20220811100531092](C:\Users\PARK\AppData\Roaming\Typora\typora-user-images\image-20220811100531092.png)

에러 발생



2. **선언하기 전에 사용할 수 있다.**

![image-20220811100701876](C:\Users\PARK\AppData\Roaming\Typora\typora-user-images\image-20220811100701876.png)

에러가 발생하지 않는다

![image-20220811100927925](C:\Users\PARK\AppData\Roaming\Typora\typora-user-images\image-20220811100927925.png)

코드가 실제로 이동하진 않지만 **최상위로 끌어올리는 것 처럼 동작** 

이것을 **호이스팅(Hoisting)** 이라고 한다.



하지만 undefined 라고 뜨는 이유는

![image-20220811101253310](C:\Users\PARK\AppData\Roaming\Typora\typora-user-images\image-20220811101253310.png)

변수의 선언은 호이스팅 되지만 할당은 호이스팅 되지 않기 때문

할당은 19번 줄에서 처리된다



let은?

![image-20220811101616625](C:\Users\PARK\AppData\Roaming\Typora\typora-user-images\image-20220811101616625.png)

에러가 발생하는데 호이스팅이 되지 않는 것일까?



### **let**과 **const**도 호이스팅이 된다

하지만  **T**emporal **D**ead **Z**one (TDZ) 의 영향을 받는다

<img src="C:\Users\PARK\AppData\Roaming\Typora\typora-user-images\image-20220811204227862.png" alt="image-20220811204227862" style="zoom: 50%;" />

TDZ 영역의 변수들은 사용할 수 없음 (할당을 하기 전에는 사용할 수 없음)

=> 코드를 예측 가능하게 하고 잠재적인 버그를 줄일 수 있음

![image-20220811115154941](C:\Users\PARK\AppData\Roaming\Typora\typora-user-images\image-20220811115154941.png)



다른 예를 확인

![image-20220811115956153](C:\Users\PARK\AppData\Roaming\Typora\typora-user-images\image-20220811115956153.png)![image-20220811120033279](C:\Users\PARK\AppData\Roaming\Typora\typora-user-images\image-20220811120033279.png)

정상적으로 작동										에러 발생		

​											

위에와 같이 **let**이 호이스팅 되지 않는 것이 아니라 

![image-20220811120316700](C:\Users\PARK\AppData\Roaming\Typora\typora-user-images\image-20220811120316700.png)

스코프 단위로 호이스팅

초록 영역이 하나의 스코프이므로 32번줄에서 호이스팅이 발생

31번줄은 TDZ 영역이기 때문에 에러 발생



## 변수의 생성 과정

1. 선언 단계

2. 초기화 단계

3. 할당 단계

### var

1. 선언 및 초기화 단계 (초기화: undefined 를 할당 해주는 단계)

	2. 할당 단계

### let

1. 선언 단계

2. 초기화 단계

3. 할당 단계

호이스팅 되면서 선언단계가 이루어지지만 초기화는 실제 코드에 도달했을때 되기 때문에 레퍼런스 에러가 발생

### const 

1. 선언 , 초기화 , 할당

![image-20220811121849235](C:\Users\PARK\AppData\Roaming\Typora\typora-user-images\image-20220811121849235.png)

선언과 동시에 할당을 하지 않았기 때문에 에러발생



## 스코프

함수가 실행될때, **함수 내에서 변수에 대한 접근이 어떻게 되든지**를 나타내는 용어



### var : 함수 스코프(function-scoped)

### let, const : 블록 스코프(block-scoped)

함수, if 문, for 문, while 문, try/catch 문 등



if 문 안에서 var 로 선언한 변수는 if 문 밖에서도 사용 가능

![image-20220811122437629](C:\Users\PARK\AppData\Roaming\Typora\typora-user-images\image-20220811122437629.png)

let 과 const 는 사용 불가능

<img src="C:\Users\PARK\AppData\Roaming\Typora\typora-user-images\image-20220811122537833.png" alt="image-20220811122537833" style="zoom: 80%;" /><img src="C:\Users\PARK\AppData\Roaming\Typora\typora-user-images\image-20220811122601347.png" alt="image-20220811122601347" style="zoom:80%;" />

var는 함수 스코프를 벗어날 수 없다

![image-20220811122826923](C:\Users\PARK\AppData\Roaming\Typora\typora-user-images\image-20220811122826923.png)