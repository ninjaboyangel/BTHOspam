# This Python file uses the following encoding: utf-8
from PyQt5 import QtCore, QtWidgets, uic
import sys
import os
import webbrowser


filterSite = "https://mail.google.com/mail/u/#settings/filters"
class Ui(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui, self).__init__()
        cwd = os.getcwd()


        self.fratC = False
        self.abroadC = False
        self.govC = False
        self.internC = False
        self.medC = False
        self.mensC = False
        self.reschC = False
        self.soroC = False
        self.sportC = False
        self.womsC = False

        uic.loadUi(cwd + '/Documents/BTHOspam/test.ui', self)


        self.button = self.findChild(QtWidgets.QPushButton, 'genButton')
        self.button.clicked.connect(self.genButtonPressed)

        self.frat = self.findChild(QtWidgets.QCheckBox, 'fratBox')
        self.frat.stateChanged.connect(self.fratClicked)

        self.abroad = self.findChild(QtWidgets.QCheckBox, 'abroadBox')
        self.abroad.stateChanged.connect(self.abroadClicked)

        self.gov = self.findChild(QtWidgets.QCheckBox, 'govBox')
        self.gov.stateChanged.connect(self.govClicked)

        self.intern = self.findChild(QtWidgets.QCheckBox, 'internBox')
        self.intern.stateChanged.connect(self.internClicked)

        self.med = self.findChild(QtWidgets.QCheckBox, 'medBox')
        self.med.stateChanged.connect(self.medClicked)

        self.mens = self.findChild(QtWidgets.QCheckBox, 'mensBox')
        self.mens.stateChanged.connect(self.mensClicked)

        self.resch = self.findChild(QtWidgets.QCheckBox, 'reschBox')
        self.resch.stateChanged.connect(self.reschClicked)

        self.soro = self.findChild(QtWidgets.QCheckBox, 'soroBox')
        self.soro.stateChanged.connect(self.soroClicked)

        self.sport = self.findChild(QtWidgets.QCheckBox, 'sportBox')
        self.sport.stateChanged.connect(self.sportClicked)

        self.woms = self.findChild(QtWidgets.QCheckBox, 'womsBox')
        self.woms.stateChanged.connect(self.womsClicked)

        self.show()





    def fratClicked(self, state):
        if state == QtCore.Qt.Checked:
            self.fratC = True

    def abroadClicked(self, state):
        if state == QtCore.Qt.Checked:
            self.abroadC = True

    def govClicked(self, state):
        if state == QtCore.Qt.Checked:
            self.govC = True

    def internClicked(self, state):
        if state == QtCore.Qt.Checked:
            self.internC = True

    def medClicked(self, state):
        if state == QtCore.Qt.Checked:
            self.medC = True

    def mensClicked(self, state):
        if state == QtCore.Qt.Checked:
            self.mensC = True

    def reschClicked(self, state):
        if state == QtCore.Qt.Checked:
            self.reschC = True

    def soroClicked(self, state):
        if state == QtCore.Qt.Checked:
            self.soroC = True

    def sportClicked(self, state):
        if state == QtCore.Qt.Checked:
            self.sportC = True

    def womsClicked(self, state):
        if state == QtCore.Qt.Checked:
            self.womsC = True

    def genButtonPressed(self):
        self.didGen = True
        cwd = os.getcwd()
        os.chdir(cwd + '/Documents/BTHOspam')
        f = open("BTHOspam.xml", "w")
        print("""<?xml version='1.0' encoding='UTF-8'?>
        <feed xmlns='http://www.w3.org/2005/Atom' xmlns:apps='http://schemas.google.com/apps/2006'>
                <title>Mail Filters</title>
                <id>tag:mail.google.com,2008:filters:z0000001567917192580*0617137246005040398</id>
                <updated>2019-09-08T03:43:39Z</updated>
                <author>
                        <name>Howdy Hack</name>
                        <email>bthospam@gmail.com</email>
                </author>""",file = f)
        if self.fratC == True:
            print("""<entry>
                        <category term='filter'></category>
                        <title>Mail Filter</title>
                        <id>tag:mail.google.com,2008:filter:z0000001567912531823*5233737762649033417</id>
                        <updated>2019-09-08T03:15:48Z</updated>
                        <content></content>
                        <apps:property name='hasTheWord' value='list:listserv.tamu.edu (alpha OR beta OR gamma OR delta OR epsilon OR zeta OR eta OR theta OR iota OR kappa OR lambda OR mu OR nu OR xi OR omikron OR pi OR rho OR sigma OR tau OR upsilon OR phi OR chi OR psi OR omega) AND fraternity'/>
                        <apps:property name='label' value='BTHO Spam'/>
                        <apps:property name='shouldArchive' value='true'/>
                        <apps:property name='sizeOperator' value='s_sl'/>
                        <apps:property name='sizeUnit' value='s_smb'/>
                </entry>""",file = f)

        if self.abroadC == True:
            print("""<entry>
                        <category term='filter'></category>
                        <title>Mail Filter</title>
                        <id>tag:mail.google.com,2008:filter:z0000001567917879904*1467880677483713220</id>
                        <updated>2019-09-08T04:44:44Z</updated>
                        <content></content>
                        <apps:property name='hasTheWord' value='list:listserv.tamu.edu abroad OR &quot;education abroad&quot;'/>
                        <apps:property name='label' value='BTHO Spam'/>
                        <apps:property name='shouldArchive' value='true'/>
                        <apps:property name='sizeOperator' value='s_sl'/>
                        <apps:property name='sizeUnit' value='s_smb'/>
                </entry>""",file = f)

        if self.govC == True:
            print("""<entry>
                        <category term='filter'></category>
                        <title>Mail Filter</title>
                        <id>tag:mail.google.com,2008:filter:z0000001567917192580*0617137246005040398</id>
                        <updated>2019-09-08T04:33:19Z</updated>
                        <content></content>
                        <apps:property name='hasTheWord' value='list:listserv.tamu.edu &quot;student government&quot; OR sga'/>
                        <apps:property name='label' value='BTHO Spam'/>
                        <apps:property name='shouldArchive' value='true'/>
                        <apps:property name='sizeOperator' value='s_sl'/>
                        <apps:property name='sizeUnit' value='s_smb'/>
                </entry>""",file = f)

        if self.internC == True:
            print("""<entry>
                        <category term='filter'></category>
                        <title>Mail Filter</title>
                        <id>tag:mail.google.com,2008:filter:z0000001567917755320*6893249877257584554</id>
                        <updated>2019-09-08T04:42:39Z</updated>
                        <content></content>
                        <apps:property name='hasTheWord' value='list:listserv.tamu.edu ISA OR &quot;international graduate student&quot;'/>
                        <apps:property name='label' value='BTHO Spam'/>
                        <apps:property name='shouldArchive' value='true'/>
                        <apps:property name='sizeOperator' value='s_sl'/>
                        <apps:property name='sizeUnit' value='s_smb'/>
                </entry>""",file = f)

        if self.medC == True:
            print("""<entry>
                        <category term='filter'></category>
                        <title>Mail Filter</title>
                        <id>tag:mail.google.com,2008:filter:z0000001567917442483*1892543553781177173</id>
                        <updated>2019-09-08T04:37:47Z</updated>
                        <content></content>
                        <apps:property name='hasTheWord' value='list:listserv.tamu.edu nurse OR doctor OR pre-med OR healthcare'/>
                        <apps:property name='label' value='BTHO Spam'/>
                        <apps:property name='shouldArchive' value='true'/>
                        <apps:property name='sizeOperator' value='s_sl'/>
                        <apps:property name='sizeUnit' value='s_smb'/>
                </entry>""",file = f)

        if self.mensC == True:
            print("""<entry>
                        <category term='filter'></category>
                        <title>Mail Filter</title>
                        <id>tag:mail.google.com,2008:filter:z0000001567915694914*8403489171388310768</id>
                        <updated>2019-09-08T04:08:25Z</updated>
                        <content></content>
                        <apps:property name='hasTheWord' value='list:listserv.tamu.edu &quot;men&apos;s organization&quot; OR brotherhood OR &quot;men&apos;s org&quot; OR &quot;men&apos;s club&quot;'/>
                        <apps:property name='label' value='BTHO Spam'/>
                        <apps:property name='shouldArchive' value='true'/>
                        <apps:property name='sizeOperator' value='s_sl'/>
                        <apps:property name='sizeUnit' value='s_smb'/>
                </entry>""",file = f)

        if self.reschC == True:
            print("""<entry>
                        <category term='filter'></category>
                        <title>Mail Filter</title>
                        <id>tag:mail.google.com,2008:filter:z0000001567918049456*4234574684999581917</id>
                        <updated>2019-09-08T04:47:35Z</updated>
                        <content></content>
                        <apps:property name='hasTheWord' value='list:listserv.tamu.edu &quot;paid AROUND 5 study&quot; OR &quot;participants AROUND 5 needed&quot;'/>
                        <apps:property name='label' value='BTHO Spam'/>
                        <apps:property name='shouldArchive' value='true'/>
                        <apps:property name='sizeOperator' value='s_sl'/>
                        <apps:property name='sizeUnit' value='s_smb'/>
                </entry>""",file = f)

        if self.soroC == True:
            print("""<entry>
                        <category term='filter'></category>
                        <title>Mail Filter</title>
                        <id>tag:mail.google.com,2008:filter:z0000001567914205434*5004510095906683057</id>
                        <updated>2019-09-08T03:43:39Z</updated>
                        <content></content>
                        <apps:property name='hasTheWord' value='list:listserv.tamu.edu (alpha OR beta OR gamma OR delta OR epsilon OR zeta OR eta OR theta OR iota OR kappa OR lambda OR mu OR nu OR xi OR omikron OR pi OR rho OR sigma OR tau OR upsilon OR phi OR chi OR psi OR omega) AND sorority'/>
                        <apps:property name='label' value='BTHO Spam'/>
                        <apps:property name='shouldArchive' value='true'/>
                        <apps:property name='sizeOperator' value='s_sl'/>
                        <apps:property name='sizeUnit' value='s_smb'/>
                </entry>""",file = f)

        if self.sportC == True:
            print("""<entry>
                        <category term='filter'></category>
                        <title>Mail Filter</title>
                        <id>tag:mail.google.com,2008:filter:z0000001567916588556*4133876267288466267</id>
                        <updated>2019-09-08T04:23:54Z</updated>
                        <content></content>
                        <apps:property name='hasTheWord' value='list:listserv.tamu.edu &quot;flag football&quot; OR soccer OR softball OR basketball OR volleyball OR fitness OR tryouts OR swim'/>
                        <apps:property name='label' value='BTHO Spam'/>
                        <apps:property name='shouldArchive' value='true'/>
                        <apps:property name='sizeOperator' value='s_sl'/>
                        <apps:property name='sizeUnit' value='s_smb'/>
                </entry>""",file = f)


        if self.womsC == True:
            print("""<entry>
                        <category term='filter'></category>
                        <title>Mail Filter</title>
                        <id>tag:mail.google.com,2008:filter:z0000001567915852475*8708319040071074691</id>
                        <updated>2019-09-08T04:10:58Z</updated>
                        <content></content>
                        <apps:property name='hasTheWord' value='list:listserv.tamu.edu sisterhood OR &quot;woman&apos;s org&quot; OR &quot;woman&apos;s organization&quot; OR &quot;woman&apos;s club&quot;'/>
                        <apps:property name='label' value='BTHO Spam'/>
                        <apps:property name='shouldArchive' value='true'/>
                        <apps:property name='sizeOperator' value='s_sl'/>
                        <apps:property name='sizeUnit' value='s_smb'/>
                </entry>""",file = f)




        print("""</feed>""",file = f)
        f.close()

app = QtWidgets.QApplication(sys.argv)
window = Ui()
app.exec_()
webbrowser.open_new_tab(filterSite)
