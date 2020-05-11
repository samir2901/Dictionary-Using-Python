from PyQt5 import QtCore, QtGui, QtWidgets
import images_rc
import sys
from PyDictionary import PyDictionary


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(380, 582)
        MainWindow.setMaximumSize(QtCore.QSize(389, 600))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/appicon/app-icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("*{\n"
"    background: #9c1de7;\n"
"    color : rgb(255,255,255);\n"
"}\n"
"\n"
"QTextEdit{\n"
"    background : rgb(255,255,255);\n"
"    color : rgb(0,0,0);\n"
"    border-radius : 5px;\n"
"}\n"
"\n"
"QPushButton{\n"
"    background-color : #f3558e;\n"
"    border-radius : 10px;\n"
"}\n"
"\n"
"QPushButton:pressed{background-color:#581b98 ;}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.word = QtWidgets.QTextEdit(self.centralwidget)
        self.word.setGeometry(QtCore.QRect(30, 60, 281, 36))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        self.word.setFont(font)
        self.word.setObjectName("word")
        self.title = QtWidgets.QLabel(self.centralwidget)
        self.title.setGeometry(QtCore.QRect(90, 20, 211, 25))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        self.title.setFont(font)
        self.title.setStyleSheet("")
        self.title.setScaledContents(True)
        self.title.setAlignment(QtCore.Qt.AlignCenter)
        self.title.setObjectName("title")
        self.searchBtn = QtWidgets.QPushButton(self.centralwidget)
        self.searchBtn.setGeometry(QtCore.QRect(320, 60, 36, 36))
        self.searchBtn.setMaximumSize(QtCore.QSize(128, 128))
        self.searchBtn.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/search-icon/search.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.searchBtn.setIcon(icon1)
        self.searchBtn.setObjectName("searchBtn")
        self.searchBtn.clicked.connect(self.searchMeaning)
        self.meaningLbl = QtWidgets.QLabel(self.centralwidget)
        self.meaningLbl.setGeometry(QtCore.QRect(30, 100, 107, 25))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.meaningLbl.setFont(font)
        self.meaningLbl.setStyleSheet("")
        self.meaningLbl.setScaledContents(True)
        self.meaningLbl.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.meaningLbl.setObjectName("meaningLbl")
        self.meaning = QtWidgets.QTextEdit(self.centralwidget)
        self.meaning.setGeometry(QtCore.QRect(30, 130, 321, 431))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        self.meaning.setFont(font)
        self.meaning.setReadOnly(True)
        self.meaning.setObjectName("meaning")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def searchMeaning(self):
        w = self.word.toPlainText()
        try:
            pyDict = PyDictionary(w)
            m = pyDict.meaning(w)   
            string = ''                     
            for i in list(m.keys()):
                string  = string + str(i) + ": " + str(m[i][0]) + "\n\n"
            self.meaning.setText(string)
        except:
            txt = "Sorry! Couldn't find it."
            self.meaning.setText(txt)            
    
        

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Dictionary"))
        self.title.setText(_translate("MainWindow", "DICTIONARY"))
        self.meaningLbl.setText(_translate("MainWindow", "Meaning:"))


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

