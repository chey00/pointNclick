from PyQt6.QtCore import QRect
from PyQt6.QtGui import QMouseEvent

from TemplateRoom import TemplateRoom


class Gang_IV(TemplateRoom):
    def __init__(self, parent=None):
        super(Gang_IV, self).__init__(parent)

        self.init_room("Gang_IV.jpg")

        self.offset_balloon_x = int((1440 - 500) / 2)
        self.offset_balloon_y = 25
        self.offset_balloon_length = 565
        self.offset_balloon_width = 150
        self.set_offset_mouth(self.offset_balloon_x + self.offset_balloon_length, self.offset_balloon_y + self.offset_balloon_width, 0, 0)

        self.hitbox_zumRaumDigitaleTransformation = QRect(225, 225, 300, 500)
        self.append_hitbox(self.hitbox_zumRaumDigitaleTransformation)

        self.hitbox_zurFraesmaschine = QRect(625, 350, 125, 200)
        self.append_hitbox(self.hitbox_zurFraesmaschine)

        self.hitbox_zumMetal3DDrucker = QRect(1025, 225, 225, 550)
        self.append_hitbox(self.hitbox_zumMetal3DDrucker)

        self.text_line_1 = "Hier geht es zu den großen Maschinen!"
        self.text_line_2 = "Rechts geht es zum Metall-3D-Drucker."
        self.text_line_3 = "Die linke Tür bringt Sie zum"
        self.text_line_4 = "Raum der digitalen Transformation"
        self.text_line_5 = "Gerade aus geht es zu den Fräsmaschinen "
        self.text_line_6 = ""

    def mousePressEvent(self, ev: QMouseEvent) -> None:
        super(Gang_IV, self).mousePressEvent(ev)

        mouse_pos = ev.pos()
 
        if self.hitbox_zumRaumDigitaleTransformation.contains(mouse_pos):
            self.new_room.emit("Raum_digitale_Transformation.jpg")
        elif self.hitbox_zurFraesmaschine.contains(mouse_pos):
            self.new_room.emit("Fraesmaschine.jpg")
        elif self.hitbox_zumMetal3DDrucker.contains(mouse_pos):
            self.new_room.emit("DreiDDruck_Normal.jpg")

        #self.update()
