# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui\shortcut_manager_dialog_ui_base.ui'
#
# Created: Mon Aug 04 17:03:49 2014
#      by: PyQt4 UI code generator 4.8.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_ShortcutManagerDialog(object):
    def setupUi(self, ShortcutManagerDialog):
        ShortcutManagerDialog.setObjectName(_fromUtf8("ShortcutManagerDialog"))
        ShortcutManagerDialog.resize(530, 397)
        self.verticalLayout = QtGui.QVBoxLayout(ShortcutManagerDialog)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.scrollArea = QtGui.QScrollArea(ShortcutManagerDialog)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName(_fromUtf8("scrollArea"))
        self.scrollAreaWidgetContents = QtGui.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 510, 329))
        self.scrollAreaWidgetContents.setObjectName(_fromUtf8("scrollAreaWidgetContents"))
        self.layout = QtGui.QVBoxLayout(self.scrollAreaWidgetContents)
        self.layout.setObjectName(_fromUtf8("layout"))
        self.shorcutWidgetsContainer = QtGui.QVBoxLayout()
        self.shorcutWidgetsContainer.setObjectName(_fromUtf8("shorcutWidgetsContainer"))
        self.layout.addLayout(self.shorcutWidgetsContainer)
        self.label_2 = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.label_2.setText(_fromUtf8(""))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.layout.addWidget(self.label_2)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout.addWidget(self.scrollArea)
        self.label = QtGui.QLabel(ShortcutManagerDialog)
        self.label.setText(_fromUtf8(""))
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout.addWidget(self.label)
        self.pushButton = QtGui.QPushButton(ShortcutManagerDialog)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.verticalLayout.addWidget(self.pushButton)

        self.retranslateUi(ShortcutManagerDialog)
        QtCore.QMetaObject.connectSlotsByName(ShortcutManagerDialog)

    def retranslateUi(self, ShortcutManagerDialog):
        ShortcutManagerDialog.setWindowTitle(QtGui.QApplication.translate("ShortcutManagerDialog", "Shortcut manager", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton.setText(QtGui.QApplication.translate("ShortcutManagerDialog", "Create shortcut", None, QtGui.QApplication.UnicodeUTF8))

