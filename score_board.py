from turtle import Turtle, Screen
window = Screen()

# كلاس لعرض وتحديث النقاط وحفظ أعلى نتيجة
class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.total_score = 0  # نتيجة اللاعب

        # قراءة أعلى نتيجة محفوظة في ملف خارجي
        # file = open('highscore.txt')
        # self.highscore = int(file.read())
        self.highscore = self.read_file()
        # file.close()


        self.color('white')
        self.penup()
        self.hideturtle()
        self.goto(0, 260)  # عرض النتيجة أعلى الشاشة
        self.the_score()

        #داله لقرأة الملف وارجاع القيمه للمتغير highscore
    def read_file(self):
        with open("highscore.txt",'r') as file :
            
            return int(file.read())
    # لتحديث الملف عند انهاء اللعبه
    def new_highscore(self) :
        with open("highscore.txt",'w') as file:
            file.write(str(self.total_score))

    # دالة لعرض النتيجة الحالية وأعلى نتيجة
    def the_score(self):
        self.write(arg=f'Score {self.total_score}     High score: {self.highscore}',
                   align='center', font=('bold', 20, 'normal'))

    # دالة لزيادة وتحديث النتيجة عند أكل تفاحة
    def new_score(self):
        self.clear()
        self.total_score += 1
        self.write(arg=f'Score {self.total_score}     High score: {self.highscore}',
                   align='center', font=('bold', 20, 'normal'))
    
    # دالة تعرض رسالة الفوز
    def Win(self):
        window.bgcolor('dark green')
        self.goto(0, 0)
        self.write(arg=f"GREAT YOU REACH THE REQUIRED SCORE {self.total_score} !",
                   align='center', font=('Courier', 15, 'normal'))

    # دالة تعرض رسالة الخسارة وتحدّث أعلى نتيجة إذا تحققت
    def lose(self):
        self.clear()
        window.bgcolor('dark red')
        self.goto(0, 0)

        if self.total_score > self.highscore:
            self.highscore = self.total_score
            self.new_highscore()

        self.write(arg=f"----------- GAME OVER ----------- \n\nFinal Score: {self.total_score} \n\n High Score: {self.highscore}",align='center', font=('Courier', 20, 'normal'))
