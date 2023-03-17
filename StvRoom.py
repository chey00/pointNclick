from PyQt6.QtCore import QRect, Qt
from PyQt6.QtGui import QMouseEvent

from TemplateRoom import TemplateRoom

class StvRoom(TemplateRoom):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.init_room("StvRoom.jpg")

        self.offset_balloon_x = 830
        self.offset_balloon_y = 15
        self.offset_balloon_width = 160
        self.offset_balloon_length = 500
        self.set_offset_mouth(730, 245, 50, 150)

        self.hitbox_forward = QRect(1225, 145, 100, 25)
        self.append_hitbox(self.hitbox_forward)

        self.__counter = 0

        self.hitbox_stift = QRect(965, 580, 75, 75)
        self.append_hitbox(self.hitbox_stift)

        self.hitbox_easter_egg = QRect(800, 590, 75, 109)

        self.text_line_1 = "Hallo, ich bin Herr Gumbmann."
        self.text_line_2 = "Schön, dass Sie hier sind!"
        self.text_line_3 = "Hier stehe ich als "
        self.text_line_4 = "stellvertretender Schulleiter."
        self.text_line_5 = "Schauen Sie sich gerne etwas um."
        self.text_line_6 = "                           weiter"

    def mousePressEvent(self, ev: QMouseEvent) -> None:
        super(StvRoom, self).mousePressEvent(ev)

        mouse_pos = ev.pos()

        if self.hitbox_easter_egg.contains(mouse_pos):
            self.text_line_1 = ""
            self.text_line_2 = ""
            self.text_line_3 = "Für einen guten Start in"
            self.text_line_4 = "den Tag, ist Kaffee unerlässlich!"
            self.text_line_5 = ""
            self.text_line_6 = ""

            self.play_sound("foundcup.mp3")

            self.update()

        if self.hitbox_stift.contains(mouse_pos):
            self.text_line_1 = "Den Kugelschreiber brauchen"
            self.text_line_2 = "Sie an dieser Schule eher"
            self.text_line_3 = "selten. Sie bekommen ein "
            self.text_line_4 = "iPad samt Apple Pen. Nur"
            self.text_line_5 = "Leistungsnachweise werden noch"
            self.text_line_6 = "größtenteils per Hand geschrieben."

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
                self.text_line_3 = "das Fach Programmieren"
                self.text_line_4 = "zuständig."
                self.text_line_5 = ""
                self.text_line_6 = "                           weiter"

            elif self.__counter == 2:
                self.text_line_1 = "Ich hoffe, Ihnen gefällt unser"
                self.text_line_2 = "Tag der offenen Tür bisher?"
                self.text_line_3 = "Schauen Sie sich gerne noch"
                self.text_line_4 = "in den anderen Räumen weiter um."
                self.text_line_5 = ""
                self.text_line_6 = "                          weiter"

            elif self.__counter == 3:
                self.text_line_1 = ""
                self.text_line_2 = ""
                self.text_line_3 = "Auf Wiedersehen und noch einen"
                self.text_line_4 = "schönen Tag!"
                self.text_line_5 = ""
                self.text_line_6 = ""

            self.__counter += 1

            self.update()
