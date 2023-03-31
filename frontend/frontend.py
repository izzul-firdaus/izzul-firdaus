import controllers.controllers as controllers
from PyQt5.QtWidgets import QMainWindow

import frontend.frontend_ui as frontend_ui


class ui_User:
    def __init__(self, data: tuple[str, str, str]):
        self.name = data[0]
        self.password = data[1]
        self.type = data[2]


ui_user_guest = ui_User(("Guest", "", ""))


class MainWindow:
    def __init__(self):
        self.currentUser = ui_user_guest

        # setup
        self.window = QMainWindow()
        self.ui = frontend_ui.Ui_MainWindow()
        self.ui.setupUi(self.window)

        # buttons
        self.ui.pageLogin_buttonLogin.clicked.connect(self.login)
        self.ui.pageAdmin_buttonLogout.clicked.connect(self.logout)
        self.ui.pageChair_buttonLogout.clicked.connect(self.logout)
        self.ui.pageAuthor_buttonLogout.clicked.connect(self.logout)
        self.ui.pageReviewer_buttonLogout.clicked.connect(self.logout)

        # button shortcuts #where does the word"MainWindow" come from 
        self.ui.pageLogin_inputPassword.returnPressed.connect(self.login)

    def show(self):
        self.init_pageLogin()
        self.window.show()

    def resetPage(self, index):
        if index == 0:
            self.reset_pageLogin()
        elif index == 1:
            self.reset_pageAdmin()
        elif index == 2:
            self.reset_pageChair()
        elif index == 3:
            self.reset_pageAuthor()
        elif index == 4:
            self.reset_pageReviewer()

    def login(self):
        uname = self.ui.pageLogin_inputName.text()
        upass = self.ui.pageLogin_inputPassword.text()
        if not (user := controllers.ControllerLogin(uname, upass)):
            self.ui.pageLogin_responseLogin.setText("Invalid login, please try again")
            return
        self.currentUser = ui_User(user)
        if self.currentUser.type == "Admin":
            self.init_pageAdmin()
        elif self.currentUser.type == "Chair":
            self.init_pageChair()
        elif self.currentUser.type == "Author":
            self.init_pageAuthor()
        elif self.currentUser.type == "Reviewer":
            self.init_pageReviewer()
        self.reset_pageLogin()

    def logout(self):
        page = self.ui.MainStack.currentIndex()
        self.currentUser = ui_user_guest
        self.ui.MainStack.setCurrentIndex(0)
        self.resetPage(page)

    def init_pageLogin(self):
        self.ui.pageLogin_buttonLogin.setText("Login")
        self.ui.MainStack.setCurrentIndex(0)

    def reset_pageLogin(self):
        self.ui.pageLogin_inputName.clear()
        self.ui.pageLogin_inputPassword.clear()
        self.ui.pageLogin_responseLogin.clear()

    def init_pageAdmin(self):
        self.ui.pageAdmin_buttonLogout.setText("Logout")
        self.ui.pageAdmin_textLogin.setText(f"Welcome {self.currentUser.name}!")
        self.ui.MainStack.setCurrentIndex(1)

    def reset_pageAdmin(self):
        self.ui.pageAdmin_textLogin.clear()

    def init_pageChair(self):
        self.ui.pageChair_buttonLogout.setText("Logout")
        self.ui.pageChair_textLogin.setText(f"Welcome {self.currentUser.name}!")
        self.ui.MainStack.setCurrentIndex(2)

    def reset_pageChair(self):
        self.ui.pageChair_textLogin.clear()

    def init_pageAuthor(self):
        self.ui.pageAuthor_buttonLogout.setText("Logout")
        self.ui.pageAuthor_textLogin.setText(f"Welcome {self.currentUser.name}!")
        self.ui.MainStack.setCurrentIndex(3)

    def reset_pageAuthor(self):
        self.ui.pageAuthor_textLogin.clear()

    def init_pageReviewer(self):
        self.ui.pageReviewer_buttonLogout.setText("Logout")
        self.ui.pageReviewer_textLogin.setText(f"Welcome {self.currentUser.name}!")
        self.ui.MainStack.setCurrentIndex(4)

    def reset_pageReviewer(self):
        self.ui.pageReviewer_textLogin.clear()
