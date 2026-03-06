from PyQt6.QtCore import QRect
from PyQt6.QtGui import QMouseEvent

from TemplateRoom import TemplateRoom

class CNC(TemplateRoom):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.init_room("CNC.jpg")

        self.offset_balloon_x = 920
        self.offset_balloon_y = 40
        self.set_offset_mouth(1250, 340, 250, 50)

        self.hitbox_fraeser = QRect(575,360, 65, 65)
        self.append_hitbox(self.hitbox_fraeser)

        self.text_line_1 = "Hallo, ich bin Patrick!"
        self.text_line_2 = "Das ist unsere CNC-Werkstatt."
        self.text_line_3 = "Hier lernen wir die Grundlagen"
        self.text_line_4 = "des Fräsens."
        self.text_line_5 = "Schaue dich gerne um, aber bitte"
        self.text_line_6 = "vergesse deine Schutzbrille nicht."

        self.hitbox_monitor = QRect(990, 330, 130, 100)
        self.append_hitbox(self.hitbox_monitor)

        self.hitbox_schraubstock = QRect(490, 440, 85, 75)
        self.append_hitbox(self.hitbox_schraubstock)

        self.hitbox_rad = QRect(980, 580, 50, 50)
        self.append_hitbox(self.hitbox_rad)

        self.hitbox_leitung = QRect(680, 200, 70, 70)
        self.append_hitbox(self.hitbox_leitung)

    def mousePressEvent(self, ev: QMouseEvent) -> None:
        super(CNC, self).mousePressEvent(ev)

        mouse_pos = ev.pos()

        if self.hitbox_fraeser.contains(mouse_pos):
            self.text_line_1 = "Hier werden die Fräser eingespannt"
            self.text_line_2 = "Vorsicht! Die Fräser sind scharf"
            self.text_line_3 = ""
            self.text_line_4 = ""
            self.text_line_5 = "Bitte immer Handschuhe anziehen!"
        elif self.hitbox_monitor.contains(mouse_pos):
            self.text_line_1 = "Das ist der Steuerungsmonitor."
            self.text_line_2 = "Hier bedienst du die Maschine."
            self.text_line_3 = ""
            self.text_line_4 = "Der rote Knopf ist der 'Not-Aus',"
            self.text_line_5 = "er stoppt die Maschine sofort."
            self.text_line_6 = ""
        elif self.hitbox_schraubstock.contains(mouse_pos):
            self.text_line_1 = "Hier siehst du den"
            self.text_line_2 = "Maschinenschraubstock."
            self.text_line_3 = ""
            self.text_line_4 = "Denke immer daran deine"
            self.text_line_5 = "Werkstücke gut zu befestigen!"
            self.text_line_6 = ""
        elif self.hitbox_rad.contains(mouse_pos):
            self.text_line_1 = "Das ist ein Handrad."
            self.text_line_2 = ""
            self.text_line_3 = "Hiermit kannst du die X-Achse der"
            self.text_line_4 = "Fräsmaschine manuell steuern."
            self.text_line_5 = ""
            self.text_line_6 = ""
        elif self.hitbox_leitung.contains(mouse_pos):
            self.text_line_1 = "Das ist eine Leitung."
            self.text_line_2 = "Hier wird Kühlmittel durchgeleitet."
            self.text_line_3 = "Wichtig um die Lebensdauer"
            self.text_line_4 = "eurer Werkzeuge zu verbessern."
            self.text_line_5 = ""
            self.text_line_6 = ""

        self.update()
