from PyQt6.QtCore import QRect
from PyQt6.QtGui import QMouseEvent

from TemplateRoom import TemplateRoom

class Gang_I(TemplateRoom):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.init_room("Gang_I.jpg")

        self.offset_balloon_x = int((1440 - 500) / 2)
        self.offset_balloon_y = 25
        self.set_offset_mouth(self.offset_balloon_x, self.offset_balloon_y, 0, 0)

        self.hitbox_zumProjekt = QRect(440, 350, 35, 180)
        self.append_hitbox(self.hitbox_zumProjekt)

        self.hitbox_zumMetall = QRect(255, 345, 120, 150)
        self.append_hitbox(self.hitbox_zumMetall)

        self.text_line_1 = "Greetings!"
        self.text_line_2 = ""
        self.text_line_3 = "So long, and"
        self.text_line_4 = "Thanks for the fish"

    def mousePressEvent(self, ev: QMouseEvent) -> None:
        super(Gang_I, self).mousePressEvent(ev)

        mouse_pos = ev.pos()
        print(mouse_pos)

        if self.hitbox_zumProjekt.contains(mouse_pos):
            pass
        elif self.hitbox_zumMetall.contains(mouse_pos):
            self.new_room.emit("Fraesmaschine.jpg")

        self.update()
