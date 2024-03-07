from PyQt6.QtCore import QRect
from PyQt6.QtGui import QMouseEvent

from TemplateRoom import TemplateRoom

class CNC(TemplateRoom):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.init_room("CNC.jpg")

        self.offset_balloon_x = 900
        self.offset_balloon_y = 25
        self.set_offset_mouth(1220, 384, 250, 50)

        self.hitbox_fraeser = QRect(710, 490, 65, 65)
        self.append_hitbox(self.hitbox_fraeser)

        self.text_line_1 = "Hallo, ich bin Philipp!"
        self.text_line_2 = ""
        self.text_line_3 = "Das ist unsere CNC-Werkstatt."
        self.text_line_4 = "Sehe dich gerne um, aber vergesse"
        self.text_line_5 = "deine Schutzbrille nicht."

        self.hitbox_monitor = QRect(950, 420, 130, 100)
        self.append_hitbox(self.hitbox_monitor)

        self.hitbox_schraubstock = QRect(650, 557, 85, 75)
        self.append_hitbox(self.hitbox_schraubstock)

        self.hitbox_rad = QRect(100, 595, 50, 50)
        self.append_hitbox(self.hitbox_rad)

    def mousePressEvent(self, ev: QMouseEvent) -> None:
        super(CNC, self).mousePressEvent(ev)

        mouse_pos = ev.pos()

        if self.hitbox_fraeser.contains(mouse_pos):
            self.text_line_1 = "Achtung der Fräser ist scharf!"
            self.text_line_2 = ""
            self.text_line_3 = ""
            self.text_line_4 = ""
            self.text_line_5 = "Nicht anfassen!"
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

        self.update()
