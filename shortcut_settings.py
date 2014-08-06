# -*- coding: utf-8 -*-
from shortcut_utils import getShortcutIcon
from shortcut_settings_ui_base import Ui_ShortcutSettings
from __init__ import default_icons_dir

from PyQt4.QtGui import QDialog, QFileDialog, QIcon
from PyQt4.QtCore import QObject, SIGNAL, QSize

import os

class ShortcutSettings(QDialog, Ui_ShortcutSettings):
    def __init__(self, parent, shortcut):
        QDialog.__init__(self, parent)
        self.setupUi(self)
        
        self._shortcut = shortcut
        
        self._shortcutName_le.setText(self._shortcut.name)
        if self._shortcut.uri != None:
            self._shortcutURI_le.setText(self._shortcut.uri)
        
        shortcutIcon = getShortcutIcon(
               self._shortcut.icon,
               self._shortcut.uri)
        self._shortcutIcon_l.setPixmap(shortcutIcon.pixmap(QSize(32,32)))
        
        self._shortcutNewIcon = self._shortcut.icon
        QObject.connect(self._changeIconBtn, SIGNAL("clicked()"), self._chooseIcon)
    
    def _chooseIcon(self):
        fileName = QFileDialog.getOpenFileName(self,
                                               self.tr("Select icon file"),
                                               default_icons_dir
                                              )
        if fileName != "":
            self._shortcutNewIcon = os.path.normpath(unicode(fileName))
            self._shortcutIcon_l.setPixmap( QIcon(self._shortcutNewIcon).pixmap(QSize(32,32)) )
    
    def _validatePage(self):
        isValid = True
        
        if self._shortcutName_le.text() == "":
            self._shortcutName_le.setPlaceholderText(self.tr("Please, fill this field"))
            isValid = False
        
        if self._shortcutURI_le.text() == "":
            self._shortcutURI_le.setPlaceholderText(self.tr("Please, fill this field"))
            isValid = False
    
        return isValid
    
    def accept(self):
        
        if self._validatePage() == False:
            return
        
        self.shortcutNewName = self._shortcutName_le.text()
        self.shortcutNewURI = self._shortcutURI_le.text()
        
        if self._shortcutNewIcon != None:
            if self._shortcutNewIcon.lower().find(default_icons_dir.lower()) == 0:
                self._shortcutNewIcon = self._shortcutNewIcon[len(default_icons_dir)+1:]
        
        self._shortcut.editShortcut(self.shortcutNewName, self.shortcutNewURI, self._shortcutNewIcon)
        
        QDialog.accept(self)