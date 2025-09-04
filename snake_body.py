from turtle import Turtle

# كلاس يمثل جسم الثعبان ويتحكم في إنشائه وحركته
class Body_turtle:
    def __init__(self):
        # مواقع أولية لقطع جسم الثعبان
        self.x = [0, 20, 40, 60]
        self.turtles = []  # قائمة لحفظ قطع جسم الثعبان
        self.creat_the_turtles()  # إنشاء القطع
        self.head = self.turtles[-1]  # الرأس هو آخر قطعة

    # دالة لإنشاء كل قطعة من جسم الثعبان
    def creat_the_turtles(self):
        for i in range(len(self.x)):
            tut = Turtle()
            tut.penup()
            tut.color('white')
            tut.shape('square')
            tut.goto(self.x[i], 0)
            self.turtles.append(tut)

    # دالة لتحريك جسم الثعبان
    def move(self):
        # كل قطعة تتحرك لمكان القطعة اللي أمامها
        for i in range(len(self.turtles) - 1):
            self.turtles[i].goto(self.turtles[i + 1].pos())
        self.head.fd(10)  # الرأس يتحرك للأمام

    # دالة لإضافة قطعة جديدة (عند أكل تفاحة)
    def extra_turtle(self):
        tut = Turtle()
        tut.penup()
        tut.color('white')
        tut.shape('square')
        tut.goto(self.turtles[0].pos())  # تضاف في بداية الجسم
        self.turtles.insert(0, tut)
