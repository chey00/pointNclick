from PyQt6.QtCore import QRect, QPoint
from PyQt6.QtGui import QMouseEvent

from TemplateRoom import TemplateRoom

class BueroVogel(TemplateRoom):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.init_room("BueroVogel.jpg")

        self.offset_balloon_x = 450
        self.offset_balloon_y = 100
        self.offset_balloon_length = 450
        self.offset_balloon_width = 200

        self.set_offset_mouth(1150, 440, 70, 100)

        self.hitbox_gieskanne = QRect(940, 810, 100, 70)
        self.append_hitbox(self.hitbox_gieskanne)

        self.hitbox_raumzuweisung = QRect(965, 390, 50, 35)
        self.append_hitbox(self.hitbox_raumzuweisung)

        self.hitbox_acces = QRect(920, 115, 60, 60)
        self.append_hitbox(self.hitbox_acces)

        self.text_line_1 = "Hallo, mein Name ist "
        self.text_line_2 = "Frau Vogel und ich stehe hier"
        self.text_line_3 = "vor meinem Büro. Ich habe die"
        self.text_line_4 = "Seminarleitung und bin die"
        self.text_line_5 = "stellvertretende"
        self.text_line_6 = "Fachschulleitung."

    def mousePressEvent(self, ev: QMouseEvent) -> None:
        super(BueroVogel, self).mousePressEvent(ev)

        mouse_pos = ev.pos()

        if self.hitbox_gieskanne.contains(mouse_pos):
            self.text_line_1 = "Hier ist Die Gießkanne"
            self.text_line_2 = ""
            self.text_line_3 = "zum Gießen der Pflanze."
            self.text_line_4 = ""
            self.text_line_5 = ""
            self.text_line_6 = ""
        elif self.hitbox_raumzuweisung.contains(mouse_pos):
            self.text_line_1 = "Hier ist Die Raumzuweisung:"
            self.text_line_2 = "EG - 105"
            self.text_line_3 = "Diese Schilder sind"
            self.text_line_4 = "an jedem Raum, um "
            self.text_line_5 = "Missverständnisse zu vermeiden."
            self.text_line_6 = ""
        elif self.hitbox_acces.contains(mouse_pos):
            self.text_line_1 = "Hier ist der Acces point zu"
            self.text_line_2 = "sehen. Er sorgt"
            self.text_line_3 = "für eine stabile"
            self.text_line_4 = "Internetverbindung und ist im"
            self.text_line_5 = "ganzen Schulhaus zu finden."
            self.text_line_6 = ""

        self.update()
