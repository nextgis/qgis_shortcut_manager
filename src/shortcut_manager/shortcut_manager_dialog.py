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

from .shortcut_creator import ShortcutCreator
from .ui.ui_shortcut_manager_dialog_ui_base import Ui_ShortcutManagerDialog

from qgis.PyQt.QtGui import QIcon
from qgis.PyQt.QtWidgets import QDialog


class ShortcutManagerDialog(QDialog, Ui_ShortcutManagerDialog):
    # def __init__(self, parent, createShortcutFunction):
    def __init__(self, parent, manager):
        """Constructor."""
        QDialog.__init__(self)

        self.setupUi(self)
        self.setWindowIcon(QIcon(":/icons/icon.png"))
        self.pushButton.clicked.connect(self.createShortcut)

        # self._createShortcutFunction = createShortcutFunction
        self._manager = manager

    def addShortcut(self, shortcutWidget):
        self.shorcutWidgetsContainer.addWidget(shortcutWidget)

    def createShortcut(self):
        # dlg = ShortcutCreator(self, self._createShortcutFunction)
        dlg = ShortcutCreator(self, self._manager.createShortcut)
        dlg.show()
        # Run the dialog event loop
        result = dlg.exec_()
        # See if OK was pressed
        if result:
            pass
