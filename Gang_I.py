from PyQt6.QtCore import QRect
from PyQt6.QtGui import QMouseEvent

from TemplateRoom import TemplateRoom

class Gang_I(TemplateRoom):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.init_room("Gang_I.jpg")

        self.offset_balloon_x = int((1440 - 500) / 2)
        self.offset_balloon_y = 25
        self.set_offset_mouth(self.offset_balloon_x + self.offset_balloon_length, self.offset_balloon_y + self.offset_balloon_width, 0, 0)

        self.hitbox_kicker = QRect(150, 530, 280, 290)
        self.append_hitbox(self.hitbox_kicker)

        self.hitbox_zumMetall = QRect(255, 345, 120, 150)
        self.append_hitbox(self.hitbox_zumMetall)

        self.text_line_1 = "Hier haben Sie die Möglichkeit"
        self.text_line_2 = "ihre Freizeit sportlich zu"
        self.text_line_3 = "gestalten."
        self.text_line_4 = "Wenn sie geradeaus weiterlaufen,"
        self.text_line_5 = "kommen sie zur CNC."
        self.text_line_6 = ""



    def mousePressEvent(self, ev: QMouseEvent) -> None:
        super(Gang_I, self).mousePressEvent(ev)

        mouse_pos = ev.pos()
        print(mouse_pos)

        if self.hitbox_kicker.contains(mouse_pos):
            self.text_line_1 = "Hier wurde schon so mancher"
            self.text_line_2 = "Jubelschrei vernommen,"
            self.text_line_3 = "und manche Träne vergossen."
            self.text_line_4 = ""
            self.text_line_5 = ""
            self.text_line_6 = ""
            self.play_sound("kicker_sound.mp3")

        elif self.hitbox_zumMetall.contains(mouse_pos):
            self.new_room.emit("CNC.jpg")

        self.update()
