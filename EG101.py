from PyQt6.QtCore import QRect
from PyQt6.QtGui import QMouseEvent

from TemplateRoom import TemplateRoom


class EG101(TemplateRoom):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.init_room("EG101.jpg")

        self.offset_balloon_x = 650
        self.offset_balloon_y = 270
        self.offset_balloon_length = 570
        self.offset_balloon_width = 170

        self.set_offset_mouth(600, 530, 0, 100)

        self.hitbox_forward = QRect(1100, 402, 100, 25)
        self.append_hitbox(self.hitbox_forward)

        self.__counter = 0

        self.hitbox_PC = QRect(480, 695, 240, 110)
        self.append_hitbox(self.hitbox_PC)

        self.hitbox_ordner = QRect(1, 710, 207, 180)
        self.append_hitbox(self.hitbox_ordner)

        self.hitbox_tafel = QRect(900, 470, 300, 200)
        self.append_hitbox(self.hitbox_tafel)

        self.hitbox_stundenplan = QRect(400, 340, 230, 125)
        self.append_hitbox(self.hitbox_stundenplan)

        self.text_line_1 = ""
        self.text_line_2 = "Hallo!"
        self.text_line_3 = "Ich bin der Herr Gumbmann."
        self.text_line_4 = "Willkommen im Raum EG101."
        self.text_line_5 = "Hier unterrichte ich die Klasse FSWI-1."
        self.text_line_6 = "                               weiter"

    def mousePressEvent(self, ev: QMouseEvent) -> None:
        super(EG101, self).mousePressEvent(ev)

        mouse_pos = ev.pos()

        if self.hitbox_forward.contains(mouse_pos):
            if self.__counter == 0:
                self.text_line_1 = ""
                self.text_line_2 = "Ich unterrichte das Fach"
                self.text_line_3 = "Programmieren."
                self.text_line_4 = ""
                self.text_line_5 = ""
                self.text_line_6 = ""

                self.__counter = 1

        if self.hitbox_PC.contains(mouse_pos):
            self.text_line_1 = "Die Schüler bekommen, ein iPad,"
            self.text_line_2 = "am Schuljahresanfang kostenlos"
            self.text_line_3 = "zur Verfügung gestellt."
            self.text_line_4 = "Die Wirtschaftsinformatiker bekommen"
            self.text_line_5 = "dazu noch ein MacBook gestellt."
            self.text_line_6 = ""

        elif self.hitbox_ordner.contains(mouse_pos):
            self.text_line_1 = ""
            self.text_line_2 = "Wir schreiben mindestens"
            self.text_line_3 = "zwei Stegreifaufgaben und"
            self.text_line_4 = "eine Schulaufgabe"
            self.text_line_5 = "pro Halbjahr!"
            self.text_line_6 = ""

        elif self.hitbox_tafel.contains(mouse_pos):
            self.text_line_1 = "Im ersten Schuljahr,"
            self.text_line_2 = "haben Wirtschaftsinformatiker"
            self.text_line_3 = "eine 37-Stunden Woche."
            self.text_line_4 = "Parallel zum Bachelor, können Sie"
            self.text_line_5 = "das Fachabitur durch eine "
            self.text_line_6 = "Ergänzungsprüfung in Englisch erwerben."

        elif self.hitbox_stundenplan.contains(mouse_pos):
            self.text_line_1 = "Lehrplan:"
            self.text_line_2 = "Deutsch, Englisch, Sozialkunde,"
            self.text_line_3 = "Programmieren 1-3, Betriebswirtschaft,"
            self.text_line_4 = "Datenbanken, Betriebssysteme,"
            self.text_line_5 = "Informations- & Kommunikationstechnik,"
            self.text_line_6 = "Softwareentwicklungsprozesse."

            self.update()
