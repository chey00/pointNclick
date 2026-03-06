from PyQt6.QtCore import QRect
from PyQt6.QtGui import QMouseEvent

from TemplateRoom import TemplateRoom


class EG101(TemplateRoom):
    def __init__(self, parent=None):
        super(EG101, self).__init__(parent)

        self.init_room("EG101.jpg")

        self.offset_balloon_x = 500
        self.offset_balloon_y = 140
        self.offset_balloon_length = 630
        self.offset_balloon_width = 170

        self.set_offset_mouth(971, 392, 0, 100)

        self.__counter = 0

        self.hitbox_PC = QRect(1034, 572, 240, 68)
        self.append_hitbox(self.hitbox_PC)

        self.hitbox_tasche = QRect(50, 658, 290, 160)
        self.append_hitbox(self.hitbox_tasche)

        self.hitbox_sparschwein = QRect(879, 586, 63, 50)
        self.append_hitbox(self.hitbox_sparschwein)

        self.hitbox_tafel = QRect(1168, 174, 300, 340)
        self.append_hitbox(self.hitbox_tafel)

        self.text_line_1 = "Hallo!"
        self.text_line_2 = "Ich bin Herr Hey und unterrichte"
        self.text_line_3 = "das Fach Programmieren. Wenn du gut"
        self.text_line_4 = "aufpasst, verstehst du nicht nur den Stoff"
        self.text_line_5 = "besser - vielleicht gibt es sogar eine"
        self.text_line_6 = "bessere Note. Also Ohren auf, Gehirn an!"

    def mousePressEvent(self, ev: QMouseEvent) -> None:
        super(EG101, self).mousePressEvent(ev)

        mouse_pos = ev.pos()

        if self.hitbox_PC.contains(mouse_pos):
            self.text_line_1 = "Die Schüler bekommen ein iPad,"
            self.text_line_2 = "am Schuljahresanfang kostenlos"
            self.text_line_3 = "zur Verfügung gestellt."
            self.text_line_4 = "Die Wirtschaftsinformatiker erhalten"
            self.text_line_5 = "dazu noch ein MacBook Air."
            self.text_line_6 = ""

        elif self.hitbox_tasche.contains(mouse_pos):
            self.text_line_1 = ""
            self.text_line_2 = "Wir schreiben mindestens zwei"
            self.text_line_3 = "Leistungsnachweise pro Halbjahr:"
            self.text_line_4 = "eine Stegreifaufgabe und eine"
            self.text_line_5 = "Schulaufgabe."
            self.text_line_6 = ""

        elif self.hitbox_sparschwein.contains(mouse_pos):
            self.text_line_1 = "Dieses Sparschwein ist"
            self.text_line_2 = "ein kleiner BWL-Experte."
            self.text_line_3 = "Als Wirtschaftsinformatiker ist."
            self.text_line_4 = "Betriebswirtschaft auch ein wichtiger"
            self.text_line_5 = "Fachbereich. In der Betriebswirtschaft "
            self.text_line_6 = "lernt man, wie man mit Geld richtig umgeht!"

        elif self.hitbox_tafel.contains(mouse_pos):
            self.text_line_1 = "Lehrplan:"
            self.text_line_2 = "Deutsch, Englisch, Sozialkunde,"
            self.text_line_3 = "Programmieren, Betriebswirtschaft,"
            self.text_line_4 = "Datenbanken, Betriebssysteme,"
            self.text_line_5 = "Informations- & Kommunikationstechnik,"
            self.text_line_6 = "Softwareentwicklungsprozesse."

            self.update()
