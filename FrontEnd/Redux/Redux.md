# Redux

![https://velog.velcdn.com/images/wooder2050/post/22581891-9ac2-40c9-bfba-bf9b7dfe6b67/redux.jpg](https://velog.velcdn.com/images/wooder2050/post/22581891-9ac2-40c9-bfba-bf9b7dfe6b67/redux.jpg)

# Redux란?

- JavaScript 상태관리 라이브러리

### 상태(State)

- 프론트엔드의 개발단위인 컴포넌트에서 각 컨포넌트가 가지고 있는 데이터를 의미
- 컴포넌트간의 상태를 공유하기 위해서 props를 사용할 수 있음 ⇒ props drilling 발생가능

![https://s1.md5.ltd/image/971a2d43b177107e77c05825d45254b6.png](https://s1.md5.ltd/image/971a2d43b177107e77c05825d45254b6.png)

![https://miro.medium.com/max/1100/1*PBgAz9U9SrkINPo-n5glgw.gif](https://miro.medium.com/max/1100/1*PBgAz9U9SrkINPo-n5glgw.gif)

# Redux의 등장배경

### MVC 패턴

- 기존의 형상관리 패턴은 MVC패턴
    - Model - 데이터 형식과 구조 관리
    - View - 사용자에게 보여지는 부분
    - Controller - 데이터의 변화를 관리, 사용자 이벤트나 서버로부터 받는 데이터를 업데이트

![https://velog.velcdn.com/images%2Fwooder2050%2Fpost%2F61336ea0-dfe2-4b43-9872-2a7c09856d55%2Fmvc.png](https://velog.velcdn.com/images%2Fwooder2050%2Fpost%2F61336ea0-dfe2-4b43-9872-2a7c09856d55%2Fmvc.png)

- 앱의 큐모가 커지게 되면서 아래 그림처럼 데이터의 흐름을 추적하기가 어려워짐

![https://velog.velcdn.com/images%2Fwooder2050%2Fpost%2Fd4cbee2e-1cb2-447f-a1e7-3e1b734438d1%2F1_1PuUNCRYbYo8GNwgcniB6w.png](https://velog.velcdn.com/images%2Fwooder2050%2Fpost%2Fd4cbee2e-1cb2-447f-a1e7-3e1b734438d1%2F1_1PuUNCRYbYo8GNwgcniB6w.png)

⇒ Flux등장

### Flux

- Flux는 MVC의 복잡성을 개선
- 단방향 데이터흐름 적용
- 예측가능

![https://velog.velcdn.com/images%2Fwooder2050%2Fpost%2Fc1c916ed-0e47-4edf-aa30-c4e5a615a0a8%2Fda8da896a90d487161273d60076163ed.png](https://velog.velcdn.com/images%2Fwooder2050%2Fpost%2Fc1c916ed-0e47-4edf-aa30-c4e5a615a0a8%2Fda8da896a90d487161273d60076163ed.png)

⇒ Flux에 Reducer개념을 도입해 Redux탄생 (by Dan Abramov)

### Redux

- 제작자(Dan Abramov) 피셜 Flux대비 Redux의 장점
    1. 리듀서의 구성
    2. 서버 랜더링
    3. 좋은 개발자 경험
    4. 간결성

# Redux 동작과정

![https://velog.velcdn.com/images%2Fwooder2050%2Fpost%2F288a5d4e-d2d4-4891-9c6d-d537a0291355%2F1_N62EZSeQNHtwVumCQOdU-Q.png](https://velog.velcdn.com/images%2Fwooder2050%2Fpost%2F288a5d4e-d2d4-4891-9c6d-d537a0291355%2F1_N62EZSeQNHtwVumCQOdU-Q.png)

![https://ko.redux.js.org/assets/images/ReduxDataFlowDiagram-49fa8c3968371d9ef6f2a1486bd40a26.gif](https://ko.redux.js.org/assets/images/ReduxDataFlowDiagram-49fa8c3968371d9ef6f2a1486bd40a26.gif)

![https://miro.medium.com/max/1400/1*T_Q66EkNEhca6TyrvY1xBQ.gif](https://miro.medium.com/max/1400/1*T_Q66EkNEhca6TyrvY1xBQ.gif)

UI또는 서버에서의 데이터 변동 

⇒ Action 생성 

⇒ Store의 Reducer로 전달 

⇒ Reducer에서 데이터 조작 

⇒ State에 반영 

⇒ UI에 반영

# Redux의 3대원칙

## 1. **Single source of truth**

- 진실은 하나의 소스로부터
- 앱의 모든 상태는 하나의 스토어 안에 하나의 객체트리구조로 저장

⇒ 모든 데이터의 원천은 항상 스토어여야한다.

## 2. **State is read-only**

- 상태는 읽기전용이다.
- 상태를 직접변경해서는 안된다
- 상태의 변경은 오직 Reducer를 통해서만 가능
- 리덕스에서 불변성을 유지해야 하는 이유는 내부적으로 데이터가 변경 되는 것을 감지하기 위하여 shallow equality 검사를 하기 때문

### 불변성(immutable)

- 객체가 생성된 후 그 상태를 변경할 수 없는 디자인 패턴을 의미
- immutability는 함수형 프로그래밍의 핵심원리
- JavaScript에서 원시타입(String, Number, Boolean, Null, Undefined, Symbol)은 immutable
- 그 외의 타입 (Array, Object)는 변경가능하다.

```jsx
const 공주 = `강동옥`
공주 = `김태현` // Uncaught TypeError: ...

const BTS = [`김태현`, `임경훈`, `양지훈`, `조성현`, `강동옥`, `정인수`, `박준영`, `성아영`]
BTS[1] = `취업`
BTS[7] = `인턴`
console.log(BTS) // [`김태현`, `취업`, `양지훈`, `조성현`, `강동옥`, `정인수`, `박준영`, `인턴`]
```

⇒ 객체의 경우 메모리 주소를 할당하므로 객체는 동일하나 내용이 달라질 수 있음

```jsx
// 배열을 입력받아 첫요소를 바꾸고 반환하는 함수
function 난모룸(text) {
	text[0] = '난모룸'
	return text
}

const textList = ['가', '나', '다']

const newList = 난모룸(textList) 

console.log(textList) // ['난모룸', '나', '다']
console.log(newList) // ['난모룸', '나', '다']
```

⇒ 위 처럼 원본 값이 달라지는 불상사가 발생할 여지가 있음

## 3. **Changes are made with pure functions**

- 리듀서는 순수 함수여야한다.
- 순수 함수
    - 이전상태와 액션객체를 파라미터로 받음
    - 새로운 상태 객체를 만들어 반환
    - 똑같은 파라미터로 호출된 리듀서함수는 항상 같은 결과를 반환

# Redux의 장단점

### **장점**

- 단방향 모델링(한가지 방향으로만 바뀐다)
    - action을 dispatch 할때마다 기록(history)이 남아 에러를 찾기 쉽고.  기록을 활용해 타임머신 기능을 사용할 수 있음
- 상태의 중앙화
    - 스토어(Store)라는 이름의 전역 자바스크립트 변수를 통해 상태를 한 곳에서 관리하는데, 이를 중앙화라 함. 전역 상태를 관리할때 굉장히 효과적
- Redux는 상태를 읽기 전용으로 취급
    - 상태가 읽기 전용이므로, 이전 상태로 돌아가기 위해서는 이전 상태를 현재 상태에 덮어쓰기만 하면 됨**.** 이런 식으로 실행 취소 기능을 구현.

### **단점**

- 아주 작은 기능이여도 리덕스로 구현하는 순간 몇 개의 파일(액션등을 미리 만들어놔야함)들을 필수로 만들어야하여 코드량이 늘어난다.
- 불변성 개념을 지키기 위해 매번 state라는 객체를 만들어줘야 함
- Redux는 상태를 읽기 전용으로 취급할 뿐, 실제 읽기 전용으로 만들어주지는 않음. 때문에 상태를 실수로 직접 변경하지 않도록 항상 주의해야 한다.

# Reference

> [https://amyhyemi.tistory.com/103](https://amyhyemi.tistory.com/103)
> 

> [https://velog.io/@wooder2050/리덕스Redux는-왜-쓰는-건데](https://velog.io/@wooder2050/%EB%A6%AC%EB%8D%95%EC%8A%A4Redux%EB%8A%94-%EC%99%9C-%EC%93%B0%EB%8A%94-%EA%B1%B4%EB%8D%B0)
> 

> [https://medium.com/lunit/redux가-필요하다는-것을-언제-알-수-있나요-426a148da64d](https://medium.com/lunit/redux%EA%B0%80-%ED%95%84%EC%9A%94%ED%95%98%EB%8B%A4%EB%8A%94-%EA%B2%83%EC%9D%84-%EC%96%B8%EC%A0%9C-%EC%95%8C-%EC%88%98-%EC%9E%88%EB%82%98%EC%9A%94-426a148da64d)
>