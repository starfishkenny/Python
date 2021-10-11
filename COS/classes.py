'''
class Pokemon:
    name = "unknown"
    def sleep(self): # self 없으면 에러
        print('Zzzzzz...')
    pass
'''

# 이렇게 수정
# sleep() 함수 호출 시 어떤 객체에서 호출되는 것인지를 파악할 수 있

'''
class Pokemon:
    name = "unknown"
    def sleep(self):
        print(self.name,"Zzzzz...")
    pass
'''

'''
class Pokemon:
    production = "Made in Japan"
    name = None # 초기화되지는 않지만, 필드는 존재함을 알림 ('아직 값이 없음')
'''

'''
class Pokemon:
    name = 'unknown'
    def sleep(self):
        print("Zzzz...")

    # name을 정하지 않으면 생성불가
    def __init__(self,arg): # 반드시 arg 매개변수에 전달할 값이 있어야 함
        self.name = arg

    pass
'''

# 인스턴스가 생성되는 과정에는 __new__ 메서드도 있음

class Pokemon:
    def __new__(self):
        print("invoke new")
        return super().__new__(self)
    def __init__(self):
        print("invoke init")
    def __del__(self):
        print("invoke del")
    pass

# 가장 먼저 __new__ 메서드가 생성되고
# 이어서 __init__ 메서드가 실행되어 변수들을 초기화
# 사용이 끝난 인스턴스들은 자동적으로 __del__이 실행되면 종료

# 필드가 리스트인 경우

'''
class Pokemon:
    production = "Made in Japan"
    name = None
    scores = [] # 필드가 초기화되면 모든 인스턴스가 같은 값을 가짐을 기억할 것
    def __init__(self,name):
        self.name = name
    pass
'''

# 각 인스턴스가 개별적으로 가져야 하는 필드(변수, 리스트 등)는 __init__에서 생성하거나 할당하는 처리를 하여야 혼란이 없을 것

'''
class Pokemon:
    name = None
    scores = None
    def __init__(self,name):
        self.name = name
        self.scores = [] # 각 인스턴스 생성 시 따로 리스트를 대입
    pass
'''

# '이름'으로 '전투'('공격'과 '방어')를 할 수 있는 클래스 생성 (상속)
class Pokemon:
    name = "Unknown"
    def sleep(self):
        print(self.name,"Zzzz...")

    def __init__(self,name):
        self.name = name

    pass

'''
class BattlePokemon(Pokemon): # Pokemon(부모)을 상속받는 BattlePokemon(자식)
    pass
'''

# BattlePokemon 클래스에는 아무것도 적지 않았지만 이미 Pokemon 클래스의 name 필드와 __init__(),sleep() 메서드를 상속받은 상태가 됨

# 전투를 위한 메서드 추가

'''
class BattlePokemon(Pokemon):
    def attack(self):
        print(self.name,"attack ~")
    def defense(self):
        print(self.name,"defense ~")
    pass
'''
# 예시: 회사(회사명, 회사주소...) -> 영업부,개발팀.. -> 직원

'''
class Company:
    name = '(주)희망찬'
    address = 'Korea,Seoul'
    phone = '02-1234-5678'
    def view(self):
        s = self.name+","+self.address+","+self.bizphone
        print(s)

class Department(Company):
    name = '영업팀'
    phone = '02-1234-5679' # 부모와 필드명 같음
    def view(self):
        super().view() # super()는 자신의 부모 클래스를 의미
        print(self.name,self.phone)

class Employee(Department):
    name = '홍길동'
    phone = '010-1111-2222' # 부모와 필드명 같음
    def view(self):
        super().view()
        print(self.name,self.phone)
'''

# name이 모두 '홍길동'만 나옴
# 부모 클래스의 변수 중 같은 이름이 있는 경우 자식 클래스의 값으로 바뀐 것(덮어쓰임)임

# 필드명이 중복되지 않도록 하는 방법으로 해결 가능 (하지만 손이 많이 감)

'''
class Company:
    name = '(주)희망찬'
    address = 'Korea,Seoul'
    bizphone = '02-1234-5678'
    def view(self):
        s = self.name+","+self.address+","+self.bizphone
        print(s)

class Department(Company):
    part_name = '영업팀'
    part_phone = '02-1234-5679'
    def view(self):
        super().view() # super()는 자신의 부모 클래스를 의미
        print(self.part_name,self.part_phone)

class Employee(Department):
    em_name = '홍길동'
    em_phone = '010-1111-2222'
    def view(self):
        super().view()
        print(self.em_name,self.em_phone)
'''

# 만약 Company 클래스의 인스턴스를 생성하여 view()메서드를 호출하면 "회사"의 정보만 보일 뿐, 그 회사에 어떤 부서가 있는지 직원들은 누가 있는지, 몇 명 있는지를 알 수 없음
# 즉 정보를 처리함에 있어 시작점(중심점)이 되는 것이 "직원"이 됨

'''
class Company:
    name = '(주)희망찬'
    address = 'Korea,Seoul'
    bizphone = '02-1234-5678'
    def view(self):
        s = self.name+","+self.address+","+self.bizphone
        print(s)

class Department(Company):
    part_name = '영업팀'
    part_phone = '02-1234-5678'
    def view(self):
        super().view() # super()는 자신의 부모 클래스를 의미
        print(self.part_name,self.part_phone)

class Employee(Department):
    em_name = '홍길동'
    em_phone = '010-1111-2222'
    def view(self):
        super().view()
        print(self.em_name,self.em_phone)
    def __init__(self,name,phone): # 직원을 여러 명 생성할 수 있도록 추
        self.em_name = name
        self.em_phone = phone
'''
     
# "상속" 개념의 코드와 "포함" 개념의 코드 비교

class Employee:
    name = ''
    phone = ''
    def __init__(self,name,phone):
        self.name = name
        self.phone = phone
    def view(self):
        print('\t\t',self.name,self.phone)

class Department:
    name = ''
    phone = ''
    crews = None
    def __init__(self,name,phone):
        self.name = name
        self.phone = phone
        self.crews = [] # '부서'에는 여러 명의 '직원'이 소속(포함)됨
    def view(self):
        print('\t',self.name,self.phone)
        for crew in self.crews:
            crew.view()
    def appendEmployee(self,name,phone):
        self.crews.append(Employee(name,phone))

class Company:
    name = ''
    address = ''
    phone = ''
    departments = None
    def __init__(self,name,address,phone):
        self.name = name
        self.address = address
        self.phone = phone
        self.departments = [] # '회사'에는 여러 개의 '부서'가 소속(포함)됨
    def view(self):
        s = self.name+","+self.address+","+self.phone
        print(s)
        for part in self.departments:
            part.view()
    def appendDepart(self,name,phone):
        self.departments.append(Department(name,phone))
        
