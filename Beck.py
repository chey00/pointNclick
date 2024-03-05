from PyQt6.QtCore import QRect, QPoint
from PyQt6.QtGui import QMouseEvent

from TemplateRoom import TemplateRoom


class Beck(TemplateRoom):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.init_room("Beck.png")

        self.offset_balloon_x = 200
        self.offset_balloon_y = 25
        self.offset_balloon_length = 600
        self.offset_balloon_width = 160

        self.set_offset_mouth(240, 360, 50, 100)

        self.hitbox_beck = QRect(130, 430, 150, 150)
        self.append_hitbox(self.hitbox_beck)

        self.hitbox_door = QRect(500, 460, 75, 75)
        self.append_hitbox(self.hitbox_door)

        self.hitbox_loescher = QRect(50, 600, 75, 75)
        self.append_hitbox(self.hitbox_loescher)

        self.hitbox_kanne = QRect(1059, 750, 75, 75)
        self.append_hitbox(self.hitbox_kanne)

        self.text_line_1 = "Guten Tag,"
        self.text_line_2 = "ich bin Herr Beck der Fachschulleiter."
        self.text_line_3 = "Hier finden Sie mein Büro. Wenn Sie mich"
        self.text_line_4 = "suchen, finden Sie mich auch beim Metall-"
        self.text_line_5 = "3D-Drucker."

    def mousePressEvent(self, ev: QMouseEvent) -> None:
        super(Beck, self).mousePressEvent(ev)

        mouse_pos = ev.pos()

        if self.hitbox_beck.contains(mouse_pos):
            self.text_line_1 = ""
            self.text_line_2 = "Ich würde mich freuen, wenn Sie ab dem"
            self.text_line_3 = "kommenden Schuljahr eine unserer Fach-"
            self.text_line_4 = "schulen besuchen würden."
            self.text_line_5 = ""
            self.text_line_6 = ""

            self.update()

        elif self.hitbox_door.contains(mouse_pos):
            self.text_line_1 = ""
            self.text_line_2 = "Sorry das Büro"
            self.text_line_3 = "ist Abgeschlossen"
            self.text_line_4 = "schau doch mal wo anders."
            self.text_line_5 = ""
            self.text_line_6 = ""

            self.update()

        elif self.hitbox_kanne.contains(mouse_pos):
            self.text_line_1 = ""
            self.text_line_2 = "Danke aber die Blumen"
            self.text_line_3 = "sind heute schon gegossen"
            self.text_line_4 = ""
            self.text_line_5 = ""
            self.text_line_6 = ""

            self.update()

        elif self.hitbox_loescher.contains(mouse_pos):
            self.text_line_1 = ""
            self.text_line_2 = "Oh nein!!!"
            self.text_line_3 = "Nicht den Feuerlöscher anfassen!"
            self.text_line_4 = ""
            self.text_line_5 = ""
            self.text_line_6 = ""

            self.init_room("Beck_fog.png")
            self.play_sound("Beck_fire_extinguisher.mp3") #fire

            self.update()
