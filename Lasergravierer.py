from PyQt6.QtCore import QRect
from PyQt6.QtGui import QMouseEvent

from TemplateRoom import TemplateRoom


class Lasergravierer(TemplateRoom):
    def __init__(self, parent=None):
        super(Lasergravierer, self).__init__(parent)

        self.init_room("Lasergravierer.jpg")

        self.offset_balloon_x = 975
        self.offset_balloon_y = 15
        self.offset_balloon_length = 450
        self.offset_balloon_width = 200
        self.set_offset_mouth(975, 215, 10, 10)

        self.hitbox_laptop = QRect(1000, 275, 400, 200)
        self.append_hitbox(self.hitbox_laptop)

        self.hitbox_laser = QRect(400, 150, 350, 300)
        self.append_hitbox(self.hitbox_laser)

        self.hitbox_easter_egg = QRect(825, 300, 100, 75)

        self.text_line_1 = "Hallo,"
        self.text_line_2 = "ich bin Michell. Du bist im"
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
            self.text_line_1 = "Die Tasse hier, hast du schon"
            self.text_line_2 = "mal gefunden. Viel Spaß bei"
            self.text_line_3 = "der weiteren Suche!"
            self.text_line_4 = ""
            self.text_line_5 = ""
            self.text_line_6 = ""

            self.play_sound("TemplateRoom.mp3")

            self.update()
