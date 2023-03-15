from PyQt6.QtCore import QRect, QPoint
from PyQt6.QtGui import QMouseEvent

from TemplateRoom import TemplateRoom

class EG101(TemplateRoom):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.init_room("EG101.jpg")


        self.offset_balloon_x = 700
        self.offset_balloon_y = 60
        self.offset_balloon_length = 570
        self.offset_balloon_width = 170

        self.set_offset_mouth(770, 307, 50, 150)

        self.hitbox_forward = QRect(1156, 190, 100, 25)
        self.append_hitbox(self.hitbox_forward)

        self.__counter = 0

        self.hitbox_iPad = QRect(380, 570, 270, 75)
        self.append_hitbox(self.hitbox_iPad)

        self.hitbox_ordner = QRect(1, 670, 200, 75)
        self.append_hitbox(self.hitbox_ordner)

        self.hitbox_tafel = QRect(1282, 103, 175, 500)
        self.append_hitbox(self.hitbox_tafel)

        self.hitbox_stundenplan = QRect(445, 60, 250, 160)
        self.append_hitbox(self.hitbox_stundenplan)

        self.text_line_1 = ""
        self.text_line_2 = "Hallo!"
        self.text_line_3 = "Ich bin der Herr Roth."
        self.text_line_4 = "Willkommen im Raum EG101."
        self.text_line_5 = "Hier unterrichte ich die Klasse FSWI-2."
        self.text_line_6 = "                               weiter"


    def mousePressEvent(self, ev: QMouseEvent) -> None:
        super(EG101, self).mousePressEvent(ev)

        mouse_pos = ev.pos()

        if self.hitbox_forward.contains(mouse_pos):
            if self.__counter == 0:
                self.text_line_1 = ""
                self.text_line_2 = "Ich unterrichte die Fächer"
                self.text_line_3 = "Softwareentwicklungsprozesse"
                self.text_line_4 = "und das Fach Programmieren."
                self.text_line_5 = ""
                self.text_line_6 = ""

        if self.hitbox_iPad.contains(mouse_pos):
            self.text_line_1 = "Das iPad, mit dem wir arbeiten."
            self.text_line_2 = "Dieses wird den Schülern"
            self.text_line_3 = "am Schuljahresanfang"
            self.text_line_4 = "kostenlos zur Verfügung gestellt."
            self.text_line_5 = "Die Wirtschaftsinformatiker bekommen"
            self.text_line_6 = "dazu noch ein MacBook gestellt."

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

