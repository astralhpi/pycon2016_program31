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

class: center, middle, inverse
# 왜 neovim 인가요?

???
한글 폰트와 영문 폰트가 상당히 안 어울리지만 그냥 넘어갑시다.
왜 이 발표에서는 neovim을 다룰까요?

--

vim, emacs, atom, sublime text 등 사용자가 더 많은 에디터도 많은데...

---

class: right, middle, inverse

# neovim .red[vs] 다른 텍스트 에디터
## vim, atom, sublime text, etc

--

![이 얼마나 끔찍하고 무시무시한 생각이니?](images/terrible.png)

---

class: center, middle, inverse

## 그냥 발표자가 지금 쓰고 있는 에디터라서요...
Python으로 비동기 플러그인 짜기도 편합니다.

---

class: center, middle, inverse
# Neovim
## 말그대로 vim의 미래
vim을 적극적으로 리팩토링한 superset

???
공식 사이트의 메인에 있는 슬로건을 그대로 옮긴다면, neovim은 '말그대로 vim의 미래'
입니다. neovim은 vim을 적극적으로 리팩토링한 프로젝트로, 기존 vim에서 기능이
추가된 superset을 지향하고 있습니다.

---

class: middle
# Neovim의 특징
--
 (vim과 비교해서)

--

- **더 강력한 플러그인**

- 더 나은 기본 설정과 기능

- embedding에 적합함

- vim에서 쉽게 이전할 수 있음


