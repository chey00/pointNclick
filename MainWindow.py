from PyQt6.QtCore import pyqtSlot
from PyQt6.QtWidgets import QMainWindow, QMenuBar, QStatusBar, QMessageBox
#from TemplateRoom import TemplateRoom
from MyRoom import MyRoom
from KatzenRoom import KatzenRoom

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.__set_rooms = set()
        self.__number_of_easter_eggs = 5

        self.__status_bar = QStatusBar(parent)
        self.setStatusBar(self.__status_bar)

        self.setWindowTitle("Schulhausrundgang")
        self.showFullScreen()

        menuBar = QMenuBar(self)
        einstellungen = menuBar.addMenu("Einstellungen")
        self.__hitbox_action = einstellungen.addAction("Hitboxen anzeigen")
        self.__hitbox_action.setCheckable(True)
        self.__hitbox_action.setChecked(True)
        self.setMenuBar(menuBar)

        self.central_widget = MyRoom(parent)
        self.setup_new_room()

    def setup_new_room(self):
        self.central_widget.setHitBoxVisible(self.__hitbox_action.isChecked())
        self.central_widget.leave_room.connect(self.change_room)
        self.central_widget.found_easter_egg.connect(self.handler_easter_egg)
        self.__hitbox_action.toggled.connect(self.central_widget.setHitBoxVisible)

        self.setCentralWidget(self.central_widget)

    @pyqtSlot(str)
    def change_room(self, old_room):
        print(old_room)

        if old_room == "90125637.jpg":
            self.central_widget = KatzenRoom()
            self.setup_new_room()
        elif old_room == "katze.jpg":
            self.central_widget = MyRoom()
            self.setup_new_room()

    @pyqtSlot(str)
    def handler_easter_egg(self, room_name):
        self.__set_rooms.add(room_name)

        number_found_rooms = len(self.__set_rooms)

        if number_found_rooms < self.__number_of_easter_eggs:
            message = "Sie haben " + str(number_found_rooms) + " von " + str(self.__number_of_easter_eggs) + " Kaffeetassen gefunden!"

            self.__status_bar.showMessage(message)
        else:
            msgBox = QMessageBox()
            msgBox.setText("Herzlichen Glückwunsch!")
            msgBox.setInformativeText("Sie haben alle Kaffeetassen gefunden. Holen Sie sich mit dem Kennwort super_geheim Ihre Kaffeetasse im Raum XYZ.")

            msgBox.exec()

