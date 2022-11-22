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
from .shortcut_settings import ShortcutSettings
from .shortcut_widget_ui_base import Ui_ShortcutWidget

from qgis.PyQt.QtWidgets import QWidget
from qgis.PyQt.QtCore import QObject, QSize


class ShortcutWidget(QWidget, Ui_ShortcutWidget):
    def __init__(self, parent, shortcut):
        QWidget.__init__(self)
        self.setupUi(self)

        self._shortcut = shortcut

        self.__shortcutUpdated()

        self.editButton.clicked.connect(self.editShortcut)
        self.deleteButton.clicked.connect(self.deleteShortcut)
        self._shortcut.updated.connect(self.__shortcutUpdated)
        self._shortcut.deleted.connect(self.__shortcutDeleted)

    def editShortcut(self):
        dlg = ShortcutSettings(self, self._shortcut)
        dlg.show()
        # Run the dialog event loop
        result = dlg.exec_()
        # See if OK was pressed
        if result:
            # Do something useful here - delete the line containing pass and
            # substitute with your code.
            # self._loadData(shortcutName)
            pass

    def deleteShortcut(self):
        self._shortcut.delete()

    def __shortcutUpdated(self):
        shortcutIcon = getShortcutIcon(
            self._shortcut.icon,
            self._shortcut.uri)
        self.shortcutIcon.setPixmap(shortcutIcon.pixmap(QSize(32, 32)))

        self.shortcutName.setText(self._shortcut.name)

    def __shortcutDeleted(self):
        self.setParent(None)
