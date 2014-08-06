from shortcut_creator_ui_base import Ui_CreateShortcutWizard
from shortcut_utils import getIconByURL, getDefaultIcon
from __init__ import default_icons_dir

from PyQt4.QtGui import QWizard, QFileDialog, QIcon
from PyQt4.QtCore import QObject, SIGNAL, QSize

import os

class ShortcutCreator(QWizard, Ui_CreateShortcutWizard):
    def __init__(self, parent, createShortcutFunction):
        QWizard.__init__(self, parent)
        self.setupUi(self)
        
        self._iconPath = None
        self._createShortcutFunction = createShortcutFunction
        
        QObject.connect(self, SIGNAL("currentIdChanged(int)"), self._processEnterInPage)
        QObject.connect(self._changeShortcutURI_Btn, SIGNAL("clicked()"), self._changeShortcutURI)
        QObject.connect(self._chooseIcon_Btn, SIGNAL("clicked()"), self._chooseIcon)
    
    def accept(self):
        if self._iconPath is not None:
            if self._iconPath.lower().find(default_icons_dir.lower()) == 0:
                self._iconPath = self._iconPath[len(default_icons_dir)+1:]
        
        self._createShortcutFunction(self._shortcutName.text(), self._shortcutURI.text(), self._iconPath)
        
        QWizard.accept(self)
        
    def validateCurrentPage(self):
        if self.currentId() == 0:
            if self._shortcutURI.text() == "":
                self._shortcutURI.setPlaceholderText(self.tr("Please, fill this field"))
                return False
            else:
                return True
            
        if self.currentId() == 1:
            if self._shortcutName.text() == "":
                self._shortcutName.setPlaceholderText(self.tr("Please, fill this field"))
                return False
            else:
                return True
        
        return True
    def _processEnterInPage(self, pageIndex):
        if pageIndex == 2:
            if self._iconPath is None:
                shortcutIcon = getIconByURL(self._getShortcutType(), self._shortcutURI.text())
                if shortcutIcon is None:
                    shortcutIcon = getDefaultIcon(self._getShortcutType())
            
                self._shortcutIcon.setPixmap(shortcutIcon.pixmap(QSize(32,32)))
        
    def _getShortcutType(self):
        if self._shortcutURI.text()[0:7] == "http://":
            shortcutType = "web"
        else:
            shortcutType = "desktop"
        return shortcutType
    
    def _changeShortcutURI(self):
        self._shortcutURI.setText( QFileDialog.getOpenFileName(self, self.tr("Select icon file")) )
    
    def _chooseIcon(self):
        fileName = QFileDialog.getOpenFileName(self,
                                               self.tr("Select icon file"),
                                               default_icons_dir
                                              )
        if fileName != "":
            self.label_7.setText(self.tr("You choose this icon: "))
            self._iconPath = os.path.normpath(unicode(fileName))
            self._shortcutIcon.setPixmap( QIcon(self._iconPath).pixmap(QSize(32,32)) )