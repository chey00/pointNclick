from PyQt6.QtCore import pyqtSlot, Qt, QRandomGenerator
from PyQt6.QtGui import QPainter, QColor, QFont, QPixmap
from PyQt6.QtPrintSupport import QPrinter, QPrintDialog
from PyQt6.QtWidgets import QMainWindow, QMenuBar, QStatusBar, QMessageBox

from Aula import Aula
from Beck import Beck
from BueroVogel import BueroVogel
from CNC import CNC
from DreiDDruck import DreiDDruck
from EG101 import EG101
from EG102 import EG102
from Eingang import Eingang
from Erasmus import EG102Reinhart
from Fraesmaschine import Fraesmaschine
from Gang_I import Gang_I
from Gang_II import Gang_II
from Gang_III import Gang_III
from Gang_IV import Ganglinks
from Gang_V import GangTech
from Schulleitung import OSTD
from Stellvertretung import StvRoom
from Treppenhaus import Treppenhaus
from Verwaltung import Verwaltung
from Wegweiser import Wegweiser
from Lasergravierer import Lasergravierer
from Zwischenraum_Treppenhaus import Zwischenraum_Treppenhaus


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.__random_generator = QRandomGenerator().securelySeeded()

        self.__set_rooms = set()
        self.__number_of_easter_eggs = 4

        self.__status_bar = QStatusBar(parent)
        self.setStatusBar(self.__status_bar)

        self.setWindowTitle("Schulhausrundgang")
        self.showFullScreen()

        menu_bar = QMenuBar(self)
        settings = menu_bar.addMenu("Einstellungen")
        self.__hitbox_action = settings.addAction("Hitboxen anzeigen")
        self.__hitbox_action.setCheckable(True)

        self.__hitbox_action.setChecked(True)
        #self.__hitbox_action.setChecked(False)

        about = menu_bar.addMenu("Über")
        about_us = about.addAction("Projekt")
        about_us.triggered.connect(self.about_us)
        self.setMenuBar(menu_bar)

        self.central_widget = Wegweiser(parent)
        #self.central_widget = Eingang(parent)
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
        elif new_room == "Gang_V.jpg":
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
        elif new_room == "Stellvertretung.jpg":
            self.central_widget = StvRoom()
            self.setup_new_room()
        elif new_room == "Aula.jpg":
            self.central_widget = Aula()
            self.setup_new_room()
        elif new_room == "BueroVogel.jpg":
            self.central_widget = BueroVogel()
            self.setup_new_room()
        elif new_room == "Schulleitung.jpg":
            self.central_widget = OSTD()
            self.setup_new_room()
        elif new_room == "CNC.jpg":
            self.central_widget = CNC()
            self.setup_new_room()
        elif new_room == "EG101.jpg":
            self.central_widget = EG101()
            self.setup_new_room()
        elif new_room == "DreiDDruck_Normal.jpg":
            self.central_widget = DreiDDruck()
            self.setup_new_room()
        elif new_room == "Gang_IV.jpg":
            self.central_widget = Ganglinks()
            self.setup_new_room()
        elif new_room == "EG102Reinhart.jpg":
            self.central_widget = EG102Reinhart()
            self.setup_new_room()
        elif new_room == "Beck.png":
            self.central_widget = Beck()
            self.setup_new_room()
        elif new_room == "Zwischenraum_Treppenhaus.jpg":
            self.central_widget = Zwischenraum_Treppenhaus()
            self.setup_new_room()
        elif new_room == "Lasergravierer.jpg":
            self.central_widget = Lasergravierer()
            self.setup_new_room()


    @pyqtSlot(str)
    def change_room(self, old_room):
        if old_room == "Wegweiser.jpg":
            self.central_widget = Aula()
            self.setup_new_room()
        elif old_room == "Treppenhaus.jpg":
            self.central_widget = Zwischenraum_Treppenhaus()
            self.setup_new_room()
        elif old_room == "Lasergravierer.jpg":
            self.central_widget = Zwischenraum_Treppenhaus()
            self.setup_new_room()
        elif old_room == "Zwischenraum_Treppenhaus.jpg":
            self.central_widget = Wegweiser()
            self.setup_new_room()
        elif old_room == "Gang_V.jpg":
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
            self.central_widget = Ganglinks()
            self.setup_new_room()
        elif old_room == "EG102.jpg":
            self.central_widget = Gang_II()
            self.setup_new_room()
        elif old_room == "Verwaltung.jpg":
            self.central_widget = Aula()
            self.setup_new_room()
        elif old_room == "Stellvertretung.jpg":
            self.central_widget = Verwaltung()
            self.setup_new_room()
        elif old_room == "Aula.jpg":
            self.central_widget = Eingang()
            self.setup_new_room()
        elif old_room == "BueroVogel.jpg":
            self.central_widget = Gang_III()
            self.setup_new_room()
        elif old_room == "Schulleitung.jpg":
            self.central_widget = Verwaltung()
            self.setup_new_room()
        elif old_room == "CNC.jpg":
            self.central_widget = Gang_I()
            self.setup_new_room()
        elif old_room == "EG101.jpg":
            self.central_widget = GangTech()
            self.setup_new_room()
        elif old_room == "DreiDDruck_Normal.jpg":
            self.central_widget = Ganglinks()
            self.setup_new_room()
        elif old_room == "DreiDDruck_Dark_Room.jpg":
            self.central_widget = Ganglinks()
            self.setup_new_room()
        elif old_room == "DreiDDruck_Under_Water.jpg":
            self.central_widget = Ganglinks()
            self.setup_new_room()
        elif old_room == "Gang_IV.jpg":
            self.central_widget = Treppenhaus()
            self.setup_new_room()
        elif old_room == "BueroVogel.jpg":
            self.central_widget = Gang_III()
            self.setup_new_room()
        elif old_room == "Erasmus.jpg":
            self.central_widget = EG102()
            self.setup_new_room()
        elif old_room == "Beck.png":
            self.central_widget = Gang_III()
            self.setup_new_room()
        elif old_room == "Beck_fog.png":
            self.central_widget = Gang_III()
            self.setup_new_room()

    @pyqtSlot(str)
    def handler_easter_egg(self, room_name):
        self.__set_rooms.add(room_name)

        number_found_rooms = len(self.__set_rooms)

        if number_found_rooms < self.__number_of_easter_eggs:
            message = "Sie haben " + str(number_found_rooms) + " von " + str(self.__number_of_easter_eggs) + \
                      " Kaffeetassen gefunden!"

            self.__status_bar.showMessage(message)
        else:
            self.__status_bar.showMessage("Sie haben alle Kaffeetassen gefunden")

            msg_box = QMessageBox()
            msg_box.setText("Herzlichen Glückwunsch!")
            msg_box.setInformativeText("Sie haben alle Kaffeetassen gefunden. Holen Sie sich mit dem Ausdruck Ihre "
                                       "Kaffeetasse im Raum EG 23 ab.")

            msg_box.exec()

            self.print_voucher()

    def print_voucher(self):
        printer = QPrinter()

        print_dialog = QPrintDialog(printer)
        print_dialog.exec()

        painter = QPainter()
        painter.begin(printer)
        painter.setPen(QColor("black"))

        page_rect = printer.pageRect(QPrinter.Unit.DevicePixel)

        painter.setFont(QFont("Helvetica [Cronyx]", 36))

        text = "Gutschein"
        bounding_rect = painter.boundingRect(page_rect, Qt.AlignmentFlag.AlignHCenter, text)
        painter.drawText(bounding_rect, text)
        page_rect.adjust(0, bounding_rect.height(), 0, 0)

        painter.setFont(QFont("Helvetica [Cronyx]", 12))

        text = "Gegen Vorlage dieses Gutscheins erhalten Sie von unseren Studierenden eine gravierte Kaffeetasse."
        bounding_rect = painter.boundingRect(page_rect, Qt.AlignmentFlag.AlignLeft, text)
        painter.drawText(bounding_rect.adjusted(0, bounding_rect.height(), 0, bounding_rect.height()), text)
        page_rect.adjust(0, bounding_rect.height(), 0, 0)

        text = "Ihr indivdueller Gutscheincode lautet:"
        bounding_rect = painter.boundingRect(page_rect, Qt.AlignmentFlag.AlignLeft, text)
        painter.drawText(bounding_rect.adjusted(0, bounding_rect.height(), 0, bounding_rect.height()), text)
        page_rect.adjust(0, 2 * bounding_rect.height(), 0, 0)

        text = str(self.__random_generator.bounded(10, 99))
        text += "-"
        text += str(self.__random_generator.bounded(10, 99))
        text += "-"
        text += str(self.__random_generator.bounded(10, 99))
        text += "-"
        text += str(self.__random_generator.bounded(10, 99))
        text += "-"
        text += str(self.__random_generator.bounded(10, 99))
        text += "-"
        text += str(self.__random_generator.bounded(10, 99))
        bounding_rect = painter.boundingRect(page_rect, Qt.AlignmentFlag.AlignHCenter, text)
        painter.drawText(bounding_rect.adjusted(0, bounding_rect.height(), 0, bounding_rect.height()), text)
        page_rect.adjust(0, 2 * bounding_rect.height(), 0, 0)

        text = "Ihre Kaffeetasse können Sie im Raum EG 23 abholen."
        bounding_rect = painter.boundingRect(page_rect, Qt.AlignmentFlag.AlignLeft, text)
        painter.drawText(bounding_rect.adjusted(0, bounding_rect.height(), 0, bounding_rect.height()), text)
        page_rect.adjust(0, 2 * bounding_rect.height(), 0, 0)

        pixmap = QPixmap("logo.png").scaledToWidth(150, Qt.TransformationMode.SmoothTransformation)
        point = page_rect.bottomRight().toPoint()
        x = point.x() - pixmap.size().width() - 50
        y = point.y() - pixmap.size().height() - 50
        painter.drawPixmap(x, y, pixmap)

        painter.end()

    def about_us(self):
        msg_box = QMessageBox(self)
        msg_box.setText("Über das Programm")
        msg_box.setInformativeText("Unser virtueller Schulhausrundgang ist im Rahmen eines Projekts der Klasse FSWI-1"
                                   " im Schuljahr 2022/23 entstanden. Wir haben die App im Fach Programmieren erstellt"
                                   " und nutzen Python mit Qt.")
        msg_box.show()
