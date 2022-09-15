# Stream

### What?

![image](https://user-images.githubusercontent.com/82459236/189738859-9dc8a9d1-162b-4c18-9a7b-8dd749c29c0c.png)

- CS에서 stream은 시간이 지남에 따라 이용 가능한 일련의 데이터 요소
- 대규모 데이터 더미가 아닌, 컨베이어 벨트 위의 물건처럼 처리되는 데이터에 비유



#### in ORACLE

![image](https://user-images.githubusercontent.com/82459236/189737760-29b4b3ae-edbb-43a7-8447-8e87dadbba36.png)

- 순차적 & 병렬적 집계 연산을 지원하는 원소 sequence
- Collection, Array처럼 하나의 고정된 데이터 집합이 아닌, 연속된 데이터의 흐름



#### Stream Package

![image](https://user-images.githubusercontent.com/82459236/189734857-c6356ea1-3a57-4cad-a0e4-df730fa91076.png)

- 원소들의 스트림에 함수형 스타일의 연산을 지원하는 클래스
- 일련의 데이터를 flow에 따라 어떻게 처리할지 방법을 제시하는 도구

> sequence 데이터를 깔끔하게 처리하는 방식



### 사용법

#### 생성

- Collection, Array, File, ...

#### 중간 연산

- filter, map, peek, sorted, distinct, limit

  - stateless : 다른 데이터 값과 무관함
  - stateful : 다른 데이터 값에 종속

- 연산의 결과는 새로운 stream을 반환

  - lazy evaluation : 최종 연산이 들어오기 전까지 중간 연산이 실제로 실행되지 않음

  - 새로운 stream 인스턴스를 반환할 뿐, 작업을 수행하지 않음 -> 루프퓨전, 쇼트서킷

    > 루프퓨전 : 여러 연산을 한 과정으로 병합하는 것
    > 쇼트서킷 : 결과가 확실하다면 모든 원소를 iteration 하지 않고 종료하는 것

#### 최종 연산

- collect, findAny, findFirst, anyMatch, allMatch, forEach
- 최종 연산자가 수행되고 나면, 스트림 파이프라인은 소비된것으로 간주되어 재사용이 불가능



### vs for-loop

```java
int[] numbers = {1346, 6523, 7245, 123, 3461, 253, 574, 8346, 12, 2};

// for-loop
int sum = 0, cnt = 0;
for (int number : numbers) {
    if (number > 1000) {
        sum += number;
        cnt ++;
    }
}
double avg = (double) sum / cnt;

// stream
double streamAvg = Arrays.stream(numbers)
    .filter(n -> n > 1000)
    .average()
    .orElse(0);
```

- 코드의 유지, 보수가 쉬움
- 코드블록으로 표현하는 for문에 비해, 선언형 코드로 가독성이 좋음
- stream은 람다식으로 변수를 제어하므로 외부 변수를 제어할 수 없음
- stateful 중간연산에 의해 의도치 않은 연산 과정이 발생할 수 있음
  - filter -> sorted -> map : filter -> sorted -> map -> sorted -> map
- 유의미하지는 않으나, iteration에 비해 다소 성능이 떨어짐
- 복잡한 logic에서, 코드가 정상적으로 동작하지 않을 경우 무엇이 문제인지 식별하기 어려움



---

https://en.wikipedia.org/wiki/Stream_(computing)

https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/util/stream/package-summary.html

https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/util/stream/Stream.html