mkdir shortcut_manager
mkdir shortcut_manager\favicon
mkdir shortcut_manager\icons
mkdir shortcut_manager\i18n
mkdir shortcut_manager\ui
xcopy *.py shortcut_manager
xcopy README.md shortcut_manager
xcopy LICENSE shortcut_manager
xcopy metadata.txt shortcut_manager
xcopy /F favicon\* shortcut_manager\favicon\
xcopy /F i18n\*.qm shortcut_manager\i18n
xcopy /F icons\* shortcut_manager\icons\
xcopy /F ui\* shortcut_manager\ui
zip -r shortcut_manager.zip shortcut_manager
del /Q shortcut_manager
rd shortcut_manager