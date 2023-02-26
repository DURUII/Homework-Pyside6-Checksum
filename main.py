# ///////////////////////////////////////////////////////////////
#
# BY: WANDERSON M.PIMENTA
# PROJECT MADE WITH: Qt Designer and PySide6
# V: 1.0.0
#
# This project can be used freely for all uses, as long as they maintain the
# respective credits only in the Python scripts, any information in the visual
# interface (GUI) can be modified without any implication.
#
# There are limitations on Qt licenses if you want to use your products
# commercially, I recommend reading them on the official website:
# https://doc.qt.io/qtforpython/licenses.html
#
# ///////////////////////////////////////////////////////////////

import sys
import os
import platform
import webbrowser

# IMPORT / GUI AND MODULES AND WIDGETS
# ///////////////////////////////////////////////////////////////
from modules import *
from widgets import *

os.environ["QT_FONT_DPI"] = "75"  # FIX Problem for High DPI and Scale above 100%

# SET AS GLOBAL WIDGETS
# ///////////////////////////////////////////////////////////////
widgets = None


class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)

        # SET AS GLOBAL WIDGETS
        # ///////////////////////////////////////////////////////////////
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        global widgets
        widgets = self.ui

        # TODO USE CUSTOM TITLE BAR | USE AS "False" FOR MAC OR LINUX
        # ///////////////////////////////////////////////////////////////
        Settings.ENABLE_CUSTOM_TITLE_BAR = False

        # APP NAME
        # ///////////////////////////////////////////////////////////////
        title = "《计算机网络》课程设计"
        description = ""

        # APPLY TEXTS
        if title is not None and title != "":
            self.setWindowTitle(title)
        if description is not None and description != "":
            widgets.titleRightInfo.setText(description)

        # TOGGLE MENU
        # ///////////////////////////////////////////////////////////////
        widgets.toggleButton.clicked.connect(lambda: UIFunctions.toggleMenu(self, True))

        # SET UI DEFINITIONS
        # ///////////////////////////////////////////////////////////////
        UIFunctions.uiDefinitions(self)

        # QTableWidget PARAMETERS
        # ///////////////////////////////////////////////////////////////
        # widgets.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        # BUTTONS CLICK
        # ///////////////////////////////////////////////////////////////

        # LEFT MENUS
        widgets.btn_home.clicked.connect(self.buttonClick)

        # TODO 输入 解析 步骤
        widgets.btn_input.clicked.connect(self.buttonClick)
        widgets.btn_parse.clicked.connect(self.buttonClick)
        widgets.btn_process.clicked.connect(self.buttonClick)

        # EXTRA LEFT BOX
        def openCloseLeftBox():
            UIFunctions.toggleLeftBox(self, True)

        widgets.toggleLeftBox.clicked.connect(openCloseLeftBox)
        widgets.extraCloseColumnBtn.clicked.connect(openCloseLeftBox)

        widgets.btn_github.clicked.connect(self.buttonClick)
        widgets.btn_wust.clicked.connect(self.buttonClick)
        widgets.btn_cnblogs.clicked.connect(self.buttonClick)

        # EXTRA RIGHT BOX
        def openCloseRightBox():
            UIFunctions.toggleRightBox(self, True)

        widgets.settingsTopBtn.clicked.connect(openCloseRightBox)

        # TODO 主题 导出
        widgets.btn_theme.clicked.connect(self.buttonClick)

        # SHOW APP
        # ///////////////////////////////////////////////////////////////
        self.show()

        # TODO SET CUSTOM THEME
        # ///////////////////////////////////////////////////////////////
        useCustomTheme = True

        # 便于一键切换主题
        self.useCustomTheme = useCustomTheme

        themeFile = "themes/py_dracula_light.qss"

        # SET THEME AND HACKS
        if useCustomTheme:
            # LOAD AND APPLY STYLE
            UIFunctions.theme(self, themeFile, True)

            # SET HACKS
            AppFunctions.setThemeHack(self)

        # SET HOME PAGE AND SELECT MENU
        # ///////////////////////////////////////////////////////////////
        widgets.stackedWidget.setCurrentWidget(widgets.page_home)
        widgets.btn_home.setStyleSheet(UIFunctions.selectMenu(widgets.btn_home.styleSheet()))

    # BUTTONS CLICK
    # Post here your functions for clicked buttons
    # ///////////////////////////////////////////////////////////////
    def buttonClick(self):
        # GET BUTTON CLICKED
        btn = self.sender()
        btnName = btn.objectName()

        if btnName == "btn_wust":
            webbrowser.open("https://www.wust.edu.cn")
        elif btnName == "btn_cnblogs":
            webbrowser.open("https://www.cnblogs.com/anrushan/")
        elif btnName == "btn_github":
            webbrowser.open("https://github.com/DURUII")

        # SHOW HOME PAGE
        if btnName == "btn_home":
            widgets.stackedWidget.setCurrentWidget(widgets.page_home)
            UIFunctions.resetStyle(self, btnName)
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))

        # TODO 输入 解析 步骤 退出

        if btnName == "btn_input":
            widgets.stackedWidget.setCurrentWidget(widgets.page_input)  # SET PAGE
            UIFunctions.resetStyle(self, btnName)  # RESET ANOTHERS BUTTONS SELECTED
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))  # SELECT MENU
            # QMessageBox.information(self, "警告", "该功能尚未实现", QMessageBox.Yes)

        if btnName == "btn_parse":
            widgets.stackedWidget.setCurrentWidget(widgets.page_parse)  # SET PAGE
            UIFunctions.resetStyle(self, btnName)  # RESET ANOTHERS BUTTONS SELECTED
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))  # SELECT MENU
            # QMessageBox.information(self, "警告", "该功能尚未实现", QMessageBox.Yes)

        if btnName == "btn_process":
            widgets.stackedWidget.setCurrentWidget(widgets.page_process)  # SET PAGE
            UIFunctions.resetStyle(self, btnName)  # RESET ANOTHERS BUTTONS SELECTED
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))  # SELECT MENU
            # QMessageBox.information(self, "警告", "该功能尚未实现", QMessageBox.Yes)

        # TODO 主题 导出

        if btnName == "btn_theme":
            if self.useCustomTheme:
                themeFile = "themes/py_dracula_dark.qss"
                UIFunctions.theme(self, themeFile, True)
                AppFunctions.setThemeHack(self)
                self.useCustomTheme = False
            else:
                themeFile = "themes/py_dracula_light.qss"
                UIFunctions.theme(self, themeFile, True)
                AppFunctions.setThemeHack(self)
                self.useCustomTheme = True

        if btnName == "btn_export":
            QMessageBox.information(self, "警告", "该功能尚未实现", QMessageBox.Yes)

        # PRINT BTN NAME
        print(f'Button "{btnName}" pressed!')

    # RESIZE EVENTS
    # ///////////////////////////////////////////////////////////////
    def resizeEvent(self, event):
        # Update Size Grips
        UIFunctions.resize_grips(self)

    # MOUSE CLICK EVENTS
    # ///////////////////////////////////////////////////////////////
    def mousePressEvent(self, event):
        # SET DRAG POS WINDOW
        self.dragPos = event.globalPos()

        # PRINT MOUSE EVENTS
        if event.buttons() == Qt.LeftButton:
            print('Mouse click: LEFT CLICK')
        if event.buttons() == Qt.RightButton:
            print('Mouse click: RIGHT CLICK')


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon("icon.png"))
    window = MainWindow()

    sys.exit(app.exec())
