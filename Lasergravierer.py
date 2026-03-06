from PyQt6.QtCore import QRect
from PyQt6.QtGui import QMouseEvent

from TemplateRoom import TemplateRoom


class Lasergravierer(TemplateRoom):
    def __init__(self, parent=None):
        super(Lasergravierer, self).__init__(parent)

        self.init_room("Lasergravierer.jpg")

        self.offset_balloon_x = 500
        self.offset_balloon_y = 89
        self.offset_balloon_length = 450
        self.offset_balloon_width = 200
        self.set_offset_mouth(500, 290, 10, 10)

        self.hitbox_laptop = QRect(246, 388, 250, 150)
        self.append_hitbox(self.hitbox_laptop)

        self.hitbox_laser = QRect(540, 458, 900, 410)
        self.append_hitbox(self.hitbox_laser)

        self.hitbox_easter_egg = QRect(171, 464, 70, 75)

        self.text_line_1 = "Hallo,"
        self.text_line_2 = "ich bin Danilo. Du bist im"
        self.text_line_3 = "Raum für den Lasergravierer."
        self.text_line_4 = "Sicher willst du deine Tasse"
        self.text_line_5 = "abholen. Hast du schon alle"
        self.text_line_6 = "Easter Eggs gefunden?"

    def mousePressEvent(self, ev: QMouseEvent) -> None:
        super(Lasergravierer, self).mousePressEvent(ev)

        mouse_pos = ev.pos()

        if self.hitbox_laptop.contains(mouse_pos):
            self.text_line_1 = "Nicht nur die Wirtschaftsin-"
            self.text_line_2 = "formatik nutzt bei uns Laptops."
            self.text_line_3 = "Hier wird deine individuelle"
            self.text_line_4 = "Tasse designt und der Laser-"
            self.text_line_5 = "gravierer angesteuert."
            self.text_line_6 = ""

            self.update()

        if self.hitbox_laser.contains(mouse_pos):
            self.text_line_1 = "Genau hier wird deine Tasse"
            self.text_line_2 = "individuell graviert!"
            self.text_line_3 = ""
            self.text_line_4 = "Sonst können wir damit nicht"
            self.text_line_5 = "nur Tassen, sondern auch Ober-"
            self.text_line_6 = "flächen bearbeiten."

            self.update()

        if self.hitbox_easter_egg.contains(mouse_pos):
            self.text_line_1 = "Super, du hast ein gutes"
            self.text_line_2 = "Augen. Viel Spaß bei der"
            self.text_line_3 = "weiteren Suche!"
            self.text_line_4 = ""
            self.text_line_5 = ""
            self.text_line_6 = ""

            self.play_sound("TemplateRoom.mp3")

            self.update()
