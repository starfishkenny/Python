import module01
ret = module01.sum(10,20)

import module02
print('Main run')

import module03
print('Main run')
module03.viewPI()
module03.PI = 3.141592 # PI 변수의 값을 변경할 수도 있음
module03.viewPI()

import module03
print('Main run')
module03.angle = 10.4
print(module03.angle) # module03.py에는 angle 함수가 없으나 파이썬은 동적임 (미리 작성된 py 파일을 import 하더라도 실행 시 해당 모듈 내에 변수를 추가로 생성할 수 있음)

import module03
print('Main run')
module03.angle = 10.24 # module03.py 내에 angle 변수를 정의하는 것이 더욱 '자연스러운' 코드가 될 것임
ret = module03.transAngle()
print(ret)

import module04
module04.setCode(10)
ret = module04.getCode() # code 값이 안변함 (파이썬은 함수 안에서 변수를 사용하면 기본적으로 "지역" 개념에서 다룸)
print(ret) # 함수 밖에 선언된 같은 이름의 변수가 있더라도 대입연산 시 함수 내부에 새로운 변수를 만드는 개념

# 폴더가 다른 모듈 파일 import 하기

'''
import mylibs # import는 py 파일을 불러오는 것 => 모듈이 폴더 안에 있을 때는 '폴더명','모듈명'으로 작성해야함
print('Main run')
a = [10,40,60,30,20]
ret = mylibs.module05.total(a)
print(ret)
'''

'''
import mylibs.module05
print('Main run')
a = [10,40,60,30,20]
ret = mylibs.module05.total(a)
print(ret)
'''

# 또는

'''
from mylibs import module05
print('Main run')
a = [10,40,60,30,20]
ret = module05.total(a)
print(ret)
'''

# 또는
'''
from mylibs.module05 import *
print('Main run')
a = [10,40,60,30,20]
ret = total(a)
print(ret)
'''

import sys # 파이썬 라이브러리가 설치되어 있는 폴더들 확인
print(sys.path)

# 모듈이 위의 경로에 있는 경우에는 폴더를 이동하거나 폴더명을 작성할 필요 없이 모듈명만을 적어 사용할 수 있음
# 자신이 사용할 폴더는 추가하기 위해 sys.path.append('추가경로')를 실행하면 바로 모듈명으로 import하여 사용할 수 있음
# 1급 시험에서 1~2문제 나올뿐만 아니라 파이썬 학습에 필수적!

'''
from classes import *

gotcha = Pokemon()
jimbar = Pokemon()
swan = Pokemon()

# 포켓몬의 이름을 정해줌
gotcha.name = '갓챠'
jimbar.name = '짐바'
swan.name = '스완'

print(gotcha.name)
print(jimbar.name)
print(swan.name)
'''
'''
from classes import *

gotcha = Pokemon()
jimbar = Pokemon()
gotcha.name = '갓챠'
jimbar.name = '짐바'

gotcha.sleep()
jimbar.sleep()
'''
# 에러 발생 -> 메서드 정의 시 반드시 소괄호 안에 self를 적어야 
# sleep 메서드를 호출할 때는 소괄호 안에 아무것도 적지 않지만
# 파이썬은 실행 시 자동으로 현재 인스턴스의 정보를 self 매개변수로 전달
# 그러므로 sleep(gotcha)가 아닌 sleep()으로 호

'''
from classes import *
poke1 = Pokemon()
poke2 = Pokemon()
poke3 = Pokemon()
print(poke1.production,id(poke1))
print(poke2.production,id(poke2))
print(poke3.production,id(poke3))
'''

# 모든 인스턴스가 같은 값을 가져야 하는 경우 클래스 정의 시 필드에 값을 대입해 놓으면 편리
# 클래스의 인스턴스를 생성할 때 필수적인 정보가 있어야 함을 알릴 수 있는데 보통 __init__ 메서드라는 것을 정의하는 방법을 사용
# __init__: 인스턴스 생성 후 변수(필드)들을 초기화한다

'''
from classes import *
gotcha = Pokemon('갓챠')
jimbar = Pokemon('짐바')
swan = Pokemon()

gotcha.sleep()
jimbar.sleep()
swan.sleep()
'''
from classes import *
gotcha = Pokemon()
