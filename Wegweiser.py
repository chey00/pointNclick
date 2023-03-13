from PyQt6.QtCore import QRect
from PyQt6.QtGui import QMouseEvent

from TemplateRoom import TemplateRoom

class Wegweiser(TemplateRoom):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.init_room("Wegweiser.jpg")

        self.offset_balloon_x = int((1440-500)/2)
        self.offset_balloon_y = 25
        self.set_offset_mouth(self.offset_balloon_x, self.offset_balloon_y + 200, 0, 0)

        self.hitbox_zumTreppenhaus = QRect(1, 1, 250, 800)
        self.append_hitbox(self.hitbox_zumTreppenhaus)

        self.hitbox_zumGangTech = QRect(1440-251, 1, 250, 800)
        self.append_hitbox(self.hitbox_zumGangTech)

        self.text_line_1 = "\t\tWegweiser:"
        self.text_line_2 = ""
        self.text_line_3 = ""
        self.text_line_6 = ""
        self.text_line_4 = "Links: zum Treppenhaus"
        self.text_line_5 = "Rechts: zu den Unterrichtsräumen"

    def mousePressEvent(self, ev: QMouseEvent) -> None:
        super(Wegweiser, self).mousePressEvent(ev)

        mouse_pos = ev.pos()
        print(mouse_pos)

        if self.hitbox_zumTreppenhaus.contains(mouse_pos):
            self.new_room.emit("Treppenhaus.jpg")
        elif self.hitbox_zumGangTech.contains(mouse_pos):
            self.new_room.emit("GangTech.jpg")

        self.update()
