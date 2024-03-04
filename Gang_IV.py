from PyQt6.QtCore import QRect
from PyQt6.QtGui import QMouseEvent

from TemplateRoom import TemplateRoom
#test
class Ganglinks(TemplateRoom):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.init_room("Gang_IV.jpg")

        self.offset_balloon_x = int((1440 - 500) / 2)
        self.offset_balloon_y = 25
        self.offset_balloon_length = 565
        self.offset_balloon_width = 150
        self.set_offset_mouth(self.offset_balloon_x + self.offset_balloon_length, self.offset_balloon_y + self.offset_balloon_width, 0, 0)

        self.hitbox_zumRaumDigitaleTransformation = QRect(310, 185, 330, 475)
        self.append_hitbox(self.hitbox_zumRaumDigitaleTransformation)

        self.hitbox_zurFraesmaschine = QRect(980, 255, 200, 300)
        self.append_hitbox(self.hitbox_zurFraesmaschine)

        self.text_line_1 = "Herzlich willkommen! Hier geht es"
        self.text_line_2 = "zu den großen Maschinen!"
        self.text_line_3 = "Die linke Tür führt Sie zum 3D Drucker."
        self.text_line_4 = "Die rechte Tür bringt Sie zur"
        self.text_line_5 = "Fräsmaschine."
        self.text_line_6 = ""

    def mousePressEvent(self, ev: QMouseEvent) -> None:
        super(Ganglinks, self).mousePressEvent(ev)

        mouse_pos = ev.pos()
 
        if self.hitbox_zumRaumDigitaleTransformation.contains(mouse_pos):
            self.new_room.emit("Raum_digitale_Transformation.jpg")
        elif self.hitbox_zurFraesmaschine.contains(mouse_pos):
            self.new_room.emit("Fraesmaschine.jpg")
        self.update()
