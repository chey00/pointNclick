from PyQt6.QtCore import QRect
from PyQt6.QtGui import QMouseEvent

from TemplateRoom import TemplateRoom

class Fraesmaschine(TemplateRoom):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.init_room("Fraesmaschine.jpg")

        self.offset_balloon_x = 600
        self.offset_balloon_y = 50
        self.set_offset_mouth(1120, 370, 50, 150)

        self.hitbox_werkzeug = QRect(600, 350, 75, 75)
        self.append_hitbox(self.hitbox_werkzeug)

        self.hitbox_easter_egg = QRect(682, 500, 45, 45)
        self.append_hitbox(self.hitbox_easter_egg)

        self.hitbox_tuer = QRect(30, 290, 500, 400)
        self.append_hitbox(self.hitbox_tuer)

        self.hitbox_weiter = QRect(605, 155, 100, 25)
        self.append_hitbox(self.hitbox_weiter)

        self.__counter = 0

        self.text_line_1 = "Hi, ich bin der Alex und "
        self.text_line_2 = "besuche die Fachschule"
        self.text_line_3 = "für Wirtschaftsinformatik."
        self.text_line_4 = ""
        self.text_line_5 = "weiter"
        self.text_line_6 = ""


    def mousePressEvent(self, ev: QMouseEvent) -> None:
        super(Fraesmaschine, self).mousePressEvent(ev)

        mouse_pos = ev.pos()

        if self.hitbox_werkzeug.contains(mouse_pos):
            self.text_line_1 = "Das ist die Werkzeugaufnahme."
            self.text_line_2 = "Hiermit werden die Werkzeuge"
            self.text_line_3 = "aus dem Magazin entnommen"
            self.text_line_4 = "und die Werkstücke bearbeitet."
            self.text_line_5 = ""
            self.text_line_6 = ""
            self.update()

        elif self.hitbox_tuer.contains(mouse_pos):
            self.text_line_1 = ""
            self.text_line_2 = "Das ist eine Sicherheitstür."
            self.text_line_3 = "Die Maschine schaltet die "
            self.text_line_4 = "Spindel nur frei, wenn diese"
            self.text_line_5 = "geschlossen ist."
            self.text_line_6 = ""
            self.update()

        elif self.hitbox_weiter.contains(mouse_pos):
            if self.__counter == 1:
                self.text_line_1 = ""
                self.text_line_2 = "Hier lernt man die richtige"
                self.text_line_3 = "Bedienung der Maschinen und das"
                self.text_line_4 = "Erstellen von CNC-Programmen"
                self.text_line_5 = "für Dreh- und Fräsmaschinen."
                self.__counter += 1

            if self.__counter ==0:
                self.text_line_1 = ""
                self.text_line_2 = "Willkommen in unserer"
                self.text_line_3 = "CNC-Ausbildungswerkstatt!"
                self.text_line_4 = ""
                self.text_line_5 = "weiter"
                self.text_line_6 = ""
                self.__counter += 1
                self.update()


        elif self.hitbox_easter_egg.contains(mouse_pos):
            self.text_line_1 = ""
            self.text_line_2 = ""
            self.text_line_3 = "Glückwunsch du hast"
            self.text_line_4 = "eine Tasse gefunden!"
            self.text_line_5 = ""
            self.text_line_6 = ""

            self.play_sound("TemplateRoom_found_cup.mp3")

            self.update()
