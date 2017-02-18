import sys
from PyQt5.QtWidgets import QApplication
from test import Example 

if __name__ == '__main__':
    
    app = QApplication(sys.argv)

    w = Example()

    
    sys.exit(app.exec_())
