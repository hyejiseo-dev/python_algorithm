class Person:
    def __init__(self, param_name): #self = 자신을 넘겨준다
        print("I am created!",self)
        self.name = param_name  # 내 안에 param_name 변수를 저장해 둔다는 뜻
    def talk(self):
        print('안녕하세요 제 이름은', self.name, '입니다')

person_1 = Person('유재석') #생성자
print(person_1.name) #저장된 이름 출력
person_1.talk()
person_2 = Person('박명수')
print(person_2.name)
person_2.talk()