import sys
from PyQt5.QtWidgets import *

# from form_accident import form_accident

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.statusBar().showMessage("Ready master Teady")
        self.setWindowTitle("Stausbar example")


        messageAction = QAction("Message",self)
        messageAction.triggered.connect(self.message)

        newAction = QAction("New",self)
        #self.connect(newAction,SIGNAL("triggered()"),self.new)
        newAction.triggered.connect(self.new)

        exitAction = QAction("Exit",self)
        exitAction.setShortcut("Ctrl-Q")
        exitAction.setStatusTip("Exit application")
        exitAction.triggered.connect(qApp.quit)

        menubar = self.menuBar()
        fileMenu = menubar.addMenu("&File")
        fileMenu.addAction(newAction)
        fileMenu.addAction(messageAction)
        fileMenu.addAction(exitAction)

        toolbar = self.addToolBar("toolbar")
        toolbar.addAction(newAction)
        toolbar.addAction(messageAction)   
        toolbar.addAction(exitAction)

        self.mdiArea = QMdiArea(self)
        self.setCentralWidget(self.mdiArea)
        textEdit = QTextEdit()
        self.mdiArea.addSubWindow(textEdit)

        self.setGeometry(300,300,350,250)
        self.show()



    def message(self):
        QMessageBox.about(self,"About a boy","Everything about a boy")

    def new(self):
        fa = QTextEdit(self)
        self.mdiArea.addSubWindow(fa)
        fa.show()
        
                            

def main():
    app = QApplication(sys.argv)
    main_window = MainWindow()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
