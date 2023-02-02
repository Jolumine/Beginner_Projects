from PyQt5.QtWidgets import QApplication

from .templates.Home import Home

import sys

def main():
    app = QApplication(sys.argv)
    home = Home()
    sys.exit(app.exec_())
    