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
import os

from PyQt4.QtCore import QObject, QSettings, pyqtSignal

from qgis.core import QgsMessageLog

def shortcutsFromSettings():
    shortcuts = []
    
    settings = QSettings()
    settings.beginGroup('/NextGIS/ShortcutManager/shortcuts')
    shortcuts_names = settings.childGroups()
    for shortcut_name in shortcuts_names:
        shortcuts.append(Shorcut(shortcut_name))
        
    return shortcuts

class Shorcut(QObject):
    updated = pyqtSignal(name = "updated")
    deleted = pyqtSignal(name = "deleted")
    
    def __init__(self, name, uri = None, icon = None):
        super(Shorcut, self).__init__()
        
        self.settings = QSettings()
        self.settings.beginGroup('/NextGIS/ShortcutManager/shortcuts')
        
        self._name = name
        
        if self._name in self.settings.childGroups():
            self._uri = self.settings.value("%s/uri"%self._name)
            self._icon = self.settings.value("%s/icon"%self._name)
            #self._directory = self.settings.value("%s/_directory"%self._name)
            
            QgsMessageLog.logMessage(
                "Shortcuts manager. Load shortcut with name: %s"% self._name,
                None, QgsMessageLog.INFO)
        else:
            self._uri = uri
            self._icon = icon
            self.settings.setValue("%s/uri"%self._name, self._uri)
            self.settings.setValue("%s/icon"%self._name, self._icon)
            #self.settings.setValue("%s/directory"%self._name, self._directory)
            QgsMessageLog.logMessage(
                "Shortcuts manager. Create shortcut with name: %s"% self._name,
                None, QgsMessageLog.INFO)
    
    def delete(self):
        self.settings.remove(self._name)
        self.deleted.emit()
    
    #def editShortcut(self, name, uri, icon, directory):
    def editShortcut(self, name, uri, icon):
        if self._name != name:
            self.settings.remove(self._name)
            
            self._name =name
            self.settings.setValue("%s/uri"%self._name,self._uri)
            self.settings.setValue("%s/icon"%self._name,self._icon)
        
        if self._uri != uri:
            self._uri = uri
            self.settings.setValue("%s/uri"%self._name,self._uri)
        
        if self._icon != icon:
            self._icon = icon
            self.settings.setValue("%s/icon"%self._name,self._icon)
        
        QgsMessageLog.logMessage(
                "Shortcuts manager. Edit shortcut with name: %s"% self._name,
                None, QgsMessageLog.INFO)
        #if self._directory != directory:
        #    self._directory = directory
        #    self.settings.setValue("%s/directory"%self._name,self._directory)
            
        self.updated.emit()
    
    @property
    def name(self):
        return self._name
    
    @property
    def uri(self):
        return self._uri
    
    @property
    def icon(self):
        return self._icon
    
    #@property
    #def directory(self):
    #    return self._directory