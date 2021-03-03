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
