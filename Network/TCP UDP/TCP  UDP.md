# TCP / UDP

를 설명하기 전에

전송계층에 대해서 먼저 알아야 해요...



## 전송계층이란?

OSI 7 계층 중 하나    **Transport Layer** 

계층 구조의 네트워크 구성요소와 프로토콜 내에서 송신자와 수신자를 연결하는 통신 서비스를 제공



### 전송 계층이 없다면?( 전송 계층의 중요성 )

* 데이터의 순차 전송 X![image-20220711170257458](C:\Users\PARK\AppData\Roaming\Typora\typora-user-images\image-20220711170257458.png)

* Flow ( 흐름 문제 )

  * 원인: 송수신자 간의 데이터 처리 속도 차이

    수신자가 처리할 수 있는 데이터량을 초과

* Congestion( 혼잡 문제 )

  * 원인: 네트워크의 데이터 처리 속도

    Network 가 혼잡할때

    

결과: 데이터 손실 발생

![image-20220711170748597](C:\Users\PARK\AppData\Roaming\Typora\typora-user-images\image-20220711170748597.png)



이렇게 때문에  생긴게



## TCP(Transmission Control Protocol)

### 연결 기반, 신뢰성

신뢰성있는 데이터 통신을 가능하게 해주는 프로토콜



### 세그먼트(Segment) - TCP 프로토콜의 PDU(단위)

<img src="https://blog.kakaocdn.net/dn/bCenX6/btqZP2MEqAq/PDyksDOf5nBnuY1et5Y2v0/img.png" alt="img" style="zoom: 50%;" />

TCP 내부적으로 데이터를 잘라서 Header를 붙인 다음에 프로토콜 안에서 이동 및 처리



### TCP Header![image-20220711174551994](C:\Users\PARK\AppData\Roaming\Typora\typora-user-images\image-20220711174551994.png)

**SYN( synchronization )** 연결 요청 플래그

* 통신 시작 시 세션을 연결하기 위한 플래그

**ACK( Acknowledgement )** 응답 플래그

* 송신측 으로부터 패킷을 잘 받았다는 걸 알려주기 위한 플래그 

**FIN( Finish )** 연결 종료 플래그

* 더 이상 전송할 데이터가 없고 세션 연결을 종료시키겠다는 플래그



### 3 way-handshake (connection 연결)

<img src="https://blog.kakaocdn.net/dn/bqWzBI/btqZV6NmcLk/KdR7yXGbKwWoH6b15jhLP0/img.png" alt="img" style="zoom: 67%;" />

1. (Client) SYN bit를 1로 설정해 패킷 송신
2. (Server) SYN, ACK bit를 1로 설정해 패킷 송신
3. (Client) ACK bit를 1로 설정해 패킷 송신

#### 상태가 ESTABLISHED 로 바뀌면 연결



### TCP의 데이터 전송 방식

<img src="https://blog.kakaocdn.net/dn/cxeJc9/btqZV5gCL1d/wbdeS5Stgr8nQ9mSfWdpEK/img.png" alt="img" style="zoom: 67%;" />

1. Client가 패킷 송신
2. Server에서 ACK 송신
3. ACK를 수신하지 못하면 재전송





### 4 way-handshake (Connection 종료)

<img src="https://t1.daumcdn.net/cfile/tistory/99229C485C1D90C038" alt="TCP 4 way handshake 내용 정리" style="zoom: 67%;" />

1. 데이터를 전부 송신한 Client가 FIN 송신
2. Server 가 ACK 송신
3. Server가 FIN 송신
4. Client가 ACK 송신



### 특징

- **순차전송**
- **Flow control**(흐름 제어)
- **Congestion control**(혼합 제어)
- **Error detection**(오류 감지)



### 단점

- 3 way-handshake connenction은 매 번 통신할 때마다 일어나기 때문에 시간 손실
- 패킷을 조금만 손실해도 재전송





## UDP (User Datagram Protocol)

### 연결없음, 신뢰안함

* TCP보다 신뢰성이 떨어지지만 전송 속도가 일반적으로 빠른 프로토콜

  

### 전송 단위: Datagram

<img src="https://blog.kakaocdn.net/dn/qj356/btqZTT815ff/t9bsCUehRXAVZbEQbr19DK/img.png" alt="img" style="zoom: 50%;" />

### UDP Header

<img src="https://blog.kakaocdn.net/dn/CkVDc/btrwnPnmZFI/dxuIaV0cB3K9R1NPBudoo1/img.png" alt="img" style="zoom:67%;" />

### UDP의 데이터 전송방식

<img src="https://blog.kakaocdn.net/dn/q0hsX/btqZYlXx6E9/gFN23XdAnKLhY4pATjCvk1/img.png" alt="img" style="zoom: 50%;" />

### 특징

* **순차전송** X
* **Flow Control**(흐름 제어) X
* **Congestion Control**(혼합 제어) X
* **Connectionless**: Client는 패킷을 확인 안하고 무조건 송신. Server는 소캣 무조건 열어두고 있음
  * 3 way-handshake X
* **Error detection**(오류 감지): UDP헤더의 CheckSum 필드를 통해 최소한의 오류만 검출한다.
* 비교적 데이터의 신뢰성이 중요하지 않을 때 사용(ex. 영상 스트리밍)





# TCP UDP 비교

<img src="https://blog.kakaocdn.net/dn/sv1cS/btqZTU1bcxs/ui7egay5SRnhTUOKjVy2v1/img.png" alt="img" style="zoom:50%;" />







# 결론

- TCP, UDP의 특성을 파악하고, 상황에 따라 적절한 프로토콜을 이용할 수 있다.
- TCP, UDP의 헤더를 파악하고 성능 개선에 이용할 수 있다.





참고: https://student513.tistory.com/75

영상으로 설명도 해줌