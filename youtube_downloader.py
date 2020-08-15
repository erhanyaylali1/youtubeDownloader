from PyQt5 import QtCore, QtGui, QtWidgets
import sys, os
from PyQt5 import QtCore, QtGui, QtWidgets
from pytube import YouTube
from pytube.cli import on_progress


class Ui_Form(QtWidgets.QWidget):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowIcon(QtGui.QIcon('logo.png'))

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(536, 222)
        font = QtGui.QFont()
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        Form.setFont(font)
        self.linkText = QtWidgets.QLineEdit(Form)
        self.linkText.setGeometry(QtCore.QRect(60, 110, 451, 31))
        self.linkText.setAutoFillBackground(False)
        self.linkText.setObjectName("linkText")
        self.linkText.setStyleSheet("padding-left: 10px;")
        self.urlText = QtWidgets.QLabel(Form)
        self.urlText.setGeometry(QtCore.QRect(20, 110, 31, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.urlText.setFont(font)
        self.urlText.setObjectName("urlText")
        self.appName = QtWidgets.QLabel(Form)
        self.appName.setGeometry(QtCore.QRect(20, 10, 221, 51))
        font = QtGui.QFont()
        font.setFamily("Bodoni MT")
        font.setPointSize(18)
        self.appName.setFont(font)
        self.appName.setStyleSheet("")
        self.appName.setObjectName("appName")
        self.downloadBtn = QtWidgets.QPushButton(Form)
        self.downloadBtn.setGeometry(QtCore.QRect(220, 170, 91, 31))
        self.downloadBtn.clicked.connect(self.func)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.downloadBtn.setFont(font)
        self.downloadBtn.setStyleSheet("")
        self.downloadBtn.setObjectName("downloadBtn")
        self.typeBox = QtWidgets.QComboBox(Form)
        self.typeBox.setGeometry(QtCore.QRect(440, 160, 71, 21))
        self.typeBox.setStyleSheet("padding-left: 10px;")
        self.typeBox.setObjectName("typeBox")
        self.typeBox.addItem("")
        self.typeBox.addItem("")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Youtube Downloader"))
        self.linkText.setPlaceholderText(_translate("Form", "Enter Link"))
        self.urlText.setText(_translate("Form", "URL"))
        self.appName.setText(_translate("Form", "MP3/MP4 Download"))
        self.downloadBtn.setText(_translate("Form", "Download"))
        self.typeBox.setItemText(0, _translate("Form", "MP3"))
        self.typeBox.setItemText(1, _translate("Form", "MP4"))


    def func(self):

            link = self.linkText.text()
            if self.typeBox.currentText() == "MP3":
    
                file = YouTube(link,on_progress_callback=on_progress)
                audio = file.streams.filter(only_audio=True, file_extension="webm").order_by("abr").desc().first()
                path = r"C:\Users\erhan\Downloads\Music"
                audio.download(path,file.title)
                os.rename(path + chr(92) + file.title + ".webm", path + chr(92) + file.title + '.mp3')
                print("\ndone")

            else:
                file = YouTube(link,on_progress_callback=on_progress)
                video = file.streams.filter(progressive = True,type="video",file_extension="mp4").order_by('resolution').desc().first()
                video.download(r"C:\Users\erhan\Downloads\Video",file.title)
                print("\ndone")


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    ex = Ui_Form()
    ex.show()
    sys.exit(app.exec_())