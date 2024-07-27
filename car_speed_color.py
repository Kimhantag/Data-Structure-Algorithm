#car_speed_color.py
#2018015027 정보통계학과 김한탁
#클래스 정의를 이용해 차의 색상, 속도를 조절하고 비교하는 프로그램
#클래스 상속과 재정의를 통헤 차 속도의 변화를 확인하는 프로그램

class Car:
    def __init__(self, color, speed = 0):
        self.color = color
        self.speed = speed
    def speedUp(self) : self.speed += 10
    def speedDown(self) : self.speed -= 10
    def __eq__(self, carB): return self.color == carB.color
    def __str__(self): return "color = %s, speed = %d" % (self.color, self.speed) 
        
car1= Car('black', 0)
car2= Car('red', 120)
car3= Car('yellow', 30)
car4= Car('blue', 0)
car5= Car('green')
car6= Car('purple', 50)

car2.speedDown()
car4.speedUp()
car3.color = 'purple'
car5.speed =100

print('car2==car6:', car2==car6)
print('car3==car6:', car3==car6)

print("[car3]", car3)

class SuperCar(Car) :
    def __init__(self, color, speed = 0, bTurbo =True):
        super().__init__(color, speed)
        self.bTurbo = bTurbo
s1 = SuperCar("Gold", 0, True)
s2 = SuperCar("white", 0, False)

s1.speedUp()
s2.speedUp()
print("슈퍼카1:", s1)
print("슈퍼카2:", s2)

def setTurbo(self, bTurbo = True):
    self.bTurbo = bTurbo
def speedUp(self):
    if self.bTurbo:
        self.speed += 50
    else :
        super().speedUp()
def __str__(self) :
    if self.bTurbo:
        return "[%s] [speed = %d] 터보모드" %(self.color, self.speed)
    else:
        return "[%s] [speed = %d] 일반모드" %(self.color, self.speed)
    
s1.speedUp()
s2.speedUp()
print("슈퍼카1:", s1)
print("슈퍼카2:", s2)
