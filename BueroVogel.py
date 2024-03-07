from PyQt6.QtCore import QRect, QPoint
from PyQt6.QtGui import QMouseEvent

from TemplateRoom import TemplateRoom

class BueroVogel(TemplateRoom):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.init_room("BueroVogel.jpg")

        self.__counter=0

        self.offset_balloon_x = 310
        self.offset_balloon_y = 100
        self.offset_balloon_length = 475
        self.offset_balloon_width = 200

        self.set_offset_mouth(940, 390, 70, 100)

        self.hitbox_gieskanne = QRect(415, 745, 200, 100)
        self.append_hitbox(self.hitbox_gieskanne)

        self.hitbox_raumzuweisung = QRect(873, 340, 50, 35)
        self.append_hitbox(self.hitbox_raumzuweisung)

        self.hitbox_acces = QRect(820, 67, 90, 90)
        self.append_hitbox(self.hitbox_acces)

        self.hitbox_weiter = QRect(645, 230, 100, 25)
        self.append_hitbox(self.hitbox_weiter)

        self.text_line_1 = "Hallo, ich bin Frau Vogel und"
        self.text_line_2 = "hier ist mein Büro. Ich bin die"
        self.text_line_3 = "Seminarleitung im Bereich Metall"
        self.text_line_4 = "und die stellvertretende Schul-"
        self.text_line_5 = "leitung für unsere Fachschulen."
        self.text_line_6 = "                       weiter"

    def mousePressEvent(self, ev: QMouseEvent) -> None:
        super(BueroVogel, self).mousePressEvent(ev)

        mouse_pos = ev.pos()

        if self.hitbox_gieskanne.contains(mouse_pos):
            self.text_line_1 = "Das ist eine Gießkanne."
            self.text_line_2 = "Damit gießen wir unsere Pflanzen."
            self.text_line_3 = ""
            self.text_line_4 = ""
            self.text_line_5 = ""
            self.text_line_6 = "                       "
        elif self.hitbox_raumzuweisung.contains(mouse_pos):
            self.text_line_1 = "Hier ist die Raumzuweisung:"
            self.text_line_2 = "EG 105."
            self.text_line_3 = "Diese Schilder sind"
            self.text_line_4 = "an jedem Raum, um "
            self.text_line_5 = "die Orientierung zu erleichtern."
            self.text_line_6 = ""
        elif self.hitbox_acces.contains(mouse_pos):
            self.text_line_1 = "Der Access Point ist kaum zu"
            self.text_line_2 = "sehen. Dennoch sorgt er für"
            self.text_line_3 = "eine stabile Internetverbindung."
            self.text_line_4 = "Unsere Schule ist über mehrere "
            self.text_line_5 = "Glasfaserleitungen mit dem "
            self.text_line_6 = "Internet verbunden."

        elif self.hitbox_weiter.contains(mouse_pos):
            if self.__counter==0:
                self.text_line_1 = "Wenn Sie wissen wollen, wie"
                self.text_line_2 = "dieses Programm entstanden ist,"
                self.text_line_3 = "können Sie gerne im Raum"
                self.text_line_4 = "EG 101 vorbeischauen."
                self.text_line_5 = ""
                self.text_line_6 = ""

                self.__counter=1

        self.update()
