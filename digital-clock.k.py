import sys
from PyQt5.QtWidgets import QApplication, QMainWindow,QLabel,QVBoxLayout,QWidget
from PyQt5.QtGui import QFont,QIcon,QPixmap
from PyQt5.QtCore import Qt ,QTime,QTimer

def main():
    class window(QMainWindow):
        def __init__(self):
            super().__init__()
            self.setWindowTitle("DIGI-CLOCK")
            self.setWindowIcon(QIcon("C:\\Users\\pkush\\Downloads\\icons8-clock-50.png"))
            self.setGeometry(600,400,300,100)
            self.timer=QTimer(self)
            self.initUI()
        
        def initUI(self):
            self.label1=QLabel("",self)
            central_widget=QWidget()
            self.setCentralWidget(central_widget)
            vbox=QVBoxLayout()
            vbox.addWidget(self.label1)
            
            central_widget.setLayout(vbox)
            
            self.label1.setAlignment(Qt.AlignCenter)
            self.label1.setStyleSheet("""color:#8410de;
                                      background-color:black;
                                      font-family:DS-Digital;
                                      font-size:150px""")

            self.timer.timeout.connect(self.time)
            self.timer.start(1000)
            self.time()
            
        def time(self):
            ctime=QTime.currentTime().toString("hh:mm:ss AP")
            self.label1.setText(ctime)
            

        
    app=QApplication(sys.argv)
    w=window()
    w.show()
    sys.exit(app.exec_())

if __name__=="__main__":
    main()