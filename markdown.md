name: title
class: center, middle, inverse

# .title_upper[Python으로 만드는]<br>NEOVIM ASYNC PLUGIN
[PYCON 2016 APAC](https://www.pycon.kr/2016apac/)

.author[송재학 ([master@hpi.cc](mailto:master@hpi.cc))]

???
안녕하세요. 이번 PYCON 2016 APAC에 훌륭한 프로그램들이 많던데, 그럼에도 불구하고
본 프로그램을 선택해주셔서 감사합니다. 본 프로그램은 Python으로 만드는 neovim
async plugin 입니다. 본 브로그램에서는 neovim에 대한 소개와 장점, 그리고 프로그램
제목처럼 python으로 neovim async plugin을 개발하는 법을 다뤄보록 하겠습니다.

---
class: middle

# 발표자

## 송재학

* 현재 백수생활 중

* (전) 문래빗 주식회사 대표
  * 판타지x러너즈 for 카카오 서버 개발 (python)

* omnisharp-sublime (sublime text를 위한 C# IDE 플러그인)

---

class: center, middle

.logo[
  ![neovim logo](./images/neovim-logo.svg)
]

--

class: center, middle
## 말그대로 vim의 미래
vim을 적극적으로 리팩토링한 superset

???
공식 사이트의 메인에 있는 슬로건을 그대로 옮긴다면, neovim은 '말그대로 vim의 미래'
입니다. neovim은 vim을 적극적으로 리팩토링한 프로젝트로, 기존 vim에서 기능이
추가된 superset을 지향하고 있습니다.

---

class: middle
# 현황
#### (2016.08.01 기준)

* stable version: v0.1.4
  * 안정적이고 실사용 가능함

* github repository
  * 활성화 되어있음
      * watch: 954
      * star: 19,471
      * fork: 1,374
---

class: middle
# 특징 

- **더 강력한 플러그인**

- 더 나은 기본 기능과 설정 

- 기본으로 내장된 embedding

- vim에서 쉽게 옮길 수 있음

---

class: middle, center

# 더 강력한 플러그인
오늘은 여기에만 집중해봅시다.

---

class: middle

## 더 강력한 플러그인
  
  * 핵심은 msgpack-rpc

---

class: middle

# msgpack-rpc
 * neovim은 서버로 동작함
 * stdin/stdout, socket을 통해 neovim의 RPC API를 사용할 수 있음

---

class: middle

# Hello World!
한번 해봅시다.

---

# Hello World!
### 0. python-neovim 설치

```bash
> # python-neovim은 neovim의 RPC API를 호출하기 위한 모듈
> pip install neovim
```

--

### 1. neovim 실행

```bash
> # NVIM_LISTEN_ADDRESS: neovim의 RPC 주소 지정
> NVIM_LISTEN_ADDRESS=127.0.0.1:121212 nvim
```

--

### 2. python REPL에서 명령어 실행

``` python
> python
>>> from neovim import attach
>>> nvim = attach('socket', path='127.0.0.1:121212')
>>> nvim.command('echo "hello world!"')

```

---

# Hello World!

.right[[asciinema로 동영상 보기](https://asciinema.org/a/81579)]
![hello world 출력 화면](./images/nvim_helloworld.png)

