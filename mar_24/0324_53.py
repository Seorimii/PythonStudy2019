class MyClass:
    def __del__(self):
     print('MyClass 인스턴트 객체가 메모리에서 제거됩니다')

obj = MyClass()
del obj