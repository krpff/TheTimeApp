# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'designed.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(365, 535)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(365, 535))
        MainWindow.setMaximumSize(QtCore.QSize(365, 535))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(10, 10, 351, 481))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        self.tabWidget.setFont(font)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.verticalLayoutWidget_7 = QtWidgets.QWidget(self.tab)
        self.verticalLayoutWidget_7.setGeometry(QtCore.QRect(9, 9, 331, 441))
        self.verticalLayoutWidget_7.setObjectName("verticalLayoutWidget_7")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_7)
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.alarm_time = QtWidgets.QTimeEdit(self.verticalLayoutWidget_7)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(13)
        self.alarm_time.setFont(font)
        self.alarm_time.setAlignment(QtCore.Qt.AlignCenter)
        self.alarm_time.setObjectName("alarm_time")
        self.verticalLayout_7.addWidget(self.alarm_time)
        self.alarm_set = QtWidgets.QPushButton(self.verticalLayoutWidget_7)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(13)
        self.alarm_set.setFont(font)
        self.alarm_set.setObjectName("alarm_set")
        self.verticalLayout_7.addWidget(self.alarm_set)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget_7)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout_5.addWidget(self.label)
        self.verticalLayout_7.addLayout(self.horizontalLayout_5)
        self.alarm_list_widget = QtWidgets.QListWidget(self.verticalLayoutWidget_7)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(13)
        self.alarm_list_widget.setFont(font)
        self.alarm_list_widget.setObjectName("alarm_list_widget")
        self.verticalLayout_7.addWidget(self.alarm_list_widget)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.alarm_delete_button = QtWidgets.QPushButton(self.verticalLayoutWidget_7)
        self.alarm_delete_button.setObjectName("alarm_delete_button")
        self.horizontalLayout_4.addWidget(self.alarm_delete_button)
        self.alarm_clearlist_button = QtWidgets.QPushButton(self.verticalLayoutWidget_7)
        self.alarm_clearlist_button.setObjectName("alarm_clearlist_button")
        self.horizontalLayout_4.addWidget(self.alarm_clearlist_button)
        self.verticalLayout_7.addLayout(self.horizontalLayout_4)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.verticalLayoutWidget_3 = QtWidgets.QWidget(self.tab_2)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(10, 10, 321, 431))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setSpacing(10)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.stopw_timer_label = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(24)
        self.stopw_timer_label.setFont(font)
        self.stopw_timer_label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.stopw_timer_label.setIndent(70)
        self.stopw_timer_label.setObjectName("stopw_timer_label")
        self.verticalLayout_5.addWidget(self.stopw_timer_label)
        self.stopw_start_button = QtWidgets.QPushButton(self.verticalLayoutWidget_3)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(13)
        self.stopw_start_button.setFont(font)
        self.stopw_start_button.setObjectName("stopw_start_button")
        self.verticalLayout_5.addWidget(self.stopw_start_button)
        self.stopw_pause_button = QtWidgets.QPushButton(self.verticalLayoutWidget_3)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(13)
        self.stopw_pause_button.setFont(font)
        self.stopw_pause_button.setObjectName("stopw_pause_button")
        self.verticalLayout_5.addWidget(self.stopw_pause_button)
        self.stopw_reset_button = QtWidgets.QPushButton(self.verticalLayoutWidget_3)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(13)
        self.stopw_reset_button.setFont(font)
        self.stopw_reset_button.setObjectName("stopw_reset_button")
        self.verticalLayout_5.addWidget(self.stopw_reset_button)
        self.stopw_round_button = QtWidgets.QPushButton(self.verticalLayoutWidget_3)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(13)
        self.stopw_round_button.setFont(font)
        self.stopw_round_button.setObjectName("stopw_round_button")
        self.verticalLayout_5.addWidget(self.stopw_round_button)
        self.stopw_save_button = QtWidgets.QPushButton(self.verticalLayoutWidget_3)
        self.stopw_save_button.setObjectName("stopw_save_button")
        self.verticalLayout_5.addWidget(self.stopw_save_button)
        self.stopw_rounds_list_widget = QtWidgets.QListWidget(self.verticalLayoutWidget_3)
        self.stopw_rounds_list_widget.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustIgnored)
        self.stopw_rounds_list_widget.setObjectName("stopw_rounds_list_widget")
        self.verticalLayout_5.addWidget(self.stopw_rounds_list_widget)
        self.verticalLayout_5.setStretch(0, 1)
        self.verticalLayout_5.setStretch(1, 5)
        self.verticalLayout_5.setStretch(3, 5)
        self.verticalLayout_5.setStretch(5, 5)
        self.verticalLayout_5.setStretch(6, 4)
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.verticalLayoutWidget_6 = QtWidgets.QWidget(self.tab_3)
        self.verticalLayoutWidget_6.setGeometry(QtCore.QRect(10, 10, 321, 431))
        self.verticalLayoutWidget_6.setObjectName("verticalLayoutWidget_6")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_6)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setContentsMargins(-1, 0, -1, 30)
        self.gridLayout.setObjectName("gridLayout")
        self.cdown_hours_label = QtWidgets.QLabel(self.verticalLayoutWidget_6)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(13)
        self.cdown_hours_label.setFont(font)
        self.cdown_hours_label.setAlignment(QtCore.Qt.AlignCenter)
        self.cdown_hours_label.setObjectName("cdown_hours_label")
        self.gridLayout.addWidget(self.cdown_hours_label, 0, 0, 1, 1)
        self.cdown_minutes_label = QtWidgets.QLabel(self.verticalLayoutWidget_6)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(13)
        self.cdown_minutes_label.setFont(font)
        self.cdown_minutes_label.setAlignment(QtCore.Qt.AlignCenter)
        self.cdown_minutes_label.setObjectName("cdown_minutes_label")
        self.gridLayout.addWidget(self.cdown_minutes_label, 0, 1, 1, 1)
        self.cdown_seconds_label = QtWidgets.QLabel(self.verticalLayoutWidget_6)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(13)
        self.cdown_seconds_label.setFont(font)
        self.cdown_seconds_label.setAlignment(QtCore.Qt.AlignCenter)
        self.cdown_seconds_label.setObjectName("cdown_seconds_label")
        self.gridLayout.addWidget(self.cdown_seconds_label, 0, 2, 1, 1)
        self.cdown_hours = QtWidgets.QSpinBox(self.verticalLayoutWidget_6)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(15)
        self.cdown_hours.setFont(font)
        self.cdown_hours.setWrapping(False)
        self.cdown_hours.setMaximum(24)
        self.cdown_hours.setObjectName("cdown_hours")
        self.gridLayout.addWidget(self.cdown_hours, 1, 0, 1, 1)
        self.cdown_minutes = QtWidgets.QSpinBox(self.verticalLayoutWidget_6)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(15)
        self.cdown_minutes.setFont(font)
        self.cdown_minutes.setWrapping(False)
        self.cdown_minutes.setMaximum(59)
        self.cdown_minutes.setObjectName("cdown_minutes")
        self.gridLayout.addWidget(self.cdown_minutes, 1, 1, 1, 1)
        self.cdown_seconds = QtWidgets.QSpinBox(self.verticalLayoutWidget_6)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(15)
        self.cdown_seconds.setFont(font)
        self.cdown_seconds.setWrapping(False)
        self.cdown_seconds.setMaximum(59)
        self.cdown_seconds.setObjectName("cdown_seconds")
        self.gridLayout.addWidget(self.cdown_seconds, 1, 2, 1, 1)
        self.verticalLayout_6.addLayout(self.gridLayout)
        self.cdown_reset_button = QtWidgets.QPushButton(self.verticalLayoutWidget_6)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(13)
        self.cdown_reset_button.setFont(font)
        self.cdown_reset_button.setObjectName("cdown_reset_button")
        self.verticalLayout_6.addWidget(self.cdown_reset_button)
        self.cdown_time_lcd = QtWidgets.QLCDNumber(self.verticalLayoutWidget_6)
        self.cdown_time_lcd.setDigitCount(8)
        self.cdown_time_lcd.setObjectName("cdown_time_lcd")
        self.verticalLayout_6.addWidget(self.cdown_time_lcd)
        self.cdown_start_button = QtWidgets.QPushButton(self.verticalLayoutWidget_6)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(13)
        self.cdown_start_button.setFont(font)
        self.cdown_start_button.setObjectName("cdown_start_button")
        self.verticalLayout_6.addWidget(self.cdown_start_button)
        self.cdown_pause_button = QtWidgets.QPushButton(self.verticalLayoutWidget_6)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(13)
        self.cdown_pause_button.setFont(font)
        self.cdown_pause_button.setObjectName("cdown_pause_button")
        self.verticalLayout_6.addWidget(self.cdown_pause_button)
        self.tabWidget.addTab(self.tab_3, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 365, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "TheTimeApp"))
        self.alarm_set.setText(_translate("MainWindow", "Добавить"))
        self.label.setText(_translate("MainWindow", "Список установленных будильников"))
        self.alarm_delete_button.setText(_translate("MainWindow", "Удалить выбранный"))
        self.alarm_clearlist_button.setText(_translate("MainWindow", "Очистить список"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Будильник"))
        self.stopw_timer_label.setText(_translate("MainWindow", "Время"))
        self.stopw_start_button.setText(_translate("MainWindow", "Старт"))
        self.stopw_pause_button.setText(_translate("MainWindow", "Пауза"))
        self.stopw_reset_button.setText(_translate("MainWindow", "Сброс"))
        self.stopw_round_button.setText(_translate("MainWindow", "Круг"))
        self.stopw_save_button.setText(_translate("MainWindow", "Сохранить запись"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Секундомер"))
        self.cdown_hours_label.setText(_translate("MainWindow", "Часы"))
        self.cdown_minutes_label.setText(_translate("MainWindow", "Минуты"))
        self.cdown_seconds_label.setText(_translate("MainWindow", "Секунды"))
        self.cdown_reset_button.setText(_translate("MainWindow", "Сброс"))
        self.cdown_start_button.setText(_translate("MainWindow", "Старт"))
        self.cdown_pause_button.setText(_translate("MainWindow", "Пауза"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "Таймер"))
