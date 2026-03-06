from PyQt6.QtCore import QRect, pyqtSignal
from PyQt6.QtGui import QMouseEvent
from TemplateRoom import TemplateRoom


class DreiDDruck(TemplateRoom):
    found_machine_key = pyqtSignal()
    machine_turned_on = pyqtSignal()

    def __init__(self, found_key, machine_key_taken, machine_is_on=False, parent=None):
        super(DreiDDruck, self).__init__(parent)

        self.__has_gang_key = found_key
        self.__key_taken = machine_key_taken
        self.__is_on = machine_is_on
        self.__box_offen = False

        self.__printer_counter = 0

        if self.__is_on:
            self.init_room("DreiDDruck_An.jpg")
        else:
            self.init_room("DreiDDruck.jpg")

        self.offset_balloon_x = 25
        self.offset_balloon_y = 25
        self.offset_balloon_length = 1200
        self.offset_balloon_width = 160
        self.set_offset_mouth(965, 380, 600, 100)

        self.hitbox_printer = QRect(36, 328, 344, 160)
        self.append_hitbox(self.hitbox_printer)

        self.hitbox_keybox = QRect(1265, 330, 80, 110)
        self.append_hitbox(self.hitbox_keybox)

        self.hitbox_notaus = QRect(395, 340, 35, 45)
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

        if self.hitbox_printer.contains(mouse_pos):
            if self.__key_taken:
                self.__is_on = True
                self.text_line_1 = "Du steckst den Schlüssel ein."
                self.text_line_2 = "Der LASERTEC 30 SLM fährt hoch und ist bereit!"
                self.text_line_3 = ""
                self.text_line_4 = ""
                self.text_line_5 = ""
                self.text_line_6 = ""
                self.init_room("DreiDDruck_An.jpg")
                self.machine_turned_on.emit()
            else:
                if self.__printer_counter == 0:
                    self.text_line_1 = "Der 3D Drucker ist momentan ausgeschaltet."
                    self.text_line_2 = "Sie brauchen einen Schlüssel zum Einschalten."
                    self.text_line_3 = "Schauen Sie in den Schlüsselkasten nach."
                    self.text_line_4 = ""
                    self.text_line_5 = ""
                    self.text_line_6 = "                                          weiter >"
                    self.__printer_counter = 1
                elif self.__printer_counter == 1:
                    self.text_line_1 = "Ein Metall-3D-Drucker ist ein industrieller 3D-Drucker,"
                    self.text_line_2 = "der speziell für die Fertigung von Metallteilen entwickelt wurde."
                    self.text_line_3 = "Im Gegensatz zu herkömmlichen 3D-Druckern, die Kunststoffe verwenden,"
                    self.text_line_4 = "verwendet ein Metall-3D-Drucker Metallpulver als Druckmaterial."
                    self.text_line_5 = "Das Verfahren heißt selektives Laserschmelzen (SLM)."
                    self.text_line_6 = ""
                    self.__printer_counter = 0
            self.update()

        if self.hitbox_notaus.contains(mouse_pos):
            if self.__is_on:
                self.play_sound("DigitaleTransformation_power.mp3")

                self.__is_on = False
                self.init_room("DreiDDruck.jpg")
                self.text_line_1 = "NOT-AUS BETÄTIGT!"
                self.text_line_2 = "Die Maschine wurde sofort gestoppt."
                self.text_line_3 = "Sie müssen sie erst wieder mit dem Schlüssel starten."
                self.text_line_4 = ""
                self.text_line_5 = ""
                self.text_line_6 = ""
            else:
                self.text_line_1 = "Die Maschine ist bereits ausgeschaltet."
                self.text_line_2 = "Der Not-Aus hat momentan keine Funktion."
                self.text_line_3 = ""
                self.text_line_4 = ""
                self.text_line_5 = ""
                self.text_line_6 = ""
            self.update()

        if self.hitbox_keybox.contains(mouse_pos):
            self.__printer_counter = 0
            if self.__key_taken:
                self.text_line_1 = "Die Box ist leer."
                self.text_line_2 = "Du hast den Schlüssel bereits rausgenommen."
                self.text_line_3 = ""
                self.text_line_4 = ""
                self.text_line_5 = ""
                self.text_line_6 = ""
            elif self.__has_gang_key and not self.__box_offen:
                self.text_line_1 = "Der Schlüssel aus dem Gang sperrt die Box auf."
                self.text_line_2 = "Der Schlüssel für den 3D Drucker kommt zum Vorschein."
                self.text_line_3 = ""
                self.text_line_4 = ""
                self.text_line_5 = ""
                self.text_line_6 = ""
                self.init_room("DreiDDruck_Schluessel.jpg")
                self.__box_offen = True
            elif self.__box_offen:
                self.text_line_1 = "Du hast den 3D Drucker Schlüssel an dich genommen."
                self.text_line_2 = ""
                self.text_line_3 = ""
                self.text_line_4 = ""
                self.text_line_5 = ""
                self.text_line_6 = ""
                if not self.__is_on:
                    self.init_room("DreiDDruck.jpg")
                self.__box_offen = False
                self.__key_taken = True
                self.found_machine_key.emit()
            else:
                self.text_line_1 = "Leider fehlt dir noch der richtige Schlüssel."
                self.text_line_2 = "Schau dich doch nochmal im Gang um."
                self.text_line_3 = ""
                self.text_line_4 = ""
                self.text_line_5 = ""
                self.text_line_6 = ""
            self.update()