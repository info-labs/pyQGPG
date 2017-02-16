from PyQt5.QtWidgets import QMainWindow

import gpgme

from models.gpgkeylistmodel import GPGKeyListModel

from ui.mainwindow import Ui_MainWindow


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ctx = gpgme.Context()

        self.keylistModel = GPGKeyListModel(self.ctx, self.ui.treeViewKeyList)
        self.ui.treeViewKeyList.setModel(self.keylistModel)
