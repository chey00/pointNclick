from PyQt6.QtCore import QRect
from PyQt6.QtGui import QMouseEvent

from TemplateRoom import TemplateRoom

class Wegweiser(TemplateRoom):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.init_room("Wegweiser.jpg")

        self.offset_balloon_x = 639
        self.offset_balloon_y = 10
        self.offset_balloon_length = 550
        self.offset_balloon_width = 150

        self.set_offset_mouth(717, 498, 50, 150)

        self.hitbox_zumTreppenhaus = QRect(1, 1, 250, 800)
        self.append_hitbox(self.hitbox_zumTreppenhaus)

        self.hitbox_zumGangTech = QRect(1440-251, 1, 250, 800)
        self.append_hitbox(self.hitbox_zumGangTech)

        self.hitbox_mouth = QRect(661, 442, 60, 75)
        self. append_hitbox(self.hitbox_mouth)

        self.text_line_1 = "Hallo, ich bin Frau Körber."
        self.text_line_2 = "Ich bin die stellvertretende"
        self.text_line_3 = "Schulleiterin."
        self.text_line_4 = "In der FSWI-2 unterrichte ich"
        self.text_line_5 = "Betriebswirtschaftliche Fächer."
        self.text_line_6 = ""

    def mousePressEvent(self, ev: QMouseEvent) -> None:
        super(Wegweiser, self).mousePressEvent(ev)

        mouse_pos = ev.pos()
        print(mouse_pos)

        if self.hitbox_zumTreppenhaus.contains(mouse_pos):
            self.new_room.emit("Treppenhaus.jpg")
        elif self.hitbox_zumGangTech.contains(mouse_pos):
            self.new_room.emit("GangTech.jpg")
        elif self.hitbox_mouth.contains(mouse_pos):
            self.text_line_1 = ""
            self.text_line_2 = "Links geht es zum Treppenhaus,"
            self.text_line_3 = "rechts geht es zu den Unterrichts-"
            self.text_line_4 = "räumen der Fachschulen."
            self.text_line_5 = ""
            self.text_line_6 = ""
        self.update()


