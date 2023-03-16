from PyQt6.QtCore import QRect, QPoint
from PyQt6.QtGui import QMouseEvent

from TemplateRoom import TemplateRoom

class EG102Reinhart(TemplateRoom):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.init_room("FrauReinhart.jpg")

        self.offset_balloon_x = 710
        self.offset_balloon_y = 100
        self.offset_balloon_length = 450
        self.offset_balloon_width = 165

        self.set_offset_mouth(690, 330, 10, 100)

        self.hitbox_forward = QRect(1045, 228, 100, 25)
        self.append_hitbox(self.hitbox_forward)

        self.__counter = 0

        self.hitbox_erasmus = QRect(1260, 540, 200, 120)
        self.append_hitbox(self.hitbox_erasmus)

        self.text_line_1 = "Hallo!"
        self.text_line_2 = "Willkommen im Raum EG102."
        self.text_line_3 = "Ich heiße Frau Reinhart und"
        self.text_line_4 = "bin die Klassenleitung"
        self.text_line_5 = "der Klasse FSWI-1."
        self.text_line_6 = "                       weiter"

    def mousePressEvent(self, ev: QMouseEvent) -> None:
        super(EG102Reinhart, self).mousePressEvent(ev)

        mouse_pos = ev.pos()





        if self.hitbox_forward.contains(mouse_pos):
            if self.__counter == 0:
                self.text_line_1 = "Hier unterrichte ich das Fach"
                self.text_line_2 = "Betriebswirtschaft im"
                self.text_line_3 = "Lernfeld:"
                self.text_line_4 = "Logistische Prozesse &"
                self.text_line_5 = "Finanzbuchhaltung."
                self.text_line_6 = ""

                self.__counter = 1

            elif self.__counter == 1:
                self.text_line_1 = "Die Schüler haben die Chance"
                self.text_line_2 = "ihre Sprachkenntnisse in"
                self.text_line_3 = "Englisch im Ausland zu"
                self.text_line_4 = "verbessern, indem Sie am"
                self.text_line_5 = "Erasmus Programm teilnehmen"
                self.text_line_6 = "                       weiter"

                self.__counter = 2

            elif self.__counter == 2:
                self.text_line_1 = "Dort besucht man zum"
                self.text_line_2 = "einem eine Schule oder man"
                self.text_line_3 = "tritt ein Praktikum an."
                self.text_line_4 = "Die dauer des Aufenhaltes"
                self.text_line_5 = "liegt bei 2 Wochen."
                self.text_line_6 = "                       weiter"

                self.__counter = 3

            elif self.__counter == 3:
                self.text_line_1 = "Bisher haben die Schüler"
                self.text_line_2 = "die Länder :"
                self.text_line_3 = "Malta, Dublin und Schweden"
                self.text_line_4 = "besucht."
                self.text_line_5 = ""
                self.text_line_6 = "                       weiter"

                self.__counter = 4

            elif self.__counter == 4:
                self.text_line_1 = ""
                self.text_line_2 = "Für Fragen stehe ich Ihnen"
                self.text_line_3 = "gerne zur Verfügung."
                self.text_line_4 = ""
                self.text_line_5 = "Machen Sie es gut!"
                self.text_line_6 = ""

                self.update()

        elif self.hitbox_erasmus.contains(mouse_pos):
                self.text_line_1 = "Dazu betreue ich auch"
                self.text_line_2 = "unser Erasmus Programm."
                self.text_line_3 = ""
                self.text_line_4 = "Sie fragen sich was das ist?"
                self.text_line_5 = "Ich erkläre es Ihnen."
                self.text_line_6 = "                       weiter"
                self.update()


