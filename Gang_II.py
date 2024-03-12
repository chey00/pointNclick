from PyQt6.QtCore import QRect
from PyQt6.QtGui import QMouseEvent

from TemplateRoom import TemplateRoom


class Gang_II(TemplateRoom):
    def __init__(self, parent=None):
        super(Gang_II, self).__init__(parent)

        self.init_room("Gang_II.jpg")

        self.offset_balloon_x = int((1440 - 500) / 2)
        self.offset_balloon_y = 25
        self.set_offset_mouth(self.offset_balloon_x + self.offset_balloon_length, self.offset_balloon_y +
                              self.offset_balloon_width, 0, 0)

        self.hitbox_zumGang_III = QRect(1, 1, 80, 800)
        self.append_hitbox(self.hitbox_zumGang_III)

        self.hitbox_zumEG102 = QRect(115, 100, 560, 800)
        self.append_hitbox(self.hitbox_zumEG102)

        self.hitbox_bilder = QRect(1150, 225, 200, 150)
        self.append_hitbox(self.hitbox_bilder)

        self.text_line_1 = "Hier ist die FSWI-2 zuhause."
        self.text_line_2 = ""
        self.text_line_3 = "Sprich Freund und tritt ein."
        self.text_line_4 = ""

    def mousePressEvent(self, ev: QMouseEvent) -> None:
        super(Gang_II, self).mousePressEvent(ev)

        mouse_pos = ev.pos()

        if self.hitbox_zumGang_III.contains(mouse_pos):
            self.new_room.emit("Gang_III.jpg")
        elif self.hitbox_zumEG102.contains(mouse_pos):
            self.new_room.emit("Erasmus.jpg")
        elif self.hitbox_bilder.contains(mouse_pos):
            self.text_line_1 = "Du hast die Bilder von den"
            self.text_line_2 = "erfolgreichen Jahrgängen vor"
            self.text_line_3 = "uns gefunden."
            self.text_line_4 = "Sehen wir dein Bild in"
            self.text_line_5 = "zwei Jahren hier?"
            self.text_line_6 = ""

        self.update()
