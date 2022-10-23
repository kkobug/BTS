# CI/CD

### background

- 전통적인 배포 파이프라인 단계는 다음과 같다.

  ```
  1. version control : 코드를 작성/수정하고, 변경사항을 커밋한다.
  
  2. acceptance tests : 미리 컴파일/빌드된 코드에 대해 테스트를 실행한다.
  
  3. independent deployment : 컴파일 및 테스트가 완료된 아티팩트를 개발 환경에 배포한다. 개발 환경은 product 환경과 가능한 같아야한다.
  
  4. production deployment : 개발 환경에서 실행이 확인된 코드를 서버에 배포한다. 배포 과정이 independent deployment 프로세스와 가능한 같아야한다. 일반적으로 운영팀 또는 Dev-Ops 팀에서 다뤄진다.
  ```

- 전통적인 방식에서의 문제점
  - 작업이 수동으로 진행되고, 반복적이라는 특징이 있어 human error가 발생할 가능성이 큼
  - 개발 기간이 일정 수준 이상으로 길어지면 오류 발생 가능성과 conflict 해결에 들어가는 비용이 커짐
  - SW 개발에서 협업이 필수적으로 자리잡으면서, version control 과정과 acceptance tests 과정에서 자원 낭비가 증가
- 개발/빌드/검증 과정의 속도를 개선하고, 자원 낭비를 막기 위해 새로운 방법(자동화)을 찾게됨
- 그러나 CI/CD의 핵심은 단순히 자동화에 있지 않음: 한번에 많은 개발을 진행하지 않고, 지속적으로 통합/배포하는 것이 가능하도록 함!



### CI/CD

- CI/CD
  - 지속적인 통합, 지속적인 서비스, 지속적인 배포
  - 개발 라이프사이클 전체에 걸쳐서 구축된 지속적인 자동화와 모니터링 시스템을 CI/CD pipeline이라함
  - 각 단계의 자동화를 통해 보다 짧은 주기로, 신뢰성 높은 제품을 사용자에게 제공하는 솔루션
  - Jenkins, Bamboo, Hudson, Travis, CircleCI, ...

- CI : Continuous Integration
  - 지속적인 통합 : 빌드 & 패키징
  - repository에 병합된 코드를 정기적으로 빌드/테스트 하는 과정
  - build, test를 실시하는 프로세스를 의미하며, 이러한 통합 을 상시로 실시하여 개발자 간의 코드 충돌을 방지하고 코드의 품질을 유지할 수 있음
  - 항상 신뢰성 있는 build 상태를 유지하고, 사용자에게 바로 제공 가능하도록 함

- CD : Continuous Delivery / Continuous Deployment
  - 지속적인 서비스 : 배포 (CI의 연장선으로, CD가 되려면 CI가 선행되어야함)
  - CI/CD pipeline의 마지막 단계로, CI 과정을 통과한 코드들을 테스트 서버와 운영 서버에 자동으로 릴리즈하는(production deployment) 것을 의미
  - 개발팀과 운영팀의 불필요한 커뮤니케이션을 최소화하여 자원 낭비를 줄여줌
  - 소프트웨어가 항상 신뢰 가능한 수준(테스트를 통과한 상태)에서 배포되도록 관리



### Jenkins

- 자바 기반의 CI/CD tool
- configuration / customization 과정에 시간이 필요하다는 단점이 있음
- 다양한 플러그인을 통해 필요한 도구를 확장할 수 있기 때문에 규모가 큰 프로젝트에 사용하기 적합

![img](https://blog.kakaocdn.net/dn/8qzBg/btqUODibyue/KJTHJlgEL90hBQkfLqeGM0/img.png)

#### Jenkinsfile

- jenkins pipeline을 정의하기 위한 방법

- 개발자 또는 dev-ops 엔지니어가 원하는 branch의 코드 또는 pull request로부터 파이프라인 빌드 프로세스를 자동으로 만들 수 있음

- 파이프라인의 코드를 리뷰하고, 반복적인 빌드 과정에 대한 기록을 추적할 수 있음

  ![img](https://blog.kakaocdn.net/dn/V4TEk/btqUL9aRYzS/D9EhhQL74fxB5G4AUheQHK/img.png)

- 권한(계정/pw)이 주어진다면, dev-ops 엔지니어가 아니더라도 프로젝트 멤버들이 파이프라인 과정을 확인하고 수정할 수 있음.



> CI/CD 환경 구축의 핵심 목적은 "한 번에 많이 개발/수정하지 말고, 조금씩 수정하여 자주 commit하라!"는 것