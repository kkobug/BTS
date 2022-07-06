# Docker

## Docker

```
도커(Docker)는 리눅스의 응용 프로그램들을 프로세스 격리 기술들을 사용해 컨테이너로 실행하고 관리하는 오픈 소스 프로젝트.
- ko.wikipedia.org/wiki/도커_(소프트웨어)

LXC(리눅스 컨테이너스)라는 커널 컨테이너 기술을 이용하여 만든 컨테이너 기술 중 하나.
- namu.wiki/w/Docker
```

## Container

```
운영 체제 수준 가상화(operating-system-level virtualization)는 운영 체제의 커널이 하나의 사용자 공간 인스턴스가 아닌, 여러 개의 격리된 사용자 공간 인스턴스를 갖출 수 있도록 하는 서버 가상화 방식이다.
- ko.wikipedia.org/wiki/운영_체제_수준_가상화

LXC(LinuX Containers)는 단일 컨트롤 호스트 상에서 여러 개의 고립된 리눅스 시스템 (컨테이너)들을 실행하기 위한 운영 시스템 레벨 가상화 방법이다.
- ko.wikipedia.org/wiki/LXC
```

## Server Virtualization

```
서버 가상화는 CPU, 메모리, 입출력 등 단일 플랫폼 상의 서버 자원을 사용자가 여러 도메인이나 서버 애플리케이션으로 분할해 사용할 수 있는 기술이다.
- wiki.hash.kr/index.php/서버_가상화
```

> 하나의 물리적 서버에 여러 서버를 실행할 수 있도록 해주는 기술

### why?

```
ex) 배달의 민족
origin_WAS (60%): 배달 주문, 리뷰, ...
new_WAS (20%): 쇼핑 라이브
```

![image-20220704224344980](https://user-images.githubusercontent.com/82459236/177202656-34bf6890-0328-492d-86ee-5e2d5c897434.png)

### vs container

![img](https://mblogthumb-phinf.pstatic.net/MjAxOTA3MzBfMjc2/MDAxNTY0NDc1MDYzNDM3.Trouf4TG1sg2B8a6LsMdq9IEO-MAefu7-74Dobq35kgg.1gqswwuinmH19Ldj22dgS3LTOWcFBF6ir4f3i8fP2YEg.PNG.shakey7/image.png?type=w800)

- 인스턴스 규모의 차이(VM이 container보다 더 큰 규모)
  - VM에서는 각 VM마다 guest OS가 있어 할당된 자원을 사용
  - container는 OS를 가상화하지 않고 기존 OS를 그대로 사용하여 가볍고 빠름


> guest OS 없이 구동하므로 배포/실행이 빠르고, 자원을 효율적으로 사용할 수 있다.

## Why use docker?

- 독립된 개발 환경 구축
  - container 공간에서 개발하므로 Host OS에 영향을 끼치지 않음

- 통합된 개발-운영 환경 구축
  - docker image를 만들어 서버(또는 다른 작업환경)로 이동

### docker engine

- 이미지와 컨테이너의 생명주기 관리, 볼륨 관리, 네트워크 관리

### docker swarm

- 서비스의 확장/관리를 효율적으로 해주는 기능 : 클러스터 관리, 서비스 관리, 네트워크 관리, 노드 관리, ...

### docker compose

- 여러 컨테이너를 하나로 정의하고 관리(생성)

## Summary

- 도커란?

  > 가상환경 '처럼' application을 격리된 공간(container)에서 실행하고 관리하기 위한 도구

- 도커를 쓰는 이유? (장점)

  > 독립된 환경에서 개발할 수 있고, 개발한 것들을 쉽고 빠르게 배포할 수 있다.
