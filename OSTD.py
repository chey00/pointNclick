from PyQt6.QtCore import QRect
from PyQt6.QtGui import QMouseEvent

from TemplateRoom import TemplateRoom

class OSTD(TemplateRoom):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.init_room("OSTD1.jpg")

        self.offset_balloon_x = 515
        self.offset_balloon_y = 150
        self.set_offset_mouth(563, 421, 100, 200)

        self.hitbox_mouth = QRect(520, 355, 75, 75)
        self.append_hitbox(self.hitbox_mouth)

        self.hitbox_door = QRect(0, -100, 140, 1000)
        self.append_hitbox(self.hitbox_door)

        self.hitbox_schulregeln = QRect(161, 195, 190, 200)
        self.append_hitbox(self.hitbox_schulregeln)

        self.hitbox_easter_egg = QRect(750, 535, 80, 80)

        self.text_line_1 = "Herzlich Willkommen!"
        self.text_line_2 = ""
        self.text_line_3 = "Mein Name ist Hr. Wirsching."
        self.text_line_4 = "Ich bin hier der Schulleiter."
        self.text_line_5 = ""
        self.text_line_6 = "Schön das Sie hier sind!"

    def mousePressEvent(self, ev: QMouseEvent) -> None:
        super(OSTD, self).mousePressEvent(ev)

        mouse_pos = ev.pos()

        if self.hitbox_mouth.contains(mouse_pos):
            self.text_line_1 = "Sollten Sie Fragen zu unserer"
            self.text_line_2 = "Schule haben, wenden Sie sich"
            self.text_line_3 = "gerne an mich oder an"
            self.text_line_4 = "unsere Lehrkräfte."
            self.text_line_5 = "Ich wünsche Ihnen einen schönen"
            self.text_line_6 = "Aufenthalt bei uns!"

            self.update()

        if self.hitbox_door.contains(mouse_pos):
            self.text_line_1 = "Das ist mein Arbeitszimmer."
            self.text_line_2 = "Von hier aus leite ich unsere"
            self.text_line_3 = "Schule und bearbeite alle"
            self.text_line_4 = "wichtigen Aufgaben damit alles"
            self.text_line_5 = "reibungslos abläuft."
            self.text_line_6 = ""

            self.update()

        if self.hitbox_easter_egg.contains(mouse_pos):
            self.text_line_1 = ""
            self.text_line_2 = ""
            self.text_line_3 = "Eine Tasse Kaffe"
            self.text_line_4 = "wäre jetzt nicht schlecht..."
            self.text_line_5 = ""
            self.text_line_6 = ""

            self.update()

        if self.hitbox_schulregeln.contains(mouse_pos):
            self.text_line_1 = ""
            self.text_line_2 = ""
            self.text_line_3 = "Hier stehen die Regeln unserer Schule"
            self.text_line_4 = ""
            self.text_line_5 = ""
            self.text_line_6 = ""

            self.update()



