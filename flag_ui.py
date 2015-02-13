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
        self.lbl = QtGui.QLabel("Selecteer een land", self)
        self.lbl.move(50, 20)
        countryPicker=QtGui.QComboBox(self)
        cList=readText()
        for c in cList:
			self.flag=Country.countryFlag(c)
			self.name=str(Country(c))
			self.name.strip()
			countryPicker.addItem(self.name)
			
        countryPicker.move(50,60)
        countryPicker.activated.connect(self.onActivated)        
         
        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('Country Picker')
        self.show()
        
        self.hbox = QtGui.QHBoxLayout()
        self.hbox.addStretch(1)
        self.hbox.addWidget(countryPicker)

        self.vbox = QtGui.QVBoxLayout()
        self.vbox.addStretch(1)
        self.vbox.addLayout(self.hbox)
        
        self.setLayout(self.vbox) 
        
    def onActivated(self, text):
      self.flagDisplay=QtGui.QFrame(self)
      self.hbox.addWidget(self.flagDisplay)
      self.flagDisplay.setStyleSheet("QFrame { background-color: %s }" % self.flag)

      

if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    ex = FlagUI()
    sys.exit(app.exec_())
	
