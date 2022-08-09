# CPU Scheduling

[1. 스케줄링](#1.-스케줄링)

[2. 선점 vs 비선점](#2.-선점-vs-비선점)

[3. 스케줄링 기준](#3.-스케줄링-기준)

[4. CPU 스케줄링의 종류](#4.-CPU-스케줄링의-종류)

### 1. 스케줄링

```
메모리에 올라온 프로세스들 중 어떤 프로세스를 먼저 처리할지 순서를 정하는 것.

CPU는 한번에 하나의 프로세스만 실행시킬 수 있다. 따라서 특정 프로세스가 I/O 요청에 의해 대기해야 할 경우 CPU는 그저 놀고있게 된다.

이런 시간을 생산적으로 활용하고자 CPU를 그 프로세스로부터 회수해 다른 프로세스에 할당한다.
```

#### [참고] 프로세스 상태도

![[반효경 운영체제] Process 1 - 프로세스의 상태 - 프로세스의 상태도](https://blog.kakaocdn.net/dn/cn4zd3/btrl5v5WHW9/2SKVCjURLzfqKe9CDBqKN1/img.png)

```markdown
시작 (New)
	프로세스가 생성 중인 상태
준비 (Ready)
	메모리에 프로그램이 올라가 있지만, CPU가 없어서 기다리는 상태
실행 (Running)
	CPU를 잡고 명령을 수행 중인 상태
봉쇄 (Blocked, Wait, Sleep)
	CPU를 할당받더라도 당장 명령을 실행할 수 없는 상태
	프로세스 자신이 요청한 이벤트가 즉시 만족 되지 않아 이를 기다리는 상태
	ex) 디스크에서 파일을 읽어와야 하는 경우
완료 (Terminated)
	수행이 끝난 상태
```

#### 동작 조건

- 한 프로세스가 실행상태에서 대기 상태로 전환될 때 (ex. I/O 요청에 의한 대기)
- 프로세스가 실행 상태에서 준비완료 상태로 전환될 때 (ex. 할당된 시간이 다 끝났을 때)
- 프로세스가 대기 상태에서 준비완료 상태로 전환될 때 (ex. I/O 종료 시)
- 프로세스가 종료될 때

<br>

### 2. 선점 vs 비선점

#### 비선점 (nonpreemptive)

> 프로세스 종료 또는 입출력 등의 이벤트가 있을 때까지 실행을 보장.

장점 : 모든 프로세스에게 공정하고, 응답시간을 예측할 수 있다.

단점 : 짧은 작업을 수행하는 프로세스라도 긴 작업이 종료될 때까지 기다려야 할 수 있다.

#### 선점 (preemptive)

> OS가 CPU 사용권을 선점할 수 있는 경우에 강제로 회수.

장점 : 높은 우선순위를 가진 프로세스를 삐르게 처리하려는 시스템에 유용하다.

단점 : 높은 우선 순위를 가진 프로세스들만 들어오는 경우 Overhead가 발생한다. 우선순위가 낮은 프로세스의 경우 기아현상이 발생할 수 있다.

<br>

### 3. 스케줄링 기준

- `CPU Utilization (이용률)` : 전체 시간 중에서 CPU가 일을 한 시간의 비율
- `Throughput (처리량)` : 주어진 시간동안 준비 큐에서 기다리고 있는 프로세스 중 몇 개를 끝마쳤는지
- `Turnaround Time (소요시간, 반환시간`) : 프로세스가 CPU를 요청한 시점부터 자신이 원하는 만큼 CPU를 다 쓰고 CPU 버스트가 끝날 때까지 걸린 시간 (준비큐에서 기다린 시간 + 실제로 CPU를 사용한 시간)
- `Waiting Time (대기 시간)` : 프로세스가 준비 큐에서 CPU를 얻기 위해 기다린 시간의 합
- `Response Time (응답 시간)` : 프로세스가 준비 큐에 들어온 후 첫 번째 CPU를 획득하기까지 기다린 시간

<br>

### 4. CPU 스케줄링의 종류

#### 비선점 스케쥴링

##### 1. FCFS (First-Come First-Served)

>  프로세스가 `Ready Queue`에 도착한 순서대로 CPU를 할당받는 것. 

![[반효경 운영체제] CPU Scheduling 1 - 스케줄링 알고리즘 (Scheduling Algorithms) - 선입 선출 스케줄링 (FCFS, First-Come First-Served)](https://blog.kakaocdn.net/dn/bQz2Y5/btrns3gYrw7/MDBIeTLGjaPtWIsX2q6zM0/img.png)

- 어떤 프로세스가 먼저 실행되느냐에 따라 전체 대기시간에 상당한 영향을 미침.
- 긴 프로세스 하나 때문에 짧은 프로세스 여러개가 기다리는 **Convoy Effect**가 발생할 수 있다.

<br>

##### 2. SJF (Shortest Job First)

> CPU 버스트가 가장 짧은 프로세스에게 제일 먼저 CPU를 할당하는 방식.
>
> 평균 대기시간을 가장 짧게 하는 알고리즘.

![Untitled](https://www.notion.so/image/https%3A%2F%2Fs3-us-west-2.amazonaws.com%2Fsecure.notion-static.com%2Fb2e8b44a-8ae7-4208-906a-7c0fe0940f6a%2FUntitled.png?table=block&id=e1b58b78-5783-4b35-9514-00386fa1dc03&spaceId=b453bd85-cb15-44b5-bf2e-580aeda8074e&width=2000&userId=80352c12-65a4-4562-9a36-2179ed0dfffb&cache=v2)

- 기아 현상 (Starvation) 이 발생할 수 있다. 짧은 프로세스로 인해 긴 프로세스가 영원히 CPU를 잡지 못할 수 있음
- CPU 버스트 시간을 미리 알 수 없음. (과거 사용시간에 기반해 추측)

<br>

##### 3. HRN (Highest Response-retio Next)

> SJF 방식의 불평등을 보완하기 위한 방법, 실행 우선순위에 따라 실행

우선순위 : (대기시간 + 실행시간 ) / 실행시간

<br>

##### 4. Priority Scheduling

> 프로세스마다 우선순위를 부여하여 높은 우선순위를 가진 프로세스에게 먼저 자원을 할당하는 기법. 우선순위가 낮을 경우 기아현상이 발생할 수 있다.

해결방법 : 에이징 (Aging) - 기아현상을 해결하기 위한 방법으로 오랫동안 기다린 프로세스에게 우선순위를 높여주는 기법.



#### 선점 스케쥴링

##### 1. SRTF (Shortest Remaining Time First)

> SJF 스케쥴링의 선점형 방식. CPU를 잡았다 하더라도 더 잛은 프로세스가 들어오면 CPU를 빼앗긴다.

![Untitled](https://www.notion.so/image/https%3A%2F%2Fs3-us-west-2.amazonaws.com%2Fsecure.notion-static.com%2F57a006cb-39ce-4913-adfa-ec036015fa07%2FUntitled.png?table=block&id=11e49da6-2cd9-484d-9c1c-a2deb4de4f9e&spaceId=b453bd85-cb15-44b5-bf2e-580aeda8074e&width=2000&userId=80352c12-65a4-4562-9a36-2179ed0dfffb&cache=v2)

##### 2. Round-Robin

> 각 프로세스는 같은 크기의 CPU 시간을 할당 받고 선입선출에 의해 수행된다. 할당시간이 지나면 Ready Queue  맨 뒤에 가서 줄을서야함.

![Untitled](https://www.notion.so/image/https%3A%2F%2Fs3-us-west-2.amazonaws.com%2Fsecure.notion-static.com%2F2ef65149-2145-4990-84c2-5d84630bb7ac%2FUntitled.png?table=block&id=b8e516ac-4e24-4355-b4c8-98999ede3e63&spaceId=b453bd85-cb15-44b5-bf2e-580aeda8074e&width=2000&userId=80352c12-65a4-4562-9a36-2179ed0dfffb&cache=v2)

- 할당시간이 큰 경우 **FCFS**에 가까워진다.
- 할당시간이 작은경우 Context Switch 오버헤드가 증가한다.

<br>

##### 3. Multi-Level Queue

> Ready Queue를 우선순위에 따라 여러개로 분할한 뒤 우선순위에 따라 스케줄링 한다.

![img](https://blog.kakaocdn.net/dn/biU9IP/btrzbeLCWaa/HFZ7PP68kEWbwH9N5hqKi1/img.png)

- Single Queue에서는 모든 프로세서의 우선순위를 찾아야 해서 복잡도가 n이지만 Multi level Queue를 도입하면 이 시간복잡도를 1로 줄일 수 있다.
- 프로세서별로 특징이 다르다. 응답이 빨리 와야하는 프로세서가 있고 비교적 천천히 처리해도 되는 프로세서가 있다. 이처럼 특징에 따라 다른 알고리즘을 사용할 수 있다. 
  ex ) 높은 우선순위를 가진 프로세서 → RR, 낮은 우선순위를 가진 프로세서 → FCFS

<br>

##### 4. Multi-Level Feedback Queue

> 다른 큐로 이동하기 힘든 Multi-Level Queue 스케줄링의 단점을 개선한 방법

![img](https://blog.kakaocdn.net/dn/u6iYj/btrzhprhpcT/S0oTuEG6vBHJxNvjZ95CW1/img.png)

- aging 기법으로 구현할 수 있다. 우선순위가 낮은 큐에서 오래 기다렸으면 우선순위가 높은 큐로 승격하는 방식.
- 멀티 레벨 피드백 큐를 정의하는 요소
  - 큐의 수
  - 각 큐의 스케줄링 알고리즘
  - 프로세스를 상위 큐로 승격하는 기준
  - 프로세스를 하위 큐로 강등하는 기준
  - 프로세스가 도착했을 때 들어갈 큐를 결정하는 기준 
  - (예시)
    - 보통 처음 들어오는 프로세스는 우선 순위가 가장 높은 큐에 CPU 할당 시간을 짧게 하여 배치한다.
    - 만약 주어진 할당 시간 안에 작업을 완료하지 못하면 CPU 할당 시간을 조금 더 주되, 우선 순위가 한 단계 낮은 큐로 강등한다.
    - 이 과정을 반복하다가 최하위 큐에 배치가 된다.





##### 참고

> 운영체제 Multilevel Queue ( 멀티 레벨 큐 ), 출처: https://wpaud16.tistory.com/254
>
>운영체제 Multilevel Feedback Queue ( 멀티레벨 피드백 큐 ), 출처: https://wpaud16.tistory.com/255 
> 
> [반효경 운영체제\] CPU Scheduling 1, (https://steady-coding.tistory.com/530#)
>
>  [OS\] 3. CPU 스케줄링 (CPU Scheduling)(https://hibee.tistory.com/296)