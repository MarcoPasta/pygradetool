# -*- coding: utf-8 -*-
import os

from PyQt5 import QtCore, QtGui, QtWidgets
import sys

class Ui_PyGradeTool(object):

    def setupUi(self, PyGradeTool):
        PyGradeTool.setObjectName("PyGradeTool")
        PyGradeTool.setEnabled(True)
        PyGradeTool.resize(800, 710)
        PyGradeTool.setTabletTracking(False)
        PyGradeTool.setFocusPolicy(QtCore.Qt.NoFocus)
        # Hat auf Linux funktioniert, sorgt in Windows aber dafür das man das Fenster nicht sehen kann
        # PyGradeTool.setWindowOpacity(0.0)        
        PyGradeTool.setAcceptDrops(False)
        PyGradeTool.setToolTipDuration(-1)
        self.zu_bewerten_in = QtWidgets.QLineEdit(PyGradeTool)
        self.zu_bewerten_in.setGeometry(QtCore.QRect(10, 50, 401, 25))
        self.zu_bewerten_in.setObjectName("zu_bewerten_in")
        self.zu_bewerten = QtWidgets.QLabel(PyGradeTool)
        self.zu_bewerten.setGeometry(QtCore.QRect(10, 30, 261, 17))
        self.zu_bewerten.setObjectName("zu_bewerten")
        self.bewertender_in = QtWidgets.QLineEdit(PyGradeTool)
        self.bewertender_in.setGeometry(QtCore.QRect(10, 100, 401, 25))
        self.bewertender_in.setObjectName("bewertender_in")
        self.bewertender = QtWidgets.QLabel(PyGradeTool)
        self.bewertender.setGeometry(QtCore.QRect(10, 80, 261, 17))
        self.bewertender.setObjectName("bewertender")
        self.kriterium = QtWidgets.QLineEdit(PyGradeTool)
        self.kriterium.setGeometry(QtCore.QRect(10, 150, 541, 25))
        self.kriterium.setObjectName("kriterium")
        self.kriterium_2 = QtWidgets.QLineEdit(PyGradeTool)
        self.kriterium_2.setGeometry(QtCore.QRect(10, 180, 541, 25))
        self.kriterium_2.setObjectName("kriterium_2")
        self.kriterium_3 = QtWidgets.QLineEdit(PyGradeTool)
        self.kriterium_3.setGeometry(QtCore.QRect(10, 210, 541, 25))
        self.kriterium_3.setObjectName("kriterium_3")
        self.kriterium_4 = QtWidgets.QLineEdit(PyGradeTool)
        self.kriterium_4.setGeometry(QtCore.QRect(10, 240, 541, 25))
        self.kriterium_4.setObjectName("kriterium_4")
        self.kriterium_5 = QtWidgets.QLineEdit(PyGradeTool)
        self.kriterium_5.setGeometry(QtCore.QRect(10, 270, 541, 25))
        self.kriterium_5.setObjectName("kriterium_5")
        self.kriterium_6 = QtWidgets.QLineEdit(PyGradeTool)
        self.kriterium_6.setGeometry(QtCore.QRect(10, 300, 541, 25))
        self.kriterium_6.setObjectName("kriterium_6")
        self.kriterium_7 = QtWidgets.QLineEdit(PyGradeTool)
        self.kriterium_7.setGeometry(QtCore.QRect(10, 330, 541, 25))
        self.kriterium_7.setObjectName("kriterium_7")
        self.kriterium_8 = QtWidgets.QLineEdit(PyGradeTool)
        self.kriterium_8.setGeometry(QtCore.QRect(10, 360, 541, 25))
        self.kriterium_8.setObjectName("kriterium_8")
        self.kriterium_von = QtWidgets.QLineEdit(PyGradeTool)
        self.kriterium_von.setGeometry(QtCore.QRect(720, 150, 61, 25))
        self.kriterium_von.setObjectName("kriterium_von")
        self.kriterium_in = QtWidgets.QLineEdit(PyGradeTool)
        self.kriterium_in.setGeometry(QtCore.QRect(630, 150, 61, 25))
        self.kriterium_in.setObjectName("kriterium_in")
        self.kriterium_in_2 = QtWidgets.QLineEdit(PyGradeTool)
        self.kriterium_in_2.setGeometry(QtCore.QRect(630, 180, 61, 25))
        self.kriterium_in_2.setObjectName("kriterium_in_2")
        self.kriterium_in_3 = QtWidgets.QLineEdit(PyGradeTool)
        self.kriterium_in_3.setGeometry(QtCore.QRect(630, 210, 61, 25))
        self.kriterium_in_3.setObjectName("kriterium_in_3")
        self.kriterium_in_4 = QtWidgets.QLineEdit(PyGradeTool)
        self.kriterium_in_4.setGeometry(QtCore.QRect(630, 240, 61, 25))
        self.kriterium_in_4.setObjectName("kriterium_in_4")
        self.kriterium_in_5 = QtWidgets.QLineEdit(PyGradeTool)
        self.kriterium_in_5.setGeometry(QtCore.QRect(630, 270, 61, 25))
        self.kriterium_in_5.setObjectName("kriterium_in_5")
        self.kriterium_in_6 = QtWidgets.QLineEdit(PyGradeTool)
        self.kriterium_in_6.setGeometry(QtCore.QRect(630, 300, 61, 25))
        self.kriterium_in_6.setObjectName("kriterium_in_6")
        self.kriterium_in_7 = QtWidgets.QLineEdit(PyGradeTool)
        self.kriterium_in_7.setGeometry(QtCore.QRect(630, 330, 61, 25))
        self.kriterium_in_7.setObjectName("kriterium_in_7")
        self.kriterium_in_8 = QtWidgets.QLineEdit(PyGradeTool)
        self.kriterium_in_8.setGeometry(QtCore.QRect(630, 360, 61, 25))
        self.kriterium_in_8.setObjectName("kriterium_in_8")
        self.kriterium_von_3 = QtWidgets.QLineEdit(PyGradeTool)
        self.kriterium_von_3.setGeometry(QtCore.QRect(720, 210, 61, 25))
        self.kriterium_von_3.setObjectName("kriterium_von_3")
        self.kriterium_von_4 = QtWidgets.QLineEdit(PyGradeTool)
        self.kriterium_von_4.setGeometry(QtCore.QRect(720, 240, 61, 25))
        self.kriterium_von_4.setObjectName("kriterium_von_4")
        self.kriterium_von_5 = QtWidgets.QLineEdit(PyGradeTool)
        self.kriterium_von_5.setGeometry(QtCore.QRect(720, 270, 61, 25))
        self.kriterium_von_5.setObjectName("kriterium_von_5")
        self.kriterium_von_6 = QtWidgets.QLineEdit(PyGradeTool)
        self.kriterium_von_6.setGeometry(QtCore.QRect(720, 300, 61, 25))
        self.kriterium_von_6.setObjectName("kriterium_von_6")
        self.kriterium_von_7 = QtWidgets.QLineEdit(PyGradeTool)
        self.kriterium_von_7.setGeometry(QtCore.QRect(720, 330, 61, 25))
        self.kriterium_von_7.setObjectName("kriterium_von_7")
        self.kriterium_von_8 = QtWidgets.QLineEdit(PyGradeTool)
        self.kriterium_von_8.setGeometry(QtCore.QRect(720, 360, 61, 25))
        self.kriterium_von_8.setObjectName("kriterium_von_8")
        self.slash_1 = QtWidgets.QLabel(PyGradeTool)
        self.slash_1.setGeometry(QtCore.QRect(700, 150, 16, 17))
        self.slash_1.setObjectName("slash_1")
        self.kriterium_von_2 = QtWidgets.QLineEdit(PyGradeTool)
        self.kriterium_von_2.setGeometry(QtCore.QRect(720, 180, 61, 25))
        self.kriterium_von_2.setObjectName("kriterium_von_2")
        self.slash_2 = QtWidgets.QLabel(PyGradeTool)
        self.slash_2.setGeometry(QtCore.QRect(700, 180, 16, 17))
        self.slash_2.setObjectName("slash_2")
        self.slash_3 = QtWidgets.QLabel(PyGradeTool)
        self.slash_3.setGeometry(QtCore.QRect(700, 210, 16, 17))
        self.slash_3.setObjectName("slash_3")
        self.slash_4 = QtWidgets.QLabel(PyGradeTool)
        self.slash_4.setGeometry(QtCore.QRect(700, 240, 16, 17))
        self.slash_4.setObjectName("slash_4")
        self.slash_5 = QtWidgets.QLabel(PyGradeTool)
        self.slash_5.setGeometry(QtCore.QRect(700, 270, 16, 17))
        self.slash_5.setObjectName("slash_5")
        self.slash_6 = QtWidgets.QLabel(PyGradeTool)
        self.slash_6.setGeometry(QtCore.QRect(700, 300, 16, 17))
        self.slash_6.setObjectName("slash_6")
        self.slash_7 = QtWidgets.QLabel(PyGradeTool)
        self.slash_7.setGeometry(QtCore.QRect(700, 330, 16, 17))
        self.slash_7.setObjectName("slash_7")
        self.slash_8 = QtWidgets.QLabel(PyGradeTool)
        self.slash_8.setGeometry(QtCore.QRect(700, 360, 16, 17))
        self.slash_8.setObjectName("slash_8")
        self.kommentar = QtWidgets.QLabel(PyGradeTool)
        self.kommentar.setGeometry(QtCore.QRect(10, 400, 91, 17))
        self.kommentar.setObjectName("kommentar")
        self.hinweise = QtWidgets.QLabel(PyGradeTool)
        self.hinweise.setGeometry(QtCore.QRect(10, 520, 91, 17))
        self.hinweise.setFocusPolicy(QtCore.Qt.NoFocus)
        self.hinweise.setObjectName("hinweise")
        self.musterloesung = QtWidgets.QLabel(PyGradeTool)
        self.musterloesung.setGeometry(QtCore.QRect(10, 640, 101, 17))
        self.musterloesung.setObjectName("musterloesung")
        self.summe_in = QtWidgets.QLineEdit(PyGradeTool)
        self.summe_in.setGeometry(QtCore.QRect(630, 390, 61, 25))
        self.summe_in.setObjectName("summe_in")
        self.summe_von = QtWidgets.QLineEdit(PyGradeTool)
        self.summe_von.setGeometry(QtCore.QRect(720, 390, 61, 25))
        self.summe_von.setObjectName("summe_von")
        self.slash_9 = QtWidgets.QLabel(PyGradeTool)
        self.slash_9.setGeometry(QtCore.QRect(700, 390, 16, 17))
        self.slash_9.setObjectName("slash_9")
        self.kommentar_in = QtWidgets.QTextEdit(PyGradeTool)
        self.kommentar_in.setGeometry(QtCore.QRect(10, 420, 541, 91))
        self.kommentar_in.setTabletTracking(True)
        self.kommentar_in.setObjectName("kommentar_in")
        self.hinweise_in = QtWidgets.QTextEdit(PyGradeTool)
        self.hinweise_in.setGeometry(QtCore.QRect(10, 540, 541, 91))
        self.hinweise_in.setObjectName("hinweise_in")
        self.musterloesung_in = QtWidgets.QLineEdit(PyGradeTool)
        self.musterloesung_in.setGeometry(QtCore.QRect(10, 660, 541, 25))
        self.musterloesung_in.setObjectName("musterloesung_in")
        self.bewertung_generieren = QtWidgets.QPushButton(PyGradeTool)
        self.bewertung_generieren.setGeometry(QtCore.QRect(630, 450, 160, 25))
        self.bewertung_generieren.setObjectName("bewertung_generieren")
        self.compiler_fehler_checkbox = QtWidgets.QCheckBox(PyGradeTool)
        self.compiler_fehler_checkbox.setGeometry(QtCore.QRect(630, 415, 25, 25))
        self.compiler_fehler_checkbox.setObjectName("compiler_fehler_checkbox")
        self.compiler_fehler_label = QtWidgets.QLabel(PyGradeTool)
        self.compiler_fehler_label.setGeometry(QtCore.QRect(650, 415, 150, 25))
        self.compiler_fehler_label.setObjectName("compiler_fehler_label")
        self.zu_bewerten_in.raise_()
        self.zu_bewerten.raise_()
        self.bewertender_in.raise_()
        self.bewertender.raise_()
        self.kriterium.raise_()
        self.kriterium_2.raise_()
        self.kriterium_3.raise_()
        self.kriterium_4.raise_()
        self.kriterium_5.raise_()
        self.kriterium_6.raise_()
        self.kriterium_7.raise_()
        self.kriterium_von.raise_()
        self.kriterium_in.raise_()
        self.kriterium_in_2.raise_()
        self.kriterium_in_3.raise_()
        self.kriterium_in_4.raise_()
        self.kriterium_in_5.raise_()
        self.kriterium_in_6.raise_()
        self.kriterium_in_7.raise_()
        self.kriterium_von_3.raise_()
        self.kriterium_von_4.raise_()
        self.kriterium_von_5.raise_()
        self.kriterium_von_6.raise_()
        self.kriterium_von_7.raise_()
        self.kriterium_von_8.raise_()
        self.slash_1.raise_()
        self.kriterium_von_2.raise_()
        self.slash_2.raise_()
        self.slash_3.raise_()
        self.slash_4.raise_()
        self.slash_5.raise_()
        self.slash_6.raise_()
        self.slash_7.raise_()
        self.slash_8.raise_()
        self.kommentar.raise_()
        self.hinweise.raise_()
        self.musterloesung.raise_()
        self.summe_in.raise_()
        self.summe_von.raise_()
        self.slash_9.raise_()
        self.hinweise_in.raise_()
        self.kommentar_in.raise_()
        self.musterloesung_in.raise_()
        self.bewertung_generieren.raise_()
        self.compiler_fehler_checkbox.raise_()
        self.compiler_fehler_label.raise_()
        self.retranslateUi(PyGradeTool)
        QtCore.QMetaObject.connectSlotsByName(PyGradeTool)

        # For debugging purposes 
        # self.bewertung_generieren.clicked.connect(self.click_on_check)
        self.bewertung_generieren.clicked.connect(self.berechne_summe)
        self.bewertung_generieren.clicked.connect(self.create_html)

    def retranslateUi(self, PyGradeTool):
        _translate = QtCore.QCoreApplication.translate
        PyGradeTool.setWindowTitle(_translate("PyGradeTool", "PyGradeTool by MarcoPasta"))
        self.zu_bewerten.setText(_translate("PyGradeTool", "Zu bewertende Person"))
        self.bewertender.setText(_translate("PyGradeTool", "Bewertende Person"))
        self.slash_1.setText(_translate("PyGradeTool", "/"))
        self.slash_2.setText(_translate("PyGradeTool", "/"))
        self.slash_3.setText(_translate("PyGradeTool", "/"))
        self.slash_4.setText(_translate("PyGradeTool", "/"))
        self.slash_5.setText(_translate("PyGradeTool", "/"))
        self.slash_6.setText(_translate("PyGradeTool", "/"))
        self.slash_7.setText(_translate("PyGradeTool", "/"))
        self.slash_9.setText(_translate("PyGradeTool", "/"))
        self.kommentar.setText(_translate("PyGradeTool", "Kommentare"))
        self.hinweise.setText(_translate("PyGradeTool", "Hinweise"))
        self.musterloesung.setText(_translate("PyGradeTool", "Musterlösung"))
        self.slash_8.setText(_translate("PyGradeTool", "/"))
        self.bewertung_generieren.setText(_translate("PyGradeTool", "Bewertung generieren"))
        self.compiler_fehler_label.setText(_translate("PyGradeTool", "Compiler Fehler"))

    def berechne_summe(self):
        self.number_in = 0
        self.number_von = 0
        if not self.kriterium_in.text() == "":
            self.number_in += int(self.kriterium_in.text())
        if not self.kriterium_in_2.text() == "":
            self.number_in += int(self.kriterium_in_2.text())
        if not self.kriterium_in_3.text() == "":
            self.number_in += int(self.kriterium_in_3.text())
        if not self.kriterium_in_4.text() == "":
            self.number_in += int(self.kriterium_in_4.text())
        if not self.kriterium_in_5.text() == "":
            self.number_in += int(self.kriterium_in_5.text())
        if not self.kriterium_in_6.text() == "":
            self.number_in += int(self.kriterium_in_6.text())
        if not self.kriterium_in_7.text() == "":
            self.number_in += int(self.kriterium_in_7.text())
        if not self.kriterium_in_8.text() == "":
            self.number_in += int(self.kriterium_in_8.text())
        # print(self.number_in)
        if self.compiler_fehler_checkbox.isChecked():
            self.number_in = 0
        self.summe_in.setText(str(self.number_in))

        if not self.kriterium_von.text() == "":
            self.number_von += int(self.kriterium_von.text())
        if not self.kriterium_von_2.text() == "":
            self.number_von += int(self.kriterium_von_2.text())
        if not self.kriterium_von_3.text() == "":
            self.number_von += int(self.kriterium_von_3.text())
        if not self.kriterium_von_4.text() == "":
            self.number_von += int(self.kriterium_von_4.text())
        if not self.kriterium_von_5.text() == "":
            self.number_von += int(self.kriterium_von_5.text())
        if not self.kriterium_von_6.text() == "":
            self.number_von += int(self.kriterium_von_6.text())
        if not self.kriterium_von_7.text() == "":
            self.number_von += int(self.kriterium_von_7.text())
        if not self.kriterium_von_8.text() == "":
            self.number_von += int(self.kriterium_von_8.text())
        # print(self.number_von)
        self.summe_von.setText(str(self.number_von))

    # For debuggin only
    # def click_on_check(self):
        # print(self.zu_bewerten.text())
        # print(self.bewertender.text())
        # print(self.kriterium.text())
        # print(self.kriterium_2.text())
        # print(self.kriterium_3.text())
        # print(self.kriterium_4.text())
        # print(self.kriterium_5.text())
        # print(self.kriterium_6.text())
        # print(self.kriterium_7.text())
        # print(self.kriterium_in.text())
        # print(self.kriterium_in_2.text())
        # print(self.kriterium_in_3.text())
        # print(self.kriterium_in_4.text())
        # print(self.kriterium_in_5.text())
        # print(self.kriterium_in_6.text())
        # print(self.kriterium_in_7.text())
        # print(self.kriterium_von.text())
        # print(self.kriterium_von_2.text())
        # print(self.kriterium_von_3.text())
        # print(self.kriterium_von_4.text())
        # print(self.kriterium_von_5.text())
        # print(self.kriterium_von_6.text())
        # print(self.kriterium_von_7.text())
        # print(self.kommentar_in.toPlainText())
        # print(self.hinweise_in.toPlainText())
        # print(self.musterloesung_in.text())

    def create_html(self):
        # Debuggin
        # print(type(program_name))
        
        # Replace spaces in current strint with underscore for better html format on linux
        program_name = self.zu_bewerten_in.text().replace(" ", "_")

        if not os.path.exists("html"):
            os.system("mkdir html")
        else:
            print("directory exists already")

        # print(program_name)
        # f = open("./html/" + program_name + ".html", "w", encoding='utf8')
        f = open("html/" + program_name + ".html", "w", encoding='utf8')

        html_file_begin = f"""<div>
                    <table class="content-table" style="border-collapse: collapse;margin: 25px 0;font-size: 0.9em;border-radius: 5px 5px 0 0;overflow: hidden;box-shadow: 0 0 20px rgba(0, 0, 0, 0.15);">
                        <thead>
                            <tr style="background-color: #009879;color: #ffffff;text-align: left;font-weight: bold;">
                                <th style="padding: 12px 15px;"></th>
                                <th style="padding: 12px 15px;"></th>
                            </tr>
                        </thead>
                        <tbody>
                            <tr style="border-bottom: 1px solid #dddddd;">
                                <td style="padding: 12px 15px;"><b>Bewertende Person</b></td>
                                <td style="padding: 12px 15px;">{self.bewertender_in.text()}</td>
                            </tr>
                            <tr style="border-bottom: 1px solid #dddddd;">
                                <td style="padding: 12px 15px;"><b>Zu Bewertende Person</b></td>
                                <td style="padding: 12px 15px;">{self.zu_bewerten_in.text()}</td>
                            </tr>
                        </tbody>
                        <thead>
                        <tr style="background-color: #009879;color: #ffffff;text-align: left;font-weight: bold;">
                            <th style="padding: 12px 15px;">Bewertungsschema</th>
                            <th style="padding: 12px 15px;">Punkte</th>
                        </tr>
                        </thead>
                        <tbody>"""

        html_krit1 = f"""<tr style="border-bottom: 1px solid #dddddd;">
            <td style="padding: 12px 15px;">{self.kriterium.text()}</td>
            <td style="padding: 12px 15px;">{self.kriterium_in.text()}/{self.kriterium_von.text()}</td>
        </tr>"""

        html_krit2 = f"""<tr class="active-row" style="border-bottom: 1px solid #dddddd;font-weight: bold;color: #009879;">
            <td style="padding: 12px 15px;">{self.kriterium_2.text()}</td>
            <td style="padding: 12px 15px;">{self.kriterium_in_2.text()}/{self.kriterium_von_2.text()}</td>
        </tr>"""

        html_krit3 = f"""<tr style="border-bottom: 1px solid #dddddd;">
            <td style="padding: 12px 15px;">{self.kriterium_3.text()}</td>
            <td style="padding: 12px 15px;">{self.kriterium_in_3.text()}/{self.kriterium_von_3.text()}</td>
        </tr>"""

        html_krit4 = f"""<tr class="active-row" style="border-bottom: 1px solid #dddddd;font-weight: bold;color: #009879;">
            <td style="padding: 12px 15px;">{self.kriterium_4.text()}</td>
            <td style="padding: 12px 15px;">{self.kriterium_in_4.text()}/{self.kriterium_von_4.text()}</td>
        </tr>"""

        html_krit5 = f"""<tr style="border-bottom: 1px solid #dddddd;">
            <td style="padding: 12px 15px;">{self.kriterium_5.text()}</td>
            <td style="padding: 12px 15px;">{self.kriterium_in_5.text()}/{self.kriterium_von_5.text()}</td>
        </tr>"""

        html_krit6 = f"""<tr class="active-row" style="border-bottom: 1px solid #dddddd;font-weight: bold;color: #009879;">
            <td style="padding: 12px 15px;">{self.kriterium_6.text()}</td>
            <td style="padding: 12px 15px;">{self.kriterium_in_6.text()}/{self.kriterium_von_6.text()}</td>
        </tr>"""

        html_krit7 = f"""<tr style="border-bottom: 1px solid #dddddd;">
            <td style="padding: 12px 15px;">{self.kriterium_7.text()}</td>
            <td style="padding: 12px 15px;">{self.kriterium_in_7.text()}/{self.kriterium_von_7.text()}</td>
        </tr>"""

        html_krit8 = f"""<tr style="border-bottom: 1px solid #dddddd;">
            <td style="padding: 12px 15px;">{self.kriterium_8.text()}</td>
            <td style="padding: 12px 15px;">{self.kriterium_in_8.text()}/{self.kriterium_von_8.text()}</td>
        </tr>"""

        if not self.compiler_fehler_checkbox.isChecked():
            html_file_end = f"""<tr class="active-row" style="border-bottom: 1px solid #dddddd;font-weight: bold;color: #009879;">
                                <td style="padding: 12px 15px;">Summe</td>
                                <td style="padding: 12px 15px;">{self.summe_in.text()}/{self.summe_von.text()}</td>
                            </tr>
                            </tbody>
                        </table>
                        <br>
                        <h4>Kommentar</h4>
                        <pre style="white-space:pre-wrap;word-wrap:break-word;">{self.kommentar_in.toPlainText()}</pre>
                        <br>
                        <h4>Hinweise</h4>
                        <pre style="white-space:pre-wrap;word-wrap:break-word;">{self.hinweise_in.toPlainText()}</pre>
                        <br>
                        <h4>Musterlösung</h4>
                        <a href="{self.musterloesung_in.text()}">{self.musterloesung_in.text()}</a>
                    </div>
            """
        else:
            html_file_end = f"""<tr class="active-row" style="border-bottom: 1px solid #dddddd;font-weight: bold;color: #009879;">
                                <td style="padding: 12px 15px;">Summe</td>
                                <td style="padding: 12px 15px;">{self.summe_in.text()}/{self.summe_von.text()}</td>
                            </tr>
                            </tbody>
                        </table>
                        <p style="font-weight: bold;color: #FF0000;">Compiler Fehler ===> 0 Punkte!</p>
                        <br>
                        <h4>Kommentar</h4>
                        <pre style="white-space:pre-wrap;word-wrap:break-word;">{self.kommentar_in.toPlainText()}</pre>
                        <br>
                        <h4>Hinweise</h4>
                        <pre style="white-space:pre-wrap;word-wrap:break-word;">{self.hinweise_in.toPlainText()}</pre>
                        <br>
                        <h4>Musterlösung</h4>
                        <a href="{self.musterloesung_in.text()}">{self.musterloesung_in.text()}</a>
                    </div>
            """

        html_file = html_file_begin

        if not (self.kriterium.text() and self.kriterium_in.text() and self.kriterium_von.text()) == "":
            html_file += html_krit1

        if not (self.kriterium_2.text() and self.kriterium_in_2.text() and self.kriterium_von_2.text()) == "":
            html_file += html_krit2

        if not (self.kriterium_3.text() and self.kriterium_in_3.text() and self.kriterium_von_3.text()) == "":
            html_file += html_krit3

        if not (self.kriterium_4.text() and self.kriterium_in_4.text() and self.kriterium_von_4.text()) == "":
            html_file += html_krit4

        if not (self.kriterium_5.text() and self.kriterium_in_5.text() and self.kriterium_von_5.text()) == "":
            html_file += html_krit5

        if not (self.kriterium_6.text() and self.kriterium_in_6.text() and self.kriterium_von_6.text()) == "":
            html_file += html_krit6

        if not (self.kriterium_7.text() and self.kriterium_in_7.text() and self.kriterium_von_7.text()) == "":
            html_file += html_krit7

        if not (self.kriterium_8.text() and self.kriterium_in_8.text() and self.kriterium_von_8.text()) == "":
            html_file += html_krit8

        html_file += html_file_end

        f.write(html_file)
        f.close()
        # Summe und Vorzeiger(?) wieder auf 0 setzen damit die Summe immer aktuell bleibt
        self.number_in = 0
        self.number_von = 0


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    PyGradeTool = QtWidgets.QWidget()
    ui = Ui_PyGradeTool()
    ui.setupUi(PyGradeTool)
    PyGradeTool.show()
    PyGradeTool.setFixedSize(PyGradeTool.size())
    sys.exit(app.exec())
