import random
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QGridLayout, QLabel
from PySide6.QtCore import Qt

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

        self.game_list= [0, 0, 4, 2,
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
            n_box.setStyleSheet('background: #696969; border-radius: 4px;')

            #Then you append that label to the list object
            #This works because the hash for the QLabel won't be the same no matter the varaible name
            #So even though the varaibe is all n_box the hash is all you care about
            self.boxes.append(n_box)
            #And add it to the game layout
            self.Game_layout.addWidget(n_box, x, y)

        # self.spawn_square()

    def spawn_square(self):
        self.box_number= random.randint(0, 15)

        self.box_number_2= random.randint(0, 15)

        if self.box_number == self.box_number_2:
            self.spawn_square()
            return

        add_box=self.boxes[self.box_number]

        add_box_2=self.boxes[self.box_number_2]

        numbers= ['2', '4', '8']
        weights= [50, 40, 10]

        number= random.choices(numbers, weights=weights)[0]

        number2= random.choices(numbers, weights=weights)[0]

        print(number, number2, '\n')


        if number == '2' and add_box.text() == '':
            add_box.setText('2')
            add_box.setAlignment(Qt.AlignmentFlag.AlignCenter)
            add_box.setStyleSheet('''
                QLabel {
                background: #FFFFC5;
                border-radius: 4px;
                border: 1px solid #000000;
                color: #000000;
                font: 40px;      
                }
''')
            self.game_list[self.box_number] = 2 # type: ignore

        if number2 == '2' and add_box_2.text() == '':
            add_box_2.setText('2')
            add_box_2.setAlignment(Qt.AlignmentFlag.AlignCenter)
            add_box_2.setStyleSheet('''
                QLabel {
                background: #FFFFC5;
                border-radius: 4px;
                border: 1px solid #000000;
                color: #000000;
                font: 40px;      
                }
''')
            self.game_list[self.box_number_2] = 2 # type: ignore

        if number == '4' and add_box.text() == '':
            add_box.setText('4')
            add_box.setAlignment(Qt.AlignmentFlag.AlignCenter)
            add_box.setStyleSheet('''
                QLabel {
                background: #FFD580;
                border-radius: 4px;
                border: 1px solid #000000;
                color: #000000;
                font: 40px;      
                }
''')
            self.game_list[self.box_number] = 4 # type: ignore

        if number2 == '4' and add_box_2.text() == '':
            add_box_2.setText('4')
            add_box_2.setAlignment(Qt.AlignmentFlag.AlignCenter)
            add_box_2.setStyleSheet('''
                QLabel {
                background: #FFD580;
                border-radius: 4px;
                border: 1px solid #000000;
                color: #000000;
                font: 40px;      
                }
''')
            self.game_list[self.box_number_2] = 4 # type: ignore

        if number == '8' and add_box.text() == '':
            add_box.setText('8')
            add_box.setAlignment(Qt.AlignmentFlag.AlignCenter)
            add_box.setStyleSheet('''
                QLabel {
                background: #ffb09c;
                border-radius: 4px;
                border: 1px solid #000000;
                color: #000000;
                font: 40px;      
                }
''')
            self.game_list[self.box_number] = 8 # type: ignore

        if number2 == '8' and add_box_2.text() == '':
            add_box_2.setText('8')
            add_box_2.setAlignment(Qt.AlignmentFlag.AlignCenter)
            add_box_2.setStyleSheet('''
                QLabel {
                background: #ffb09c;
                border-radius: 4px;
                border: 1px solid #000000;
                color: #000000;
                font: 40px;      
                }
''')
            self.game_list[self.box_number_2] = 8 # type: ignore

        for i in range(0, len(self.game_list), 4):
            print(*self.game_list[i : i + 4])


    #The name of the function matters in this case
    def keyPressEvent(self, event):
        #TODO Figure out how you are going to make the game work
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
        #TODO Figure out how to make the needed algorithm (Idk name)


        print('\n')
        for i in range(0, len(self.game_list), 4):
            print(*self.game_list[i : i + 4])

        

    def move_right(self):
        print('e')

    def move_up(self):
        print('l')

    def move_down(self):
        print('o')

if __name__ == '__main__':
    main()