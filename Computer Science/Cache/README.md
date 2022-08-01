# Cache

#### what?

- 데이터나 값을 미리 복사해 놓는 임시 저장소

#### why?

- 반복되는 통신/연산 결과를 복사하여 다시 연산하는 시간을 절약하고 싶을 때 사용

![image](https://user-images.githubusercontent.com/82459236/179534516-a07cae8c-680d-4f62-9e7b-fc6518f28b31.png)

![image](https://user-images.githubusercontent.com/82459236/179697290-ec72982d-4187-4051-8b72-d20cddcacdc9.png)

##### Pareto principle

- 상위 20%가 전체 생산의 80%를 해낸다는 법칙. 더 정확하게는 **전체 인원의 제곱근에 해당하는 인원이 전체 생산의 50%를 해낸다**는 법칙.

#### Example

##### 캐시 메모리

- 속도가 빠른 장치와 느린 장치에서 속도 차이에 따른 병목 현상을 줄이기 위한 메모리

  ![clip_image002](https://t1.daumcdn.net/cfile/tistory/226C1F3B55ADF36F20)

  ![img](https://blog.kakaocdn.net/dn/OzsrQ/btrzr74T6iz/lE64mY7H3qFntzPcSRESm1/img.png)

---

![img](https://blog.kakaocdn.net/dn/bBcYTn/btrzuQ3UQeb/koWrZpwOcqdsPQxQNmmmcK/img.png)

##### HTTP 캐시

- 기존의 리소스를 재사용하여 웹 사이트의 레이턴시와 트래픽을 줄여 성능을 향상시기 위한 캐시

###### 브라우저 캐시 (private)

- 개인 브라우저의 캐시 저장소에 웹사이트의 정적 리소스(HTTP를 통해 다운로드된 문서; js, css, image, ...)를 저장하여 참조
- HTTP 패킷에 cache 정보를 담아 시간/버전정보를 통해 갱신
- 뒤로가기, 새로고침의 반응 향상

###### 프록시 캐시 (public)

> 프록시 : 클라이언트와 서버 사이에서 통신을 수행하는 것

- 한 명 이상의 사용자에 의해 재사용되는 응답을 저장하는 캐시
- 지역기반 네트워크처럼 프록시 서버가 운영되고 있다면 프록시서버에서 캐싱된 데이터 자체 응답

##### DB 캐시

- 쿼리의 결과를 캐시 DB에 저장하여 요청 쿼리 수를 줄이고 응답시간 향상
- main DB보다 읽기속도가 빠른 DB를 주로 사용
- Redis, MongoDB, ...

1. Look-Aside(Cache-Aside) 읽기 전략
   - 캐시를 먼저 확인하고, 없으면 DB를 참조한 후 캐시에 저장
2. Read-Through 읽기 전략
   - 캐시에서만 데이터를 가져오며, 데이터가 없을 경우 캐시가 DB를 읽어옴
3. Write-Around 쓰기 전략
   - 데이터를 캐시에 먼저 저장한 후 DB에 데이터 저장
4. Write-Through 쓰기 전략
   - DB에만 데이터를 저장
5. Write-Back 쓰기 전략
   - 캐시에만 데이터를 저장하며, 특정 시점마다 저장된 데이터들을 DB에 한번에 저장

##### CDN

- Content Delivery Network. 지리적 제약 없이 전 세계 사용자에게 빠르고 안전하게 콘텐츠를 전송할 수 있는 콘텐츠 전송 기술
- 웹 사이트에서 그래픽 이미지, 동영상 파일 등의 콘텐츠를 캐싱
- 서버와 사용자 사이의 물리적인 거리를 줄여 콘텐츠 로딩에 소요되는 시간을 최소화, 서버 트래픽 감소
- Cloudflare, SK브로드밴드, 네이버 클라우드, ...

#### 주의사항

- 자주 읽어지는 요청에 대해 캐싱하지 않을 경우, 오히려 성능이 악화됨
- 적절한 시기에 만료/업데이트 정책을 적용하지 않으면 정확한 데이터를 전달할 수 없음

#### Summary

> 캐시란, 데이터나 값을 미리 복사해두는 임시 저장소
> HTTP(브라우저 캐시, 프록시 캐시), DB 캐시, CDN가 있음!

###### reference

- https://ko.wikipedia.org/wiki/%EC%BA%90%EC%8B%9C
- https://namu.wiki/w/%ED%8C%8C%EB%A0%88%ED%86%A0%20%EB%B2%95%EC%B9%99
- https://gyoogle.dev/blog/computer-science/computer-architecture/%EC%BA%90%EC%8B%9C%20%EB%A9%94%EB%AA%A8%EB%A6%AC.html
- https://loosie.tistory.com/800
