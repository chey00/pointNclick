from PyQt6.QtCore import QRect
from PyQt6.QtGui import QMouseEvent

from TemplateRoom import TemplateRoom

class Aula(TemplateRoom):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.init_room("Aula.jpg")

        self.offset_balloon_x = int((1440-500)/2)
        self.offset_balloon_y = 25
        self.set_offset_mouth(self.offset_balloon_x, self.offset_balloon_y, 0, 0)

        self.hitbox_zurVerwaltung = QRect(1, 1, 250, 800)
        self.append_hitbox(self.hitbox_zurVerwaltung)

        self.hitbox_zumWegweiser = QRect(1440 - 251, 1, 250, 800)
        self.append_hitbox(self.hitbox_zumWegweiser)

        self.text_line_1 = "\t\tWegweiser:"
        self.text_line_2 = ""
        self.text_line_3 = ""
        self.text_line_4 = "Links: zur Verwaltung"
        self.text_line_5 = "Rechts: zu den Unterrichtsräumen"
        self.text_line_6 = ""

    def mousePressEvent(self, ev: QMouseEvent) -> None:
        super(Aula, self).mousePressEvent(ev)

        mouse_pos = ev.pos()
        print(mouse_pos)

        if self.hitbox_zurVerwaltung.contains(mouse_pos):
            self.new_room.emit("Verwaltung.jpg")
        elif self.hitbox_zumWegweiser.contains(mouse_pos):
            self.new_room.emit("Wegweiser.jpg")

        self.update()
