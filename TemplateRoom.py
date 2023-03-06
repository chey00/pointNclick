from PyQt6.QtCore import QPoint, QRect, pyqtSignal, pyqtSlot, QSize, Qt
from PyQt6.QtGui import QPixmap, QMouseEvent, QPaintEvent, QPainter, QColor, QFont
from PyQt6.QtWidgets import QLabel


class TemplateRoom(QLabel):
    leave_room = pyqtSignal(str)
    found_easter_egg = pyqtSignal(str)

    def __init__(self, parent=None):
        super().__init__(parent)
        self.__room_name = None
        self.__background_pixmap = None

        self.__size = QSize(1440, 900)
        self.__offset_exit = 10
        self.__heigth_box = 30

        self.__hitboxes = list()
        self.__hitbox_visible = False

        self.text_line_1 = None
        self.text_line_2 = None
        self.text_line_3 = None
        self.text_line_4 = None
        self.text_line_5 = None
        self.text_line_6 = None

        self.__mouse_pos = QPoint()

        self.__offset_balloon_length = 500
        self.__offset_balloon_width = 150

        self.hitbox_exit = QRect()
        self.append_hitbox(self.hitbox_exit)

        self.hitbox_easter_egg = QRect(0,0,0,0)
        self.setMouseTracking(True)
        self.setCursor(Qt.CursorShape.CrossCursor)

    def mouseMoveEvent(self, ev: QMouseEvent) -> None:
        for hitbox in self.__hitboxes:
            if hitbox.contains(ev.pos()):
                if self.cursor().shape() != Qt.CursorShape.PointingHandCursor:
                    self.setCursor(Qt.CursorShape.PointingHandCursor)

                return

        if self.cursor().shape() != Qt.CursorShape.CrossCursor:
            self.setCursor(Qt.CursorShape.CrossCursor)

    def mousePressEvent(self, ev: QMouseEvent) -> None:
        self.__mouse_pos = ev.pos()

        if self.hitbox_exit.contains(self.__mouse_pos):
            self.leave_room.emit(self.__room_name)
        elif self.hitbox_easter_egg.contains(self.__mouse_pos):
            self.found_easter_egg.emit(self.__room_name)

    def paintEvent(self, a0: QPaintEvent) -> None:
        painter = QPainter(self)

        painter.drawPixmap(QPoint(0, 0), self.__background_pixmap)

        if self.__mouse_pos:
            painter.setPen(QColor("red"))
            painter.drawEllipse(self.__mouse_pos, 10, 10)

        painter.fillRect(QRect(self.offset_balloon_x, self.offset_balloon_y, self.__offset_balloon_length + 5, self.__offset_balloon_width + 5), QColor("goldenrod"))
        painter.fillRect(QRect(self.offset_balloon_x + 5, self.offset_balloon_y + 5, self.__offset_balloon_length, self.__offset_balloon_width), QColor("gold"))

        painter.fillRect(QRect(self.__offset_exit, self.__pos_x_exit, 100, self.__heigth_box), QColor("darkred"))
        painter.fillRect(QRect(self.__offset_exit + 5, self.__pos_x_exit + 5, 95, self.__heigth_box - 5), QColor("red"))

        font = QFont("Courier", 24)
        font.setBold(True)
        font.setItalic(True)
        painter.setFont(font)
        painter.setPen(QColor("black"))
        painter.drawText(self.offset_balloon_x + 10, self.offset_balloon_y + 25, self.text_line_1)
        painter.drawText(self.offset_balloon_x + 10, self.offset_balloon_y + 50, self.text_line_2)
        painter.drawText(self.offset_balloon_x + 10, self.offset_balloon_y + 75, self.text_line_3)
        painter.drawText(self.offset_balloon_x + 10, self.offset_balloon_y + 100, self.text_line_4)
        painter.drawText(self.offset_balloon_x + 10, self.offset_balloon_y + 125, self.text_line_5)
        painter.drawText(self.offset_balloon_x + 10, self.offset_balloon_y + 150, self.text_line_6)

        painter.drawText(self.__offset_exit + 10, self.__pos_x_exit + 25, "Zurück")

        if self.__hitbox_visible:
            painter.setPen(QColor("red"))
            for hitbox in self.__hitboxes:
                painter.drawRect(hitbox)

            if self.hitbox_easter_egg:
                painter.drawRect(hitbox)

    @pyqtSlot(bool)
    def setHitBoxVisible(self, visible: bool):
        self.__hitbox_visible = visible

        self.update()

    def init_room(self, room_name):
        self.__room_name = room_name
        self.__background_pixmap = QPixmap(self.__room_name).scaled(self.__size.width(), self.__size.height())

        self.__pos_x_exit = self.__size.height() - self.__offset_exit - self.__heigth_box - 30
        self.hitbox_exit = QRect(self.__offset_exit, self.__pos_x_exit, 100, self.__heigth_box)

    def append_hitbox(self, hitbox):
        self.__hitboxes.append(hitbox)
