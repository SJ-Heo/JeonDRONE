# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1086, 748)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        Dialog.setFont(font)
        self.Set_button = QtWidgets.QPushButton(Dialog)
        self.Set_button.setGeometry(QtCore.QRect(970, 560, 105, 31))
        self.Set_button.setObjectName("Set_button")
        self.Duty_high = QtWidgets.QPushButton(Dialog)
        self.Duty_high.setGeometry(QtCore.QRect(593, 560, 105, 31))
        self.Duty_high.setObjectName("Duty_high")
        self.Fre_high = QtWidgets.QPushButton(Dialog)
        self.Fre_high.setGeometry(QtCore.QRect(473, 560, 105, 31))
        self.Fre_high.setObjectName("Fre_high")
        self.Fre_low = QtWidgets.QPushButton(Dialog)
        self.Fre_low.setGeometry(QtCore.QRect(473, 600, 105, 31))
        self.Fre_low.setObjectName("Fre_low")
        self.Duty_low = QtWidgets.QPushButton(Dialog)
        self.Duty_low.setGeometry(QtCore.QRect(593, 600, 105, 31))
        self.Duty_low.setObjectName("Duty_low")
        self.Frequency_text = QtWidgets.QLineEdit(Dialog)
        self.Frequency_text.setGeometry(QtCore.QRect(730, 560, 113, 32))
        self.Frequency_text.setObjectName("Frequency_text")
        self.Duty_text = QtWidgets.QLineEdit(Dialog)
        self.Duty_text.setGeometry(QtCore.QRect(850, 560, 113, 32))
        self.Duty_text.setObjectName("Duty_text")
        self.Fre_label = QtWidgets.QLabel(Dialog)
        self.Fre_label.setGeometry(QtCore.QRect(730, 540, 131, 22))
        self.Fre_label.setObjectName("Fre_label")
        self.Duty_label = QtWidgets.QLabel(Dialog)
        self.Duty_label.setGeometry(QtCore.QRect(850, 540, 68, 22))
        self.Duty_label.setObjectName("Duty_label")
        self.AngleY_split = QtWidgets.QSplitter(Dialog)
        self.AngleY_split.setGeometry(QtCore.QRect(150, 180, 281, 23))
        self.AngleY_split.setOrientation(QtCore.Qt.Horizontal)
        self.AngleY_split.setObjectName("AngleY_split")
        self.AngleY_LCD = QtWidgets.QLCDNumber(self.AngleY_split)
        self.AngleY_LCD.setObjectName("AngleY_LCD")
        self.AngleY_v_LCD = QtWidgets.QLCDNumber(self.AngleY_split)
        self.AngleY_v_LCD.setObjectName("AngleY_v_LCD")
        self.AngleY_a_LCD = QtWidgets.QLCDNumber(self.AngleY_split)
        self.AngleY_a_LCD.setObjectName("AngleY_a_LCD")
        self.AngleZ_split = QtWidgets.QSplitter(Dialog)
        self.AngleZ_split.setGeometry(QtCore.QRect(150, 280, 281, 23))
        self.AngleZ_split.setOrientation(QtCore.Qt.Horizontal)
        self.AngleZ_split.setObjectName("AngleZ_split")
        self.AngleZ_LCD = QtWidgets.QLCDNumber(self.AngleZ_split)
        self.AngleZ_LCD.setObjectName("AngleZ_LCD")
        self.AngleZ_v_LCD = QtWidgets.QLCDNumber(self.AngleZ_split)
        self.AngleZ_v_LCD.setObjectName("AngleZ_v_LCD")
        self.AngleZ_a_LCD = QtWidgets.QLCDNumber(self.AngleZ_split)
        self.AngleZ_a_LCD.setObjectName("AngleZ_a_LCD")
        self.Single_R = QtWidgets.QPushButton(Dialog)
        self.Single_R.setGeometry(QtCore.QRect(940, 450, 105, 31))
        self.Single_R.setObjectName("Single_R")
        self.Single_L = QtWidgets.QPushButton(Dialog)
        self.Single_L.setGeometry(QtCore.QRect(710, 460, 105, 31))
        self.Single_L.setObjectName("Single_L")
        self.Single_BWD = QtWidgets.QPushButton(Dialog)
        self.Single_BWD.setGeometry(QtCore.QRect(820, 490, 105, 31))
        self.Single_BWD.setObjectName("Single_BWD")
        self.Single_FWD = QtWidgets.QPushButton(Dialog)
        self.Single_FWD.setGeometry(QtCore.QRect(820, 420, 105, 31))
        self.Single_FWD.setObjectName("Single_FWD")
        self.layoutWidget = QtWidgets.QWidget(Dialog)
        self.layoutWidget.setGeometry(QtCore.QRect(810, 80, 201, 34))
        self.layoutWidget.setObjectName("layoutWidget")
        self.RotationX_layout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.RotationX_layout.setContentsMargins(0, 0, 0, 0)
        self.RotationX_layout.setObjectName("RotationX_layout")
        self.GLXP = QtWidgets.QLineEdit(self.layoutWidget)
        self.GLXP.setObjectName("GLXP")
        self.RotationX_layout.addWidget(self.GLXP)
        self.GLXI = QtWidgets.QLineEdit(self.layoutWidget)
        self.GLXI.setObjectName("GLXI")
        self.RotationX_layout.addWidget(self.GLXI)
        self.GLXD = QtWidgets.QLineEdit(self.layoutWidget)
        self.GLXD.setObjectName("GLXD")
        self.RotationX_layout.addWidget(self.GLXD)
        self.layoutWidget_2 = QtWidgets.QWidget(Dialog)
        self.layoutWidget_2.setGeometry(QtCore.QRect(810, 120, 201, 34))
        self.layoutWidget_2.setObjectName("layoutWidget_2")
        self.RotationY_layout = QtWidgets.QHBoxLayout(self.layoutWidget_2)
        self.RotationY_layout.setContentsMargins(0, 0, 0, 0)
        self.RotationY_layout.setObjectName("RotationY_layout")
        self.GLYP = QtWidgets.QLineEdit(self.layoutWidget_2)
        self.GLYP.setObjectName("GLYP")
        self.RotationY_layout.addWidget(self.GLYP)
        self.GLYI = QtWidgets.QLineEdit(self.layoutWidget_2)
        self.GLYI.setObjectName("GLYI")
        self.RotationY_layout.addWidget(self.GLYI)
        self.GLYD = QtWidgets.QLineEdit(self.layoutWidget_2)
        self.GLYD.setObjectName("GLYD")
        self.RotationY_layout.addWidget(self.GLYD)
        self.P_label = QtWidgets.QLabel(Dialog)
        self.P_label.setGeometry(QtCore.QRect(840, 50, 31, 22))
        self.P_label.setObjectName("P_label")
        self.I_label = QtWidgets.QLabel(Dialog)
        self.I_label.setGeometry(QtCore.QRect(910, 50, 31, 22))
        self.I_label.setObjectName("I_label")
        self.D_label = QtWidgets.QLabel(Dialog)
        self.D_label.setGeometry(QtCore.QRect(970, 50, 31, 22))
        self.D_label.setObjectName("D_label")
        self.line = QtWidgets.QFrame(Dialog)
        self.line.setGeometry(QtCore.QRect(700, 30, 331, 20))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(Dialog)
        self.line_2.setGeometry(QtCore.QRect(1020, 40, 20, 311))
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.Gain_RotationX_label = QtWidgets.QLabel(Dialog)
        self.Gain_RotationX_label.setGeometry(QtCore.QRect(710, 70, 80, 22))
        self.Gain_RotationX_label.setObjectName("Gain_RotationX_label")
        self.Gain_RotationY_label = QtWidgets.QLabel(Dialog)
        self.Gain_RotationY_label.setGeometry(QtCore.QRect(710, 110, 80, 22))
        self.Gain_RotationY_label.setObjectName("Gain_RotationY_label")
        self.Gain_RotationZ_label = QtWidgets.QLabel(Dialog)
        self.Gain_RotationZ_label.setGeometry(QtCore.QRect(710, 150, 80, 22))
        self.Gain_RotationZ_label.setObjectName("Gain_RotationZ_label")
        self.line_3 = QtWidgets.QFrame(Dialog)
        self.line_3.setGeometry(QtCore.QRect(700, 190, 331, 20))
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.line_4 = QtWidgets.QFrame(Dialog)
        self.line_4.setGeometry(QtCore.QRect(690, 40, 20, 311))
        self.line_4.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.Duty_FL_LCD = QtWidgets.QLCDNumber(Dialog)
        self.Duty_FL_LCD.setGeometry(QtCore.QRect(740, 420, 64, 23))
        self.Duty_FL_LCD.setObjectName("Duty_FL_LCD")
        self.Duty_FR_LCD = QtWidgets.QLCDNumber(Dialog)
        self.Duty_FR_LCD.setGeometry(QtCore.QRect(940, 420, 64, 23))
        self.Duty_FR_LCD.setObjectName("Duty_FR_LCD")
        self.Duty_BL_LCD = QtWidgets.QLCDNumber(Dialog)
        self.Duty_BL_LCD.setGeometry(QtCore.QRect(740, 500, 64, 23))
        self.Duty_BL_LCD.setObjectName("Duty_BL_LCD")
        self.Duty_BR_LCD = QtWidgets.QLCDNumber(Dialog)
        self.Duty_BR_LCD.setGeometry(QtCore.QRect(940, 500, 64, 23))
        self.Duty_BR_LCD.setObjectName("Duty_BR_LCD")
        self.Title = QtWidgets.QLabel(Dialog)
        self.Title.setGeometry(QtCore.QRect(0, 0, 191, 51))
        font = QtGui.QFont()
        font.setPointSize(25)
        font.setBold(True)
        font.setWeight(75)
        self.Title.setFont(font)
        self.Title.setObjectName("Title")
        self.Fre_Step_text = QtWidgets.QLineEdit(Dialog)
        self.Fre_Step_text.setGeometry(QtCore.QRect(480, 660, 100, 32))
        self.Fre_Step_text.setObjectName("Fre_Step_text")
        self.Duty_Step_text = QtWidgets.QLineEdit(Dialog)
        self.Duty_Step_text.setGeometry(QtCore.QRect(590, 660, 100, 32))
        self.Duty_Step_text.setObjectName("Duty_Step_text")
        self.Gap_Duty_text = QtWidgets.QLineEdit(Dialog)
        self.Gap_Duty_text.setGeometry(QtCore.QRect(480, 500, 100, 32))
        self.Gap_Duty_text.setObjectName("Gap_Duty_text")
        self.Step_Fre = QtWidgets.QLabel(Dialog)
        self.Step_Fre.setGeometry(QtCore.QRect(493, 640, 68, 22))
        self.Step_Fre.setObjectName("Step_Fre")
        self.Step_Duty = QtWidgets.QLabel(Dialog)
        self.Step_Duty.setGeometry(QtCore.QRect(610, 640, 81, 22))
        self.Step_Duty.setObjectName("Step_Duty")
        self.Gap_Duty = QtWidgets.QLabel(Dialog)
        self.Gap_Duty.setGeometry(QtCore.QRect(490, 480, 91, 22))
        self.Gap_Duty.setObjectName("Gap_Duty")
        self.AngleY_label = QtWidgets.QLabel(Dialog)
        self.AngleY_label.setGeometry(QtCore.QRect(170, 160, 51, 22))
        self.AngleY_label.setObjectName("AngleY_label")
        self.AngleX_label = QtWidgets.QLabel(Dialog)
        self.AngleX_label.setGeometry(QtCore.QRect(170, 70, 81, 22))
        self.AngleX_label.setObjectName("AngleX_label")
        self.AngleZ_label = QtWidgets.QLabel(Dialog)
        self.AngleZ_label.setGeometry(QtCore.QRect(170, 260, 61, 22))
        self.AngleZ_label.setObjectName("AngleZ_label")
        self.AngleX_v_label = QtWidgets.QLabel(Dialog)
        self.AngleX_v_label.setGeometry(QtCore.QRect(260, 70, 81, 22))
        self.AngleX_v_label.setObjectName("AngleX_v_label")
        self.AngleX_a_label = QtWidgets.QLabel(Dialog)
        self.AngleX_a_label.setGeometry(QtCore.QRect(360, 70, 81, 22))
        self.AngleX_a_label.setObjectName("AngleX_a_label")
        self.AngleY_v_label = QtWidgets.QLabel(Dialog)
        self.AngleY_v_label.setGeometry(QtCore.QRect(260, 160, 71, 22))
        self.AngleY_v_label.setObjectName("AngleY_v_label")
        self.AngleY_a_label = QtWidgets.QLabel(Dialog)
        self.AngleY_a_label.setGeometry(QtCore.QRect(360, 160, 71, 22))
        self.AngleY_a_label.setObjectName("AngleY_a_label")
        self.AngleZ_v_label = QtWidgets.QLabel(Dialog)
        self.AngleZ_v_label.setGeometry(QtCore.QRect(260, 260, 81, 22))
        self.AngleZ_v_label.setObjectName("AngleZ_v_label")
        self.AngleZ_a_label = QtWidgets.QLabel(Dialog)
        self.AngleZ_a_label.setGeometry(QtCore.QRect(360, 260, 71, 22))
        self.AngleZ_a_label.setObjectName("AngleZ_a_label")
        self.AngleX_split = QtWidgets.QSplitter(Dialog)
        self.AngleX_split.setGeometry(QtCore.QRect(150, 90, 281, 23))
        self.AngleX_split.setOrientation(QtCore.Qt.Horizontal)
        self.AngleX_split.setObjectName("AngleX_split")
        self.AngleX_LCD = QtWidgets.QLCDNumber(self.AngleX_split)
        self.AngleX_LCD.setObjectName("AngleX_LCD")
        self.AngleX_v_LCD = QtWidgets.QLCDNumber(self.AngleX_split)
        self.AngleX_v_LCD.setObjectName("AngleX_v_LCD")
        self.AngleX_a_LCD = QtWidgets.QLCDNumber(self.AngleX_split)
        self.AngleX_a_LCD.setObjectName("AngleX_a_LCD")
        self.layoutWidget1 = QtWidgets.QWidget(Dialog)
        self.layoutWidget1.setGeometry(QtCore.QRect(810, 160, 201, 34))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.RatationZ_layout = QtWidgets.QHBoxLayout(self.layoutWidget1)
        self.RatationZ_layout.setContentsMargins(0, 0, 0, 0)
        self.RatationZ_layout.setObjectName("RatationZ_layout")
        self.GLZP = QtWidgets.QLineEdit(self.layoutWidget1)
        self.GLZP.setObjectName("GLZP")
        self.RatationZ_layout.addWidget(self.GLZP)
        self.GLZI = QtWidgets.QLineEdit(self.layoutWidget1)
        self.GLZI.setObjectName("GLZI")
        self.RatationZ_layout.addWidget(self.GLZI)
        self.GLZD = QtWidgets.QLineEdit(self.layoutWidget1)
        self.GLZD.setObjectName("GLZD")
        self.RatationZ_layout.addWidget(self.GLZD)
        self.L_check = QtWidgets.QCheckBox(Dialog)
        self.L_check.setGeometry(QtCore.QRect(530, 390, 101, 27))
        self.L_check.setObjectName("L_check")
        self.F_check = QtWidgets.QCheckBox(Dialog)
        self.F_check.setGeometry(QtCore.QRect(570, 360, 101, 27))
        self.F_check.setObjectName("F_check")
        self.Frequency_LCD = QtWidgets.QLCDNumber(Dialog)
        self.Frequency_LCD.setGeometry(QtCore.QRect(743, 610, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.Frequency_LCD.setFont(font)
        self.Frequency_LCD.setObjectName("Frequency_LCD")
        self.Duty_LCD = QtWidgets.QLCDNumber(Dialog)
        self.Duty_LCD.setGeometry(QtCore.QRect(860, 610, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.Duty_LCD.setFont(font)
        self.Duty_LCD.setObjectName("Duty_LCD")
        self.R_check = QtWidgets.QCheckBox(Dialog)
        self.R_check.setGeometry(QtCore.QRect(600, 390, 101, 27))
        self.R_check.setObjectName("R_check")
        self.B_check = QtWidgets.QCheckBox(Dialog)
        self.B_check.setGeometry(QtCore.QRect(570, 420, 101, 27))
        self.B_check.setObjectName("B_check")
        self.AngleX_tar_label = QtWidgets.QLabel(Dialog)
        self.AngleX_tar_label.setGeometry(QtCore.QRect(50, 80, 80, 22))
        font = QtGui.QFont()
        font.setFamily("PibotoLt")
        self.AngleX_tar_label.setFont(font)
        self.AngleX_tar_label.setObjectName("AngleX_tar_label")
        self.PosY_v_label = QtWidgets.QLabel(Dialog)
        self.PosY_v_label.setGeometry(QtCore.QRect(260, 460, 81, 22))
        self.PosY_v_label.setObjectName("PosY_v_label")
        self.Gain_PosX_label = QtWidgets.QLabel(Dialog)
        self.Gain_PosX_label.setGeometry(QtCore.QRect(710, 200, 80, 22))
        self.Gain_PosX_label.setObjectName("Gain_PosX_label")
        self.PosY_a_label = QtWidgets.QLabel(Dialog)
        self.PosY_a_label.setGeometry(QtCore.QRect(360, 460, 71, 22))
        self.PosY_a_label.setObjectName("PosY_a_label")
        self.PosX_a_label = QtWidgets.QLabel(Dialog)
        self.PosX_a_label.setGeometry(QtCore.QRect(360, 360, 71, 22))
        self.PosX_a_label.setObjectName("PosX_a_label")
        self.PosX_split = QtWidgets.QSplitter(Dialog)
        self.PosX_split.setGeometry(QtCore.QRect(150, 380, 281, 23))
        self.PosX_split.setOrientation(QtCore.Qt.Horizontal)
        self.PosX_split.setObjectName("PosX_split")
        self.PosX_LCD = QtWidgets.QLCDNumber(self.PosX_split)
        self.PosX_LCD.setObjectName("PosX_LCD")
        self.PosX_v_LCD = QtWidgets.QLCDNumber(self.PosX_split)
        self.PosX_v_LCD.setObjectName("PosX_v_LCD")
        self.PosX_a_LCD = QtWidgets.QLCDNumber(self.PosX_split)
        self.PosX_a_LCD.setObjectName("PosX_a_LCD")
        self.PosX_v_label = QtWidgets.QLabel(Dialog)
        self.PosX_v_label.setGeometry(QtCore.QRect(260, 360, 71, 22))
        self.PosX_v_label.setObjectName("PosX_v_label")
        self.PosY_label = QtWidgets.QLabel(Dialog)
        self.PosY_label.setGeometry(QtCore.QRect(170, 460, 61, 22))
        self.PosY_label.setObjectName("PosY_label")
        self.line_7 = QtWidgets.QFrame(Dialog)
        self.line_7.setGeometry(QtCore.QRect(700, 280, 331, 20))
        self.line_7.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_7.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_7.setObjectName("line_7")
        self.PosX_label = QtWidgets.QLabel(Dialog)
        self.PosX_label.setGeometry(QtCore.QRect(170, 360, 51, 22))
        self.PosX_label.setObjectName("PosX_label")
        self.Gain_PosY_label = QtWidgets.QLabel(Dialog)
        self.Gain_PosY_label.setGeometry(QtCore.QRect(710, 240, 80, 22))
        self.Gain_PosY_label.setObjectName("Gain_PosY_label")
        self.PosY_split = QtWidgets.QSplitter(Dialog)
        self.PosY_split.setGeometry(QtCore.QRect(150, 480, 281, 23))
        self.PosY_split.setOrientation(QtCore.Qt.Horizontal)
        self.PosY_split.setObjectName("PosY_split")
        self.PosY_LCD = QtWidgets.QLCDNumber(self.PosY_split)
        self.PosY_LCD.setObjectName("PosY_LCD")
        self.PosY_v_LCD = QtWidgets.QLCDNumber(self.PosY_split)
        self.PosY_v_LCD.setObjectName("PosY_v_LCD")
        self.PosY_a_LCD = QtWidgets.QLCDNumber(self.PosY_split)
        self.PosY_a_LCD.setObjectName("PosY_a_LCD")
        self.layoutWidget_3 = QtWidgets.QWidget(Dialog)
        self.layoutWidget_3.setGeometry(QtCore.QRect(810, 210, 201, 34))
        self.layoutWidget_3.setObjectName("layoutWidget_3")
        self.PosX_layout = QtWidgets.QHBoxLayout(self.layoutWidget_3)
        self.PosX_layout.setContentsMargins(0, 0, 0, 0)
        self.PosX_layout.setObjectName("PosX_layout")
        self.GVXP = QtWidgets.QLineEdit(self.layoutWidget_3)
        self.GVXP.setObjectName("GVXP")
        self.PosX_layout.addWidget(self.GVXP)
        self.GVXI = QtWidgets.QLineEdit(self.layoutWidget_3)
        self.GVXI.setObjectName("GVXI")
        self.PosX_layout.addWidget(self.GVXI)
        self.GVXD = QtWidgets.QLineEdit(self.layoutWidget_3)
        self.GVXD.setObjectName("GVXD")
        self.PosX_layout.addWidget(self.GVXD)
        self.layoutWidget_4 = QtWidgets.QWidget(Dialog)
        self.layoutWidget_4.setGeometry(QtCore.QRect(810, 250, 201, 34))
        self.layoutWidget_4.setObjectName("layoutWidget_4")
        self.PosY_layout = QtWidgets.QHBoxLayout(self.layoutWidget_4)
        self.PosY_layout.setContentsMargins(0, 0, 0, 0)
        self.PosY_layout.setObjectName("PosY_layout")
        self.GVYP = QtWidgets.QLineEdit(self.layoutWidget_4)
        self.GVYP.setObjectName("GVYP")
        self.PosY_layout.addWidget(self.GVYP)
        self.GVYI = QtWidgets.QLineEdit(self.layoutWidget_4)
        self.GVYI.setObjectName("GVYI")
        self.PosY_layout.addWidget(self.GVYI)
        self.GVYD = QtWidgets.QLineEdit(self.layoutWidget_4)
        self.GVYD.setObjectName("GVYD")
        self.PosY_layout.addWidget(self.GVYD)
        self.Gain_Height_label = QtWidgets.QLabel(Dialog)
        self.Gain_Height_label.setGeometry(QtCore.QRect(720, 290, 51, 22))
        self.Gain_Height_label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.Gain_Height_label.setObjectName("Gain_Height_label")
        self.Height_a_label = QtWidgets.QLabel(Dialog)
        self.Height_a_label.setGeometry(QtCore.QRect(360, 580, 71, 22))
        self.Height_a_label.setObjectName("Height_a_label")
        self.Height_split = QtWidgets.QSplitter(Dialog)
        self.Height_split.setGeometry(QtCore.QRect(150, 600, 281, 23))
        self.Height_split.setOrientation(QtCore.Qt.Horizontal)
        self.Height_split.setObjectName("Height_split")
        self.Height_LCD = QtWidgets.QLCDNumber(self.Height_split)
        self.Height_LCD.setObjectName("Height_LCD")
        self.Height_v_LCD = QtWidgets.QLCDNumber(self.Height_split)
        self.Height_v_LCD.setObjectName("Height_v_LCD")
        self.Height_a_LCD = QtWidgets.QLCDNumber(self.Height_split)
        self.Height_a_LCD.setObjectName("Height_a_LCD")
        self.Height_label = QtWidgets.QLabel(Dialog)
        self.Height_label.setGeometry(QtCore.QRect(170, 580, 51, 22))
        self.Height_label.setObjectName("Height_label")
        self.layoutWidget_5 = QtWidgets.QWidget(Dialog)
        self.layoutWidget_5.setGeometry(QtCore.QRect(810, 300, 201, 34))
        self.layoutWidget_5.setObjectName("layoutWidget_5")
        self.Height_layout = QtWidgets.QHBoxLayout(self.layoutWidget_5)
        self.Height_layout.setContentsMargins(0, 0, 0, 0)
        self.Height_layout.setObjectName("Height_layout")
        self.GHP = QtWidgets.QLineEdit(self.layoutWidget_5)
        self.GHP.setObjectName("GHP")
        self.Height_layout.addWidget(self.GHP)
        self.GHI = QtWidgets.QLineEdit(self.layoutWidget_5)
        self.GHI.setObjectName("GHI")
        self.Height_layout.addWidget(self.GHI)
        self.GHD = QtWidgets.QLineEdit(self.layoutWidget_5)
        self.GHD.setObjectName("GHD")
        self.Height_layout.addWidget(self.GHD)
        self.Height_v_label = QtWidgets.QLabel(Dialog)
        self.Height_v_label.setGeometry(QtCore.QRect(260, 580, 71, 22))
        self.Height_v_label.setObjectName("Height_v_label")
        self.line_10 = QtWidgets.QFrame(Dialog)
        self.line_10.setGeometry(QtCore.QRect(700, 340, 331, 20))
        self.line_10.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_10.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_10.setObjectName("line_10")
        self.AngleY_tar_label = QtWidgets.QLabel(Dialog)
        self.AngleY_tar_label.setGeometry(QtCore.QRect(50, 170, 80, 22))
        font = QtGui.QFont()
        font.setFamily("PibotoLt")
        self.AngleY_tar_label.setFont(font)
        self.AngleY_tar_label.setObjectName("AngleY_tar_label")
        self.AngleY_target = QtWidgets.QLineEdit(Dialog)
        self.AngleY_target.setGeometry(QtCore.QRect(50, 190, 80, 32))
        self.AngleY_target.setObjectName("AngleY_target")
        self.PosX_target = QtWidgets.QLineEdit(Dialog)
        self.PosX_target.setGeometry(QtCore.QRect(50, 380, 80, 32))
        self.PosX_target.setObjectName("PosX_target")
        self.AngleZ_tar_label = QtWidgets.QLabel(Dialog)
        self.AngleZ_tar_label.setGeometry(QtCore.QRect(50, 270, 80, 22))
        font = QtGui.QFont()
        font.setFamily("PibotoLt")
        self.AngleZ_tar_label.setFont(font)
        self.AngleZ_tar_label.setObjectName("AngleZ_tar_label")
        self.AngleZ_target = QtWidgets.QLineEdit(Dialog)
        self.AngleZ_target.setGeometry(QtCore.QRect(50, 290, 80, 32))
        self.AngleZ_target.setObjectName("AngleZ_target")
        self.PosX_tar_label = QtWidgets.QLabel(Dialog)
        self.PosX_tar_label.setGeometry(QtCore.QRect(50, 360, 80, 22))
        font = QtGui.QFont()
        font.setFamily("PibotoLt")
        self.PosX_tar_label.setFont(font)
        self.PosX_tar_label.setObjectName("PosX_tar_label")
        self.PosY_tar_label = QtWidgets.QLabel(Dialog)
        self.PosY_tar_label.setGeometry(QtCore.QRect(50, 470, 80, 22))
        font = QtGui.QFont()
        font.setFamily("PibotoLt")
        self.PosY_tar_label.setFont(font)
        self.PosY_tar_label.setObjectName("PosY_tar_label")
        self.PosY_target = QtWidgets.QLineEdit(Dialog)
        self.PosY_target.setGeometry(QtCore.QRect(50, 490, 80, 32))
        self.PosY_target.setObjectName("PosY_target")
        self.Height_target = QtWidgets.QLineEdit(Dialog)
        self.Height_target.setGeometry(QtCore.QRect(50, 600, 80, 32))
        self.Height_target.setObjectName("Height_target")
        self.Height_tar_label = QtWidgets.QLabel(Dialog)
        self.Height_tar_label.setGeometry(QtCore.QRect(50, 580, 80, 22))
        font = QtGui.QFont()
        font.setFamily("PibotoLt")
        self.Height_tar_label.setFont(font)
        self.Height_tar_label.setObjectName("Height_tar_label")
        self.Hovering_check = QtWidgets.QCheckBox(Dialog)
        self.Hovering_check.setGeometry(QtCore.QRect(230, 40, 101, 27))
        self.Hovering_check.setObjectName("Hovering_check")
        self.Single_Time_text = QtWidgets.QLineEdit(Dialog)
        self.Single_Time_text.setGeometry(QtCore.QRect(590, 500, 100, 32))
        self.Single_Time_text.setObjectName("Single_Time_text")
        self.Single_time = QtWidgets.QLabel(Dialog)
        self.Single_time.setGeometry(QtCore.QRect(590, 480, 121, 22))
        self.Single_time.setObjectName("Single_time")
        self.Single_TR = QtWidgets.QPushButton(Dialog)
        self.Single_TR.setGeometry(QtCore.QRect(910, 370, 111, 30))
        self.Single_TR.setObjectName("Single_TR")
        self.Single_TL = QtWidgets.QPushButton(Dialog)
        self.Single_TL.setGeometry(QtCore.QRect(730, 370, 111, 30))
        self.Single_TL.setObjectName("Single_TL")
        self.Gain_RotationX_check = QtWidgets.QCheckBox(Dialog)
        self.Gain_RotationX_check.setGeometry(QtCore.QRect(740, 90, 41, 27))
        self.Gain_RotationX_check.setText("")
        self.Gain_RotationX_check.setObjectName("Gain_RotationX_check")
        self.Gain_RotationY_check = QtWidgets.QCheckBox(Dialog)
        self.Gain_RotationY_check.setGeometry(QtCore.QRect(740, 130, 41, 27))
        self.Gain_RotationY_check.setText("")
        self.Gain_RotationY_check.setObjectName("Gain_RotationY_check")
        self.Gain_RotationZ_check = QtWidgets.QCheckBox(Dialog)
        self.Gain_RotationZ_check.setGeometry(QtCore.QRect(740, 170, 41, 27))
        self.Gain_RotationZ_check.setText("")
        self.Gain_RotationZ_check.setObjectName("Gain_RotationZ_check")
        self.Gain_Height_check = QtWidgets.QCheckBox(Dialog)
        self.Gain_Height_check.setGeometry(QtCore.QRect(740, 310, 41, 27))
        self.Gain_Height_check.setText("")
        self.Gain_Height_check.setObjectName("Gain_Height_check")
        self.Gain_PosY_check = QtWidgets.QCheckBox(Dialog)
        self.Gain_PosY_check.setGeometry(QtCore.QRect(740, 260, 41, 27))
        self.Gain_PosY_check.setText("")
        self.Gain_PosY_check.setObjectName("Gain_PosY_check")
        self.Gain_PosX_check = QtWidgets.QCheckBox(Dialog)
        self.Gain_PosX_check.setGeometry(QtCore.QRect(740, 220, 41, 27))
        self.Gain_PosX_check.setText("")
        self.Gain_PosX_check.setObjectName("Gain_PosX_check")
        self.Cal_button = QtWidgets.QPushButton(Dialog)
        self.Cal_button.setGeometry(QtCore.QRect(970, 610, 105, 31))
        self.Cal_button.setObjectName("Cal_button")
        self.layoutWidget_6 = QtWidgets.QWidget(Dialog)
        self.layoutWidget_6.setGeometry(QtCore.QRect(150, 210, 281, 34))
        self.layoutWidget_6.setObjectName("layoutWidget_6")
        self.AngleY_const_Layout = QtWidgets.QHBoxLayout(self.layoutWidget_6)
        self.AngleY_const_Layout.setContentsMargins(0, 0, 0, 0)
        self.AngleY_const_Layout.setObjectName("AngleY_const_Layout")
        self.AngleY_const = QtWidgets.QLineEdit(self.layoutWidget_6)
        self.AngleY_const.setObjectName("AngleY_const")
        self.AngleY_const_Layout.addWidget(self.AngleY_const)
        self.AngleY_v_const = QtWidgets.QLineEdit(self.layoutWidget_6)
        self.AngleY_v_const.setObjectName("AngleY_v_const")
        self.AngleY_const_Layout.addWidget(self.AngleY_v_const)
        self.AngleY_a_const = QtWidgets.QLineEdit(self.layoutWidget_6)
        self.AngleY_a_const.setObjectName("AngleY_a_const")
        self.AngleY_const_Layout.addWidget(self.AngleY_a_const)
        self.layoutWidget_7 = QtWidgets.QWidget(Dialog)
        self.layoutWidget_7.setGeometry(QtCore.QRect(150, 310, 281, 34))
        self.layoutWidget_7.setObjectName("layoutWidget_7")
        self.AngleZ_const_Layout = QtWidgets.QHBoxLayout(self.layoutWidget_7)
        self.AngleZ_const_Layout.setContentsMargins(0, 0, 0, 0)
        self.AngleZ_const_Layout.setObjectName("AngleZ_const_Layout")
        self.AngleZ_const = QtWidgets.QLineEdit(self.layoutWidget_7)
        self.AngleZ_const.setObjectName("AngleZ_const")
        self.AngleZ_const_Layout.addWidget(self.AngleZ_const)
        self.AngleZ_v_const = QtWidgets.QLineEdit(self.layoutWidget_7)
        self.AngleZ_v_const.setObjectName("AngleZ_v_const")
        self.AngleZ_const_Layout.addWidget(self.AngleZ_v_const)
        self.AngleZ_a_const = QtWidgets.QLineEdit(self.layoutWidget_7)
        self.AngleZ_a_const.setObjectName("AngleZ_a_const")
        self.AngleZ_const_Layout.addWidget(self.AngleZ_a_const)
        self.layoutWidget_8 = QtWidgets.QWidget(Dialog)
        self.layoutWidget_8.setGeometry(QtCore.QRect(150, 410, 281, 34))
        self.layoutWidget_8.setObjectName("layoutWidget_8")
        self.PosX_const_Layout = QtWidgets.QHBoxLayout(self.layoutWidget_8)
        self.PosX_const_Layout.setContentsMargins(0, 0, 0, 0)
        self.PosX_const_Layout.setObjectName("PosX_const_Layout")
        self.PosX_const = QtWidgets.QLineEdit(self.layoutWidget_8)
        self.PosX_const.setObjectName("PosX_const")
        self.PosX_const_Layout.addWidget(self.PosX_const)
        self.PosX_v_const = QtWidgets.QLineEdit(self.layoutWidget_8)
        self.PosX_v_const.setObjectName("PosX_v_const")
        self.PosX_const_Layout.addWidget(self.PosX_v_const)
        self.PosX_a_const = QtWidgets.QLineEdit(self.layoutWidget_8)
        self.PosX_a_const.setObjectName("PosX_a_const")
        self.PosX_const_Layout.addWidget(self.PosX_a_const)
        self.layoutWidget_9 = QtWidgets.QWidget(Dialog)
        self.layoutWidget_9.setGeometry(QtCore.QRect(150, 510, 281, 34))
        self.layoutWidget_9.setObjectName("layoutWidget_9")
        self.PosY_const_Layout = QtWidgets.QHBoxLayout(self.layoutWidget_9)
        self.PosY_const_Layout.setContentsMargins(0, 0, 0, 0)
        self.PosY_const_Layout.setObjectName("PosY_const_Layout")
        self.PosY_const = QtWidgets.QLineEdit(self.layoutWidget_9)
        self.PosY_const.setObjectName("PosY_const")
        self.PosY_const_Layout.addWidget(self.PosY_const)
        self.PosY_v_const = QtWidgets.QLineEdit(self.layoutWidget_9)
        self.PosY_v_const.setObjectName("PosY_v_const")
        self.PosY_const_Layout.addWidget(self.PosY_v_const)
        self.PosY_a_const = QtWidgets.QLineEdit(self.layoutWidget_9)
        self.PosY_a_const.setObjectName("PosY_a_const")
        self.PosY_const_Layout.addWidget(self.PosY_a_const)
        self.layoutWidget_10 = QtWidgets.QWidget(Dialog)
        self.layoutWidget_10.setGeometry(QtCore.QRect(150, 630, 281, 34))
        self.layoutWidget_10.setObjectName("layoutWidget_10")
        self.Height_layout_2 = QtWidgets.QHBoxLayout(self.layoutWidget_10)
        self.Height_layout_2.setContentsMargins(0, 0, 0, 0)
        self.Height_layout_2.setObjectName("Height_layout_2")
        self.Height_const = QtWidgets.QLineEdit(self.layoutWidget_10)
        self.Height_const.setObjectName("Height_const")
        self.Height_layout_2.addWidget(self.Height_const)
        self.Height_v_const = QtWidgets.QLineEdit(self.layoutWidget_10)
        self.Height_v_const.setObjectName("Height_v_const")
        self.Height_layout_2.addWidget(self.Height_v_const)
        self.Height_a_const = QtWidgets.QLineEdit(self.layoutWidget_10)
        self.Height_a_const.setObjectName("Height_a_const")
        self.Height_layout_2.addWidget(self.Height_a_const)
        self.AngleX_target = QtWidgets.QLineEdit(Dialog)
        self.AngleX_target.setGeometry(QtCore.QRect(50, 100, 80, 32))
        self.AngleX_target.setObjectName("AngleX_target")
        self.layoutWidget2 = QtWidgets.QWidget(Dialog)
        self.layoutWidget2.setGeometry(QtCore.QRect(150, 120, 281, 34))
        self.layoutWidget2.setObjectName("layoutWidget2")
        self.AngleX_const_Layout = QtWidgets.QHBoxLayout(self.layoutWidget2)
        self.AngleX_const_Layout.setContentsMargins(0, 0, 0, 0)
        self.AngleX_const_Layout.setObjectName("AngleX_const_Layout")
        self.AngleX_const = QtWidgets.QLineEdit(self.layoutWidget2)
        self.AngleX_const.setObjectName("AngleX_const")
        self.AngleX_const_Layout.addWidget(self.AngleX_const)
        self.AngleX_v_const = QtWidgets.QLineEdit(self.layoutWidget2)
        self.AngleX_v_const.setObjectName("AngleX_v_const")
        self.AngleX_const_Layout.addWidget(self.AngleX_v_const)
        self.AngleX_a_const = QtWidgets.QLineEdit(self.layoutWidget2)
        self.AngleX_a_const.setObjectName("AngleX_a_const")
        self.AngleX_const_Layout.addWidget(self.AngleX_a_const)
        self.Exit_button = QtWidgets.QPushButton(Dialog)
        self.Exit_button.setGeometry(QtCore.QRect(970, 700, 105, 31))
        self.Exit_button.setObjectName("Exit_button")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.Set_button.setText(_translate("Dialog", "Set"))
        self.Duty_high.setText(_translate("Dialog", "Duty_up"))
        self.Fre_high.setText(_translate("Dialog", "Fre_up"))
        self.Fre_low.setText(_translate("Dialog", "Fre_down"))
        self.Duty_low.setText(_translate("Dialog", "Duty_down"))
        self.Frequency_text.setText(_translate("Dialog", "300"))
        self.Duty_text.setText(_translate("Dialog", "30"))
        self.Fre_label.setText(_translate("Dialog", "Frequency [MHz]"))
        self.Duty_label.setText(_translate("Dialog", "Duty [%]"))
        self.Single_R.setText(_translate("Dialog", "Single_R"))
        self.Single_L.setText(_translate("Dialog", "Single_L"))
        self.Single_BWD.setText(_translate("Dialog", "Single_BWD"))
        self.Single_FWD.setText(_translate("Dialog", "Single_FWD"))
        self.GLXP.setText(_translate("Dialog", "1"))
        self.GLXI.setText(_translate("Dialog", "0"))
        self.GLXD.setText(_translate("Dialog", "0"))
        self.GLYP.setText(_translate("Dialog", "1"))
        self.GLYI.setText(_translate("Dialog", "0"))
        self.GLYD.setText(_translate("Dialog", "0"))
        self.P_label.setText(_translate("Dialog", "P"))
        self.I_label.setText(_translate("Dialog", "I"))
        self.D_label.setText(_translate("Dialog", "D"))
        self.Gain_RotationX_label.setText(_translate("Dialog", "RotataionX"))
        self.Gain_RotationY_label.setText(_translate("Dialog", "RotationY"))
        self.Gain_RotationZ_label.setText(_translate("Dialog", "RotationZ"))
        self.Title.setText(_translate("Dialog", "JeonDRONE"))
        self.Fre_Step_text.setText(_translate("Dialog", "10"))
        self.Duty_Step_text.setText(_translate("Dialog", "1"))
        self.Gap_Duty_text.setText(_translate("Dialog", "3"))
        self.Step_Fre.setText(_translate("Dialog", "Step_Fre"))
        self.Step_Duty.setText(_translate("Dialog", "Step_Duty"))
        self.Gap_Duty.setText(_translate("Dialog", "gap_Duty"))
        self.AngleY_label.setText(_translate("Dialog", "AngleY"))
        self.AngleX_label.setText(_translate("Dialog", "AngleX"))
        self.AngleZ_label.setText(_translate("Dialog", "AngleZ"))
        self.AngleX_v_label.setText(_translate("Dialog", "AngleX_v"))
        self.AngleX_a_label.setText(_translate("Dialog", "AnlgeX_a"))
        self.AngleY_v_label.setText(_translate("Dialog", "AngleY_v"))
        self.AngleY_a_label.setText(_translate("Dialog", "AngleY_a"))
        self.AngleZ_v_label.setText(_translate("Dialog", "AngleZ_v"))
        self.AngleZ_a_label.setText(_translate("Dialog", "AngleZ_a"))
        self.GLZP.setText(_translate("Dialog", "1"))
        self.GLZI.setText(_translate("Dialog", "0"))
        self.GLZD.setText(_translate("Dialog", "0"))
        self.L_check.setText(_translate("Dialog", "L"))
        self.F_check.setText(_translate("Dialog", "F"))
        self.R_check.setText(_translate("Dialog", "R"))
        self.B_check.setText(_translate("Dialog", "B"))
        self.AngleX_tar_label.setText(_translate("Dialog", "AngleX"))
        self.PosY_v_label.setText(_translate("Dialog", "PosY_v"))
        self.Gain_PosX_label.setText(_translate("Dialog", "PositionX"))
        self.PosY_a_label.setText(_translate("Dialog", "PosY_a"))
        self.PosX_a_label.setText(_translate("Dialog", "PosX_a"))
        self.PosX_v_label.setText(_translate("Dialog", "PosX_v"))
        self.PosY_label.setText(_translate("Dialog", "PosY"))
        self.PosX_label.setText(_translate("Dialog", "PosX"))
        self.Gain_PosY_label.setText(_translate("Dialog", "PositionY"))
        self.GVXP.setText(_translate("Dialog", "1"))
        self.GVXI.setText(_translate("Dialog", "0"))
        self.GVXD.setText(_translate("Dialog", "0"))
        self.GVYP.setText(_translate("Dialog", "1"))
        self.GVYI.setText(_translate("Dialog", "0"))
        self.GVYD.setText(_translate("Dialog", "0"))
        self.Gain_Height_label.setText(_translate("Dialog", "Height"))
        self.Height_a_label.setText(_translate("Dialog", "Height_a"))
        self.Height_label.setText(_translate("Dialog", "Height"))
        self.GHP.setText(_translate("Dialog", "1"))
        self.GHI.setText(_translate("Dialog", "0"))
        self.GHD.setText(_translate("Dialog", "0"))
        self.Height_v_label.setText(_translate("Dialog", "Height_v"))
        self.AngleY_tar_label.setText(_translate("Dialog", "AngleY"))
        self.AngleY_target.setText(_translate("Dialog", "0"))
        self.PosX_target.setText(_translate("Dialog", "0"))
        self.AngleZ_tar_label.setText(_translate("Dialog", "AngleZ"))
        self.AngleZ_target.setText(_translate("Dialog", "0"))
        self.PosX_tar_label.setText(_translate("Dialog", "Position X"))
        self.PosY_tar_label.setText(_translate("Dialog", "PositionY"))
        self.PosY_target.setText(_translate("Dialog", "0"))
        self.Height_target.setText(_translate("Dialog", "0"))
        self.Height_tar_label.setText(_translate("Dialog", "Height"))
        self.Hovering_check.setText(_translate("Dialog", "Hovering"))
        self.Single_Time_text.setText(_translate("Dialog", "100"))
        self.Single_time.setText(_translate("Dialog", "single time[ms]"))
        self.Single_TR.setText(_translate("Dialog", "Turn_Right"))
        self.Single_TL.setText(_translate("Dialog", "Turn_Left"))
        self.Cal_button.setText(_translate("Dialog", "Calibration"))
        self.AngleY_const.setText(_translate("Dialog", "0"))
        self.AngleY_v_const.setText(_translate("Dialog", "0"))
        self.AngleY_a_const.setText(_translate("Dialog", "0"))
        self.AngleZ_const.setText(_translate("Dialog", "0"))
        self.AngleZ_v_const.setText(_translate("Dialog", "0"))
        self.AngleZ_a_const.setText(_translate("Dialog", "0"))
        self.PosX_const.setText(_translate("Dialog", "0"))
        self.PosX_v_const.setText(_translate("Dialog", "0"))
        self.PosX_a_const.setText(_translate("Dialog", "0"))
        self.PosY_const.setText(_translate("Dialog", "0"))
        self.PosY_v_const.setText(_translate("Dialog", "0"))
        self.PosY_a_const.setText(_translate("Dialog", "0"))
        self.Height_const.setText(_translate("Dialog", "0"))
        self.Height_v_const.setText(_translate("Dialog", "0"))
        self.Height_a_const.setText(_translate("Dialog", "0"))
        self.AngleX_target.setText(_translate("Dialog", "0"))
        self.AngleX_const.setText(_translate("Dialog", "0"))
        self.AngleX_v_const.setText(_translate("Dialog", "0"))
        self.AngleX_a_const.setText(_translate("Dialog", "0"))
        self.Exit_button.setText(_translate("Dialog", "EXIT"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

