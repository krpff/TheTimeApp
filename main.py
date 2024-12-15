import datetime
import sys
import sqlite3

from PyQt5 import uic, QtCore, QtMultimedia
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QFileDialog
from PyQt5.QtCore import QTime, QTimer
from PyQt5.QtGui import QIcon
from datetime import timedelta
import time


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        uic.loadUi('data/designed.ui', self)
        self.setWindowIcon(QIcon('data/icon.png'))
        # DB connecting
        self.con = sqlite3.connect("data/TheTimeAppDB.db")
        self.cur = self.con.cursor()

        # Alarm and Timer ringtone
        self.load_mp3('data/alarm.mp3')
        # Countdown
        self.cdown_timer = QTimer()
        self.cdown_time_lcd.display("00:00:00")
        self.cdown_start_button.clicked.connect(self.cdown_start)
        self.cdown_pause_button.clicked.connect(self.cdown_pause)
        self.cdown_paused = False
        self.cdown_reset_button.clicked.connect(self.cdown_reset)
        self.cdown_timer.timeout.connect(self.cdown_update)
        self.cdown_preset_1.clicked.connect(self.cdown_set_from_preset)
        self.cdown_preset_2.clicked.connect(self.cdown_set_from_preset)
        self.cdown_preset_3.clicked.connect(self.cdown_set_from_preset)
        self.cdown_set_preset()

        # Stopwatch
        self.stopw_timer = QTimer()
        self.stopw_start_button.clicked.connect(self.stopw_start)
        self.stopw_reset_button.clicked.connect(self.stopw_reset)
        self.stopw_pause_button.clicked.connect(self.stopw_pause)
        self.stopw_save_button.clicked.connect(self.stopw_save)
        self.stopw_paused = False
        self.stopw_timer.timeout.connect(self.stopw_update)
        self.stopw_round_button.clicked.connect(self.stopw_round)
        self.stopw_round_points = [0]
        self.stopw_rounds_list = []
        self.stopw_rounds_count = 0
        self.stopw_csv_prepare = ['N;Время в с;Время\n']

        # Alarm
        self.alarm_set.clicked.connect(self.alarm_add)
        self.alarm_delete_button.clicked.connect(self.alarm_del)
        self.alarm_clearlist_button.clicked.connect(self.alarm_clear)
        self.alarms = []
        self.alarm_get()
        self.alarm_timer = QTimer()
        self.alarm_timer.timeout.connect(self.alarm_work)
        self.alarm_timer.start(30000)


    # Countdown - Таймер
    def cdown_pause(self):
        if not self.cdown_paused:
            self.cdown_timer.stop()
            self.cdown_pause_button.setText("Продолжить")
            self.cdown_paused = True
        else:
            self.cdown_timer.start(1000)
            self.cdown_pause_button.setText("Пауза")
            self.cdown_paused = False

    def cdown_reset(self):
        self.cdown_timer.stop()
        self.cdown_time_lcd.display("00:00:00")
        self.cdown_hours.setValue(0)
        self.cdown_minutes.setValue(0)
        self.cdown_seconds.setValue(0)
        self.cdown_sec = 1

    def cdown_start(self):
        start_hours = int(self.cdown_hours.text())
        start_minutes = int(self.cdown_minutes.text())
        start_seconds = int(self.cdown_seconds.text())

        if start_hours == 24 and (start_minutes > 0 or start_seconds > 0):
            self.show_warning_messagebox("Таймер ограничен 24 часами")
            return

        self.cdown_sec = 0
        self.cdown_sec = start_hours * 3600 + start_minutes * 60 + start_seconds

        if self.cdown_sec == 0:
            self.show_warning_messagebox("Введите время больше 0")
            return

        self.cdown_time_lcd.display(str(timedelta(seconds=self.cdown_sec)))

        self.cdown_timer.start(1000)

    def cdown_update(self):
        self.cdown_sec -= 1
        self.cdown_time_lcd.display(str(timedelta(seconds=self.cdown_sec)))
        if self.cdown_sec == 0:
            self.cdown_timer.stop()
            self.player.play()
            self.show_info_messagebox("Время вышло")

    def cdown_set_preset(self):
        result = self.cur.execute("""SELECT time FROM cdown_preset""").fetchall()
        self.cdown_preset_1.setText(f'{result[0][0]} минут')
        self.cdown_preset_2.setText(f'{result[1][0]} минут')
        self.cdown_preset_3.setText(f'{result[2][0]} минут')

    def cdown_set_from_preset(self):
        minutes = int(self.sender().text().split()[0])
        self.cdown_minutes.setValue(minutes)

    # Stopwatch - Секундомер
    def stopw_pause(self):
        if not self.stopw_paused:
            self.stopw_timer.stop()
            self.stopw_pause_button.setText("Продолжить")
            self.stopw_paused = True
        else:
            self.stopw_timer.start(100)
            self.stopw_pause_button.setText("Пауза")
            self.stopw_paused = False

    def stopw_reset(self):
        self.stopw_timer.stop()
        self.stopw_sec = 0
        self.stopw_timer_label.setText("Время")
        self.stopw_pause_button.setText("Пауза")
        self.stopw_paused = False
        self.stopw_round_points = [0]
        self.stopw_rounds_list = []
        self.stopw_rounds_list_widget.clear()
        self.stopw_rounds_count = 0

    def stopw_start(self):
        self.stopw_sec = 0
        self.stopw_timer_label.setText(
            str(timedelta(milliseconds=self.stopw_sec))[:9])
        self.stopw_timer.start(100)

    def stopw_update(self):
        self.stopw_sec += 100
        self.stopw_timer_label.setText(
            str(timedelta(milliseconds=self.stopw_sec))[:9])

    def stopw_round(self):
        # print(str(timedelta(milliseconds=self.stopw_sec))[:9])
        self.stopw_round_points.append(self.stopw_sec)
        self.stopw_rounds_count += 1
        self.stopw_rounds_list.append((
                                              self.stopw_round_points[
                                                  self.stopw_rounds_count] -
                                              self.stopw_round_points[
                                                  self.stopw_rounds_count - 1]) / 1000)
        # print(self.stopw_rounds_list)
        self.stopw_rounds_list_widget.addItem(
            f"{self.stopw_rounds_count}. "
            f"{self.stopw_rounds_list[-1]}s   "
            f"{str(timedelta(seconds=self.stopw_rounds_list[-1]))[:9]}")
        self.stopw_csv_prepare.append(
            f"{self.stopw_rounds_count};"
            f"{self.stopw_rounds_list[-1]};"
            f"{str(timedelta(seconds=self.stopw_rounds_list[-1]))[:9]} \n")
        # print(self.stopw_csv_prepare)

    def stopw_save(self):
        if self.stopw_paused == False:
            self.stopw_pause()
        fileName = self.saveFileDialog()
        file = open(fileName, "w")
        file.writelines(self.stopw_csv_prepare)

    # Alarm - Будильник
    def alarm_add(self):
        self.alarms.append(self.alarm_time.time().toString()[:5])
        self.cur.execute(f"""INSERT INTO alarms(stime) VALUES ('{self.alarm_time.time().toString()[:5]}')""")
        self.con.commit()
        self.alarm_get()
        # print(QTime.currentTime().toString()[:5])

    def alarm_get(self):
        self.alarm_list_widget.clear()
        self.alarms.clear()
        result = self.cur.execute("""SELECT * FROM alarms""").fetchall()
        for row in result:
            self.alarms.append(row[0])
            self.alarm_list_widget.addItem(row[0])

    def alarm_work(self):
        for i in self.alarms:
            if i == QTime.currentTime().toString()[:5]:
                self.player.play()
                time.sleep(2)
                self.show_info_messagebox(f"Будильник на {i} сработал!")

    def alarm_del(self):
        t = self.alarm_list_widget.item(self.alarm_list_widget.currentRow()).text()
        self.cur.execute(f"""DELETE FROM alarms WHERE stime = '{t}'""")
        self.con.commit()
        self.alarm_get()
        self.alarm_list_widget.takeItem(self.alarm_list_widget.currentRow())

    def alarm_clear(self):
        self.cur.execute("""DELETE FROM alarms""")
        self.con.commit()
        self.alarm_get()

    # Загрузка плеера для рингтона
    def load_mp3(self, filename):
        media = QtCore.QUrl.fromLocalFile(filename)
        content = QtMultimedia.QMediaContent(media)
        self.player = QtMultimedia.QMediaPlayer()
        self.player.setMedia(content)

    # Вспомогательные функции с активацией всплывающих окон
    def show_warning_messagebox(self, s):
        warn = QMessageBox()
        warn.setIcon(QMessageBox.Warning)
        warn.setText(s)
        warn.setWindowTitle("Ошибка")
        warn.setStandardButtons(QMessageBox.Ok)
        retval = warn.exec_()

    def show_info_messagebox(self, s):
        info = QMessageBox()
        info.setIcon(QMessageBox.Information)
        info.setText(s)
        info.setWindowTitle("Инфо")
        info.setStandardButtons(QMessageBox.Ok)
        retval = info.exec_()

    def saveFileDialog(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, fileFormat = QFileDialog.getSaveFileName(self, "QFileDialog"
                                                                 ".getSaveFileName()",
                                                           "", ".csv;;.txt",
                                                           options=options)
        if fileName:
            return f"{fileName}{fileFormat}"


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec_()
