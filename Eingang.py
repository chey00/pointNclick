from PyQt6.QtCore import QRect
from PyQt6.QtGui import QMouseEvent

from TemplateRoom import TemplateRoom

class Eingang(TemplateRoom):
    def __init__(self, parent=None):
        super(Eingang, self).__init__()

        self.init_room("Eingang.jpg")

        self.offset_balloon_x = 750
        self.offset_balloon_y = 20
        self.offset_balloon_width = 180
        self.offset_balloon_length = 650

        self.set_offset_mouth(787, 271, 50, 150)

        self.hitbox_door_1 = QRect(5, 215, 350, 600)
        self.append_hitbox(self.hitbox_door_1)

        self.hitbox_door_2 = QRect(1150, 215, 275, 600)
        self.append_hitbox(self.hitbox_door_2)

        self.hitbox_forward = QRect(1270, 150, 100, 25)
        self.append_hitbox(self.hitbox_forward)

        self.__counter = 0

        self.hitbox_easter_egg = QRect(740, 410, 35, 35)

        self.text_line_1 = ""
        self.text_line_2 = "Hey,"
        self.text_line_3 = "Herzlich Willkommen an der"
        self.text_line_4 = "SBS Herzogenaurach!"
        self.text_line_5 = ""
        self.text_line_6 = "                                    weiter"

    def mousePressEvent(self, ev: QMouseEvent) -> None:
        super(Eingang, self).mousePressEvent(ev)

        mouse_pos = ev.pos()

        if self.hitbox_easter_egg.contains(mouse_pos):
            self.text_line_1 = ""
            self.text_line_2 = ""
            self.text_line_3 = "GLÜCKWUNSCH!!!"
            self.text_line_4 = "Sie haben Ihre erste Kaffetasse gefunden."
            self.text_line_5 = ""
            self.text_line_6 = "                                    weiter"

            self.update()

        elif self.hitbox_door_1.contains(mouse_pos):
            self.new_room.emit("Aula.jpg")
        elif self.hitbox_door_2.contains(mouse_pos):
            self.new_room.emit("Aula.jpg")

        elif self.hitbox_forward.contains(mouse_pos):
            if self.__counter == 0:
                self.text_line_1 = ""
                self.text_line_2 = "Ich heiße David Ojimba"
                self.text_line_3 = "und begleite euch heute,"
                self.text_line_4 = "durch unsere Schule."
                self.text_line_5 = ""
                self.text_line_6 = "                                    weiter"

            elif self.__counter == 1:
                self.text_line_1 = "Hier ist unser Point & Click adventure,"
                self.text_line_2 = "klicke dich gerne von Raum zu Raum"
                self.text_line_3 = "um einen Einblick in unsere verschiedenen,"
                self.text_line_4 = "Fachschulen, zu gewinnen."
                self.text_line_5 = ""
                self.text_line_6 = "                                    weiter"

            elif self.__counter == 2:
                self.text_line_1 = ""
                self.text_line_2 = "Hitboxen werden angezeigt und"
                self.text_line_3 = "Easter Eggs sind auch versteckt."
                self.text_line_4 = ""
                self.text_line_5 = ""
                self.text_line_6 = "                                    weiter"

            elif self.__counter == 3:
                self.text_line_1 = "In manchen Räumen ist eine Tasse versteckt."
                self.text_line_2 = ""
                self.text_line_3 = "Findet und sammelt sie,"
                self.text_line_4 = "den am Ende, habt Ihr die Chance"
                self.text_line_5 = "ein 'Easter Present' zu gewinnen."
                self.text_line_6 = "                                    weiter"

            elif self.__counter == 4:
                self.text_line_1 = ""
                self.text_line_2 = ""
                self.text_line_3 = "Naaa, haben Sie schon"
                self.text_line_4 = "eine Tasse entdeckt?"
                self.text_line_5 = ""
                self.text_line_6 = "                                    weiter"

            elif self.__counter == 5:
                self.text_line_1 = "Ihre erste Tasse haben Sie bereits gefunden."
                self.text_line_2 = ""
                self.text_line_3 = "Sammelt Sie und gehen Sie nun von"
                self.text_line_4 = "Raum zu Raum."
                self.text_line_5 = ""
                self.text_line_6 = "                                    weiter"

            elif self.__counter == 6:
                self.text_line_1 = ""
                self.text_line_2 = ""
                self.text_line_3 = ""
                self.text_line_4 = "Viel Spaß bei der Suche!!"
                self.text_line_5 = ""
                self.text_line_6 = ""

            self.__counter += 1

            self.update()
