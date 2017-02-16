from PyQt5.QtCore import Qt
from PyQt5.QtCore import QVariant
from PyQt5.QtCore import QModelIndex

from .abstract import AbstractItemModel


class GPGKeyListModel(AbstractItemModel):
    def __init__(self, ctx, parent=None):
        super().__init__(parent)
        self.ctx = ctx
        self.keylist = list(self.ctx.keylist())
        # keylist x name-email-comment
        self.setItemSize(len(self.keylist), 3)

    def hasChildren(self, parent=QModelIndex()):
        # TODO
        return not parent.isValid()

    def headerData(self, section, orientation, role=Qt.DisplayRole):
        if role != Qt.DisplayRole:
            return QVariant()
        if orientation == Qt.Vertical:
            return QVariant(section)
        if section == 0:
            return QVariant("name")
        elif section == 1:
            return QVariant("email")
        elif section == 2:
            return QVariant("comment")
        return QVariant(section)

    def data(self, index=QModelIndex(), role=Qt.DisplayRole):
        if role != Qt.DisplayRole:
            return QVariant()
        row = list(self.keylist)[index.row()]
        if index.column() == 0:
            return QVariant(row.uids[0].name)
        elif index.column() == 1:
            return QVariant(row.uids[0].email)
        elif index.column() == 2:
            return QVariant(row.uids[0].comment)
        return QVariant()
