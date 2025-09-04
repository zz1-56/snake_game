import random
from turtle import Turtle, Screen

# كلاس يمثل التفاحة ويحدد موقعها
class Apple(Turtle):
    def __init__(self):
        super().__init__()
        self.creat_apple()  # إنشاء التفاحة مباشرة

    # دالة لإنشاء تفاحة جديدة في مكان عشوائي
    def creat_apple(self):
        self.shape('circle')
        self.penup()
        self.color('red')
        self.shapesize(0.5)  # تصغير حجم التفاحة

        # تحديد موقع عشوائي داخل الشاشة
        self.x = random.randint(-380, 380)
        self.y = random.randint(-280, 280)
        self.goto(self.x, self.y)

    # دالة لمسح التفاحة (عند أكلها)
    def hide_apple(self):
        self.clear()
