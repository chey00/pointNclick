from PyQt6.QtCore import QRect
from PyQt6.QtGui import QMouseEvent

from TemplateRoom import TemplateRoom

class KatzenRoom(TemplateRoom):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.init_room("KatzenRoom.jpg")

        self.offset_balloon_x = 10
        self.offset_balloon_y = 10
        self.set_offset_mouth(549, 533, 50, 150)

        self.text_line_1 = "Hallo, ich bin die"
        self.text_line_2 = "Katze!"
        self.text_line_3 = ""
        self.text_line_4 = ""
        self.text_line_5 = ""
        self.text_line_6 = "Du kannst mich streicheln oder ..."

        self.hitbox_nose = QRect(570, 475, 75, 75)
        self.append_hitbox(self.hitbox_nose)

        self.hitbox_fur = QRect(1000, 750, 200, 100)
        self.append_hitbox(self.hitbox_fur)

        self.hitbox_easter_egg = QRect(800, 400, 50, 50)

    def mousePressEvent(self, ev: QMouseEvent) -> None:
        super(KatzenRoom, self).mousePressEvent(ev)

        mouse_pos = ev.pos()

        if self.hitbox_nose.contains(mouse_pos):
            self.text_line_1 = "AUA"
            self.text_line_2 = ""
            self.text_line_3 = ""
            self.text_line_4 = ""
            self.text_line_5 = ""
            self.text_line_6 = ""
        elif self.hitbox_fur.contains(mouse_pos):
            self.text_line_1 = "MIAU"
            self.text_line_2 = ""
            self.text_line_3 = ""
            self.text_line_4 = ""
            self.text_line_5 = ""
            self.text_line_6 = "Du hast mein Fell gesteichelt!"

        self.update()
        