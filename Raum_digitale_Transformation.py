from PyQt6.QtCore import QRect
from PyQt6.QtGui import QMouseEvent
from TemplateRoom import TemplateRoom

# Gesprochener Text Hitbox_Kopf
'''
    self.text_line_1 = "Hallo, mein Name ist Lisa Krickhahn und "
    self.text_line_2 = "ich habe im zweiten Jahr meines Mechatronik-"
    self.text_line_3 = "Technikers mit meinen Mitschülern der Klasse FSMT-2 "
    self.text_line_4 = "im Rahmen des Faches Robotertechnik die Möglichkeit "
    self.text_line_5 = "gehabt, einen Einblick in die Welt der 6-Achs-Roboter, "
    self.text_line_6 = "mithilfe unserer neuen kollaborativen Roboter zu "
    self.text_line_7 = "erhalten. In diesem Fach lernen wir als angehende "

    self.text_line_8 = "Techniker die Steuerung, Wegmesssysteme, "
    self.text_line_9 = "Kinematik, Antriebe und Sensorik kennen. So können  "
    self.text_line_10 = "wir bereits erste eigene Programme entwickeln und "
    self.text_line_11 = "praktische Erfahrungen im Umgang mit Robotik  "
    self.text_line_12 = "Systemen sammeln."
'''

class Raum_digitale_Transformation(TemplateRoom):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.init_room("Raum_digitale_Transformation.jpg")

        self.offset_balloon_x = 200
        self.offset_balloon_y = 150
        self.offset_balloon_length = 1050
        self.offset_balloon_width = 150
        self.set_offset_mouth(705,482,450,80)

        self.hitbox_mouth = QRect(616, 448, 75, 75)
        self.append_hitbox(self.hitbox_mouth)

        self.hitbox_roboter_01 = QRect(203, 397, 190, 200)
        self.append_hitbox(self.hitbox_roboter_01)

        self.hitbox_roboter_02 = QRect(800, 397, 100, 200)
        self.append_hitbox(self.hitbox_roboter_02)

        self.hitbox_notaus_01 = QRect(279, 795, 20, 20)
        self.append_hitbox(self.hitbox_notaus_01)

        self.hitbox_notaus_02 = QRect(465, 523, 20, 20)
        self.append_hitbox(self.hitbox_notaus_02)

        self.hitbox_notaus_03 = QRect(983, 508, 20, 20)
        self.append_hitbox(self.hitbox_notaus_03)

        self.hitbox_notaus_04 = QRect(933, 751, 20, 20)
        self.append_hitbox(self.hitbox_notaus_04)
        
        self.text_line_1 = "Im Rahmen des Faches Robotertechnik erhalten Schüler "
        self.text_line_2 = "in diesem Raum die Möglichkeit, mit den neuen " 
        self.text_line_3 = "kollaborativen Robotern, die Themengebiete: Steuerung, " 
        self.text_line_4 = "Wegmesssysteme, Kinematik, Antriebe und "
        self.text_line_5 = "Sensorik kennenzulernen."
    

    def mousePressEvent(self, ev: QMouseEvent) -> None:
        super(Raum_digitale_Transformation, self).mousePressEvent(ev)

        mouse_pos = ev.pos()

        if self.hitbox_mouth.contains(mouse_pos):
            #self.stop_sound()
            self.play_sound("Raum_digitale_Transformation_Vorlese_assistent.mp3")
            self.update()
        if self.hitbox_roboter_01.contains(mouse_pos):
            #self.stop_sound()
            self.play_sound("Raum_digitale_Transformation_works.mp3")
            self.update()
        if self.hitbox_roboter_02.contains(mouse_pos):
            #self.stop_sound()
            self.play_sound("Raum_digitale_Transformation_works.mp3")
            self.update()
        if self.hitbox_notaus_01.contains(mouse_pos):
            #self.stop_sound()
            self.play_sound("Raum_digitale_Transformation_power-down.mp3")
            self.update()
        if self.hitbox_notaus_02.contains(mouse_pos):
            #self.stop_sound()
            self.play_sound("Raum_digitale_Transformation_power-down.mp3")
            self.update()
        if self.hitbox_notaus_03.contains(mouse_pos):
            #self.stop_sound()
            self.play_sound("Raum_digitale_Transformation_power-down.mp3")
            self.update()
        if self.hitbox_notaus_04.contains(mouse_pos):
            #self.stop_sound()
            self.play_sound("Raum_digitale_Transformation_power-down.mp3")
            self.update()






