from PyQt6.QtCore import QRect, QPoint
from PyQt6.QtGui import QMouseEvent

from TemplateRoom import TemplateRoom

class BueroVogel(TemplateRoom):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.init_room("BueroVogel2.jpg")

        self.__counter=0

        self.offset_balloon_x = 450
        self.offset_balloon_y = 100
        self.offset_balloon_length = 475
        self.offset_balloon_width = 200

        self.set_offset_mouth(1150, 440, 70, 100)

        self.hitbox_gieskanne = QRect(940, 810, 100, 70)
        self.append_hitbox(self.hitbox_gieskanne)

        self.hitbox_raumzuweisung = QRect(970, 403, 50, 35)
        self.append_hitbox(self.hitbox_raumzuweisung)

        self.hitbox_acces = QRect(925, 130, 62, 62)
        self.append_hitbox(self.hitbox_acces)

        self.hitbox_weiter = QRect(783, 230, 100, 25)
        self.append_hitbox(self.hitbox_weiter)

        self.text_line_1 = "Hallo, ich stehe hier vor dem"
        self.text_line_2 = "Büro von Frau Vogel. Wenn Sie "
        self.text_line_3 = "sehen wollen wie das Programm"
        self.text_line_4 = "mit dem Bild von Frau Vogel"
        self.text_line_5 = "entsteht, können Sie im Raum"
        self.text_line_6 = "EG 101 gerne zusehen.  weiter"

    def mousePressEvent(self, ev: QMouseEvent) -> None:
        super(BueroVogel, self).mousePressEvent(ev)

        mouse_pos = ev.pos()

        if self.hitbox_gieskanne.contains(mouse_pos):
            self.text_line_1 = "Das ist eine Gießkanne"
            self.text_line_2 = ""
            self.text_line_3 = ""
            self.text_line_4 = ""
            self.text_line_5 = ""
            self.text_line_6 = "                       "
        elif self.hitbox_raumzuweisung.contains(mouse_pos):
            self.text_line_1 = "Hier ist Die Raumzuweisung:"
            self.text_line_2 = "EG-105."
            self.text_line_3 = "Diese Schilder sind"
            self.text_line_4 = "an jedem Raum, um "
            self.text_line_5 = "Missverständnisse zu vermeiden."
            self.text_line_6 = ""
        elif self.hitbox_acces.contains(mouse_pos):
            self.text_line_1 = "Der Access Point ist kaum zu"
            self.text_line_2 = "sehen. Dennoch sorgt er für"
            self.text_line_3 = "eine stabile Internetverbindung."
            self.text_line_4 = ""
            self.text_line_5 = "Unsere Schule ist mit mehreren"
            self.text_line_6 = "Glasfaserleitungen im Internet."
        elif self.hitbox_weiter.contains(mouse_pos):
            if self.__counter==0:
                self.text_line_1 = "Frau Vogel hat die Seminar-"
                self.text_line_2 = "leitung Metall und ist die"
                self.text_line_3 = "stellvertretende Schulleitung"
                self.text_line_4 = "für unsere Fachschulen."
                self.text_line_5 = ""
                self.text_line_6 = ""

                self.__counter=1

        self.update()
