# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui\shortcut_settings.ui'
#
# Created: Sun Feb 01 19:16:26 2015
#      by: PyQt4 UI code generator 4.10.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_ShortcutSettings(object):
    def setupUi(self, ShortcutSettings):
        ShortcutSettings.setObjectName(_fromUtf8("ShortcutSettings"))
        ShortcutSettings.setWindowModality(QtCore.Qt.NonModal)
        ShortcutSettings.resize(511, 127)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(ShortcutSettings.sizePolicy().hasHeightForWidth())
        ShortcutSettings.setSizePolicy(sizePolicy)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/plugins/ShortcutManager/icon.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        ShortcutSettings.setWindowIcon(icon)
        ShortcutSettings.setModal(True)
        self.verticalLayout = QtGui.QVBoxLayout(ShortcutSettings)
        self.verticalLayout.setSizeConstraint(QtGui.QLayout.SetMinAndMaxSize)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setSizeConstraint(QtGui.QLayout.SetMinAndMaxSize)
        self.gridLayout.setContentsMargins(-1, -1, -1, 0)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self._shortcutName_le = QtGui.QLineEdit(ShortcutSettings)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self._shortcutName_le.sizePolicy().hasHeightForWidth())
        self._shortcutName_le.setSizePolicy(sizePolicy)
        self._shortcutName_le.setText(_fromUtf8(""))
        self._shortcutName_le.setObjectName(_fromUtf8("_shortcutName_le"))
        self.gridLayout.addWidget(self._shortcutName_le, 0, 1, 1, 1)
        self.label_2 = QtGui.QLabel(ShortcutSettings)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 1)
        self.label = QtGui.QLabel(ShortcutSettings)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self._shortcutURI_le = QtGui.QLineEdit(ShortcutSettings)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self._shortcutURI_le.sizePolicy().hasHeightForWidth())
        self._shortcutURI_le.setSizePolicy(sizePolicy)
        self._shortcutURI_le.setObjectName(_fromUtf8("_shortcutURI_le"))
        self.gridLayout.addWidget(self._shortcutURI_le, 2, 1, 1, 1)
        self.label_3 = QtGui.QLabel(ShortcutSettings)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout.addWidget(self.label_3, 3, 0, 1, 1)
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setContentsMargins(0, -1, -1, -1)
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self._shortcutIcon_l = QtGui.QLabel(ShortcutSettings)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self._shortcutIcon_l.sizePolicy().hasHeightForWidth())
        self._shortcutIcon_l.setSizePolicy(sizePolicy)
        self._shortcutIcon_l.setLineWidth(0)
        self._shortcutIcon_l.setText(_fromUtf8(""))
        self._shortcutIcon_l.setPixmap(QtGui.QPixmap(_fromUtf8(":/ShortcutManager/icons/icon.png")))
        self._shortcutIcon_l.setScaledContents(False)
        self._shortcutIcon_l.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self._shortcutIcon_l.setIndent(0)
        self._shortcutIcon_l.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self._shortcutIcon_l.setObjectName(_fromUtf8("_shortcutIcon_l"))
        self.horizontalLayout_5.addWidget(self._shortcutIcon_l)
        self._changeIconBtn = QtGui.QPushButton(ShortcutSettings)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self._changeIconBtn.sizePolicy().hasHeightForWidth())
        self._changeIconBtn.setSizePolicy(sizePolicy)
        self._changeIconBtn.setObjectName(_fromUtf8("_changeIconBtn"))
        self.horizontalLayout_5.addWidget(self._changeIconBtn)
        self.pbSetDefaultIcon = QtGui.QPushButton(ShortcutSettings)
        self.pbSetDefaultIcon.setObjectName(_fromUtf8("pbSetDefaultIcon"))
        self.horizontalLayout_5.addWidget(self.pbSetDefaultIcon)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem)
        self.gridLayout.addLayout(self.horizontalLayout_5, 3, 1, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.buttonBox = QtGui.QDialogButtonBox(ShortcutSettings)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.buttonBox.sizePolicy().hasHeightForWidth())
        self.buttonBox.setSizePolicy(sizePolicy)
        self.buttonBox.setStyleSheet(_fromUtf8(""))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setCenterButtons(False)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(ShortcutSettings)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), ShortcutSettings.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), ShortcutSettings.reject)
        QtCore.QMetaObject.connectSlotsByName(ShortcutSettings)

    def retranslateUi(self, ShortcutSettings):
        ShortcutSettings.setWindowTitle(_translate("ShortcutSettings", "Shortcut settings", None))
        self.label_2.setText(_translate("ShortcutSettings", "URI:", None))
        self.label.setText(_translate("ShortcutSettings", "Name:", None))
        self.label_3.setText(_translate("ShortcutSettings", "Icon:", None))
        self._changeIconBtn.setText(_translate("ShortcutSettings", "Choose icon...", None))
        self.pbSetDefaultIcon.setText(_translate("ShortcutSettings", "Set default", None))

import resources_rc
