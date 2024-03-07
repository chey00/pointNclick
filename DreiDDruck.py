from PyQt6.QtCore import QRect, QPoint
from PyQt6.QtGui import QMouseEvent

from TemplateRoom import TemplateRoom

class DreiDDruck(TemplateRoom):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.init_room("DreiDDruck_Normal.jpg")

        self.offset_balloon_x = 200
        self.offset_balloon_y = 25
        self.offset_balloon_length = 1200
        self.offset_balloon_width = 160

        self.set_offset_mouth(1150, 375, 500, 100)

        self.hitbox_mouth = QRect(0, 160, 650, 650)
        self.append_hitbox(self.hitbox_mouth)

        self.hitbox_water = QRect(990,460,90,150)
        self.append_hitbox(self.hitbox_water)

        self.hitbox_notaus = QRect(1402,328,30,25)
        self.append_hitbox(self.hitbox_notaus)

        self.text_line_1 = "Sehr geehrte Damen und Herren,"
        self.text_line_2 = "es ist mir eine große Freude,"
        self.text_line_3 = "dich in unserem Bereich für 3D-Drucker an unserer Schule begrüßen zu dürfen."
        self.text_line_4 = "Hier findest du nicht nur Kunststoff-3D-Drucker,"
        self.text_line_5 = "sondern auch eine herausragende Besonderheit."
        self.text_line_6 = "Das Herzstück dieses Bereiches ist zweifellos unser Metall-3D-Drucker."

    def mousePressEvent(self, ev: QMouseEvent) -> None:
        super(DreiDDruck, self).mousePressEvent(ev)

        mouse_pos = ev.pos()

        if self.hitbox_mouth.contains(mouse_pos):
            self.text_line_1 = "Ein Metall-3D-Drucker ist ein industrieller 3D-Drucker,"
            self.text_line_2 = "der speziell für die Fertigung von Metallteilen entwickelt wurde."
            self.text_line_3 = "Im Gegensatz zu herkömmlichen 3D-Druckern, die in der Regel Kunststoffe verwenden,"
            self.text_line_4 = "verwendet ein Metall-3D-Drucker Metallpulver als Druckmaterial."
            self.text_line_5 = "Das Verfahren, das für den 3D-Druck mit Metall verwendet wird,"
            self.text_line_6 = "heißt selektives Laserschmelzen (SLM)."
            self.init_room("DreiDDruck_Normal.jpg")
            self.update()

        if self.hitbox_water.contains(mouse_pos):
            self.text_line_1 = ""
            self.text_line_2 = ""
            self.text_line_3 = "WASSER MARSCH !!!!!"
            self.text_line_4 = ""
            self.text_line_5 = ""
            self.text_line_6 = ""

            self.init_room("DreiDDruck_Under_Water.jpg")
            self.play_sound("DreiDDrucker_Water_sound.mp3")

            self.update()

        if self.hitbox_notaus.contains(mouse_pos):
            self.text_line_1 = ""
            self.text_line_2 = "Das war der Notaus !"
            self.text_line_3 = ""
            self.text_line_4 = ""
            self.text_line_5 = "Alles Dunkel D:"
            self.text_line_6 = ""

            self.init_room("DreiDDruck_Dark_Room.jpg")
            self.play_sound("DreiDDruck_Lightswitch.mp3")

            self.update()
