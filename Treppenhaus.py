from PyQt6.QtCore import QRect
from PyQt6.QtGui import QMouseEvent

from TemplateRoom import TemplateRoom

class Treppenhaus(TemplateRoom):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.init_room("Treppenhaus.jpg")

        self.offset_balloon_x = int((1440 - 500) / 2)
        self.offset_balloon_y = 25
        self.set_offset_mouth(self.offset_balloon_x, self.offset_balloon_y, 0, 0)

        self.hitbox_zumDrucker = QRect(1, 1, 250, 800)
        self.append_hitbox(self.hitbox_zumDrucker)

        self.hitbox_zumGang_I = QRect(1440 - 251, 1, 250, 800)
        self.append_hitbox(self.hitbox_zumGang_I)

        self.text_line_1 = "Wegweiser:"
        self.text_line_2 = ""
        self.text_line_3 = ""
        self.text_line_4 = ""
        self.text_line_5 = "Links: zum 3D Drucker"
        self.text_line_6 = "Rechts: zu Projektraum/Metallraum"

    def mousePressEvent(self, ev: QMouseEvent) -> None:
        super(Treppenhaus, self).mousePressEvent(ev)

        mouse_pos = ev.pos()

        if self.hitbox_zumDrucker.contains(mouse_pos):
            pass
        elif self.hitbox_zumGang_I.contains(mouse_pos):
            self.new_room.emit("Gang_I.jpg")

        self.update()
