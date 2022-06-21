# Object Oriented Programming

## WHAT?

- 상태(property)와 행위(method)로 이루어진 객체를 구현하고, 이를 조합하여 프로그래밍 하는 방법
  - 클래스 : 객체를 만들어 내기 위한 설계도(상태와 행위를 정의하는 틀)
  - 객체 : 어플리케이션 내에 구현된 모든 대상
  - 인스턴스 : 클래스를 바탕으로 구현된 실제 데이터
  - method : 객체가 수행하는 동작(연산)
  - property : 객체가 보유한 데이터 값

## **WHY?**

- 설계단계에서, 코드를 직관적으로 만들어 유지/보수를 쉽게 하기 위함
- 설계란, 의존성(dependency) 관리를 통해 결합도와 응집도를 control하는 것

## **HOW?**

### 캡슐화

- property / method를 하나의 단위로 묶는 것
- class로 구현되며 instance를 생성하여 property와 method에 접근할 수 있음

### 은닉성

- property / method를 외부에 드러나지 않도록 숨겨 코드 응집도를 높이고, 외부와의 결합도를 떨어트림

### 상속

- 부모 클래스의 property / method를 재정의 없이 그대로 사용하여 코드 반복을 줄이는 기법

### 다형성

- 하나의 메시지에 대해 각 객체가 가진 고유한 방법으로 응답하는 것
- 오버라이딩/오버로딩

```java
public abstract class Student {  // 클래스
    private boolean 교육지원금 = false;  // property

    public void 동의하기() {  // method
        교육지원금 = true;
    }
}

public class 반장 extends Student {
    private boolean 자치회_회의 = false;

    public void 회의참석() {
        자치회_회의 = true;
    }
}

public class 팀장 extends Student {
    private 중간평가 = false;
    private 최종평가 = false;

    public void 중간평가() {
        중간평가 = true;
    }

    public void 최종평가() {
        최종평가 = true;
    }
}

public class 팀원 extends Student { }

public class Main {
    public static void main(String[] args) {
        반장 성아영; // 객체
        팀장 박준영;
        팀원 강동옥;
        성아영 = new 반장(); // 인스턴스
        박준영 = new 팀장();
        강동옥 = new 팀원();
        강동옥.동의하기();
        성아영.회의참석();
    }
}
```

## SOLID

### SRP: Single Responsibility Priciple

- 단일 책임 원칙
- 하나의 클래스는 하나의 기능을 가짐

### OCP: Open-Closed Priciple

- 개방-폐쇄 원칙
- 확장에 대해서는 Open, 수정에 대해서는 Closed 해야함
- 새로운 기능을 추가할 때, 기존 코드를 수정하지 않고 확장할 수 있어야함

### LSP: Liskov Substitution Principle

- 리스코프 치환 원칙
- 자식클래스는 부모클래스를 대체할 수 있어야함

### ISP: Interface Segregation Principle

- 인터페이스 분리 원칙
- 사용되지 않는 메서드는 구현하지 않음 → 더 작은 인터페이스로 분리하여 필요한 것만 구현한다

### DIP: Dependency Inversion Principle

- 의존성 역전 원칙
- 추상적인 high level의 클래스는 구체적인 low level의 클래스에 의존하지 않도록 함

## **결론**

> 좀 더 나은(=유지보수가 쉬운) 프로그램을 만들기 위해 프로그래밍의 의존성을 설계하는 방법
