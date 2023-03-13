from PyQt6.QtCore import QRect, QPoint
from PyQt6.QtGui import QMouseEvent

from TemplateRoom import TemplateRoom

class EG102(TemplateRoom):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.init_room("EG102.jpg")

        self.offset_balloon_x = 500
        self.offset_balloon_y = 167
        self.offset_balloon_length = 550
        self.offset_balloon_width = 150

        self.set_offset_mouth(280, 517, 50, 150)

        self.hitbox_freddy = QRect(229, 433, 75, 100)
        self.append_hitbox(self.hitbox_freddy)

        self.hitbox_taffel = QRect(62, 82, 360, 340)
        self.append_hitbox(self.hitbox_taffel)

        self.hitbox_beamer = QRect(1024, 87, 400, 600)
        self.append_hitbox(self.hitbox_beamer)

        self.hitbox_schwamm = QRect(521, 519, 70, 30)
        self.append_hitbox(self.hitbox_schwamm)

        self.text_line_1 = "Hallo!"
        self.text_line_2 = ""
        self.text_line_3 = "Willkommen im Raum EG102."
        self.text_line_4 = ""

    def mousePressEvent(self, ev: QMouseEvent) -> None:
        super(EG102, self).mousePressEvent(ev)

        mouse_pos = ev.pos()

        if self.hitbox_freddy.contains(mouse_pos):
            self.text_line_1 = "Ich heiße Freddy und"
            self.text_line_2 = "besuche die Klasse FSWI-1."
            self.text_line_3 = "Bei Fragen"
            self.text_line_4 = "sprechen Sie mich gerne "
            self.text_line_5 = "oder einen anderen aus der Klasse an."
            self.text_line_6 = ""

            self.update()

        if self.hitbox_taffel.contains(mouse_pos):
            self.text_line_1 = "Auf der Taffel steht"
            self.text_line_2 = "meistens nicht viel,"
            self.text_line_3 = "da der Unterricht"
            self.text_line_4 = "digital gestalltet ist."
            self.text_line_5 = ""
            self.text_line_6 = ""

            self.update()

        if self.hitbox_beamer.contains(mouse_pos):
            self.text_line_1 = "Dank dem digitalen Unterricht"
            self.text_line_2 = "findet dieser über dem Beamer"
            self.text_line_3 = "statt."
            self.text_line_4 = ""
            self.text_line_5 = ""
            self.text_line_6 = ""

            self.update()

        if self.hitbox_schwamm.contains(mouse_pos):
            self.text_line_1 = "Wer lebt in der Annanas"
            self.text_line_2 = "ganz tief im Meer?"
            self.text_line_3 = ""
            self.text_line_4 = ""
            self.text_line_5 = ""
            self.text_line_6 = ""

            self.update()
