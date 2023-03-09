from PyQt6.QtCore import QRect, QPoint
from PyQt6.QtGui import QMouseEvent

from TemplateRoom import TemplateRoom

class MyRoom(TemplateRoom):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.init_room("90125637.jpg")

        self.offset_balloon_x = 900
        self.offset_balloon_y = 25
        self.offset_balloon_length = 500
        self.offset_balloon_width = 150

       #self.offset_mouth

        self.mouth_to_speech.append(QPoint(771, 429))
        self.mouth_to_speech.append(QPoint(self.offset_balloon_x + self.offset_balloon_width, self.offset_balloon_y + 50))
        self.mouth_to_speech.append(QPoint(self.offset_balloon_x + self.offset_balloon_width, self.offset_balloon_y + 150))

        self.hitbox_mouth = QRect(570, 475, 75, 75)
        self.append_hitbox(self.hitbox_mouth)

        self.text_line_1 = "Greetings!"
        self.text_line_2 = ""
        self.text_line_3 = "So long, and"
        self.text_line_4 = "Thanks for the fish"

    def mousePressEvent(self, ev: QMouseEvent) -> None:
        super(MyRoom, self).mousePressEvent(ev)

        mouse_pos = ev.pos()

        if self.hitbox_mouth.contains(mouse_pos):
            self.text_line_1 = "AUA"
            self.text_line_2 = ""
            self.text_line_3 = ""
            self.text_line_4 = ""
            self.text_line_5 = ""
            self.text_line_6 = "Du hast eine harte Rechte!"

            self.update()
