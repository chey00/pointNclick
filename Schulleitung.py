from PyQt6.QtCore import QRect
from PyQt6.QtGui import QMouseEvent

from TemplateRoom import TemplateRoom


class Schulleitung(TemplateRoom):
    def __init__(self, parent=None):
        super(Schulleitung, self).__init__(parent)

        self.init_room("Schulleitung.jpg")

        self.offset_balloon_x = 586
        self.offset_balloon_y = 150
        self.offset_balloon_length = 550
        self.offset_balloon_width = 165
        self.set_offset_mouth(671, 442, 100, 200)

        self.hitbox_mouth = QRect(1005, 280, 100, 30)
        self.append_hitbox(self.hitbox_mouth)

        self.hitbox_door = QRect(975, 725, 300, 125)
        self.append_hitbox(self.hitbox_door)

        self.hitbox_schulregeln = QRect(25, 75, 425, 400)
        self.append_hitbox(self.hitbox_schulregeln)

        self.hitbox_easter_egg = QRect(569, 650, 80, 80)

        self.text_line_1 = "Herzlich Willkommen!"
        self.text_line_2 = ""
        self.text_line_3 = "Mein Name ist Frau Wirzberger-Camacho."
        self.text_line_4 = "Ich bin hier die Schulleiterin."
        self.text_line_5 = "Schön, dass Sie hier sind!"
        self.text_line_6 = "                             Weiter"

    def mousePressEvent(self, ev: QMouseEvent) -> None:
        super(Schulleitung, self).mousePressEvent(ev)

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
            self.text_line_4 = "wichtigen Aufgaben, damit alles"
            self.text_line_5 = "reibungslos abläuft."
            self.text_line_6 = ""

            self.update()

        if self.hitbox_easter_egg.contains(mouse_pos):
            self.text_line_1 = ""
            self.text_line_2 = ""
            self.text_line_3 = "Eine Tasse Kaffee"
            self.text_line_4 = "wäre jetzt nicht schlecht..."
            self.text_line_5 = ""
            self.text_line_6 = ""

            self.play_sound("TemplateRoom.mp3")

            self.update()

        if self.hitbox_schulregeln.contains(mouse_pos):
            self.text_line_1 = "Sie haben das Leitbild unserer "
            self.text_line_2 = "Schule gefunden. Der wertschätzende "
            self.text_line_3 = "Umgang an unserer Schule ist "
            self.text_line_4 = "der Schulfamilie eine "
            self.text_line_5 = "Herzensangelegenheit."
            self.text_line_6 = ""

            self.update()
