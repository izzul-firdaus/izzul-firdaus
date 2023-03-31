import sys

from PyQt5.QtWidgets import QApplication, QStyleFactory

import frontend.frontend as front

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyle(QStyleFactory.create("Fusion"))
    main_win = front.MainWindow()
    main_win.show()
    sys.exit(app.exec_())
