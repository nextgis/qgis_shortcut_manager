# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'create_shortcut_wizard.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_CreateShortcutWizard(object):
    def setupUi(self, CreateShortcutWizard):
        CreateShortcutWizard.setObjectName("CreateShortcutWizard")
        CreateShortcutWizard.resize(429, 360)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(CreateShortcutWizard.sizePolicy().hasHeightForWidth())
        CreateShortcutWizard.setSizePolicy(sizePolicy)
        CreateShortcutWizard.setModal(True)
        self.wizardPage1 = QtWidgets.QWizardPage()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.wizardPage1.sizePolicy().hasHeightForWidth())
        self.wizardPage1.setSizePolicy(sizePolicy)
        self.wizardPage1.setObjectName("wizardPage1")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.wizardPage1)
        self.verticalLayout_2.setSizeConstraint(QtWidgets.QLayout.SetMinAndMaxSize)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_3 = QtWidgets.QLabel(self.wizardPage1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setStyleSheet("margin:25px; font:15px;")
        self.label_3.setObjectName("label_3")
        self.verticalLayout_2.addWidget(self.label_3)
        self.label = QtWidgets.QLabel(self.wizardPage1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setStyleSheet("margin-left:15px")
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self._shortcutURI = QtWidgets.QLineEdit(self.wizardPage1)
        self._shortcutURI.setStyleSheet("margin-left:15px")
        self._shortcutURI.setObjectName("_shortcutURI")
        self.horizontalLayout.addWidget(self._shortcutURI)
        self._changeShortcutURI_Btn = QtWidgets.QPushButton(self.wizardPage1)
        self._changeShortcutURI_Btn.setObjectName("_changeShortcutURI_Btn")
        self.horizontalLayout.addWidget(self._changeShortcutURI_Btn)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        CreateShortcutWizard.addPage(self.wizardPage1)
        self.wizardPage2 = QtWidgets.QWizardPage()
        self.wizardPage2.setObjectName("wizardPage2")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.wizardPage2)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_2 = QtWidgets.QLabel(self.wizardPage2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setStyleSheet("margin:25px; font:15px;")
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.label_4 = QtWidgets.QLabel(self.wizardPage2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        self.label_4.setStyleSheet("margin-left:15px")
        self.label_4.setObjectName("label_4")
        self.verticalLayout.addWidget(self.label_4)
        self._shortcutName = QtWidgets.QLineEdit(self.wizardPage2)
        self._shortcutName.setStyleSheet("margin-left:15px")
        self._shortcutName.setObjectName("_shortcutName")
        self.verticalLayout.addWidget(self._shortcutName)
        CreateShortcutWizard.addPage(self.wizardPage2)
        self.wizardPage3 = QtWidgets.QWizardPage()
        self.wizardPage3.setObjectName("wizardPage3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.wizardPage3)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_5 = QtWidgets.QLabel(self.wizardPage3)
        self.label_5.setStyleSheet("margin:25px; font:15px;")
        self.label_5.setObjectName("label_5")
        self.verticalLayout_3.addWidget(self.label_5)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_7 = QtWidgets.QLabel(self.wizardPage3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy)
        self.label_7.setStyleSheet("margin-left:15px")
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_2.addWidget(self.label_7)
        self._shortcutIcon = QtWidgets.QLabel(self.wizardPage3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self._shortcutIcon.sizePolicy().hasHeightForWidth())
        self._shortcutIcon.setSizePolicy(sizePolicy)
        self._shortcutIcon.setFrameShape(QtWidgets.QFrame.Box)
        self._shortcutIcon.setFrameShadow(QtWidgets.QFrame.Plain)
        self._shortcutIcon.setText("")
        self._shortcutIcon.setPixmap(QtGui.QPixmap(":/plugins/ShortcutManager/icon.png"))
        self._shortcutIcon.setObjectName("_shortcutIcon")
        self.horizontalLayout_2.addWidget(self._shortcutIcon)
        self.label_8 = QtWidgets.QLabel(self.wizardPage3)
        self.label_8.setText("")
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_2.addWidget(self.label_8)
        self._chooseIcon_Btn = QtWidgets.QPushButton(self.wizardPage3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self._chooseIcon_Btn.sizePolicy().hasHeightForWidth())
        self._chooseIcon_Btn.setSizePolicy(sizePolicy)
        self._chooseIcon_Btn.setObjectName("_chooseIcon_Btn")
        self.horizontalLayout_2.addWidget(self._chooseIcon_Btn)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        CreateShortcutWizard.addPage(self.wizardPage3)

        self.retranslateUi(CreateShortcutWizard)
        QtCore.QMetaObject.connectSlotsByName(CreateShortcutWizard)

    def retranslateUi(self, CreateShortcutWizard):
        _translate = QtCore.QCoreApplication.translate
        CreateShortcutWizard.setWindowTitle(_translate("CreateShortcutWizard", "Create shortcut"))
        self.label_3.setText(
            _translate("CreateShortcutWizard", "For what element it is necessary to create a shortcut?"))
        self.label.setText(_translate("CreateShortcutWizard", "Enter element placement:"))
        self._changeShortcutURI_Btn.setText(_translate("CreateShortcutWizard", "Browse..."))
        self.label_2.setText(_translate("CreateShortcutWizard", "How to call a shortcut?"))
        self.label_4.setText(_translate("CreateShortcutWizard", "Enter shortcut name:"))
        self.label_5.setText(_translate("CreateShortcutWizard", "What icon the shortcut has to have?"))
        self.label_7.setText(_translate("CreateShortcutWizard", "Icon by default the specified element:"))
        self._chooseIcon_Btn.setText(_translate("CreateShortcutWizard", "Choose another..."))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    CreateShortcutWizard = QtWidgets.QWizard()
    ui = Ui_CreateShortcutWizard()
    ui.setupUi(CreateShortcutWizard)
    CreateShortcutWizard.show()
    sys.exit(app.exec_())
