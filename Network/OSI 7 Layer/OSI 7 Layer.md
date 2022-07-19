## OSI 7 Layer

> 네트워크에서 통신이 일어나는 과정을 7 단계로 나눈 것을 말한다.



### OSI 7 계층을 나눈 이유?

```
- 초기에 여러 정보 통신 업체 장비들은 자신의 업체 장비들 끼리만 연결이되어 서로 호환이 되지 않았다.
- 모든 시스템들의 상호 연결에 있어 문제없도록 표준을 정한 것이 OSI 7 계층
- 흐름을 한눈에 알아보기 쉽고 네트워크상의 문제가 생겼을 때 이상이 생긴 단계만 빠르게 고칠 수 있다.
```

![OSI 7 계층이란?, OSI 7 계층을 나눈 이유](https://t1.daumcdn.net/cfile/tistory/995EFF355B74179035)

#### 작동 원리

1. 전송 시 7계층에서 1계층으로 각각의 층마다 인식할 수 있어야 하는 헤더를 붙임 (캡슐화)
2. 수신 시 1계층에서 7계층으로 헤더를 떼어냄 (디캡슐화)

![img](https://faq.hostway.co.kr/files/attach/images/784/434/001/679c0026b17573f5f0ba7edcafe8ad20.jpg)

#### 1. 물리 계층 (Physical Layer)

- 전기적, 기계적, 기능적인 특성을 이용해 데이터를 전송

- 데이터는 0과 1의 비트, 즉 On Off의 전기적 신호 상태로 이루어져 해당 계층은 단지 데이터를 전달 (알고리즘, 오류제어 기능이 없음)

- 통신 케이블, 리피터, 허브가 있다.

  ![img](https://mblogthumb-phinf.pstatic.net/20160423_189/kyg3766_1461413890981KnzMX_JPEG/1%B0%E8%C3%FE.jpg?type=w2)

#### 2. 데이터 링크 계층 (DataLink Layer)

- 같은 네트워크에 있는 여러 대의 컴퓨터들이 데이터를 주고받기 위한 계층

- 물리 계층을 통해 송수신 되는 정보의 오류와 흐름을 관리하여 안전한 정보의 전달을 수행할 수 있도록 도와줌. (통신의 오류도 찾아주고 재 전송 하는 기능도 가지고 있음)

- MAC(Media Access Control Address) 주소를 통해서 통신

- 프레임 단위로 데이터를 전송함

- 브릿지, 스위치를 통해 맥 주소를 가지고 물리계층에서 받은 정보를 전달함.

  ![img](https://mblogthumb-phinf.pstatic.net/20160426_219/kyg3766_1461676821586qxWBp_PNG/%C1%A6%B8%F1_%BE%F8%C0%BD.png?type=w2)

#### 3. 네트워크 계층 (Network Layer)

- 경로를 선택(Route)하고 주소를 정하고(IP) 경로에 따라 패킷을 전달해주는 역할.

- 패킷단위로 데이터를 주고받음

- 라우터 (서로 다른 네트워크를 연결해주는 장비), 스위치에 라우팅 기능을 장착한 layer3 스위치

  ![img](https://t1.daumcdn.net/cfile/tistory/99FBCA335A2CEB552E)

![OSI 7계층 | N's Blog](https://ngwoon.github.io/assets/images/post/Network/OSI%207%EA%B3%84%EC%B8%B5/network-layer.png)

#### 4. 전송 계층 (Transport Layer)

- 신뢰성 있고 정확한 데이터 전송을 담당 
- 포트를 열어서 응용프로그램들이 전송을 할 수 있게 한다.
- 데이터를 전송받는 경우 4계층에서 모든 데이터를 하나로 합쳐서 5계층으로 넘겨줌
- 세그먼트 단위(TCP)로 데이터를 주고받음

![img](https://mblogthumb-phinf.pstatic.net/20160426_86/kyg3766_1461678612274BtO4A_PNG/%C1%A6%B8%F1_%BE%F8%C0%BD.png?type=w2)

#### 5. 세션 계층 (Session Layer)

- 응용프로그램 간의 통신을 유지하기 위한 구조 제공

- 세션 관리, 동기화, 대화 제어, 종료의 기능이 있다.

- 동기화 신호 syn 신호를 데이터에 붙여서 보냄. 

- TCP/IP 세션을 만들고 없앤다.

- SSL, TLS

  ![img](https://mblogthumb-phinf.pstatic.net/20160426_275/kyg3766_1461680665371n43Q0_PNG/%C1%A6%B8%F1_%BE%F8%C0%BD.png?type=w2)

#### 6. 표현 계층 (Presentation Layer)

- 데이터를 어떻게 표현할지 정하는 계층

- 전송하는 데이터의 인코딩 및 디코딩이 이루어지는 계층

- 응용 계층에서 데이터를 이해할 수 있게 응용프로그램에 맞춰 변환 (JPEG, GIF, MPEG ...)

  ![img](https://mblogthumb-phinf.pstatic.net/20160426_72/kyg3766_1461681304197IuOYw_PNG/%C1%A6%B8%F1_%BE%F8%C0%BD.png?type=w2)

#### 7. 응용 계층 (Application Layer)

- 사용자와 가장 밀접한 계층, 메일 전송, 인터넷 접속 등의 작업을 수행할 수 있다.

- HTTP, FTP, SMTP, POP3, IMAP, Telenet과 같은 프로토콜이 있다.

- 네트워크 소프트웨어 UI 부분, 사용자의 입출력 부분

  ![img](https://mblogthumb-phinf.pstatic.net/20160426_243/kyg3766_1461681766246yIVa3_PNG/%C1%A6%B8%F1_%BE%F8%C0%BD.png?type=w2)





