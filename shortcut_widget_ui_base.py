# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui\shortcut_widget.ui'
#
# Created: Mon Aug 04 16:21:08 2014
#      by: PyQt4 UI code generator 4.8.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_ShortcutWidget(object):
    def setupUi(self, ShortcutWidget):
        ShortcutWidget.setObjectName(_fromUtf8("ShortcutWidget"))
        ShortcutWidget.resize(300, 41)
        self.horizontalLayout = QtGui.QHBoxLayout(ShortcutWidget)
        self.horizontalLayout.setSizeConstraint(QtGui.QLayout.SetFixedSize)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.deleteButton = QtGui.QPushButton(ShortcutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.deleteButton.sizePolicy().hasHeightForWidth())
        self.deleteButton.setSizePolicy(sizePolicy)
        self.deleteButton.setObjectName(_fromUtf8("deleteButton"))
        self.horizontalLayout.addWidget(self.deleteButton)
        self.editButton = QtGui.QPushButton(ShortcutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.editButton.sizePolicy().hasHeightForWidth())
        self.editButton.setSizePolicy(sizePolicy)
        self.editButton.setObjectName(_fromUtf8("editButton"))
        self.horizontalLayout.addWidget(self.editButton)
        self.shortcutIcon = QtGui.QLabel(ShortcutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.shortcutIcon.sizePolicy().hasHeightForWidth())
        self.shortcutIcon.setSizePolicy(sizePolicy)
        self.shortcutIcon.setStyleSheet(_fromUtf8("margin-left:25px"))
        self.shortcutIcon.setText(_fromUtf8(""))
        self.shortcutIcon.setPixmap(QtGui.QPixmap(_fromUtf8(":/ShortcutManager/icons/default-shortcut-desk.png")))
        self.shortcutIcon.setObjectName(_fromUtf8("shortcutIcon"))
        self.horizontalLayout.addWidget(self.shortcutIcon)
        self.shortcutName = QtGui.QLabel(ShortcutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.shortcutName.sizePolicy().hasHeightForWidth())
        self.shortcutName.setSizePolicy(sizePolicy)
        self.shortcutName.setObjectName(_fromUtf8("shortcutName"))
        self.horizontalLayout.addWidget(self.shortcutName)

        self.retranslateUi(ShortcutWidget)
        QtCore.QMetaObject.connectSlotsByName(ShortcutWidget)

    def retranslateUi(self, ShortcutWidget):
        ShortcutWidget.setWindowTitle(QtGui.QApplication.translate("ShortcutWidget", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.deleteButton.setText(QtGui.QApplication.translate("ShortcutWidget", "Delete", None, QtGui.QApplication.UnicodeUTF8))
        self.editButton.setText(QtGui.QApplication.translate("ShortcutWidget", "Edit", None, QtGui.QApplication.UnicodeUTF8))
        self.shortcutName.setText(QtGui.QApplication.translate("ShortcutWidget", "shortcutName", None, QtGui.QApplication.UnicodeUTF8))

import resources_rc
