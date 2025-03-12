from PyQt6.QtCore import QRect
from PyQt6.QtGui import QMouseEvent

from TemplateRoom import TemplateRoom


class DreiDDruck(TemplateRoom):
    def __init__(self, found_key, parent=None):
        super(DreiDDruck, self).__init__(parent)

        self.__has_key = found_key

        self.init_room("DreiDDruck.jpg")

        self.offset_balloon_x = 25
        self.offset_balloon_y = 25
        self.offset_balloon_length = 1200
        self.offset_balloon_width = 160

        self.set_offset_mouth(965, 380, 600, 100)

        self.hitbox_printer = QRect(40, 255, 720, 550)
        self.append_hitbox(self.hitbox_printer)

        self.hitbox_keybox = QRect(1265, 330, 80, 110)
        self.append_hitbox(self.hitbox_keybox)

        self.text_line_1 = "Sehr geehrte Damen und Herren,"
        self.text_line_2 = "es ist mir eine große Freude,"
        self.text_line_3 = "dich in unserem Bereich für 3D-Drucker an unserer Schule begrüßen zu dürfen."
        self.text_line_4 = "Hier findest du nicht nur Kunststoff-3D-Drucker,"
        self.text_line_5 = "sondern auch eine herausragende Besonderheit."
        self.text_line_6 = "Das Herzstück dieses Bereiches ist zweifellos unser Metall-3D-Drucker."

    def mousePressEvent(self, ev: QMouseEvent) -> None:
        super(DreiDDruck, self).mousePressEvent(ev)

        mouse_pos = ev.pos()

        if self.hitbox_printer.contains(mouse_pos):
            self.text_line_1 = "Ein Metall-3D-Drucker ist ein industrieller 3D-Drucker,"
            self.text_line_2 = "der speziell für die Fertigung von Metallteilen entwickelt wurde."
            self.text_line_3 = "Im Gegensatz zu herkömmlichen 3D-Druckern, die in der Regel Kunststoffe verwenden,"
            self.text_line_4 = "verwendet ein Metall-3D-Drucker Metallpulver als Druckmaterial."
            self.text_line_5 = "Das Verfahren, das für den 3D-Druck mit Metall verwendet wird,"
            self.text_line_6 = "heißt selektives Laserschmelzen (SLM)."
            self.init_room("DreiDDruck.jpg")

            self.update()

        if self.hitbox_keybox.contains(mouse_pos):
            if self.__has_key:
                self.text_line_1 = "Der Schlüssel sperrt die Box auf."
                self.text_line_2 = ""
                self.text_line_3 = ""
                self.text_line_4 = ""
                self.text_line_5 = ""
                self.text_line_6 = ""
            else:
                self.text_line_1 = "Leider fehlt Ihnen noch der richtige Schlüssel."
                self.text_line_2 = ""
                self.text_line_3 = "Wo könnten Sie den Schlüssel nur finden?"
                self.text_line_4 = ""
                self.text_line_5 = ""
                self.text_line_6 = ""

            self.update()
