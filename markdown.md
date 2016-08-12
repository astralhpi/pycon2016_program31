name: title
class: middle, center, inverse

.pycon_logo[![PYCON 2016 APAC](./images/mark-white.png)]
# .title_upper[Python으로 만드는]<br>NEOVIM ASYNC PLUGIN

.author[송재학 ([master@hpi.cc](mailto:master@hpi.cc))]

---
class: middle

# 발표자

## 송재학

* 현재 백수이지만 열심히 살고 있습니다.

* (전) 문래빗 주식회사 대표
  * 판타지x러너즈 for 카카오 서버 개발 (python)

* omnisharp-sublime (sublime text를 위한 C# IDE 플러그인)

---

class: center, middle

### 저는 오랫동안 vim을 주력 에디터로 쓰고 **싶었습니다.**

--

#### vim은 위대한 텍스트 에디터이지만
#### 매우 주관적인 장애물이 좀 있었습니다.

---
class: middle

.logo[
  ![vim logo](./images/vim_editor.gif)
]

* 로고랑 사이트가 오래됨.

* hip 하지 않음.

* 개인적으로 Vimscript가 좀 별로임.
  * 다른 언어 붙이긴 귀찮음 (빌드할 때부터 신경 써줘야함)

* 커뮤니티보다는 개인의 노력으로 개발되고 있음.

* ** 대부분의 플러그인이 sync로 동작하여, 플러그인에 의해 쉽게 느려짐**

  * async로 동작하는 플러그인 개발이 쉽지 않음. 


---
class: center, middle

.logo[
  ![neovim logo](./images/neovim-logo.svg)
]

--

class: center, middle
## 말그대로 Vim의 미래
Vim을 적극적으로 리팩토링한 superset

---
class: middle

.logo[
  ![neovim logo](./images/neovim-logo.svg)
]

* 로고와 사이트가 최근에 만들어졌는가? (O)

--

* hip한가? (O)

--

* 쉽게 다른 언어로 플러그인 개발을 할 수 있는가? (O)

--

* GitHub에서 핫한가? (O)
  * watch: 957
  * star: 19,586
  * fork: 1,384

--

* async 플러그인 개발이 쉬운가? (O)


---

class: center, middle

### 다 좋은데, 안정적일까?

---

class: middle
# 현황
#### (2016.08.12 기준)

* stable version: v0.1.4

  * v0.1.0 목표가 stable한 빌드.
    * v0.1.0 이후로도 릴리즈가 4번이나 됨.

  * 현재 안정적이고 실사용 가능.

---

class: center, middle


.logo[
  ![어머 저건! 꼭 써봐야해~](./images/imustbuy.jpg)

]

## 지금 당장 Neovim을 설치해야겠다! 

---

class: middle
# 특징 

공식 사이트에 따르면...

- **더 강력한 플러그인**

- 더 나은 기본 기능과 설정 

- 기본으로 내장된 embedding

- Vim에서 쉽게 옮길 수 있음

---

class: middle

# 더 강력한 플러그인

  * 오늘은 여기에만 집중해봅시다.

---

class: middle

# 더 강력한 플러그인
  
  * 핵심은 Msgpack-RPC

---

class: middle

# Msgpack-RPC

 * Neovim은 서버로 동작합니다.

 * stdin/stdout, socket 등을 통해 Neovim의 RPC API를 사용할 수 있습니다.

---

## 현재 API 클라이언트 모듈이 있는 플랫폼

* C#
* C++
* Clojure
* Common Lisp
* Elixir
* Filesystem
* Go
* Haskell
* Java
* Julia
* Lua
* Node.js
* Perl
* R
* Ruby
* Rust

...

---

class: middle

# 그리고 당연히 **Python**!!

---

class: middle

# Hello World!

--

### python-neovim 모듈을 사용해서 "Hello World!" 출력 해봅시다.

---

# Hello World!
### 0. python-neovim 설치

```bash
> # neovim의 RPC API을 사용하기  위한 모듈
> pip install neovim
```

--

### 1. Neovim 실행

```bash
> # NVIM_LISTEN_ADDRESS: neovim의 RPC 주소 지정
> NVIM_LISTEN_ADDRESS=/tmp/nvim nvim
```

--

### 2. Python REPL에서 명령어 실행

``` python
> python
>>> from neovim import attach
>>> nvim = attach('socket', path='/tmp/nvim')
>>> nvim.command('echo "hello world!"')

```

---

# Hello World!

![hello world 출력 화면](./images/nvim_helloworld.png)

---

class: middle

## 왜 Python REPL을 사용한거죠?

--

* 부담 없이 API를 테스트 해볼 수 있습니다.

* help 함수로 API 문서를 즉석에서 확인할 수 있습니다.
---

class: middle
# "REMOTE PLUGIN"

--
## Neovim의 Msgpack-RPC를 통해 동작하는 플러그인

---

class: middle
## 어떤 언어로든 쉽게 Neovim 플러그인 개발 가능!!

* 아까 얼마나 많은 언어를 사용하 수 있는지 보셨죠?

---
class: middle

## 이미 여러 플러그인들이 Python으로 개발됨
### Floobits, deoplete, lldb.nvim, nvim-ipy, proteome.nvim ...

---
class: middle

## 간단한 플러그인을 만들어 봅시다.
### 파일 하나면 됩니다.


---

class: middle

## SimplePlugin 플러그인 예제

```python
# ~/.config/nvim/rplugin/python/simple.py

import neovim

@neovim.plugin
class SimplePlugin(object):

    def __init__(self, nvim):
        self.nvim = nvim

    @neovim.function('SimpleFunc')
    def func(self, args):
        self.nvim.command('echo "simple func"')

    @neovim.command('SimpleCommand', range='', nargs='*')
    def command(self, args, range):
        self.nvim.command('echo "simple command"')

    @neovim.autocmd('BufEnter', pattern="*.py")
    def autocmd(self):
        self.nvim.command('echo "simple autocmd"')
```

---

class: middle
### 파일 작성 후, neovim상에서
```vim
:UpdateRemotePlugins
```
### 해주면 플러그인이 동작합니다!

---

class: middle

## 참 쉽죠?

--

### 그래도 차근차근 살펴봅시다.

---

class: middle

## SimplePlugin 살펴보기- class 선언 

```python
import neovim
import time

@neovim.plugin
class SimplePlugin(object):

    def __init__(self, nvim):
        self.nvim = nvim
```

플러그인 class를 선언하고 생성자를 지정해 줍니다.

---

class: middle

## SimplePlugin 살펴보기- vim 함수 등록

```python
    @neovim.function('SimpleFunc')
    def func(self, args):
        self.nvim.command('echo "simple func"')
```

* Vim 함수를 등록합니다.

--

#### 다른 vim 함수와 똑같이 사용할 수 있습니다.
```vim
:call SimpleFunc()
"simple func"

```

---

class: middle

## SimplePlugin 살펴보기- command 등록

```python
    @neovim.command('SimpleCommand', range='', nargs='*')
    def command(self, args, range):
        self.nvim.command('echo "simple command"')
```

* Vim command를 등록합니다.

--

#### 마찬가지로, vim의 다른 command와 똑같이 사용할 수 있습니다.
```vim
:SimpleCommand
"simple command"
```
 
---

class: middle

## SimplePlugin 살펴보기 - autocmd 등록

```python
    @neovim.autocmd('BufEnter', pattern="*.py")
    def autocmd(self):
        self.nvim.command('echo "simple autocmd"')
```


* autocmd를등록합니다.
  * autocmd는 이벤트 처리를 위해 사용할 수 있습니다.

* 위의 autocmd는...
  * 버퍼에 들어가는 경우 실행되는 autocmd 입니다.
  * 확장자가 py로 끝나는 경우에만 실행됩니다.

--

```vim
:help autocommand-events
```

명령어로 지원하는 이벤트를 확인할 수 있습니다.

---

class: middle

## 이제,

--

 1. nvim의 RPC API를 파이썬 쉘에서 실행해볼 수 있습니다.
 
--

 2. 플러그인을 만들 수 있습니다.
     1. 함수를 만들 수 있습니다.
     2. command를 만들 수 있습니다.
     3. 이벤트를 처리할 수 있습니다. (autocmd)

---

class: middle, center

![우오오오오](./images/uooooo.jpg)
### 본격적으로 플러그인을 만들 준비가 되었습니다!

---

class: middle

## 플러그인 만들어보기

---

class: middle

## 사례

* 덕룡이는 최근 Python으로 알고리즘 문제를 풀고 있습니다.

* 그런데, 수동으로 코드를 실행해보는 것이 너무 귀찮습니다. 

* 코드를 저장할 때마다 자동으로 코드가 실행되었으면 합니다.


---

class: middle

### 우리가 해결할 수 있을 것 같습니다!


---
class: middle

## 플러그인 만들기

* 다행히 덕룡이는 정답 체크를 할 수 있는 스크립트를 미리 만들어 뒀습니다.

---
### 미리 만들어둔 스크립트

```bash
    > python checker.py solution.py
    ==============================
    input
    ==============================
    3
    1 1
    2 2
    3 3

    ==============================
    expected output
    ==============================
    2
    4
    6

    ==============================
    output
    ==============================
    2
    4
    6

    ==============================
    run time: 0.039005
    ==============================
    succeed!
```
---
class: middle

## 플러그인 만들기

* 이 스크립트를 Vim에 붙여봅시다.

---
class: middle

### 커맨드 만들기

```vim
:CheckSolution <file 경로>
```

로 실행할 수 있는 커맨드를 만들어 봅시다.

---
class: middle

### 커맨드 만들기

```python
import neovim
import os
from .checker import check

@neovim.plugin
class AlgoTestPlugin(object):

    def __init__(self, nvim):
        self.nvim = nvim
```
플러그인 클래스를 정의해주고,

---

class: middle

### 커맨드 만들기

```python
    @neovim.command('CheckSolution', nargs='*')
    def command(self, args):
        for filename in args:
            dirname = os.path.dirname(filename)
            inputfile = os.path.join(dirname, 'input.txt')
            outputfile = os.path.join(dirname, 'output.txt')

            result = check(filename, inputfile, outputfile)

            self.nvim.command('echo "%s"' % result)
```
커맨드를 정의해줍니다.

---

### 커맨드 만들기

```vim
:CheckSolution solution.py
```
커맨드을 실행해봅니다.

--

```bash
==============================
input
==============================
2
1 1
2 2
==============================
expected output
==============================
2
4
==============================
output
==============================
2
4
==============================
run time: 0.040526
==============================
succeed!
```

잘됩니다.

---

class: middle

### 그런데...

--
class: middle

.small_img[![귀차니스트](./images/bothering_man.jpeg)]
#### 덕룡이는 귀차니스트입니다.

 * 하지만 매번 인자를 넣어줘야하는 것이 귀찮다네요.

 * 인자를 생략하면 현재 파일의 경로가 들어가게 합시다.

---

class: middle

그런데 API를 모르다보니, 어디서 시작을 해야할지 모르겠네요.
--


[Hello World!에서 했던 것처럼](#15) python REPL을 사용해봅시다.


---

### 커맨드 인자 생략

```python
>> help(nvim.current)
# nvim.current에 buffer가 있는 것을 확인함.

```

--

```python
>> help(nvim.current.buffer)
# buffer에 name이 있는 것을 확인함.
```

--

```python
>> nvim.current.buffer.name
'/Users/jaehak/Projects/algotest/sample/solution.py'
```
우리에게 필요한 내용인 것 같습니다.

--

 ---

같은 폴더의 input.txt을 열고 확인해봅니다.

```python
>> nvim.current.buffer.name
'/Users/jaehak/Projects/algotest/sample/input.txt'
```

이 API를 사용하면 될 것 같습니다!

---

### 커맨드 인자 생략

```python
    @neovim.command('CheckSolution', nargs='*')
    def command(self, args):
+
+        if len(args) == 0:
+            args = [self.nvim.current.buffer.name]
+
        for filename in args:
            dirname = os.path.dirname(filename)
            inputfile = os.path.join(dirname, 'input.txt')
            outputfile = os.path.join(dirname, 'output.txt')

            result = check(filename, inputfile, outputfile)

            self.nvim.command('echo "%s"' % result)
```

--
```vim
:CheckSolution

==============================
input
==============================
3
...
```
잘 되네요.

---

class: middle

![bothering](./images/bothering.jpeg)
## 그래도 귀찮다고 하네요.
문제는 어떻게 푸나 몰라.

--

 * 현재까지는 :CheckSolution 커맨드를 실행해줘야합니다.
 
 * 파일을 저장할 때, 자동으로 실행되었으면 좋겠네요.

---

class: middle

### 플러그인 만들기 - autocmd 등록하기

저장할 때, 자동으로 실행되는 autocmd를 등록해봅시다.

---

class: middle

### 플러그인 만들기 - autocmd 등록하기

```vim
# autocmd 이벤트 리스트 확인하기
:help autocommand-events
```
버퍼를 파일로 저장한 이후 실행되는 'BufWritePost' 이벤트를 발견했습니다.

---
class: middle

### 플러그인 만들기 - autocmd 등록하기

'BufWritePost' autocmd를 등록합시다.

--

```python
    @neovim.autocmd("BufWritePost", pattern="*.py", sync=True)
    def on_bufwrite_post(self):
        filename = self.nvim.current.buffer.name

        dirname = os.path.dirname(filename)
        inputfile = os.path.join(dirname, 'input.txt')
        outputfile = os.path.join(dirname, 'output.txt')

        # input/output 파일이 있는 경우에만 실행
        if all([os.path.exists(path) for path in [inputfile, outputfile]]):
            self.nvim.command('CheckSolution %s' % filename)
```

---
class: middle

### 플러그인 만들기 - autocmd 등록하기

```vim
:w
```

```bash
==============================
input
==============================
3
1 1
2 2
3 3

==============================
expected output
==============================
2
4
6
...
```

역시 잘 동작합니다.

---

class: middle, center

![echo를 사용하는 플러그인](./images/plugin_echo.gif)

그런데, 출력을 위해 echo를 사용하다보니 불편하네요.

---
class: middle, center

![책임감](./images/sense_of_responsibility.jpg)
### 덕룡이가 이대로는 쓸 수없다며 책임감을 요구하네요.

--
#### 출력 전용 버퍼를 만들어 만족시켜 줍시다. 

---

class: middle

### 플러그인 만들기 - 출력용 버퍼 만들기
출력용 버퍼를 만들어서, 그 버퍼에 출력해봅시다.


---
### 플러그인 만들기 - 출력용 버퍼 만들기
python REPL를 활용해서 API를 파악해봅시다.

--

#### 버퍼 생성 테스트해보기
```python
>>> nvim.command('set splitright')
>>> nvim.command('vnew')
# 오른쪽에 빈 버퍼가 생성됩니다.
# vsplit되서 포커싱 됨
```

--

#### 버퍼 가져오기
```python
>>> b = nvim.current.buffer
>>> b.name
''
```

--

#### 모든 버퍼 리스트 가져오기
```python
>>> names = [b.name for b in nvim.buffers]
>>> print(names)
['', '/Users/jaehak/Projects/algotest/sample/solution.py']
```


---

### 플러그인 만들기 - 출력용 버퍼 만들기

#### 버퍼 설정하기
```python
# 이름 설정
>>> b.name = "__algotest_result"

# 저장 안되고, swap파일 생성 안되게 설정
>>> nvim.command("setlocal buftype=nofile noswapfile")

```

---

### 플러그인 만들기 - 출력용 버퍼 만들기

#### 버퍼 내용 조작해보기
```python
>>> b[0]
''
>>> b[0] = 'Hello World!'
# 1번째 라인이 'Hello World!'로 바뀜

>>> b.append('Hello World2')
# 2번째 라인에 'Hello World2'가 추가됨

>>> del b[0]
# 1번째 라인을 제거함
```

--

##### vim 화면

```vim
  1                                       |  1 Hello World2
~                                         |~
~                                         |~
~                                         |~
```

---

class: middle

### 플러그인 만들기 - 출력용 버퍼 만들기

#### 필요한 API는 모두 파악했습니다.
--


이제 플러그인 코드만 짜면 됩니다.


---

### 플러그인 만들기 - 출력용 버퍼 만들기

일단 필요한 메소드들을 정의해줍시다.

--

 ---
#### 1. 버퍼를 생성하거나 가져오는 메소드

```python
    def create_or_get_buffer(self, name):
        # 이미 있는 버퍼 중, 이름이 일치하는 버퍼가 있으면 리턴
        for b in self.nvim.buffers:
            bname = os.path.basename(b.name)

            if bname == name:
                return b

        # 새 버퍼 생성
        self.nvim.command('set splitright')
        self.nvim.command('vnew')

        b = self.nvim.current.buffer
        b.name = name
        self.nvim.command("setlocal buftype=nofile noswapfile")
        return  b
```
--

* 이미 버퍼가 생성되어있으면 해당 버퍼를 리턴해줍니다.
* 버퍼가 없다면 버퍼를 생성해줍니다.

---

### 플러그인 만들기 - 출력용 버퍼 만들기

#### 2. 버퍼를 초기화는 메소드

```python
    def clear_buffer(self, buffer):
        buffer[:] = []
```

#### 3. 버퍼에 출력을 추가해주는 메소드

```python
    def append_text(self, buffer, text):
        lines = text.splitlines()
        buffer[len(buffer):] = lines
```

---
### 플러그인 만들기 - 출력용 버퍼 만들기
그리고 command에서 출력을 echo 대신 버퍼를 사용하도록 합시다.


```diff
    @neovim.command('CheckSolution', nargs='*')
    def command(self, args):

        if len(args) == 0:
            args = [self.nvim.current.buffer.name]

+        buffer = self.create_or_get_buffer('__algotest_result')
+        self.clear_buffer(buffer)
+
        for filename in args:
            dirname = os.path.dirname(filename)
            inputfile = os.path.join(dirname, 'input.txt')
            outputfile = os.path.join(dirname, 'output.txt')

            result = check(filename, inputfile, outputfile)

-            self.nvim.command('echo "%s"' % result)
+            self.append_text(buffer, result)

```

---

class: middle, center

### 결과를 확인해봅시다!

![플러그인 buffer 버전](./images/plugin_buffer.gif)

---

class: middle, center

# 완성!

---

class: middle, center


![고객 만족](./images/wow.jpg)
### 덕룡이도 만족할꺼예요.
#### 덕룡이가 우리 고객은 아니지만요...

---

class: middle, center

## 그런데... 좀 허전하네요.

--
### 제목이 'Python으로 만드는 NEOVIM ASYNC PLUGIN' 아니었나요?
--

비동기는 어디갔죠?
--


이런식이면 저장할 때 엄청 느려지는 것 아닌가요?

---
class: middle, center

### 실은....
### 이제까지 만든 것이 비동기 플러그인 입니다.

--

저장할 때 느려지지 않아요.

---

class: middle

### neovim의 python-client 모듈을 사용하면
### 기본적으로 비동기로 동작합니다.

 * function call
 * command
 * autocmd

---
### 필요하다면 sync로 동작하게 할 수는 있어요.

```diff
import neovim

@neovim.plugin
class SimplePlugin(object):

    def __init__(self, nvim):
        self.nvim = nvim

-    @neovim.function('SimpleFunc')
+    @neovim.function('SimpleFunc', sync=False)
    def func(self, args):
        self.nvim.command('echo "simple func"')

-    @neovim.command('SimpleCommand', range='', nargs='*')
+    @neovim.command('SimpleCommand', range='', nargs='*', sync=False)
    def command(self, args, range):
        self.nvim.command('echo "simple command"')

-    @neovim.autocmd('BufEnter', pattern="*.py")
+    @neovim.autocmd('BufEnter', pattern="*.py", sync=False)
    def autocmd(self):
        self.nvim.command('echo "simple autocmd"')
```

---
class: middle, center

# SYNC vs ASYNC
이제까지 만들어본 플러그인으로 비교해봅시다.

--
```python
time.sleep(5)
```
이 들어가있는 코드에서 플러그인 사용해봅시다.

---
class: middle, center

## SYNC 버전

![SYNC 버전](./images/plugin_sync.gif)

---
class: middle, center

## SYNC 버전

![이 얼마나 끔찍하고 무시무시한 플러그인이니?](./images/terrible.png)
### 끔찍하게도 실행시간 5.03초동안 vim이 프리징 됩니다.

---
class: middle, center

## ASYNC 버전

![ASYNC 버전](./images/plugin_async.gif)

---

class: middle, center

## ASYNC 버전

![아... 회복된다.](./images/healing.jpeg)
###  반면, ASYNC버전은 vim이 프리징되지 않습니다.

---

class: middle

## 최종 정리

1. neovim 좋아요.

--

1. neovim 플러그인은 python으로 쉽게 만들 수 있어요.

--

2. python REPL을 활용하면 neovim API를 쉽게 테스트해볼 수 있어요.

---

class: middle, center

.small_img[![bob](./images/bob.jpg)]

## 없으면 만들어서 씁시다.
### 우린 코딩할 수 있으니까요.

---

class: middle, center

# QnA

---

class: middle, center

## 이 프레젠테이션 자료는
## [remark.js](http://remarkjs.com/#1)를 사용하여 작성되었으며,
## [GitHub Pages](https://pages.github.com/)로 호스팅됩니다.

---

class: middle, center

# 감사합니다.

