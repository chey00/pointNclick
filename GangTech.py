from PyQt6.QtCore import QRect
from PyQt6.QtGui import QMouseEvent

from TemplateRoom import TemplateRoom

class GangTech(TemplateRoom):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.init_room("GangTech.jpg")

        self.offset_balloon_x = int((1440 - 500) / 2)
        self.offset_balloon_y = 25
        self.set_offset_mouth(self.offset_balloon_x, self.offset_balloon_y, 0, 0)

        self.hitbox_zumGang_II = QRect(1, 1, 250, 800)
        self.append_hitbox(self.hitbox_zumGang_II)

        self.hitbox_zumEG101 = QRect(715, 200, 360, 630)
        self.append_hitbox(self.hitbox_zumEG101)

        self.text_line_1 = "Greetings!"
        self.text_line_2 = ""
        self.text_line_3 = "So long, and"
        self.text_line_4 = "Thanks for the fish"

    def mousePressEvent(self, ev: QMouseEvent) -> None:
        super(GangTech, self).mousePressEvent(ev)

        mouse_pos = ev.pos()
        print(mouse_pos)

        if self.hitbox_zumGang_II.contains(mouse_pos):
            self.new_room.emit("Gang_II.jpg")
        elif self.hitbox_zumEG101.contains(mouse_pos):
            pass
        self.update()
