# -*- coding: utf-8 -*-
"""
/***************************************************************************
 ShortcutManager
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
import weakref
# import resources_rc

from .shortcut import Shorcut, shortcutsFromSettings
from .shortcut_manager_dialog import ShortcutManagerDialog
from .shortcut_action import ShorcutAction
from .shortcut_widget import ShortcutWidget

from qgis.PyQt.QtCore import QSettings, QTranslator, qVersion, QCoreApplication
from qgis.PyQt.QtGui import QIcon
from qgis.PyQt.QtWidgets import QAction

from qgis.core import QgsMessageLog, Qgis
from . import about_dialog


class ShortcutManager:
    def __init__(self, iface):
        self._iface = iface

        QgsMessageLog.logMessage(
            "Shortcuts manager. Load shortcuts from settings.", None, Qgis.Info
        )

        self._shortcuts = shortcutsFromSettings()

        # create actions
        self._actions = []
        for shortcut in self._shortcuts:
            self._actions.append(ShorcutAction(self._iface, shortcut))

        # create manager dialoog
        # self.dialog = ShortcutManagerDialog(None, self.createShortcut)
        self.dialog = ShortcutManagerDialog(None, weakref.proxy(self))
        for shortcut in self._shortcuts:
            self.dialog.addShortcut(ShortcutWidget(None, shortcut))

    def createShortcut(self, name, uri, icon):
        shortcut = Shorcut(name, uri, icon)

        self._shortcuts.append(shortcut)
        self._actions.append(ShorcutAction(self._iface, shortcut))
        self.dialog.addShortcut(ShortcutWidget(None, shortcut))

    # TODO bad decision
    def unload(self):
        for action in self._actions:
            self._iface.removeToolBarIcon(action)
        # del self.dialog


class ShortcutManagerPlugin:
    """QGIS Plugin Implementation."""

    def __init__(self, iface):
        """Constructor.

        :param iface: An interface instance that will be passed to this class
            which provides the hook by which you can manipulate the QGIS
            application at run time.
        :type iface: QgsInterface
        """
        # Save reference to the QGIS interface
        self.iface = iface
        # initialize plugin directory
        self.plugin_dir = os.path.dirname(__file__)
        # initialize locale
        locale = QSettings().value("locale/userLocale")[0:2]
        locale_path = os.path.join(
            self.plugin_dir, "i18n", "ShortcutManager_{}.qm".format(locale)
        )

        if os.path.exists(locale_path):
            self.translator = QTranslator()
            self.translator.load(locale_path)

            if qVersion() > "4.3.3":
                QCoreApplication.installTranslator(self.translator)

        # Declare instance attributes
        self.actions = []
        self.menu = self.tr("&Shortcut Manager")

        # self.toolbar = self.iface.addToolBar(u'ShortcutManager')
        # self.toolbar.setObjectName(u'ShortcutManager')

        self.manager = ShortcutManager(self.iface)

    # noinspection PyMethodMayBeStatic
    def tr(self, message):
        """Get the translation for a string using Qt translation API.

        We implement this ourselves since we do not inherit QObject.

        :param message: String for translation.
        :type message: str, QString

        :returns: Translated version of message.
        :rtype: QString
        """
        return QCoreApplication.translate(__class__.__name__, message)

    def add_action(
        self,
        icon,
        text,
        callback,
        enabled_flag=True,
        add_to_menu=True,
        add_to_toolbar=True,
        status_tip=None,
        whats_this=None,
        parent=None,
    ):
        if icon:
            action = QAction(icon, text, parent)
        else:
            action = QAction(text, parent)
        action.triggered.connect(callback)
        action.setEnabled(enabled_flag)

        if status_tip is not None:
            action.setStatusTip(status_tip)

        if whats_this is not None:
            action.setWhatsThis(whats_this)

        if add_to_toolbar:
            # self.toolbar.addAction(action)
            self.iface.addToolBarIcon(action)

        if add_to_menu:
            self.iface.addPluginToMenu(self.menu, action)

        self.actions.append(action)

        return action

    def initGui(self):
        """Create the menu entries and toolbar icons inside the QGIS GUI."""

        shortcutManageIcon = QIcon(":/ShortcutManager/icons/icon.png")
        shortcutManageText = "Shortcut manager"
        self.add_action(
            shortcutManageIcon,
            shortcutManageText,
            callback=self.run,
            parent=self.iface.mainWindow(),
            add_to_toolbar=False,
        )
        shortcutAboutText = self.tr("About plugin…")
        self.add_action(
            None,
            shortcutAboutText,
            callback=self.about,
            parent=self.iface.mainWindow(),
            add_to_toolbar=False,
        )

    def unload(self):
        """Removes the plugin menu item and icon from QGIS GUI."""
        for action in self.actions:
            self.iface.removePluginMenu(self.menu, action)
            self.iface.removeToolBarIcon(action)
            action.deleteLater()

        self.manager.unload()
        # del self.manager

        # print '{} objects collected'.format(gc.collect())

    def run(self):
        """Run method that performs all the real work"""
        self.manager.dialog.show()

        # Run the dialog event loop
        result = self.manager.dialog.exec_()

        # See if OK was pressed
        if result:
            # Do something useful here - delete the line containing pass and
            # substitute with your code.
            pass

    def about(self):
        dialog = about_dialog.AboutDialog(os.path.basename(self.plugin_dir))
        dialog.exec_()
