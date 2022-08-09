# REST

## REST

REST는 Representational State Transfer 의 약자로 자원을 이름으로 구분해 자원의 상태를 주고 받는 것

1. HTTP URI(Uniform Resource Identifier)를 통해 자원(Resource)을 명시
2. HTTP Method(POST, GET, PUT, DELETE)를 통해 자원을 요청
3. 자원에 대한 CRUD Operation을 적용하는 것

## REST의 구성요소

### 자원(Resource)

- 모든 자원에 고유한 ID가 존재하고, 이 자원은 Server에 존재한다.
- 자원을 구별하는 ID는 ‘/groups/:group_id’와 같은 HTTP URI 다.
- Client는 URI를 이용해서 자원을 지정하고 해당 자원의 상태(정보)에 대한 조작을 Server에 요청한다.

### 행위(Verb)

- HTTP 프로토콜의 Method를 사용한다.
- GET, POST, PUT, DELETE 와 같은 메서드를 제공한다.

### 표현(Representation)

- Client가 자원의 상태에 대한 조작을 요청하면 Server는 이에 적절한 응답을 보낸다.
- REST에서 하나의 자원은 JSON, XML, TEXT, RSS 등 여러 형태의 응답으로 나타내어 질 수 있다. 일반적으로 JSON 혹은 XML를 통해 데이터를 주고 받는다.

## ****REST의 특징****

### Server-Client(서버-클라이언트 구조)

REST 서버는 API 제공, 로직 처리, 정보 저장

클라이언트는 사용자 인증이나 컨텍스트(세션, 로그인 정보) 등을 직접 관리

각각의 역할이 확실히 구분되기 때문에 클라이언트와 서버에서 개발해야 할 내용이 명확해지고 서로 간 **의존성**이 줄어들게 된다.

### Stateless(무상태)

서버는 클라이언트에 대한 사전 정보나 클라이언트의 상태를 저장하지 않음

서비스의 클라이언트가 동작하는 과정에서 생기는 상태 변화에 대해 서버는 관여하지 않고 오로지 클라이언트 단에서 감당

요청은 반드시 서버가 해당 요청을 처리하기 위해 필요로 하는 모든 정보를 함께 전송해야함

상태가 없다, 라고 하는 것은 서버의 기준에서 하는 표현

### Cacheable(캐시 처리 가능)

웹 표준 HTTP 프로토콜을 그대로 사용하므로 웹에서 사용하는 기존의 인프라를 그대로 활용 가능

캐싱이 가능한 데이터라면 클라이언트 차원에서 캐시에 저장해두고 이후에 같은 요청에 대해선 해당 데이터를 이용

### Layered System(계층화)

REST 서버는 다중 계층으로 구성될 수 있다

보안, 로드 밸런싱, 암호화 계층을 추가해 구조상의 유연성을 둘 수 있다

PROXY, 게이트웨이 같은 네트워크 기반의 중간매체를 사용할 수 있다

### Uniform Interface(인터페이스 일관성)

HTTP 표준에만 따른다면, 안드로이드/IOS 플랫폼이든, 특정 언어나 기술에 종속되지 않고 모든 플랫폼에 사용 가능

URI로 지정한 리소스에 대한 조작이 가능한 아키텍처 스타일을 의미

## REST의 장단점

장점

- HTTP 프로토콜의 인프라를 그대로 사용하므로 REST API 사용을 위한 별도의 **인프라를 구축할 필요가 없다**.
- HTTP 프로토콜의 **표준을 최대한 활용하여 여러 추가적인 장점**을 함께 가져갈 수 있게 해준다.
- HTTP 표준 프로토콜에 따르는 모든 플랫폼에서 사용이 가능하다.
- Hypermedia API의 기본을 충실히 지키면서 범용성을 보장한다.
- REST API 메시지가 의도하는 바를 명확하게 나타내므로 의도하는 바를 쉽게 파악할 수 있다.
- 여러 가지 서비스 디자인에서 생길 수 있는 문제를 최소화한다.
- 서버와 클라이언트의 역할을 명확하게 분리한다.

단점

- 표준이 자체가 존재하지 않아 정의가 필요하다.
- 사용할 수 있는 메소드가 4가지밖에 없다.
- 브라우저를 통해 테스트할 일이 많은 서비스라면 쉽게 고칠 수 있는 URL보다 Header 정보의 값을 처리해야 하므로 전문성이 요구된다.
- 구형 브라우저에서 호환이 되지 않아 지원해주지 못하는 동작이 많다.(익스폴로어)

## GET VS POST

GET 메서드는 기본적으로 서버에서 데이터를 받아오기 위해서 사용되는 메서드이다. 데이터베이스의 SELECT 쿼리문과 같은 역할을 한다고 생각하면 된다.

POST 메서드는 서버에서 데이터를 수정하거나 새로 추가할 때 사용하는 메서드이다.

![Untitled](REST%205ab2123f5975413493271b1a01f495b7/Untitled.png)

**idempotent란?**

idempotent는 **멱등법칙** (冪等法則) 또는 **멱등성** (冪等性)이란 뜻으로, 수학이나 전산학에서 연산의 한 성질을 나타내는 것으로, 연산을 여러 번 적용하더라도 결과가 달라지지 않는 성질을 의미한다.

참조

[https://khj93.tistory.com/entry/네트워크-REST-API란-REST-RESTful이란](https://khj93.tistory.com/entry/%EB%84%A4%ED%8A%B8%EC%9B%8C%ED%81%AC-REST-API%EB%9E%80-REST-RESTful%EC%9D%B4%EB%9E%80)

[https://gmlwjd9405.github.io/2018/09/21/rest-and-restful.html](https://gmlwjd9405.github.io/2018/09/21/rest-and-restful.html)

[https://stitchcoding.tistory.com/21](https://stitchcoding.tistory.com/21)

[http://www.incodom.kr/REST#h_c9da54c50b7d469b56863a778d4c9695](http://www.incodom.kr/REST#h_c9da54c50b7d469b56863a778d4c9695)