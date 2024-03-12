from PyQt6.QtCore import QRect, QPoint
from PyQt6.QtGui import QMouseEvent, QPixmap, QPaintEvent, QPainter

from TemplateRoom import TemplateRoom


class Verwaltung(TemplateRoom):
    def __init__(self, parent=None):
        super(Verwaltung, self).__init__(parent)

        self.init_room("Verwaltung.jpg")

        self.offset_balloon_x = 550
        self.offset_balloon_y = 200
        self.offset_balloon_length = 550
        self.offset_balloon_width = 200
        self.set_offset_mouth(502, 484, 50, 150)

        self.hitbox_mouth = QRect(950, 320, 150, 50)
        self.append_hitbox(self.hitbox_mouth)

        self.hitbox_unterlagen = QRect(640, 680, 190, 140)
        self.append_hitbox(self.hitbox_unterlagen)

        self.hitbox_computer = QRect(700, 435, 110, 120)
        self.append_hitbox(self.hitbox_computer)

        self.hitbox_zumStvRoom = QRect(1340, 1, 99, 800)
        self.append_hitbox(self.hitbox_zumStvRoom)

        self.hitbox_zumOSTD = QRect(1, 1, 99, 800)
        self.append_hitbox(self.hitbox_zumOSTD)

        self.text_line_1 = "Herzlich Willkommen in der"
        self.text_line_2 = "Verwaltung!"
        self.text_line_3 = ""
        self.text_line_4 = "Ich bin Frau Del Popolo."
        self.text_line_5 = "Wie kann ich Ihnen behilflich"
        self.text_line_6 = "sein?                         Weiter"

        self.__show_qr = False
        self.__pixmap = QPixmap("QR-Code.png")

    def mousePressEvent(self, ev: QMouseEvent) -> None:
        super(Verwaltung, self).mousePressEvent(ev)

        mouse_pos = ev.pos()

        if self.hitbox_mouth.contains(mouse_pos):
            self.text_line_1 = "Sie brauchen eine Schulbescheinigung"
            self.text_line_2 = "für Ihre Krankenkasse?"
            self.text_line_3 = ""
            self.text_line_4 = "Gerne, da kann ich Ihnen helfen!"
            self.text_line_5 = "Sie können diese in der nächsten"
            self.text_line_6 = "Pause abholen."

            self.update()

        elif self.hitbox_unterlagen.contains(mouse_pos):
            self.text_line_6 = " "
            self.text_line_1 = "Nein das sind nicht Ihre Unterlagen."
            self.text_line_2 = "Mensch, Finger weg!"
            self.text_line_3 = "Warten Sie kurz... ah, hier."
            self.text_line_4 = "Bitteschön, Ihre Unterlagen sind"
            self.text_line_5 = "hier."
            self.text_line_6 = "Haben Sie noch einen Wunsch?"

            self.update()

        elif self.hitbox_computer.contains(mouse_pos):
            self.text_line_1 = "Für Sie zur Info: Sie haben auch die"
            self.text_line_2 = "Möglichkeit Ihre Unterlagen online"
            self.text_line_3 = "zu beantragen. Unsere Website:"
            self.text_line_4 = ""
            self.text_line_5 = "www.sbs-herzogenaurach.de"
            self.text_line_6 = ""

            self.__show_qr = True

        elif self.hitbox_zumStvRoom.contains(mouse_pos):
            self.new_room.emit("Stellvertretung.jpg")
        elif self.hitbox_zumOSTD.contains(mouse_pos):
            self.new_room.emit("Schulleitung.jpg")

        self.update()

    def paintEvent(self, a0: QPaintEvent) -> None:
        super(Verwaltung, self).paintEvent(a0)

        painter = QPainter()
        painter.begin(self)

        if self.__show_qr:
            painter.drawPixmap(25, 25, self.__pixmap)

            self.__show_qr = False

        painter.end()
