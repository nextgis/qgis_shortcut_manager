# -*- coding: utf-8 -*-
"""
/***************************************************************************
 ShortcutManager
                                 A QGIS plugin
 This plugin create shortcuts in toolbar
                             -------------------
        begin                : 2014-07-18
        copyright            : (C) 2014 by NextGIS
        email                : info@nextgis.ru
        git sha              : $Format:%H$
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
 This script initializes the plugin, making it known to QGIS.
 
 
pylupdate4 __init__.py shortcut.py shortcut_action.py shortcut_creator.py shortcut_manager.py shortcut_manager_dialog.py shortcut_settings.py shortcut_utils.py shortcut_widget.py shortcut_creator_ui_base.py shortcut_settings_ui_base.py shortcut_widget_ui_base.py  -ts i18n\ShortcutManager_ru.ts
"""
import os
import sys

real_plugin_dir = os.path.dirname(__file__)
default_icons_dir = os.path.join(real_plugin_dir, "icons4shortcuts")


# noinspection PyPep8Naming
def classFactory(iface):  # pylint: disable=invalid-name
    """Load ShortcutManager class from file ShortcutManager.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from .shortcut_manager import ShortcutManagerPlugin
    return ShortcutManagerPlugin(iface)
