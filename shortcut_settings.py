# -*- coding: utf-8 -*-
"""
/***************************************************************************
 ShortcutManagerDialog
                                 A QGIS plugin
 This plugin create shortcuts in toolbar
                             -------------------
        begin                : 2014-07-18
        git sha              : $Format:%H$
        copyright            : (C) 2014 by NextGIS
        email                : info@nextgis.ru
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""

from .shortcut_utils import getShortcutIcon
from .shortcut_settings_ui_base import Ui_ShortcutSettings
from .__init__ import default_icons_dir

from qgis.PyQt.QtGui import QIcon
from qgis.PyQt.QtWidgets import QDialog, QFileDialog
from qgis.PyQt.QtCore import QObject, QSize

import os


class ShortcutSettings(QDialog, Ui_ShortcutSettings):
    def __init__(self, parent, shortcut):
        QDialog.__init__(self, parent)
        self.setupUi(self)

        self._shortcut = shortcut

        self._shortcutName_le.setText(self._shortcut.name)

        if self._shortcut.uri is not None:
            self._shortcutURI_le.setText(self._shortcut.uri)

        shortcutIcon = getShortcutIcon(self._shortcut.icon, self._shortcut.uri)
        self._shortcutIcon_l.setPixmap(shortcutIcon.pixmap(QSize(32, 32)))

        self._shortcutNewIcon = self._shortcut.icon
        self._changeIconBtn.clicked.connect(self._chooseIcon)
        self.pbSetDefaultIcon.clicked.connect(self._setDefaultIcon)

    def _chooseIcon(self):
        fileName = QFileDialog.getOpenFileName(
            self, self.tr("Select icon file"), default_icons_dir
        )
        if fileName != "":
            self._shortcutNewIcon = os.path.normpath(unicode(fileName))
            self._shortcutIcon_l.setPixmap(
                QIcon(self._shortcutNewIcon).pixmap(QSize(32, 32))
            )

    def _setDefaultIcon(self):
        self._shortcutNewIcon = None
        shortcutIcon = getShortcutIcon(
            self._shortcutNewIcon, self._shortcut.uri
        )
        self._shortcutIcon_l.setPixmap(shortcutIcon.pixmap(QSize(32, 32)))

    def _validatePage(self):
        isValid = True

        if self._shortcutName_le.text() == "":
            self._shortcutName_le.setPlaceholderText(
                self.tr("Please, fill this field")
            )
            isValid = False

        if self._shortcutURI_le.text() == "":
            self._shortcutURI_le.setPlaceholderText(
                self.tr("Please, fill this field")
            )
            isValid = False

        return isValid

    def accept(self):
        # print("ShortcutSettings accept")
        if self._validatePage() == False:
            return

        self.shortcutNewName = self._shortcutName_le.text()
        self.shortcutNewURI = self._shortcutURI_le.text()

        # print "self._shortcutNewIcon: ", self._shortcutNewIcon

        if self._shortcutNewIcon is not None:
            if (
                self._shortcutNewIcon.lower().find(default_icons_dir.lower())
                == 0
            ):
                self._shortcutNewIcon = self._shortcutNewIcon[
                    len(default_icons_dir) + 1 :
                ]

        self._shortcut.editShortcut(
            self.shortcutNewName, self.shortcutNewURI, self._shortcutNewIcon
        )

        QDialog.accept(self)
