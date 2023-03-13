from PyQt6.QtCore import QRect
from PyQt6.QtGui import QMouseEvent

from TemplateRoom import TemplateRoom

class Gang_II(TemplateRoom):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.init_room("Gang_II.jpg")

        self.offset_balloon_x = int((1440 - 500) / 2)
        self.offset_balloon_y = 25
        self.set_offset_mouth(self.offset_balloon_x, self.offset_balloon_y, 0, 0)

        self.hitbox_zumGang_III = QRect(1, 1, 80, 800)
        self.append_hitbox(self.hitbox_zumGang_III)

        self.hitbox_zumEG102 = QRect(115, 100, 560, 800)
        self.append_hitbox(self.hitbox_zumEG102)

        self.text_line_1 = "Greetings!"
        self.text_line_2 = ""
        self.text_line_3 = "So long, and"
        self.text_line_4 = "Thanks for the fish"

    def mousePressEvent(self, ev: QMouseEvent) -> None:
        super(Gang_II, self).mousePressEvent(ev)

        mouse_pos = ev.pos()
        print(mouse_pos)

        if self.hitbox_zumGang_III.contains(mouse_pos):
            self.new_room.emit("Gang_III.jpg")
        elif self.hitbox_zumEG102.contains(mouse_pos):
            self.new_room.emit("EG102.jpg")

        self.update()
