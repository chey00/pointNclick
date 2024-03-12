from PyQt6.QtCore import QRect, QPoint
from PyQt6.QtGui import QMouseEvent

from TemplateRoom import TemplateRoom


class Beck(TemplateRoom):
    def __init__(self, parent=None):
        super(Beck, self).__init__(parent)

        self.init_room("Beck.png")

        self.offset_balloon_x = 200
        self.offset_balloon_y = 25
        self.offset_balloon_length = 600
        self.offset_balloon_width = 160

        self.set_offset_mouth(240, 360, 50, 100)

        self.hitbox_door = QRect(500, 460, 75, 75)
        self.append_hitbox(self.hitbox_door)

        self.hitbox_loescher = QRect(50, 600, 75, 75)
        self.append_hitbox(self.hitbox_loescher)

        self.hitbox_kanne = QRect(1059, 750, 75, 75)
        self.append_hitbox(self.hitbox_kanne)

        self.text_line_1 = "Guten Tag,"
        self.text_line_2 = "ich bin Herr Beck, der Fachschulleiter."
        self.text_line_3 = "Hier finden Sie mein Büro,"
        self.text_line_4 = "wenn Sie mich suchen."

    def mousePressEvent(self, ev: QMouseEvent) -> None:
        super(Beck, self).mousePressEvent(ev)

        mouse_pos = ev.pos()

        if self.hitbox_door.contains(mouse_pos):
            self.text_line_1 = ""
            self.text_line_2 = "Sorry, das Büro ist abgeschlossen."
            self.text_line_3 = ""
            self.text_line_4 = "Schauen Sie sich noch andere Räume an."
            self.text_line_5 = ""
            self.text_line_6 = ""

            self.update()

        elif self.hitbox_kanne.contains(mouse_pos):
            self.text_line_1 = ""
            self.text_line_2 = "Danke, aber die Blumen"
            self.text_line_3 = "sind heute schon gegossen worden."
            self.text_line_4 = ""
            self.text_line_5 = ""
            self.text_line_6 = ""

            self.update()

        elif self.hitbox_loescher.contains(mouse_pos):
            self.text_line_1 = ""
            self.text_line_2 = "Oh, nein!"
            self.text_line_3 = "Nicht auf den Feuerlöscher!"
            self.text_line_4 = ""
            self.text_line_5 = ""
            self.text_line_6 = ""

            self.init_room("Beck_fog.png")
            self.play_sound("Beck_fog.mp3")

            self.update()
