import random
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QGridLayout, QLabel, QPushButton, QHBoxLayout
from PySide6.QtCore import Qt, QSize

def main():
    app= QApplication()
    window= Game()
    window.show()
    app.exec()


class Game(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('2048 Game')
        self.setFixedSize(700, 700)

        #TODO Fix recursion error so you can end the game
        #TODO Make Homescreen

        self.two= '''
                QLabel {
                background: #FFFFC5;
                border-radius: 4px;
                border: 1px solid #000000;
                color: #000000;
                font: 40px;      
                }
'''

        self.four= '''
                QLabel {
                background: #FFD580;
                border-radius: 4px;
                border: 1px solid #000000;
                color: #000000;
                font: 40px;      
                }
'''

        self.eight= '''
                QLabel {
                background: #ffb09c;
                border-radius: 4px;
                border: 1px solid #000000;
                color: #000000;
                font: 40px;      
                }
'''

        self.sixteen= '''
                QLabel {
                background: #FF5F15;
                border-radius: 4px;
                border: 1px solid #000000;
                color: #000000;
                font: 40px;      
                }
'''

        self.thirty_two= '''
                QLabel {
                background: #DC143C;
                border-radius: 4px;
                border: 1px solid #000000;
                color: #000000;
                font: 40px;      
                }
'''

        self.sixty_four= '''
                QLabel {
                background: #9B870C;
                border-radius: 4px;
                border: 1px solid #000000;
                color: #000000;
                font: 40px;      
                }
'''

        self.hundred_twenty_eight= '''
                QLabel {
                background: #FFC0CB;
                border-radius: 4px;
                border: 1px solid #000000;
                color: #000000;
                font: 40px;      
                }
'''

        self.thundred_fifty_six= '''
                QLabel {
                background: #8B0000;
                border-radius: 4px;
                border: 1px solid #000000;
                color: #000000;
                font: 40px;
                }
'''
        self.fhundred_twelve= '''
                QLabel {
                background: #90bd71;
                border-radius: 4px;
                border: 1px solid #000000;
                color: #000000;
                font: 40px;
                }
'''

        self.thousand_twenty_four= '''
                QLabel {
                background: #692b87;
                border-radius: 4px;
                border: 1px solid #000000;
                color: #000000;
                font: 40px;
                }
'''

        self.tthousand_fourty_eight= '''
                QLabel {
                background: #21473f;
                border-radius: 4px;
                border: 1px solid #000000;
                color: #000000;
                font: 40px;
                }
'''



        self.Grid()

    def Grid(self):
        self.Game_container= QWidget()
        self.setCentralWidget(self.Game_container)
        self.Game_container.setStyleSheet('background: #FFFFFF')
        self.Game_layout= QGridLayout(self.Game_container)

        Grid_list= [(0, 0), (0, 1), (0, 2), (0, 3),
                    (1, 0), (1, 1), (1, 2), (1, 3),
                    (2, 0), (2, 1), (2, 2), (2, 3),
                    (3, 0), (3, 1), (3, 2), (3, 3)]

        self.boxes= []

        self.game_list= [0, 0, 0, 0,
                         0, 0, 0, 0,
                         0, 0, 0, 0,
                         0, 0, 0, 0]

        for i in range(0, len(self.game_list), 4):
            print(*self.game_list[i : i + 4])


        #How this work is that you make a list object first
        for x, y in Grid_list:

            #The you make the Label for this run through
            n_box= QLabel()
            #And style it
            n_box.setText('')
            n_box.setStyleSheet('background: #696969; border-radius: 4px;')

            #Then you append that label to the list object
            #This works because the hash for the QLabel won't be the same no matter the varaible name
            #So even though the varaibe is all n_box the hash is all you care about
            self.boxes.append(n_box)
            #And add it to the game layout
            self.Game_layout.addWidget(n_box, x, y)

        self.spawn_square()

    def spawn_square(self):
        self.box_number= random.randint(0, 15)

        if not self.game_list[self.box_number] == 0:
            self.spawn_square()
            return

        add_box=self.boxes[self.box_number]

        numbers= ['2', '4', '8']
        weights= [50, 40, 10]

        number= random.choices(numbers, weights=weights)[0]

        if number == '2':
            add_box.setText('2')
            add_box.setAlignment(Qt.AlignmentFlag.AlignCenter)
            add_box.setStyleSheet(self.two)
            self.game_list[self.box_number] = 2 # type: ignore

        elif number == '4':
            add_box.setText('4')
            add_box.setAlignment(Qt.AlignmentFlag.AlignCenter)
            add_box.setStyleSheet(self.four)
            self.game_list[self.box_number] = 4 # type: ignore

        elif number == '8':
            add_box.setText('8')
            add_box.setAlignment(Qt.AlignmentFlag.AlignCenter)
            add_box.setStyleSheet(self.eight)
            self.game_list[self.box_number] = 8 # type: ignore


        for i in range(0, len(self.game_list), 4):
            print(*self.game_list[i : i + 4])

        self.game_lines()


    #The name of the function matters in this case
    def keyPressEvent(self, event):
        key= event.key()

        if key == Qt.Key.Key_Left:
            self.move_left()

        if key == Qt.Key.Key_Right:
            self.move_right()

        if key == Qt.Key.Key_Up:
            self.move_up()
        
        if key == Qt.Key.Key_Down:
            self.move_down()


        if key == Qt.Key.Key_A:
            self.move_left()

        if key == Qt.Key.Key_D:
            self.move_right()

        if key == Qt.Key.Key_W:
            self.move_up()

        if key == Qt.Key.Key_S:
            self.move_down()

    def move_left(self):
        try:
            for n in range(len(self.rows)):
                row= self.rows[n]
                #You need range(len(nums)). You can just do in nums
                x=0
                for i in range(len(row)):
                    if row[i]:
                        #Use line below to switch values
                        row[x], row[i] = row[i], row[x]
                        x+=1
                        
                #To understand it get a sheet of paper and write it out
                for j in range(len(row)):
                    if row[j] and j > 0:
                        if row[j] == row[j-1]:
                            row[j-1]= row[j] + row[j-1]
                            row[j]=0

                y=0
                for i in range(len(row)):
                    if row[i]:
                        #Use line below to switch values
                        row[y], row[i] = row[i], row[y]
                        y+=1
                

            x=0
            y=0
            self.update_game_rows()
        
        except RecursionError:
            self.lose_game()

        print('\n')
        for i in range(0, len(self.game_list), 4):
            print(*self.game_list[i : i + 4])


    def move_right(self):
        try:
            for n in range(len(self.rows)):
                row= self.rows[n]
                x=len(row) -1

                for i in range(len(row)-1, -1, -1):
                    if row[i]:
                        #Use line below to switch values
                        row[x], row[i] = row[i], row[x]
                        x-=1

                #To figure out write it out
                for j in range(len(row)-1, -1, -1):
                    if row[j] and j+1 < len(row):
                        if row[j] == row[j+1]:
                            row[j]= row[j] + row[j+1]
                            row[j+1]=0


                y=len(row) -1
                for i in range(len(row)-1, -1, -1):
                    if row[i]:
                        #Use line below to switch values
                        row[y], row[i] = row[i], row[y]
                        y-=1


            x=0
            y=0
            self.update_game_rows()
        
        except RecursionError:
            self.lose_game()

        print('\n')
        for i in range(0, len(self.game_list), 4):
            print(*self.game_list[i : i + 4])


    def move_up(self):
        try:
            for n in range(len(self.colmuns)):
                colmun= self.colmuns[n]
                #You need range(len(nums)). You can just do in nums
                x=0
                for i in range(len(colmun)):
                    if colmun[i]:
                        #Use line below to switch values
                        colmun[x], colmun[i] = colmun[i], colmun[x]
                        x+=1
                        

                for j in range(len(colmun)):
                    if colmun[j] and j > 0:
                            if colmun[j] == colmun[j-1]:
                                colmun[j-1]= colmun[j] + colmun[j-1]
                                colmun[j]=0


                y=0
                for i in range(len(colmun)):
                    if colmun[i]:
                        #Use line below to switch values
                        colmun[y], colmun[i] = colmun[i], colmun[y]
                        y+=1
                

            x=0
            y=0
            self.update_game_colmuns()

        except RecursionError:
            self.lose_game()

        print('\n')
        for i in range(0, len(self.game_list), 4):
            print(*self.game_list[i : i + 4])

    def move_down(self):
        try:
            for n in range(len(self.colmuns)):
                colmun= self.colmuns[n]
                x=len(colmun) -1

                for i in range(len(colmun)-1, -1, -1):
                    if colmun[i]:
                        #Use line below to switch values
                        colmun[x], colmun[i] = colmun[i], colmun[x]
                        x-=1

                for j in range(len(colmun)-1, -1, -1):
                    if colmun[j] and j+1 < len(colmun):
                        try:
                            if colmun[j] == colmun[j+1]:
                                colmun[j+1]= colmun[j] + colmun[j+1]
                                colmun[j]=0

                        except IndexError:
                            pass

                y=len(colmun) -1
                for i in range(len(colmun)-1, -1, -1):
                    if colmun[i]:
                        #Use line below to switch values
                        colmun[y], colmun[i] = colmun[i], colmun[y]
                        y-=1


            x=0
            y=0
            self.update_game_colmuns()

        except RecursionError:
            self.lose_game()

        print('\n')
        for i in range(0, len(self.game_list), 4):
            print(*self.game_list[i : i + 4])

    def game_lines(self):
        self.rows= [[self.game_list[0], self.game_list[1], self.game_list[2], self.game_list[3]],
                    [self.game_list[4], self.game_list[5], self.game_list[6], self.game_list[7]],
                    [self.game_list[8], self.game_list[9], self.game_list[10], self.game_list[11]],
                    [self.game_list[12], self.game_list[13], self.game_list[14], self.game_list[15]]]

        self.colmuns= [[self.game_list[0], self.game_list[4], self.game_list[8], self.game_list[12]],
                       [self.game_list[1], self.game_list[5], self.game_list[9], self.game_list[13]],
                       [self.game_list[2], self.game_list[6], self.game_list[10], self.game_list[14]],
                       [self.game_list[3], self.game_list[7], self.game_list[11], self.game_list[15]]]


    def update_game_rows(self):
        one=0
        two=1
        three=2
        four=3
        for o, t, th, f in self.rows:
            self.game_list[one] = o
            self.game_list[two]= t
            self.game_list[three]= th
            self.game_list[four]= f
            one+=4
            two+=4
            three+=4
            four+=4


        self.spawn_square()
        self.game_lines()
        self.update_squares()

    def update_game_colmuns(self):
        one=0
        two=4
        three=8
        four=12
        for o, t, th, f in self.colmuns:
            self.game_list[one] = o
            self.game_list[two]= t
            self.game_list[three]= th
            self.game_list[four]= f
            one+=1
            two+=1
            three+=1
            four+=1


        self.spawn_square()
        self.game_lines()
        self.update_squares()

    def update_squares(self):
        for i in range(len(self.boxes)):
            self.boxes[i].setStyleSheet('background: #696969; border-radius: 4px;')
            self.boxes[i].setText('')

        for i in range(len(self.game_list)):
            current_box= self.boxes[i]

            if self.game_list[i] == 2:
                current_box.setText('2')
                current_box.setAlignment(Qt.AlignmentFlag.AlignCenter)
                current_box.setStyleSheet(self.two)

            if self.game_list[i] == 4:
                current_box.setText('4')
                current_box.setAlignment(Qt.AlignmentFlag.AlignCenter)
                current_box.setStyleSheet(self.four)

            if self.game_list[i] == 8:
                current_box.setText('8')
                current_box.setAlignment(Qt.AlignmentFlag.AlignCenter)
                current_box.setStyleSheet(self.eight)

            if self.game_list[i] == 16:
                current_box.setText('16')
                current_box.setAlignment(Qt.AlignmentFlag.AlignCenter)
                current_box.setStyleSheet(self.sixteen)

            if self.game_list[i] == 32:
                current_box.setText('32')
                current_box.setAlignment(Qt.AlignmentFlag.AlignCenter)
                current_box.setStyleSheet(self.thirty_two)

            if self.game_list[i] == 64:
                current_box.setText('64')
                current_box.setAlignment(Qt.AlignmentFlag.AlignCenter)
                current_box.setStyleSheet(self.sixty_four)

            if self.game_list[i] == 128:
                current_box.setText('128')
                current_box.setAlignment(Qt.AlignmentFlag.AlignCenter)
                current_box.setStyleSheet(self.hundred_twenty_eight)

            if self.game_list[i] == 256:
                current_box.setText('256')
                current_box.setAlignment(Qt.AlignmentFlag.AlignCenter)
                current_box.setStyleSheet(self.thundred_fifty_six)

            if self.game_list[i] == 512:
                current_box.setText('512')
                current_box.setAlignment(Qt.AlignmentFlag.AlignCenter)
                current_box.setStyleSheet(self.fhundred_twelve)

            if self.game_list[i] == 1024:
                current_box.setText('1024')
                current_box.setAlignment(Qt.AlignmentFlag.AlignCenter)
                current_box.setStyleSheet(self.thousand_twenty_four)

            if self.game_list[i] == 2048:
                current_box.setText('2048')
                current_box.setAlignment(Qt.AlignmentFlag.AlignCenter)
                current_box.setStyleSheet(self.tthousand_fourty_eight)
                self.win_game()

    def win_game(self):
        for i in range(len(self.boxes)):
            self.boxes[i].hide()

        win_msg= QLabel('You Won!')
        win_msg.setFixedSize(QSize(300, 100))
        win_msg.setStyleSheet('''
            QLabel {
            background: #FFFFFF;
            color: #000000;
            font: 40px;
            border: 5px solid #000000;
            }
''')
        win_msg.setAlignment(Qt.AlignmentFlag.AlignCenter)

        leave= QPushButton('Back To Homescreen')
        leave.setFixedSize(QSize(200, 100))
        leave.setStyleSheet('''
            QPushButton {
                background: #696969;
                color: #000000;
                border-radius: 4px;
                border: 1px solid #000000;
                font: 20px;
            }

            QPushButton:hover {
                background: #B0B0B0;
            }

''')
        leave.clicked.connect(self.close)
        
        button_layout= QHBoxLayout()

        button_layout.addSpacing(4)
        button_layout.addWidget(leave)


        self.Game_layout.addWidget(win_msg, 1, 1)
        self.Game_layout.addLayout(button_layout, 2, 1)

    def lose_game(self):
        x=0
        for i in range(len(self.boxes)):
            if not len(self.boxes[i].text()) == 0:
                x+=1

        self.rows_2= self.rows
        self.colmuns_2= self.colmuns

        if x == 16:
            self.lose_game_check()
            self.game_lines()

            if self.rows == self.rows_2 and self.colmuns == self.colmuns_2:
                self.lose_game_screen()
        
        else:
            return



    def lose_game_check(self):
            for n in range(len(self.rows_2)):
                row= self.rows_2[n]

                #left check
                x=0
                for i in range(len(row)):
                    if row[i]:
                        #Use line below to switch values
                        row[x], row[i] = row[i], row[x]
                        x+=1
                        
                #To understand it get a sheet of paper and write it out
                for j in range(len(row)):
                    if row[j] and j > 0:
                        if row[j] == row[j-1]:
                            row[j-1]= row[j] + row[j-1]
                            row[j]=0

                y=0
                for i in range(len(row)):
                    if row[i]:
                        #Use line below to switch values
                        row[y], row[i] = row[i], row[y]
                        y+=1
            

                #right check
                x= len(row)-1
                for i in range(len(row)-1, -1, -1):
                    if row[i]:
                        #Use line below to switch values
                        row[x], row[i] = row[i], row[x]
                        x-=1

                #To figure out write it out
                for j in range(len(row)-1, -1, -1):
                    if row[j] and j+1 < len(row):
                        if row[j] == row[j+1]:
                            row[j]= row[j] + row[j+1]
                            row[j+1]=0


                y=len(row) -1
                for i in range(len(row)-1, -1, -1):
                    if row[i]:
                        #Use line below to switch values
                        row[y], row[i] = row[i], row[y]
                        y-=1

            for n in range(len(self.colmuns_2)):
                colmun= self.colmuns_2[n]
                #up check
                x=0
                for i in range(len(colmun)):
                    if colmun[i]:
                        #Use line below to switch values
                        colmun[x], colmun[i] = colmun[i], colmun[x]
                        x+=1
                        

                for j in range(len(colmun)):
                    if colmun[j] and j > 0:
                            if colmun[j] == colmun[j-1]:
                                colmun[j-1]= colmun[j] + colmun[j-1]
                                colmun[j]=0


                y=0
                for i in range(len(colmun)):
                    if colmun[i]:
                        #Use line below to switch values
                        colmun[y], colmun[i] = colmun[i], colmun[y]
                        y+=1
            


                #down check
                x=len(colmun) -1

                for i in range(len(colmun)-1, -1, -1):
                    if colmun[i]:
                        #Use line below to switch values
                        colmun[x], colmun[i] = colmun[i], colmun[x]
                        x-=1

                for j in range(len(colmun)-1, -1, -1):
                    if colmun[j] and j+1 < len(colmun):
                        try:
                            if colmun[j] == colmun[j+1]:
                                colmun[j+1]= colmun[j] + colmun[j+1]
                                colmun[j]=0

                        except IndexError:
                            pass

                y=len(colmun) -1
                for i in range(len(colmun)-1, -1, -1):
                    if colmun[i]:
                        #Use line below to switch values
                        colmun[y], colmun[i] = colmun[i], colmun[y]
                        y-=1


    def lose_game_screen(self):
        for i in range(len(self.boxes)):
            self.boxes[i].hide()

        lose_msg= QLabel('You Lost!')
        lose_msg.setFixedSize(QSize(300, 100))
        lose_msg.setStyleSheet('''
            QLabel {
            background: #FFFFFF;
            color: #000000;
            font: 40px;
            border: 5px solid #000000;
            }
''')
        lose_msg.setAlignment(Qt.AlignmentFlag.AlignCenter)

        leave= QPushButton('Back To Homescreen')
        leave.setFixedSize(QSize(200, 100))
        leave.setStyleSheet('''
            QPushButton {
                background: #696969;
                color: #000000;
                border-radius: 4px;
                border: 1px solid #000000;
                font: 20px;
            }

            QPushButton:hover {
                background: #B0B0B0;
            }

''')
        leave.clicked.connect(self.close)
        
        button_layout= QHBoxLayout()

        button_layout.addSpacing(4)
        button_layout.addWidget(leave)


        self.Game_layout.addWidget(lose_msg, 1, 1)
        self.Game_layout.addLayout(button_layout, 2, 1)

if __name__ == '__main__':
    main()