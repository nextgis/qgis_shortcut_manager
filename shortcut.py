# -*- coding: utf-8 -*-

from PyQt4.QtCore import QObject, QSettings, pyqtSignal

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
        else:
            self._uri = uri
            self._icon = icon
            self.settings.setValue("%s/uri"%self._name,self._uri)
            self.settings.setValue("%s/icon"%self._name,self._icon)
        
    
    def delete(self):
        self.settings.remove(self._name)
        self.deleted.emit()
    
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