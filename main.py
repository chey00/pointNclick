import sys

from PyQt6.QtCore import Qt, QThread
from PyQt6.QtGui import QPixmap, QColor
from PyQt6.QtWidgets import QApplication, QSplashScreen

from MainWindow import MainWindow
# All you need is
# https://doc.qt.io/qtforpython/

app = QApplication(sys.argv)

splash = QSplashScreen(QPixmap("logo.png"))
splash.show()

app.processEvents()
#QThread.sleep(2)

main_window = MainWindow()
splash.finish(main_window)
main_window.show()
sys.exit(app.exec())
