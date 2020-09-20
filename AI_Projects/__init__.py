from PyQt5 import QtWidgets
import sys

from ui.ui import UI, predict_expression

if __name__=="__main__":
    app = QtWidgets.QApplication(sys.argv)
    form = QtWidgets.QMainWindow()
    ui = UI(form)
    # predict_expression()
    form.show()
    sys.exit(app.exec_())

