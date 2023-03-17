from PyQt6.QtCore import QRect
from PyQt6.QtGui import QMouseEvent

from TemplateRoom import TemplateRoom


class EG102(TemplateRoom):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.__counter = 0

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

        self.hitbox_forword = QRect(943, 272, 100, 25)
        self.append_hitbox(self.hitbox_forword)

        self.hitbox_raumwecksel = QRect(683, 248, 100, 25)
        self.append_hitbox(self.hitbox_raumwecksel)

        self.text_line_1 = "Hallo!"
        self.text_line_2 = ""
        self.text_line_3 = "Willkommen im Raum EG102."
        self.text_line_4 = ""

    def mousePressEvent(self, ev: QMouseEvent) -> None:
        super(EG102, self).mousePressEvent(ev)

        mouse_pos = ev.pos()

        if self.hitbox_freddy.contains(mouse_pos):
            self.text_line_1 = "Ich heiße Freddy und"
            self.text_line_2 = "besuche die Klasse FSWI-1. Bei Fragen"
            self.text_line_3 = "sprechen Sie gerne mich oder einen"
            self.text_line_4 = "anderen Mitschüler aus der Klasse an."
            self.text_line_5 = "                              WEITER"
            self.text_line_6 = ""

            self.update()

        if self.hitbox_forword.contains(mouse_pos):
            if self.__counter == 0:
                self.text_line_1 = "Wenn Sie mit der Klassenleitung "
                self.text_line_2 = "sprechen wollen dann klicken Sie hier."
                self.text_line_3 = ""
                self.text_line_4 = "            WEITER"
                self.text_line_5 = ""
                self.text_line_6 = ""

                self.__counter = 1

        if self.hitbox_raumwecksel.contains(mouse_pos):
            if self.__counter == 1:
                self.new_room.emit("EG102Reinhart.jpg")

                self.__counter = 2

        if self.hitbox_taffel.contains(mouse_pos):
            self.text_line_1 = "Auf der Tafel steht"
            self.text_line_2 = "meistens nicht viel,"
            self.text_line_3 = "da der Unterricht"
            self.text_line_4 = "digital gestaltet ist."
            self.text_line_5 = ""
            self.text_line_6 = ""

            self.update()

        if self.hitbox_beamer.contains(mouse_pos):
            self.text_line_1 = "Dank dem digitalen Unterricht"
            self.text_line_2 = "findet dieser mithilfe des Beamers"
            self.text_line_3 = "statt."
            self.text_line_4 = ""
            self.text_line_5 = ""
            self.text_line_6 = ""

            self.update()

        if self.hitbox_schwamm.contains(mouse_pos):
            self.text_line_1 = "Wer lebt in der Ananas"
            self.text_line_2 = "ganz tief im Meer?"
            self.text_line_3 = ""
            self.text_line_4 = ""
            self.text_line_5 = ""
            self.text_line_6 = ""

            self.play_sound("der_schwamm.mp3")
            self.update()
