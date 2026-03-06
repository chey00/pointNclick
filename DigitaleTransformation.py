from PyQt6.QtCore import QRect
from PyQt6.QtGui import QMouseEvent
from TemplateRoom import TemplateRoom

# Gesprochener Text Hitbox_Kopf
'''
        self.text_line_1 = "Willkommen! Ich betreue hier an der SBS-Herzogenaurach"
        self.text_line_2 = "den Fachbereich für Digitale Transformation."
        self.text_line_3 = "Gemeinsam mit unseren angehenden Technikern und"
        self.text_line_4 = "Auszubildenden erarbeiten wir hier die Grundlagen der"
        self.text_line_5 = "modernen Industrierobotik. In meinem Unterricht führen wir"
        self.text_line_6 = "Sie theoretisch und praktisch in die Welt der"
        self.text_line_7 = "6-Achs-Roboter und Cobots ein."

        self.text_line_8 = "Wir analysieren Steuerungen, Wegmesssysteme,"
        self.text_line_9 = "Kinematik, Antriebe sowie modernste Sensorik."
        self.text_line_10 = "Mein Ziel ist es, dass jeder Schüler eigene"
        self.text_line_11 = "Programme entwickelt und wertvolle praktische"
        self.text_line_12 = "Erfahrung im Umgang mit Robotik-Systemen sammelt."
'''


class DigitaleTransformation(TemplateRoom):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.init_room("DigitaleTransformation.jpg")

        self.offset_balloon_x = 250
        self.offset_balloon_y = 50
        self.offset_balloon_length = 1050
        self.offset_balloon_width = 150
        self.set_offset_mouth(815, 327, 450, 80)

        # Hitboxes
        self.hitbox_mouth = QRect(734, 275, 81, 97)
        self.hitbox_roboter_01 = QRect(290, 250, 135, 265)
        self.hitbox_roboter_02 = QRect(935, 270, 160, 260)
        self.hitbox_notaus_01 = QRect(367, 671, 27, 25)
        self.hitbox_notaus_02 = QRect(1091, 652, 22, 20)
        self.hitbox_notaus_03 = QRect(704, 464, 17, 14)
        # self.hitbox_notaus_04 = QRect(933, 751, 20, 20)

        self.append_hitbox(self.hitbox_mouth)
        self.append_hitbox(self.hitbox_roboter_01)
        self.append_hitbox(self.hitbox_roboter_02)
        self.append_hitbox(self.hitbox_notaus_01)
        self.append_hitbox(self.hitbox_notaus_02)
        self.append_hitbox(self.hitbox_notaus_03)
        # self.append_hitbox(self.hitbox_notaus_04)

        # New Text for SBS-Herzogenaurach
        self.text_line_1 = "Willkommen im Fachbereich Robotertechnik der SBS-Herzogenaurach!"
        self.text_line_2 = "Hier im Raum Digitale Transformation bereiten wir angehende Techniker"
        self.text_line_3 = "und Auszubildende auf die Industrie 4.0 vor. An unseren modernen "
        self.text_line_4 = "kollaborativen Robotern lernen Sie alles über Steuerung,"
        self.text_line_5 = "Kinematik und Sensorik für Ihre berufliche Zukunft."

    def mousePressEvent(self, ev: QMouseEvent) -> None:
        super(DigitaleTransformation, self).mousePressEvent(ev)
        mouse_pos = ev.pos()

        # Logic remains the same
        if self.hitbox_mouth.contains(mouse_pos):
            self.play_sound("DigitaleTransformation_assistent.mp3")
        elif self.hitbox_roboter_01.contains(mouse_pos) or self.hitbox_roboter_02.contains(mouse_pos):
            self.play_sound("DigitaleTransformation_work.mp3")
        elif any(hb.contains(mouse_pos) for hb in
                 # [self.hitbox_notaus_01, self.hitbox_notaus_02, self.hitbox_notaus_03, self.hitbox_notaus_04]):
                 [self.hitbox_notaus_01, self.hitbox_notaus_02, self.hitbox_notaus_03]):
            self.play_sound("DigitaleTransformation_power.mp3")

        self.update()





