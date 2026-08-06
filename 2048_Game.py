from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QGridLayout, QLabel


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

        #How this work is that you make a list object first
        for x_y in Grid_list:
            x= x_y[0]
            y= x_y[1]

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





if __name__ == '__main__':
    main()