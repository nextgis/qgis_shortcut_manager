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

from PyQt4.QtGui import QIcon, QPixmap, QImage

from __init__ import default_icons_dir

def getShortcutIcon(iconPath = None, uri = None):
    if iconPath is not None:
        if os.path.exists(iconPath):
            return QIcon(iconPath)
        elif os.path.exists( os.path.join(default_icons_dir,iconPath) ):
            return QIcon( os.path.join(default_icons_dir,iconPath) )

    elif uri is not None:
        shortcutIcon = getIconByURL(getShortcutType(uri), uri)
        if shortcutIcon is None:
            return getDefaultIcon(getShortcutType(uri))
        else:
            return shortcutIcon

    return getDefaultIcon(getShortcutType(None))

def getDefaultIcon(shortcutType):
    if shortcutType == "desktop":
        #icon_path = os.path.join(defaultIconPath, "default-shortcut-desk.png")
        icon_path = ":/ShortcutManager/icons/default-shortcut-desk.png"
    elif shortcutType == "web":
        #icon_path = os.path.join(defaultIconPath, "default-shortcut-web.png")
        icon_path = ":/ShortcutManager/icons/default-shortcut-web.png"
    else:
        #icon_path = os.path.join(defaultIconPath, "default-shortcut.png")
        icon_path = ":/ShortcutManager/icons/default-shortcut.png"
    
    return  QIcon(icon_path)

def getIconByURL(shortcutType, uri):
    if shortcutType == "desktop":
        return _getAppIcon(uri)
    elif shortcutType == "web":
        return _getWebFavIcon(uri)
    
def _getAppIcon(app):
    import win32ui
    import win32gui
    
    try:
        large, small = win32gui.ExtractIconEx(app, 0)
        win32gui.DestroyIcon(small[0])
                    
        hdc = win32ui.CreateDCFromHandle(win32gui.GetDC(0))
        hbmp = win32ui.CreateBitmap()
        hbmp.CreateCompatibleBitmap(hdc, 32, 32)
        hdc = hdc.CreateCompatibleDC()
        hdc.SelectObject(hbmp)
        hdc.DrawIcon((0, 0), large[0])
        hdc.DeleteDC()
        return QIcon(QPixmap.fromWinHBITMAP(hbmp.GetHandle(), 2))
    except:
        return None
    
def _getWebFavIcon(url):
    from favicon import find_favicon_from_url
    import requests
    
    shortcutURL = find_favicon_from_url(url)
    
    if shortcutURL is not None:
        r = requests.get(shortcutURL)
        return QIcon(QPixmap.fromImage(QImage.fromData(r.content)))
    else:
        return None

def getShortcutType(uri):
    if uri is None:
        return "unknown"
    
    if uri[0:7] == "http://":
        shortcutType = "web"
    else:
        shortcutType = "desktop"
    return shortcutType