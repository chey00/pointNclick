from PyQt6.QtCore import QRect
from PyQt6.QtGui import QMouseEvent

from TemplateRoom import TemplateRoom


class ZwischenraumTreppenhaus(TemplateRoom):
    def __init__(self, parent=None):
        super(ZwischenraumTreppenhaus).__init__(parent)

        self.init_room("ZwischenraumTreppenhaus.jpg")

        self.offset_balloon_x = int((1440 - 500) / 2)
        self.offset_balloon_y = 25
        self.offset_balloon_length = 565
        self.offset_balloon_width = 150
        self.set_offset_mouth(self.offset_balloon_x + self.offset_balloon_length, self.offset_balloon_y +
                              self.offset_balloon_width, 0, 0)

        self.hitbox_Treppenhaus = QRect(450, 275, 400, 500)
        self.append_hitbox(self.hitbox_Treppenhaus)

        self.hitbox_Lasergravierer = QRect(1, 1, 250, 800)
        self.append_hitbox(self.hitbox_Lasergravierer)

        self.text_line_1 = "Wegweiser Treppenhaus"
        self.text_line_2 = ""
        self.text_line_3 = "Über das Treppenhaus gelangst du"
        self.text_line_4 = "nach unten. Gehst du nach links,"
        self.text_line_5 = "siehst du den Lasergravierer."

    def mousePressEvent(self, ev: QMouseEvent) -> None:
        super(ZwischenraumTreppenhaus, self).mousePressEvent(ev)

        mouse_pos = ev.pos()

        if self.hitbox_Treppenhaus.contains(mouse_pos):
            self.new_room.emit("Treppenhaus.jpg")
        elif self.hitbox_Lasergravierer.contains(mouse_pos):
            self.new_room.emit("Lasergravierer.jpg")
        self.update()
