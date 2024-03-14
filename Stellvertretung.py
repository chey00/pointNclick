from PyQt6.QtCore import QRect, Qt
from PyQt6.QtGui import QMouseEvent

from TemplateRoom import TemplateRoom


class Stellvertretung(TemplateRoom):
    def __init__(self, parent=None):
        super(Stellvertretung, self).__init__(parent)

        self.init_room("Stellvertretung.jpg")

        self.offset_balloon_x = 600
        self.offset_balloon_y = 25
        self.offset_balloon_width = 160
        self.offset_balloon_length = 500
        self.set_offset_mouth(1000, 475, 50, 50)

        self.hitbox_forward = QRect(975, 150, 125, 50)
        self.append_hitbox(self.hitbox_forward)

        self.__counter = 0

        self.hitbox_easter_egg = QRect(960, 696, 75, 109)

        self.text_line_1 = "Hallo, ich bin Frau Körber."
        self.text_line_2 = "Schön, dass Sie hier sind!"
        self.text_line_3 = "Hier sitze ich als "
        self.text_line_4 = "stellvertretende Schulleiterin."
        self.text_line_5 = "Schauen Sie sich gerne etwas um."
        self.text_line_6 = "                           weiter"

    def mousePressEvent(self, ev: QMouseEvent) -> None:
        super(Stellvertretung, self).mousePressEvent(ev)

        mouse_pos = ev.pos()

        if self.hitbox_easter_egg.contains(mouse_pos):
            self.text_line_1 = ""
            self.text_line_2 = ""
            self.text_line_3 = "Für einen guten Start in den Tag"
            self.text_line_4 = "ist Kaffee unerlässlich!"
            self.text_line_5 = ""
            self.text_line_6 = ""

            self.play_sound("TemplateRoom.mp3")

            self.update()

        if self.hitbox_forward.contains(mouse_pos):
            if self.__counter == 0:
                self.text_line_1 = ""
                self.text_line_2 = "Sie wollen wissen, welche"
                self.text_line_3 = "Fächer ich an der Fachschule"
                self.text_line_4 = "unterrichte?"
                self.text_line_5 = ""
                self.text_line_6 = "                           weiter"

            elif self.__counter == 1:
                self.text_line_1 = ""
                self.text_line_2 = "Hauptsächlich bin ich für"
                self.text_line_3 = "das Fach Betriebswirtschaft"
                self.text_line_4 = "zuständig."
                self.text_line_5 = ""
                self.text_line_6 = "                           weiter"

            elif self.__counter == 2:
                self.text_line_1 = "Ich hoffe, Ihnen gefällt unser"
                self.text_line_2 = "Tag der offenen Tür bisher?"
                self.text_line_3 = "Schauen Sie sich gerne noch"
                self.text_line_4 = "in den anderen Räumen weiter um."
                self.text_line_5 = ""
                self.text_line_6 = "                           weiter"

            elif self.__counter == 3:
                self.text_line_1 = ""
                self.text_line_2 = ""
                self.text_line_3 = "Auf Wiedersehen und noch einen"
                self.text_line_4 = "schönen Tag!"
                self.text_line_5 = ""
                self.text_line_6 = ""

            self.__counter += 1

            self.update()
