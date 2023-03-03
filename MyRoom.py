from TemplateRoom import TemplateRoom

class MyRoom(TemplateRoom):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.offset_balloon_x = 200
        self.offset_balloon_y = 100
        self.offset_balloon_length = 300
        self.offset_balloon_width = 100

        self.text_line_1 = "Greetings!"
        self.text_line_2 = ""
        self.text_line_3 = "So long, and"
        self.text_line_4 = "Thanks for the fish"
