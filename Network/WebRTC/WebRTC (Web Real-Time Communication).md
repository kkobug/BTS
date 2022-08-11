# WebRTC (Web Real-Time Communication)

>  웹 애플리케이션과 사이트가 중간자 없이 브라우저 간에 오디오나 영상 미디어를 포착하고 마음대로 스트림할 뿐 아니라, 임의의 데이터도 교환할 수 있도록 하는 기술
>
> 즉, 서버와 같은 중간자를 거치지 않고 브라우저와 브라우저를 P2P로 연결해 데이터를 주고받는 기술



### vs Websocket

![WebRTC vs WebSockets • BlogGeek.me](https://bloggeek.me/wp-content/uploads/2019/05/201905-websocket-vs-datachannel-1024x384.jpg)



### 통신과정

1. Signalling을 통해 통신할 peer간 정보를 교환한다. ex) 네트워크 구성정보, 세션 제어 메세지, 미디어 기능 등의 정보
2. WebRTC를 사용해 연결을 맺고, peer의 단말에서 미디어를 가져와 교환한다.

>  **Singalling을 통해 한번 연결되고 나면 데이터를 주고받을 때 추가적인 서버가 필요없음**

![image-20220726165123445](https://user-images.githubusercontent.com/55776650/184129967-70e60b90-7239-46f3-acc8-435b9a878098.png)



### 시그널링

>  연결하고자 하는 Peer들을 논리적으로 묶고 서로간의 정보를 교환해준다.

- Session Control Messages (세션 제어 메세지) :  통신의 초기화, 종료, 그리고 에러메세지
- Network Configuration (네트워크 구성정보) : 외부에서 바라보는 IP와 포트정보
- Media Capabilities (미디어 기능) : 상호 두 단말의 브라우저에서 사용가능한 코덱, 해상도



### STUN/TURN 서버

> P2P로 클라이언트끼리 통신하는 데 왜 서버가 필요해 ?
>
> - 시그널링 서버를 통해 P2P로 연결하기 위해서는 상대방의 Public IP 주소를 알아야한다. 하지만 클라이언트가 방화벽이나 NAT뒤에 있는 경우가 대부분이기 때문에 Public IP 주소를 알기 어렵다. 이 문제를 해결하기 위해 STUN 서버를 권장한다.

#### 	STUN (Session Traversal Utilities for NAT)

![img](https://velog.velcdn.com/images%2Fheejinkim0812%2Fpost%2F651a28e3-1fb6-4209-881c-5dea81d9e624%2Fimage.png)

​	NAT 트래버셜 작업이 **STUN** 서버에 의해 이루어진다. 클라이언트가 STUN 서버에 요청을 보내면 공인 IP 주소와 함께 통신에 필요한 정보들을 보내주는데 클라이언트는 이를 이용해 다른 기기와 통신한다. 하지만 이런 경우에도 통신이 되지 않는다면 TURN 서버로 넘기게 된다.

#### TURN (Traversal Using Relays around NAT)

![img](https://velog.velcdn.com/images%2Fheejinkim0812%2Fpost%2F768e918a-b7e3-4899-8077-ab2f03b886c1%2Fimage.png)

​	STUN 서버를 이용하더라도 항상 자신의 정보를 알아낼 수 있는 것은 아니다. 어떤 라우터들은 방화벽 정책을 달리할 수도 있고, 이전에 연결된 적이 있는 네트워크만 연결할 수 있게 제한을 걸기도 하기 때문이다 (Symmetric NAT). 이 때문에 STUN 서버를 통해 자신의 주소를 알아내지 못했을 때는 TURN 서버를 이용한다

TURN 서버는 이런 Symmetric NAT 제약조건을 우회하기 위해 만들어졌다. TURN 서버와 연결을 맺고 이 서버에서 모든 교환과정을 중계한다. 모든 기기는 TURN 서버로 패킷을 보내고, 서버가 이를 포워딩 한다.

![webRTC, websocket, django-channel (1)](https://velog.velcdn.com/images/mquat/post/1424979e-1366-40e8-b4a1-87447310fa38/image.png)

###### SDP (Session Description Protocol)

해상도나 형식, 코덱, 암호화 등의 멀티미디어 컨텐츠의 연결을 설명하기 위한 표준

![img](https://velog.velcdn.com/images%2Fkkj53051000%2Fpost%2Ff51c9fa8-22b9-4cc8-9ccd-3e034a7f4be1%2F%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3%E1%86%BA%202022-01-21%20%E1%84%8B%E1%85%A9%E1%84%92%E1%85%AE%202.30.17.png)



###### ICE (Interactive Connectivity Establishment)

브라우저가 peer를 통한 연결이 가능하도록 하게 해주는 프레임워크

![img](https://velog.velcdn.com/images%2Fkkj53051000%2Fpost%2F4b24c075-9b7f-40bd-84ea-eeb1a6b205ea%2F%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3%E1%86%BA%202022-01-21%20%E1%84%8B%E1%85%A9%E1%84%92%E1%85%AE%202.41.09.png)



### 장단점

#### 장점

```
1. Latency가 짧아서 real-time 통신이 가능하다.
2. 별 다른 소프트웨어 없이 실시간 커뮤니케이션이 가능하다.
```

#### 단점

```
1. 크로스 브라우징 문제가 있다.
2. 확장성에 제약이 있다.
```





### 결론

- **웹 애플리케이션과 사이트가 중간자 없이 브라우저 간에 오디오나 영상 미디어를 포착하고 마음대로 스트림할 뿐 아니라, 임의의 데이터도 교환할 수 있도록 하는 기술**입니다.







##### 참고

> https://developer.mozilla.org/ko/docs/Web/API/WebRTC_API
>
> https://medium.com/@hyun.sang/webrtc-webrtc%EB%9E%80-43df68cbe511
>
> https://velog.io/@happyjarban/WebRTC-%ED%8C%8C%ED%97%A4%EC%B9%98%EA%B8%B01-WebRTC-%EC%9D%B4%EB%A1%A0
>
> https://doublem.org/webrtc-story-02/

