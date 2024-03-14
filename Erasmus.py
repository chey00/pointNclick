from PyQt6.QtCore import QRect, QPoint, Qt
from PyQt6.QtGui import QMouseEvent, QPixmap, QPaintEvent, QPainter

from TemplateRoom import TemplateRoom


class Erasmus(TemplateRoom):
    def __init__(self, parent=None):
        super(Erasmus, self).__init__(parent)

        self.init_room("Erasmus.jpg")

        self.offset_balloon_x = 25
        self.offset_balloon_y = 25
        self.offset_balloon_length = 460
        self.offset_balloon_width = 175

        self.set_offset_mouth(275, 500, 10, 100)

        self.hitbox_forward = QRect(350, 150, 125, 50)
        self.append_hitbox(self.hitbox_forward)

        self.hitbox_erasmus = QRect(620, 70, 760, 510)
        self.append_hitbox(self.hitbox_erasmus)
        self.__counter = 0

        self.text_line_1 = "Hallo!"
        self.text_line_2 = "Willkommen im Raum EG102."
        self.text_line_3 = "Ich heiße Frau Reinhart und"
        self.text_line_4 = "bin die Klassenleitung"
        self.text_line_5 = "der Klasse FSWI-2."
        self.text_line_6 = "                       weiter"

        self.__pixmap = QPixmap("Erasmus_Helsinki.jpg")
        self.__pixmap = self.__pixmap.scaledToHeight(500)

    def mousePressEvent(self, ev: QMouseEvent) -> None:
        super(Erasmus, self).mousePressEvent(ev)

        mouse_pos = ev.pos()

        if self.hitbox_forward.contains(mouse_pos):
            if self.__counter == 0:
                self.text_line_1 = "Hier unterrichte ich das Fach"
                self.text_line_2 = "Betriebswirtschaft im Lern-"
                self.text_line_3 = "feld Logistische Prozesse &"
                self.text_line_4 = "Finanzbuchhaltung."
                self.text_line_5 = ""
                self.text_line_6 = ""

                self.__counter = 1

            elif self.__counter == 2:
                self.text_line_1 = "Unsere Studenten haben die"
                self.text_line_2 = "Chance ihre Sprachkenntnisse"
                self.text_line_3 = "in Englisch zu verbessern. "
                self.text_line_4 = "Dazu besuchen sie eine Sprach-"
                self.text_line_5 = "schule im Ausland."
                self.text_line_6 = "                       weiter"

                self.__counter = 3

            elif self.__counter == 3:
                self.text_line_1 = "Vor Ort gehen unsere Studenten"
                self.text_line_2 = "in einen Sprachkurs oder machen"
                self.text_line_3 = "ein Praktikum. Die Aufenhalts-"
                self.text_line_4 = "dauer beträgt zwei Wochen."
                self.text_line_5 = ""
                self.text_line_6 = "                       weiter"

                self.__counter = 4

            elif self.__counter == 4:
                self.text_line_1 = "Bisher haben unsere Studenten"
                self.text_line_2 = "die Länder Malta, Irland"
                self.text_line_3 = "und Schweden besucht. Dieses"
                self.text_line_4 = "Jahr geht es nach Helsinki."
                self.text_line_5 = ""
                self.text_line_6 = "                       weiter"

                self.__counter = 5

            elif self.__counter == 5:
                self.text_line_1 = "Bei Fragen stehe ich Ihnen"
                self.text_line_2 = "gerne zur Verfügung. Machen"
                self.text_line_3 = "Sie es gut und hoffentlich"
                self.text_line_4 = "bis bald!"
                self.text_line_5 = ""
                self.text_line_6 = ""

        elif self.hitbox_erasmus.contains(mouse_pos):
            if self.__counter == 1 or self.__counter == 0:
                self.text_line_1 = "Ich betreue auch unser Erasmus"
                self.text_line_2 = "Programm. Sie fragen sich, was"
                self.text_line_3 = "das ist? Ich erkläre es Ihnen"
                self.text_line_4 = "gleich."
                self.text_line_5 = ""
                self.text_line_6 = "                       weiter"

                self.__counter = 2

        self.update()

    def paintEvent(self, a0: QPaintEvent) -> None:
        super(Erasmus, self).paintEvent(a0)

        painter = QPainter()

        painter.begin(self)

        painter.drawPixmap(625, 75, self.__pixmap)

        painter.end()
