import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QCheckBox
from PyQt5.QtCore import Qt


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setGeometry(700, 300, 500, 500)

        # First checkbox
        self.checkbox = QCheckBox("Do you like food?", self)
        self.checkbox.setGeometry(20, 20, 300, 40)
        self.checkbox.setStyleSheet("""
            font-size: 30px;
            font-family: Times New Roman;
        """)

        # Second checkbox
        self.checkbox2 = QCheckBox("What kind of food?", self)
        self.checkbox2.setGeometry(20, 80, 300, 40)
        self.checkbox2.hide()

        # Third checkbox
        self.checkbox3 = QCheckBox("Veg", self)
        self.checkbox3.setGeometry(50, 140, 150, 30)
        self.checkbox3.hide()

        # Fourth checkbox
        self.checkbox4 = QCheckBox("Non Veg", self)
        self.checkbox4.setGeometry(50, 180, 150, 30)
        self.checkbox4.hide()

        # Connect signals
        self.checkbox.stateChanged.connect(self.checkbox_changed)
        self.checkbox2.stateChanged.connect(self.food_type_changed)

    def checkbox_changed(self, state):
        if state == Qt.Checked:
            print("You like food")
            self.checkbox2.show()
        else:
            print("You DO NOT like food")
            self.checkbox2.setChecked(False)
            self.checkbox2.hide()
            self.checkbox3.hide()
            self.checkbox4.hide()

    def food_type_changed(self, state):
        if state == Qt.Checked:
            self.checkbox3.show()
            self.checkbox4.show()
        else:
            self.checkbox3.hide()
            self.checkbox4.hide()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())