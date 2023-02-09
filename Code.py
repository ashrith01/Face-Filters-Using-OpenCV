# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'sip.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import cv2,time
import numpy as np
from PyQt5.QtWidgets import QFileDialog

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1239, 833)
        font = QtGui.QFont()
        font.setPointSize(10)
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.upload = QtWidgets.QPushButton(self.centralwidget)
        self.upload.setGeometry(QtCore.QRect(110, 720, 111, 28))
        self.upload.setObjectName("upload")
        self.upload.raise_()
        self.label_1 = QtWidgets.QLabel(self.centralwidget)
        self.label_1.setGeometry(QtCore.QRect(50, 280, 201, 161))
        self.label_1.setObjectName("label_1")
        self.label_1.raise_()
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(360, 280, 201, 161))
        self.label_2.setObjectName("label_2")
        self.label_2.raise_()
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(70, 170, 121, 31))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox_2 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_2.setGeometry(QtCore.QRect(390, 170, 121, 31))
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_3 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_3.setGeometry(QtCore.QRect(680, 170, 131, 31))
        self.comboBox_3.setObjectName("comboBox_3")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_4 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_4.setGeometry(QtCore.QRect(970, 170, 121, 31))
        self.comboBox_4.setObjectName("comboBox_4")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(660, 280, 201, 161))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(950, 280, 201, 161))
        self.label_4.setObjectName("label_4")
        self.applyfilters = QtWidgets.QPushButton(self.centralwidget)
        self.applyfilters.setGeometry(QtCore.QRect(720, 720, 121, 28))
        self.applyfilters.setObjectName("applyfilters")
        self.save = QtWidgets.QPushButton(self.centralwidget)
        self.save.setGeometry(QtCore.QRect(1020, 720, 93, 28))
        self.save.setObjectName("save")
        self.live = QtWidgets.QPushButton(self.centralwidget)
        self.live.setGeometry(QtCore.QRect(430, 720, 93, 28))
        self.live.setObjectName("live")
        self.comboBox_5 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_5.setGeometry(QtCore.QRect(550, 550, 121, 31))
        self.comboBox_5.setObjectName("comboBox_5")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1239, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.comboBox.currentTextChanged.connect(self.setPhoto_1)
        self.comboBox_2.currentTextChanged.connect(self.setPhoto_2)
        self.comboBox_3.currentTextChanged.connect(self.setPhoto_3)
        self.comboBox.currentTextChanged.connect(self.pressed_1)
        self.comboBox_2.currentTextChanged.connect(self.pressed_2)
        self.comboBox_3.currentTextChanged.connect(self.pressed_3)
        self.comboBox_4.currentTextChanged.connect(self.pressed_4)
        self.comboBox_5.currentTextChanged.connect(self.pressed_5)
        self.comboBox_4.currentTextChanged.connect(self.setPhoto_4)
        self.upload.clicked.connect(self.loadImage)
        self.save.clicked.connect(self.savePhoto)
        self.live.clicked.connect(self.live_pressed)
        self.applyfilters.clicked.connect(self.applyfilter_pressed)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


    def applyfilter_pressed(self):
        gl = None if (self.comboBox.currentText() == "None") else self.comboBox.currentText() + ".png"
        no = None if (self.comboBox_2.currentText() == "None") else self.comboBox_2.currentText() + ".png"
        mu = None if (self.comboBox_3.currentText() == "None") else self.comboBox_3.currentText() + ".png"
        fa = None if (self.comboBox_4.currentText() == "None") else self.comboBox_4.currentText() + ".png"
        self.runner(gl, no, mu, fa, False)

    def pressed_1(self):
        if (self.comboBox.currentText() != "None"):
            self.comboBox_4.setCurrentText("None")
            self.comboBox_5.setCurrentText("None")

    def pressed_2(self):
        if (self.comboBox_2.currentText() != "None"):
            self.comboBox_4.setCurrentText("None")
            self.comboBox_5.setCurrentText("None")

    def pressed_3(self):
        if (self.comboBox_3.currentText() != "None"):
            self.comboBox_4.setCurrentText("None")
            self.comboBox_5.setCurrentText("None")

    def pressed_4(self):
        if (self.comboBox_4.currentText() != "None"):
            self.comboBox.setCurrentText("None")
            self.comboBox_2.setCurrentText("None")
            self.comboBox_3.setCurrentText("None")
            self.comboBox_5.setCurrentText("None")

    def pressed_5(self):
        if (self.comboBox_5.currentText() != "None"):
            self.comboBox.setCurrentText("None")
            self.comboBox_2.setCurrentText("None")
            self.comboBox_3.setCurrentText("None")
            self.comboBox_4.setCurrentText("None")

    def loadImage(self):
        self.filename = QFileDialog.getOpenFileName(filter="Image (*.*)")[0]
        self.image = cv2.imread(self.filename)

    def savePhoto(self):
        filename = QFileDialog.getSaveFileName(filter="JPG(*.jpg);;PNG(*.png);;TIFF(*.tiff);;BMP(*.bmp)")[0]
        cv2.imwrite(filename, self.result)
        print('Image saved as:', filename)

    def setPhoto_1(self):
        img_add = "assets/" + self.comboBox.currentText() + ".png"
        self.label_1.setPixmap(QtGui.QPixmap(img_add))
        self.label_1.setScaledContents(True)

    def setPhoto_2(self):
        img_add = "assets/" + self.comboBox_2.currentText() + ".png"
        self.label_2.setPixmap(QtGui.QPixmap(img_add))
        self.label_2.setScaledContents(True)

    def setPhoto_3(self):
        img_add = "assets/" + self.comboBox_3.currentText() + ".png"
        self.label_3.setPixmap(QtGui.QPixmap(img_add))
        self.label_3.setScaledContents(True)

    def setPhoto_4(self):
        img_add = "assets/" + self.comboBox_4.currentText() + ".png"
        self.label_4.setPixmap(QtGui.QPixmap(img_add))
        self.label_4.setScaledContents(True)

    def live_pressed(self):
        gl = None if (self.comboBox.currentText()=="None") else self.comboBox.currentText()+".png"
        no = None if (self.comboBox_2.currentText() == "None") else self.comboBox_2.currentText() + ".png"
        mu = None if (self.comboBox_3.currentText() == "None") else self.comboBox_3.currentText() + ".png"
        fa = None if (self.comboBox_4.currentText() == "None") else self.comboBox_4.currentText() + ".png"
        frame_filter = None if (self.comboBox_5.currentText() == "None") else self.comboBox_5.currentText()
        if ((gl or no or mu or fa) is not None):
            self.runner(gl,no,mu,fa,True)
        else:
            self.cap = cv2.VideoCapture(0)
            if (frame_filter == "overlay"):
                while (True):
                    ret, frame = self.cap.read()
                    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2BGRA)
                    color_overlay = self.apply_color_overlay(frame.copy(), intensity=.8, red=123, green=231)
                    cv2.imshow('color_overlay', color_overlay)
                    if cv2.waitKey(20) & 0xFF == ord('q'):
                        break
                self.cap.release()
                cv2.destroyAllWindows()
            if(frame_filter=="sepia"):
                while (True):
                    ret, frame = self.cap.read()
                    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2BGRA)
                    sepia = self.apply_sepia(frame.copy(), intensity=.8)
                    cv2.imshow('sepia', sepia)
                    if cv2.waitKey(20) & 0xFF == ord('q'):
                        break
                self.cap.release()
                cv2.destroyAllWindows()
            if(frame_filter=="invert"):
                while (True):
                    ret, frame = self.cap.read()
                    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2BGRA)
                    invert = self.apply_invert(frame.copy())
                    cv2.imshow('invert', invert)
                    if cv2.waitKey(20) & 0xFF == ord('q'):
                        break
                self.cap.release()
                cv2.destroyAllWindows()
            if(frame_filter=="portrait"):
                while (True):
                    ret, frame = self.cap.read()
                    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2BGRA)
                    portrait = self.portrait_mode(frame.copy())
                    cv2.imshow('portrait', portrait)
                    if cv2.waitKey(20) & 0xFF == ord('q'):
                        break
                self.cap.release()
                cv2.destroyAllWindows()


    def verify_alpha_channel(self,frame):
        try:
            frame.shape[3]  # looking for the alpha channel
        except IndexError:
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2BGRA)
        return frame

    def apply_color_overlay(self,frame, intensity=0.5, blue=0, green=0, red=0):
        frame = self.verify_alpha_channel(frame)
        frame_h, frame_w, frame_c = frame.shape
        sepia_bgra = (blue, green, red, 1)
        overlay = np.full((frame_h, frame_w, 4), sepia_bgra, dtype='uint8')
        cv2.addWeighted(overlay, intensity, frame, 1.0, 0, frame)
        return frame

    def apply_invert(self,frame):
        return cv2.bitwise_not(frame)

    def apply_sepia(self,frame, intensity=0.5):
        frame = self.verify_alpha_channel(frame)
        frame_h, frame_w, frame_c = frame.shape
        sepia_bgra = (20, 66, 112, 1)
        overlay = np.full((frame_h, frame_w, 4), sepia_bgra, dtype='uint8')
        cv2.addWeighted(overlay, intensity, frame, 1.0, 0, frame)
        return frame

    def alpha_blend(self,frame_1, frame_2, mask):
        alpha = mask / 255.0
        blended = cv2.convertScaleAbs(frame_1 * (1 - alpha) + frame_2 * alpha)
        return blended

    def portrait_mode(self,frame):
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        _, mask = cv2.threshold(gray, 100, 255, cv2.THRESH_BINARY)
        mask = cv2.cvtColor(mask, cv2.COLOR_GRAY2BGRA)
        blured = cv2.GaussianBlur(frame, (21, 21), 11)
        blended = self.alpha_blend(frame, blured, mask)
        frame = cv2.cvtColor(blended, cv2.COLOR_BGRA2BGR)
        return frame

    def overlayPNG(self,imgBack, imgFront, pos=[0, 0]):
        hf, wf, cf = imgFront.shape
        hb, wb, cb = imgBack.shape
        *_, mask = cv2.split(imgFront)
        maskBGRA = cv2.cvtColor(mask, cv2.COLOR_GRAY2BGRA)
        maskBGR = cv2.cvtColor(mask, cv2.COLOR_GRAY2BGR)
        imgRGBA = cv2.bitwise_and(imgFront, maskBGRA)
        imgRGB = cv2.cvtColor(imgRGBA, cv2.COLOR_BGRA2BGR)
        imgMaskFull = np.zeros((hb, wb, cb), np.uint8)
        imgMaskFull[pos[1]:hf + pos[1], pos[0]:wf + pos[0], :] = imgRGB
        imgMaskFull2 = np.ones((hb, wb, cb), np.uint8) * 255
        maskBGRInv = cv2.bitwise_not(maskBGR)
        imgMaskFull2[pos[1]:hf + pos[1], pos[0]:wf + pos[0], :] = maskBGRInv
        imgBack = cv2.bitwise_and(imgBack, imgMaskFull2)
        imgBack = cv2.bitwise_or(imgBack, imgMaskFull)
        return imgBack

    def runner(self,glass_file=None, nose_file=None, mustache_file=None, face_file=None, feed=True):
        self.face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
        self.eyecascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')
        self.nosecascade = cv2.CascadeClassifier('haarcascade_nose.xml')

        self.cap = cv2.VideoCapture(0)
        self.prev_frame_time = 0
        self.new_frame_time = 0

        if (glass_file is not None):
            glass_add = "assets/" + glass_file
            glasses_filter = cv2.imread(glass_add, -1)
        if (nose_file is not None):
            nose_add = "assets/" + nose_file
            nose_filter = cv2.imread(nose_add, -1)
        if (mustache_file is not None):
            mustache_add = "assets/" + mustache_file
            mustache_filter = cv2.imread(mustache_add, -1)
        if (face_file is not None):
            face_add = "assets/" + face_file
            face_filter = cv2.imread(face_add, -1)

        while True:
            if(feed is True):
                _, frame = self.cap.read()
            else:
                frame = self.image.copy()
            frame2 = frame.copy()
            gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            faces = self.face_cascade.detectMultiScale(gray_frame, 1.3, 5)

            self.delay_time = 50
            cv2.waitKey(self.delay_time)
            for (x, y, w, h) in faces:
                rol_gray = gray_frame[y:y + h, x:x + h]

                if (face_file is not None):
                    overlay_resize = cv2.resize(face_filter.copy(), (int(1 * w), int(1 * h)))
                    frame = self.overlayPNG(frame, overlay_resize, [x, y - 40])
                    frame2 = cv2.rectangle(frame2, (x, y - 40), (x + int(1 * w), y + int(1 * h)), (0, 0, 255), 3)

                eyes = self.eyecascade.detectMultiScale(rol_gray, 1.3, 3)
                cood = []
                for (ex, ey, ew, eh) in eyes:
                    cood.append([ex, ey])
                    wid = ew
                    hei = eh
                if (len(cood) > 1):
                    ex = cood[0][0] if (cood[0][0] < cood[1][0]) else cood[1][0]
                    ey = cood[0][1]
                    if (glass_file is not None):
                        overlay_resize = cv2.resize(glasses_filter.copy(), (int(3 * wid), int(1.3 * hei)))
                        frame = self.overlayPNG(frame, overlay_resize, [x + ex - 10, y + ey])
                        frame2 = cv2.rectangle(frame2, (x + ex - 10, y + ey),
                                           (x + ex + int(2.6 * wid), y + ey + int(1.2 * hei)),
                                           (0, 255, 0), 3)

                nose = self.nosecascade.detectMultiScale(rol_gray, 1.3, 3)
                cood = []
                for (nx, ny, nw, nh) in nose:
                    cood.append([nx, ny])
                    wid = nw
                    hei = nh
                if (len(cood) > 0):
                    ex = cood[0][0]
                    ey = cood[0][1]
                    if (nose_file is not None):
                        overlay_resize = cv2.resize(nose_filter.copy(), (int(1.1 * wid) - 10, int(0.9 * hei) - 5))
                        frame = self.overlayPNG(frame, overlay_resize, [x + ex + 5, y + ey + 5])
                        frame2 = cv2.rectangle(frame2, (x + ex + 5, y + ey + 5),
                                           (x + ex + int(1.1 * wid) - 10, y + ey + int(0.9 * hei) - 5), (255, 0, 0), 3)
                    if (mustache_file is not None):
                        overlay_resize = cv2.resize(mustache_filter, (int(1.8 * wid), int(0.7 * hei)))
                        frame = self.overlayPNG(frame, overlay_resize,
                                           [x + ex + 5 - int(wid / 2), y + ey + int(0.9 * hei) - 5])
                        frame2 = cv2.rectangle(frame2, (x + ex + 5 - int(wid / 2), y + ey + int(0.9 * hei) - 5),
                                           (x + ex + + 5 - int(wid / 2) + int(1.8 * wid),
                                            y + ey + +int(0.9 * hei) - 10 + int(0.7 * hei)), (255, 255, 0), 3)


            if (feed is False):
                self.result=frame

            if (feed is True):
                cv2.imshow('frame', frame)
                cv2.imshow('detect', frame2)
                if (cv2.waitKey(1) == ord('q')):
                    break

        self.cap.release()
        cv2.destroyAllWindows()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "SIP Project"))
        self.upload.setText(_translate("MainWindow", "Upload"))
        self.label_1.setText(_translate("MainWindow", ""))
        self.label_2.setText(_translate("MainWindow", ""))
        self.comboBox.setItemText(0, _translate("MainWindow", "thug_glasses"))
        self.comboBox.setItemText(1, _translate("MainWindow", "glasses"))
        self.comboBox.setItemText(2, _translate("MainWindow", "sunglasses_1"))
        self.comboBox.setItemText(3, _translate("MainWindow", "sunglasses_2"))
        self.comboBox.setItemText(4, _translate("MainWindow", "shades"))
        self.comboBox.setItemText(5, _translate("MainWindow", "None"))
        self.comboBox_2.setItemText(0, _translate("MainWindow", "clown-nose"))
        self.comboBox_2.setItemText(1, _translate("MainWindow", "bear-nose"))
        self.comboBox_2.setItemText(2, _translate("MainWindow", "cat-nose"))
        self.comboBox_2.setItemText(3, _translate("MainWindow", "dog-nose"))
        self.comboBox_2.setItemText(4, _translate("MainWindow", "pig-nose"))
        self.comboBox_2.setItemText(5, _translate("MainWindow", "None"))
        self.comboBox_3.setItemText(0, _translate("MainWindow", "mustache"))
        self.comboBox_3.setItemText(1, _translate("MainWindow", "mustache_2"))
        self.comboBox_3.setItemText(2, _translate("MainWindow", "mustache_3"))
        self.comboBox_3.setItemText(3, _translate("MainWindow", "None"))
        self.comboBox_4.setItemText(0, _translate("MainWindow", "pig"))
        self.comboBox_4.setItemText(1, _translate("MainWindow", "bear"))
        self.comboBox_4.setItemText(2, _translate("MainWindow", "dog"))
        self.comboBox_4.setItemText(3, _translate("MainWindow", "cat"))
        self.comboBox_4.setItemText(4, _translate("MainWindow", "None"))
        self.label_3.setText(_translate("MainWindow", ""))
        self.label_4.setText(_translate("MainWindow", ""))
        self.applyfilters.setText(_translate("MainWindow", "Apply Filters"))
        self.save.setText(_translate("MainWindow", "Save"))
        self.live.setText(_translate("MainWindow", "Live"))
        self.comboBox_5.setItemText(0, _translate("MainWindow", "overlay"))
        self.comboBox_5.setItemText(1, _translate("MainWindow", "sepia"))
        self.comboBox_5.setItemText(2, _translate("MainWindow", "invert"))
        self.comboBox_5.setItemText(3, _translate("MainWindow", "portrait"))
        self.comboBox_5.setItemText(4, _translate("MainWindow", "None"))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
