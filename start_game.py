import time
from turtle import Turtle, Screen
from score_board import Score
from apple import Apple
from snake_body import Body_turtle

# إعداد نافذة اللعبة
window = Screen()
window.setup(800, 600)
window.bgcolor("black")
window.title("Snake Game")
window.tracer(0)  # إيقاف التحديث التلقائي

# إنشاء الكائنات الأساسية
body_turtle = Body_turtle()
aplle = Apple()
score = Score()

# دالة تُستدعى عند الخسارة
def lose():
    window.bgcolor('dark red')
    tut = Turtle()
    tut.hideturtle()
    tut.penup()
    tut.color('white')
    tut.write(arg=f"------ GAME OVER ------\n     YOUR SCORE IS:{score.total_score}",
              align='center', font=('Courier', 20, 'normal'))

# دالة تُستدعى عند الفوز
def Win():
    window.bgcolor('dark green')
    tut = Turtle()
    tut.hideturtle()
    tut.penup()
    tut.color('white')
    tut.write(arg=f"GREAT YOU REACH THE REQUIRED SCORE {score.total_score} !",
              align='center', font=('Courier', 15, 'normal'))

# إعداد التحكم في الأسهم لتحريك الثعبان
def keys():
    def Up(): body_turtle.head.setheading(90)
    def Down(): body_turtle.head.setheading(270)
    def Left(): body_turtle.head.setheading(180)
    def Right(): body_turtle.head.setheading(0)

    window.listen()
    window.onkey(Up, "Up")
    window.onkey(Down, "Down")
    window.onkey(Right, "Right")
    window.onkey(Left, "Left")

keys()

# بدء تشغيل اللعبة
game_on = True
defulte_time = 0.1  # سرعة اللعبة

try:
    while game_on and score.total_score < 100:
        window.update()
        time.sleep(defulte_time)  # تأخير للحركة
        body_turtle.move()  # تحريك الثعبان

        # التحقق من الاصطدام بالجدار
        if body_turtle.head.xcor() >= 390 or body_turtle.head.xcor() <= -400:
            game_on = False
        elif body_turtle.head.ycor() >= 300 or body_turtle.head.ycor() <= -290:
            game_on = False

        # التحقق من الاصطدام بالجسم
        for i in range(len(body_turtle.turtles) - 1):
            if body_turtle.head.distance(body_turtle.turtles[i]) < 8:
                game_on = False

        # التحقق من أكل التفاحة
        if body_turtle.head.distance(aplle) < 15:
            defulte_time *= 0.98  # تسريع الحركة
            score.new_score()  # تحديث النقاط
            aplle.hide_apple()  # إخفاء القديمة
            aplle.creat_apple()  # إنشاء تفاحة جديدة
            body_turtle.extra_turtle()  # إضافة قطعة جديدة للجسم

    # عند انتهاء اللعبة
    if score.total_score >= 100:
        score.Win()  # عرض الفوز
    else:
        score.lose()  # عرض الخسارة

    window.exitonclick()  # إغلاق النافذة عند النقر
except:
    pass  # منع ظهور أخطاء في حال حدوث استثناء
