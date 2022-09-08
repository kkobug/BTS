# Redux

**Redux란?**

- 리액트에서 상태를 더 효율적으로 관리하는 데 사용하는 상태 관리 라이브러리
- 리덕스는 쉽게 설명하면 상태 관리의 로직을 컴포넌트 밖에서 처리 하는 것이다.
- 리덕스를 사용하면 스토어라는 개체 내부에 상태를 담게 된다.

**용어 정리**

- **액션(Action)** : 상태 변화를 일으킬 때 참조하는 객체이다.
    - const mapActionToProps = (dispatch) => { } 함수 사용
    - Action이라는 단어는 Event와 같아고 생각하면 된다.
    - dispatch 인수에서 Ruduce로 넘길 객체(type)를 정의한다.
    - Action이 실행되고 끝나면 type을 반환하는데 type은 Reduce로 전달된다.
- **스토어(Store)** : 애플리케이션의 상태 값들을 내장하고 있다.
    - state 값을 가지고 있다.
    - 중앙에서 변수 관리 개념이라고 생각하면 된다.
    - 리듀스에 의해서만 state의 값이 변경된다.
- **리듀서(Reducer)** : 상태를 변화시키는 로직이 있는 함수이다.
    - ex) export function reducer(state = {state : 10, age:100}, action)
    - Reducer 함수를 생성 할 때 살찐 에로우를 사용하지 않는다.
    - Reducer 함수는 순수함수여야 한다. 결과 값을 출력 할 때는 파라미터 값에만 의존해야 하며, 언제나 같은 결과를 출력해야 한다.
    - Reducer에서 state를 사용한다면 반드시 state를 초기화 해야 한다.
    - Reducer에서 state의 변화가 일어난다.
    - 값의 갱신은 반드시 reducer에서 해야 한다.
- **State** : 컴포넌트에 최종 출력하기 전 거치는 중간과정이다.
    - mpaStateToProps(state) 함수 사용
    - state는 store에서 가져왔다 라고 생각하면 된다.
    - Store에 저장되어 있는 변수를 가져와서 최종 가공을 위한 목적으로 사용된다.
    - 예를 들어, num:state.num*100 이라고 갱신을 하더라도 실제 num의 값은 갱신되지 않고 컴포넌트에 출력하는 값을 가공한 것이다.
    - 중간 과정을 거치게 되면 중간 수정이 가능하다. 원화를 달러로 바꿀 수 있듯이 가지고 있는 원화를 실제로 출력을 할 때는 달러로 출력을 하게 되는 것이며, 원화는 변화지 않는다.
- **디스패치(dispatch)** : 액션을 스토어에 전달하는 것을 의미한다.
- **구독** : 스토어 값이 필요한 컴포넌트는 스토어를 구독한다.
    - 리액트 컴포넌트에서 리덕스 스토어를 구독하는 작업은 후에 react-redux의 connect 함수가 대신 한다.
    - 리덕스의 내장 함수를 사용하여 subscribe, unsubscribe 함수를 사용하여 구독 및 구독 취소를 할 수 있다.
    
    ![Untitled](Redux%207e1f670420bf49218e60cb90a838ff87/Untitled.png)
    
    1. getState를 통해 state의 데이터를 요청
    2. state에서 데이터를 반환
    3. state 데이터를 통해서 ui를 랜더링
    4. subscribe : state가 변경될 때마다 render함수를 호출한다.
    
    ![Untitled](Redux%207e1f670420bf49218e60cb90a838ff87/Untitled%201.png)
    
    1. 유저가 이벤트를 작동
    2. Dispatch를 발생
    3. Dispatch가 Reducer를 호출
    4. Reducer가 state의 데이터를 변환
    5. Dispatch가 subscribe를 호출
    6. subscribe가 render를 호출
    7. 위에 과정을 진행
    
    # redux의 세가지 규칙
    
    ### 1. 단일 스토어
    
    하나의 애플리케이션 안에는 하나의 스토어가 있다. 여러개의 스토어를 사용하는것이 불가는 한건 아니지만 상태관리가 복잡해질수 있어 권장 하지 않는다.
    
    ### 2. 읽기 전용 상태
    
    리덕스의 상태는 읽기 전용이다.기존에 리액트에서 setState를 사용하여 state를 업데이트할 때도 객체나 배열을 업데이트 하는 과정에서 불변성을 지켜주기 위해 spread연산자를 사용하거나 immer와 같은 불변성 관리 라이브러리를 사용했다. 리덕스도 마찬가지이다.**상태를 업데이트 할때는 기존의 객체는 건드리지 않고 새로운 객체를 생성해 주어야 한다.**
    
    ### 3. 리듀서는 순수한 함수
    
    순수한 함수는?
    
    - 리듀서 함수는 이전 상태와 액션 객체를 파라미터로 받는다
    - 파라미터 외의 값에는 의존하면 안된다.
    - 이전 상태는 절대로 건드리지 않고, 변화를 준 새로운 상태 객체를 만들어서 반환한다.
    - 똑같은 파라미터로 호출된 리듀서 함수는 언제나 똑같은 결과 값을 반환해야 한다.
    
    참고
    
    [https://biio-studying.tistory.com/103](https://biio-studying.tistory.com/103)
    
    [https://hwan1001.tistory.com/38](https://hwan1001.tistory.com/38)
    
    [https://velog.io/@gay0ung/Redux](https://velog.io/@gay0ung/Redux)
    
    [https://velog.io/@junghyunhao/Redux-l5y6fs8n](https://velog.io/@junghyunhao/Redux-l5y6fs8n)