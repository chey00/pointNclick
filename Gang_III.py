from PyQt6.QtCore import QRect
from PyQt6.QtGui import QMouseEvent

from TemplateRoom import TemplateRoom


class Gang_III(TemplateRoom):
    def __init__(self, parent=None):
        super(Gang_III, self).__init__(parent)

        self.init_room("Gang_III.jpg")

        self.offset_balloon_x = int((1440 - 500) / 2)
        self.offset_balloon_y = 25
        self.set_offset_mouth(self.offset_balloon_x, self.offset_balloon_y, 0, 0)

        self.hitbox_zuHerrnBeck = QRect(185, 250, 270, 550)
        self.append_hitbox(self.hitbox_zuHerrnBeck)

        self.hitbox_zuFrauVogel = QRect(1030, 260, 250, 530)
        self.append_hitbox(self.hitbox_zuFrauVogel)
        self.text_line_1 = "Greetings!"
        self.text_line_2 = ""
        self.text_line_3 = "So long, and"
        self.text_line_4 = "Thanks for the fish"

        self.show_speech_bubble(False)

    def mousePressEvent(self, ev: QMouseEvent) -> None:
        super(Gang_III, self).mousePressEvent(ev)

        mouse_pos = ev.pos()
 
        if self.hitbox_zuHerrnBeck.contains(mouse_pos):
            self.new_room.emit("Beck.png")
        elif self.hitbox_zuFrauVogel.contains(mouse_pos):
            self.new_room.emit("Vogel.jpg")

        self.update()
