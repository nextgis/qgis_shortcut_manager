# -*- coding: utf-8 -*-
from shortcut_utils import getShortcutIcon
from shortcut_settings import ShortcutSettings
from shortcut_widget_ui_base import Ui_ShortcutWidget

from PyQt4.QtGui import QWidget
from PyQt4.QtCore import QObject, SIGNAL, QSize

class ShortcutWidget(QWidget, Ui_ShortcutWidget):
    def __init__(self, parent, shortcut):
        QWidget.__init__(self)
        self.setupUi(self)
        
        self._shortcut = shortcut
        """
        self.verticalLayout = QVBoxLayout(self)
        self.horizontalLayout = QHBoxLayout(self)
        self.verticalLayout.addLayout(self.horizontalLayout)
        spFixed = QSizePolicy(QSizePolicy.Fixed,QSizePolicy.Fixed)
        
        # deleteButton
        self.deleteButton = QPushButton(self)
        self.deleteButton.setText("Delete")
        self.deleteButton.setSizePolicy(spFixed)
        self.horizontalLayout.addWidget(self.deleteButton)
        # editButton
        self.editButton = QPushButton(self)
        self.editButton.setText("Edit")
        self.editButton.setSizePolicy(spFixed)
        self.horizontalLayout.addWidget(self.editButton)
        
        # shortcutIcon
        self.shortcutIcon = QLabel(self)
        self.shortcutIcon.setSizePolicy(spFixed)
        self.shortcutIcon.setStyleSheet("margin-left:25px")
        self.horizontalLayout.addWidget(self.shortcutIcon)
        
        # shortcutName
        self.shortcutName = QLabel(self)
        self.horizontalLayout.addWidget(self.shortcutName)
        """
        self.__shortcutUpdated()
        
        QObject.connect(self.editButton, SIGNAL("clicked()"), self.editShortcut)
        QObject.connect(self.deleteButton, SIGNAL("clicked()"), self.deleteShortcut)
        QObject.connect(self._shortcut, SIGNAL("updated()"), self.__shortcutUpdated)
        QObject.connect(self._shortcut, SIGNAL("deleted()"), self.__shortcutDeleted)

    def editShortcut(self):
        dlg = ShortcutSettings(self, self._shortcut)
        dlg.show()
        # Run the dialog event loop
        result = dlg.exec_()
        # See if OK was pressed
        if result:
            # Do something useful here - delete the line containing pass and
            # substitute with your code.
            #self._loadData(shortcutName)
            pass
        
    def deleteShortcut(self):
        self._shortcut.delete()
    
    def __shortcutUpdated(self):
        shortcutIcon = getShortcutIcon(
               self._shortcut.icon,
               self._shortcut.uri)
        self.shortcutIcon.setPixmap(shortcutIcon.pixmap(QSize(32,32)))
        
        self.shortcutName.setText(self._shortcut.name)
    
    def __shortcutDeleted(self):
        self.setParent(None)