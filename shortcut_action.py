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

import sys
import subprocess
import webbrowser
import functools

from PyQt4.QtGui import QAction, QMessageBox
from PyQt4.QtCore import QObject, SIGNAL

from shortcut_utils import getShortcutIcon, getShortcutType

class ShorcutAction(QAction):
    def __init__(self, iface, shortcut):
        self._iface = iface
        QAction.__init__(self, self._iface.mainWindow())
        
        self._shortcut = shortcut
        
        self.setEnabled(True)
        
        QObject.connect(self._shortcut, SIGNAL("updated()"), self.__shortcutUpdated)
        QObject.connect(self._shortcut, SIGNAL("deleted()"), self.__shortcutDeleted)
        
        self.__shortcutUpdated()
        
        self._iface.addToolBarIcon(self)
        
        self.triggered.connect(self._triggeredFunction)
    
    def __shortcutUpdated(self):
        self.setIcon(getShortcutIcon(self._shortcut.icon, self._shortcut.uri))
        self.setText(self._shortcut.name)
        
        shortcutType = getShortcutType(self._shortcut.uri)

        if shortcutType == "desktop":
            #self._callbackFunction = functools.partial(self._runApplication, self._shortcut.uri, self._shortcut.directory)
            self._callbackFunction = functools.partial(self._runApplication, self._shortcut.uri)
        elif shortcutType == "web":
            self._callbackFunction = functools.partial(self._runBrowser, self._shortcut.uri)
        else:
            self._callbackFunction = lambda: QMessageBox.information(
                                            self._iface.mainWindow(), 
                                            'Unknown shortcut type',
                                            'Unknown shortcut type',
                                            QMessageBox.Ok)
    def _triggeredFunction(self):
        self._callbackFunction()
    
    def __shortcutDeleted(self):
        self.setParent(None)
        self._iface.removeToolBarIcon(self)
    
    def _runBrowser(self, url):
        webbrowser.open(url)
        
    def _runApplication(self, app):
        subprocess.Popen([app.encode(sys.getfilesystemencoding())])