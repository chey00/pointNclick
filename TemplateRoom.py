from PyQt6.QtCore import QPoint, QRect, pyqtSignal, pyqtSlot
from PyQt6.QtGui import QPixmap, QMouseEvent, QPaintEvent, QPainter, QColor, QFont
from PyQt6.QtWidgets import QLabel


class TemplateRoom(QLabel):
    leave_room = pyqtSignal(str)
    found_easter_egg = pyqtSignal(str)

    def __init__(self, parent=None):
        super().__init__(parent)

        self.room_name = "katze.jpg"

        self.__hitbox_nose = QRect(310, 320, 20, 20)
        self.__hitbox_fur = QRect(500, 450, 200, 100)
        self.__hitbox_exit = QRect(10, 500, 100, 30)
        self.__hitbox_easter_egg = QRect(750, 550, 50, 50)

        self.offset_balloon_x = 10
        self.offset_balloon_y = 10
        self.offset_balloon_length = 275
        self.offset_balloon_width = 175

        self.text_line_1 = "Miau!"
        self.text_line_2 = "Ich habe Hunger"
        self.text_line_3 = ""
        self.text_line_4 = ""

        self.__mouse_pos = QPoint()

        self.__pixmap = QPixmap(self.room_name)

        self.__hitbox_visible = False

        self.setMouseTracking(True)

    def mouseMoveEvent(self, ev: QMouseEvent) -> None:
        if self.__hitbox_nose.contains(ev.pos()):
            print("drine")

    def mousePressEvent(self, ev: QMouseEvent) -> None:
        self.__mouse_pos = ev.pos()
        print(self.__mouse_pos.x(), self.__mouse_pos.y())

        if self.__hitbox_nose.contains(self.__mouse_pos):
            self.text_line_1 = "AUA"
            self.text_line_2 = ""
            self.text_line_3 = ""
            self.text_line_4 = ""
        elif self.__hitbox_fur.contains(self.__mouse_pos):
            self.text_line_1 = "MIAU"
            self.text_line_2 = ""
            self.text_line_3 = ""
            self.text_line_4 = ""
        elif self.__hitbox_exit.contains(self.__mouse_pos):
            self.leave_room.emit(self.room_name)
        elif self.__hitbox_easter_egg.contains(self.__mouse_pos):
            self.found_easter_egg.emit(self.room_name)

        self.update()

    def paintEvent(self, a0: QPaintEvent) -> None:
        painter = QPainter(self)

        painter.drawPixmap(QPoint(0, 0), self.__pixmap)

        if self.__mouse_pos:
            painter.setPen(QColor("red"))
            painter.drawEllipse(self.__mouse_pos, 10, 10)

        painter.fillRect(QRect(self.offset_balloon_x, self.offset_balloon_y, self.offset_balloon_length + 5, self.offset_balloon_width + 5), QColor("goldenrod"))
        painter.fillRect(QRect(self.offset_balloon_x + 5, self.offset_balloon_y + 5, self.offset_balloon_length, self.offset_balloon_width), QColor("gold"))

        painter.fillRect(QRect(10, 500, 100, 30), QColor("darkred"))
        painter.fillRect(QRect(15, 505, 95, 25), QColor("red"))

        font = QFont("Courier", 24)
        font.setBold(True)
        font.setItalic(True)
        painter.setFont(font)
        painter.setPen(QColor("black"))
        painter.drawText(self.offset_balloon_x + 10, self.offset_balloon_y + 25, self.text_line_1)
        painter.drawText(self.offset_balloon_x + 10, self.offset_balloon_y + 50, self.text_line_2)
        painter.drawText(self.offset_balloon_x + 10, self.offset_balloon_y + 75, self.text_line_3)
        painter.drawText(self.offset_balloon_x + 10, self.offset_balloon_y + 100, self.text_line_4)

        painter.drawText(20, 525, "Zurück")

        if self.__hitbox_visible:
            painter.setPen(QColor("green"))
            painter.drawRect(self.__hitbox_nose)
            painter.drawRect(self.__hitbox_fur)
            painter.drawRect(self.__hitbox_exit)
            painter.drawRect(self.__hitbox_easter_egg)

    @pyqtSlot(bool)
    def setHitBoxVisible(self, visible: bool):
        self.__hitbox_visible = visible

        self.update()
