# #!/usr/bin/env python
# flag_ui.py
# Olivier Louwaars s2814714
# 13-2-2015

from country import *

class FlagUI(QtGui.QWidget):
    
    def __init__(self):
        super(FlagUI, self).__init__()
        self.initUI()
        
    def initUI(self):
        text = QtGui.QLabel("Selecteer een land", self)
        countryPicker=QtGui.QComboBox(self)
        cList=readText()
        for self.c in cList:
            self.name=str(Country(self.c)).strip()
            countryPicker.addItem(self.name)
			
        countryPicker.activated.connect(self.onActivated)        
         
        self.setGeometry(200, 200, 100, 150)
        self.setWindowTitle('Country Picker')
        self.show()
        
        self.hbox = QtGui.QHBoxLayout()
        self.flagDisplay=QtGui.QFrame(self)
        self.flagDisplay.setFrameShape(QtGui.QFrame.StyledPanel)
        self.hbox.addWidget(text)
        self.hbox.addWidget(countryPicker)
        

        self.vbox = QtGui.QVBoxLayout()
        self.vbox.addLayout(self.hbox)
        self.setLayout(self.vbox)
        self.vbox.addWidget(self.flagDisplay)

        
    def onActivated(self, text):
        self.flag=Country.countryFlag(self.c)
        self.flagDisplay.setStyleSheet("QFrame { background-color: %s }" % self.flag.name())

      

if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    ex = FlagUI()
    sys.exit(app.exec_())
	
