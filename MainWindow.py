from PyQt6.QtCore import pyqtSlot
from PyQt6.QtWidgets import QMainWindow, QMenuBar, QStatusBar, QMessageBox

from MyRoom import MyRoom
from KatzenRoom import KatzenRoom
from Wegweiser import Wegweiser
from Treppenhaus import Treppenhaus
from Gang_I import Gang_I
from Gang_II import Gang_II
from Gang_III import Gang_III
from GangTech import GangTech
from Aula import Aula
from Fraesmaschine import Fraesmaschine
from EG102 import EG102
from Verwaltung import Verwaltung
from StvRoom import StvRoom
from Eingang import Eingang
from BueroVogel import BueroVogel


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

        self.central_widget = Eingang(parent)
        self.setup_new_room()

    def setup_new_room(self):
        self.central_widget.setHitBoxVisible(self.__hitbox_action.isChecked())
        self.central_widget.leave_room.connect(self.change_room)
        self.central_widget.new_room.connect(self.renew_room)
        self.central_widget.found_easter_egg.connect(self.handler_easter_egg)
        self.__hitbox_action.toggled.connect(self.central_widget.setHitBoxVisible)
        self.setCentralWidget(self.central_widget)

    @pyqtSlot(str)
    def renew_room(self, new_room):
        if new_room == "Treppenhaus.jpg":
            self.central_widget = Treppenhaus()
            self.setup_new_room()
        elif new_room == "GangTech.jpg":
            self.central_widget = GangTech()
            self.setup_new_room()
        elif new_room == "Gang_I.jpg":
            self.central_widget = Gang_I()
            self.setup_new_room()
        elif new_room == "Gang_II.jpg":
            self.central_widget = Gang_II()
            self.setup_new_room()
        elif new_room == "Gang_III.jpg":
            self.central_widget = Gang_III()
            self.setup_new_room()
        elif new_room == "Wegweiser.jpg":
            self.central_widget = Wegweiser()
            self.setup_new_room()
        elif new_room == "Fraesmaschine.jpg":
            self.central_widget = Fraesmaschine()
            self.setup_new_room()
        elif new_room == "EG102.jpg":
            self.central_widget = EG102()
            self.setup_new_room()
        elif new_room == "Verwaltung.jpg":
            self.central_widget = Verwaltung()
            self.setup_new_room()
        elif new_room == "StvRoom.jpg":
            self.central_widget = StvRoom()
            self.setup_new_room()
        elif new_room == "Aula.jpg":
            self.central_widget = Aula()
            self.setup_new_room()
        elif new_room == "BueroVogel.jpg":
            self.central_widget = BueroVogel()
            self.setup_new_room()

    @pyqtSlot(str)
    def change_room(self, old_room):
        if old_room == "MyRoom.jpg":
            self.central_widget = KatzenRoom()
            self.setup_new_room()
        elif old_room == "KatzenRoom.jpg":
            self.central_widget = MyRoom()
            self.setup_new_room()
        elif old_room == "Wegweiser.jpg":
            self.central_widget = Aula()
            self.setup_new_room()
        elif old_room == "Treppenhaus.jpg":
            self.central_widget = Wegweiser()
            self.setup_new_room()
        elif old_room == "GangTech.jpg":
            self.central_widget = Wegweiser()
            self.setup_new_room()
        elif old_room == "Gang_I.jpg":
            self.central_widget = Treppenhaus()
            self.setup_new_room()
        elif old_room == "Gang_II.jpg":
            self.central_widget = GangTech()
            self.setup_new_room()
        elif old_room == "Gang_III.jpg":
            self.central_widget = Gang_II()
            self.setup_new_room()
        elif old_room == "Wegweiser.jpg":
            self.central_widget = Aula()
            self.setup_new_room()
        elif old_room == "Fraesmaschine.jpg":
            self.central_widget = Gang_I()
            self.setup_new_room()
        elif old_room == "EG102.jpg":
            self.central_widget = Gang_II()
            self.setup_new_room()
        elif old_room == "Verwaltung.jpg":
            self.central_widget = Aula()
            self.setup_new_room()
        elif old_room == "StvRoom.jpg":
            self.central_widget = Verwaltung()
            self.setup_new_room()
        elif old_room == "Aula.jpg":
            self.central_widget = Eingang()
            self.setup_new_room()
        elif old_room == "BueroVogel.jpg":
            self.central_widget = Gang_III()
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

