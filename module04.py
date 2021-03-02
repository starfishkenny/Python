code = 0
def getCode():
    return code # code 변수의 값을 반환
def setCode(arg):
    global code # 전역변수 (함수 밖에 선언된) code를 사용
    code = arg # code 변수에 arg를 대입
