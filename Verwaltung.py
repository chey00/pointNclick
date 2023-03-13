from PyQt6.QtCore import QRect, QPoint
from PyQt6.QtGui import QMouseEvent

from TemplateRoom import TemplateRoom

class Verwaltung(TemplateRoom):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.init_room("Verwaltung.jpg")

        self.offset_balloon_x = 550
        self.offset_balloon_y = 200
        self.offset_balloon_length = 550
        self.offset_balloon_width = 200
        self.set_offset_mouth(502, 484, 50, 150)

        self.hitbox_mouth = QRect(430, 375, 120, 135)
        self.append_hitbox(self.hitbox_mouth)

        self.hitbox_unterlagen = QRect(640, 680, 190, 140)
        self.append_hitbox(self.hitbox_unterlagen)

        self.hitbox_computer = QRect(700, 435, 110, 120)
        self.append_hitbox(self.hitbox_computer)

        self.hitbox_zumStvRoom= QRect(1340, 1, 99, 800)
        self.append_hitbox(self.hitbox_zumStvRoom)

        self.text_line_1 = "Herzlich Willkommen in der"
        self.text_line_2 = "Verwaltung!"
        self.text_line_3 = ""
        self.text_line_4 = "Ich bin die Frau Müller!"
        self.text_line_5 = "Wie kann ich Ihnen behilflich"
        self.text_line_6 = "sein?"

    def mousePressEvent(self, ev: QMouseEvent) -> None:
        super(Verwaltung, self).mousePressEvent(ev)

        mouse_pos = ev.pos()

        if self.hitbox_mouth.contains(mouse_pos):
            self.text_line_1 = "Sie brauchen eine Schulbescheinigung"
            self.text_line_2 = "für Ihre Krankenkasse?"
            self.text_line_3= ""
            self.text_line_4 = "Gerne, ich mach sie es Ihnen fertig!"
            self.text_line_5 = "Sie können es in der nächste Pause"
            self.text_line_6 = "abholen"

            self.update()

        elif self.hitbox_unterlagen.contains(mouse_pos):
            self.text_line_1 = "Hallo nochmal!"
            self.text_line_2 = "Nein das sind nicht Ihre Unterlagen."
            self.text_line_3 = "Mensch, Finger weg!"
            self.text_line_4 = "Warten Sie kurz... ah hier."
            self.text_line_5 = "Bitteschön, Ihre Unterlagen sind hier!"
            self.text_line_6 = "Haben Sie noch einen Wunsch?"

            self.update()

        elif self.hitbox_computer.contains(mouse_pos):
            self.text_line_1 = "Für Sie zur Info, Sie haben auch die"
            self.text_line_2 = "Möglichkeit Ihre Unterlagen Online"
            self.text_line_3 = "zu beantragen. Unter unsere Webseite:"
            self.text_line_4 = ""
            self.text_line_5 = "WWW.SBS-herzogenaurach.de"
            self.text_line_6 = ""

        elif self.hitbox_zumStvRoom.contains(mouse_pos):
            self.new_room.emit("StvRoom.jpg")

        self.update()
