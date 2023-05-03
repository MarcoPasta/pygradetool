# -*- coding: utf-8 -*-
import sys
import os
from PyQt5 import QtWidgets, QtCore, QtGui

import modules.html_template as tmplt
import modules.auto_pdf as auto_pdf

class Ui_PyGradeTool(QtWidgets.QWidget):

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
        self.zu_bewerten = QtWidgets.QLabel(PyGradeTool)
        self.zu_bewerten.setGeometry(QtCore.QRect(10, 30, 261, 17))
        self.zu_bewerten.setObjectName("zu_bewerten")
        self.zu_bewerten_in = QtWidgets.QLineEdit(PyGradeTool)
        self.zu_bewerten_in.setGeometry(QtCore.QRect(10, 50, 401, 25))
        self.zu_bewerten_in.setObjectName("zu_bewerten_in")
        self.bewertender = QtWidgets.QLabel(PyGradeTool)
        self.bewertender.setGeometry(QtCore.QRect(10, 80, 261, 17))
        self.bewertender.setObjectName("bewertender")
        self.bewertender_in = QtWidgets.QLineEdit(PyGradeTool)
        self.bewertender_in.setGeometry(QtCore.QRect(10, 100, 401, 25))
        self.bewertender_in.setObjectName("bewertender_in")
        # Kriterien Input ----------------------------------
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
        # Liste mit Kriterien
        self.krit = [self.kriterium, self.kriterium_2, self.kriterium_3, self.kriterium_4,
                     self.kriterium_5, self.kriterium_6, self.kriterium_7, self.kriterium_8]
        # Krit Score In ----------------------------------
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
        # Liste mit Kriterien Inputs
        self.krit_in = [self.kriterium_in, self.kriterium_in_2, self.kriterium_in_3,
                        self.kriterium_in_4, self.kriterium_in_5, self.kriterium_in_6,
                        self.kriterium_in_7, self.kriterium_in_8]
        # Krit Score Von --------------------------------------------
        self.kriterium_von = QtWidgets.QLineEdit(PyGradeTool)
        self.kriterium_von.setGeometry(QtCore.QRect(720, 150, 61, 25))
        self.kriterium_von.setObjectName("kriterium_von")
        self.kriterium_von_2 = QtWidgets.QLineEdit(PyGradeTool)
        self.kriterium_von_2.setGeometry(QtCore.QRect(720, 180, 61, 25))
        self.kriterium_von_2.setObjectName("kriterium_von_2")
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
        # Liste mit Krit Von
        self.krit_von = [self.kriterium_von, self.kriterium_von_2, self.kriterium_von_3,
                         self.kriterium_von_4, self.kriterium_von_5, self.kriterium_von_6,
                         self.kriterium_von_7, self.kriterium_von_8]
        # Slash -------------------------------------------
        self.slash_1 = QtWidgets.QLabel(PyGradeTool)
        self.slash_1.setGeometry(QtCore.QRect(700, 150, 16, 17))
        self.slash_1.setObjectName("slash_1")
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
        # Kommentare - Hinweise - Musterloesung ------------
        self.kommentar = QtWidgets.QLabel(PyGradeTool)
        self.kommentar.setGeometry(QtCore.QRect(10, 400, 91, 17))
        self.kommentar.setObjectName("kommentar")
        self.kommentar_in = QtWidgets.QTextEdit(PyGradeTool)
        self.kommentar_in.setGeometry(QtCore.QRect(10, 420, 541, 91))
        self.kommentar_in.setTabletTracking(True)
        self.kommentar_in.setObjectName("kommentar_in")
        self.hinweise = QtWidgets.QLabel(PyGradeTool)
        self.hinweise.setGeometry(QtCore.QRect(10, 520, 91, 17))
        self.hinweise.setFocusPolicy(QtCore.Qt.NoFocus)
        self.hinweise.setObjectName("hinweise")
        self.hinweise_in = QtWidgets.QTextEdit(PyGradeTool)
        self.hinweise_in.setGeometry(QtCore.QRect(10, 540, 541, 91))
        self.hinweise_in.setObjectName("hinweise_in")
        self.musterloesung = QtWidgets.QLabel(PyGradeTool)
        self.musterloesung.setGeometry(QtCore.QRect(10, 640, 101, 17))
        self.musterloesung.setObjectName("musterloesung")
        self.musterloesung_in = QtWidgets.QLineEdit(PyGradeTool)
        self.musterloesung_in.setGeometry(QtCore.QRect(10, 660, 541, 25))
        self.musterloesung_in.setObjectName("musterloesung_in")
        # Summe -------------------------------------------
        self.summe_in = QtWidgets.QLineEdit(PyGradeTool)
        self.summe_in.setGeometry(QtCore.QRect(630, 390, 61, 25))
        self.summe_in.setObjectName("summe_in")
        self.summe_von = QtWidgets.QLineEdit(PyGradeTool)
        self.summe_von.setGeometry(QtCore.QRect(720, 390, 61, 25))
        self.summe_von.setObjectName("summe_von")
        self.slash_9 = QtWidgets.QLabel(PyGradeTool)
        self.slash_9.setGeometry(QtCore.QRect(700, 390, 16, 17))
        self.slash_9.setObjectName("slash_9")
        # Buttons - Checkboxes ----------------------------
        self.file_dialog_label = QtWidgets.QLabel(PyGradeTool)
        self.file_dialog_label.setGeometry(QtCore.QRect(630, 70, 110, 30))
        self.file_dialog_label.setObjectName("file_dialog_label")
        self.file_dialog = QtWidgets.QPushButton(PyGradeTool)
        self.file_dialog.setGeometry(QtCore.QRect(630, 100, 61, 30))
        self.file_dialog.setObjectName("file_dialog_button")
        self.compiler_fehler_label = QtWidgets.QLabel(PyGradeTool)
        self.compiler_fehler_label.setGeometry(QtCore.QRect(650, 415, 150, 25))
        self.compiler_fehler_label.setObjectName("compiler_fehler_label")
        self.compiler_fehler_checkbox = QtWidgets.QCheckBox(PyGradeTool)
        self.compiler_fehler_checkbox.setGeometry(QtCore.QRect(630, 415, 25, 25))
        self.compiler_fehler_checkbox.setObjectName("compiler_fehler_checkbox")
        self.bewertung_generieren = QtWidgets.QPushButton(PyGradeTool)
        self.bewertung_generieren.setGeometry(QtCore.QRect(630, 450, 160, 25))
        self.bewertung_generieren.setObjectName("bewertung_generieren")
        self.colorpicker_green_checkbox = QtWidgets.QCheckBox(PyGradeTool)
        self.colorpicker_green_checkbox.setGeometry(QtCore.QRect(630, 490, 25, 25))
        self.colorpicker_green_checkbox.setObjectName("colopicker_green_checkbox")
        self.colorpicker_green_label = QtWidgets.QLabel(PyGradeTool)
        self.colorpicker_green_label.setGeometry(QtCore.QRect(670, 492, 20, 20))
        self.colorpicker_green_label.setObjectName("color_green_picker")

        self.colorpicker_blue_checkbox = QtWidgets.QCheckBox(PyGradeTool)
        self.colorpicker_blue_checkbox.setGeometry(QtCore.QRect(630, 520, 25, 25))
        self.colorpicker_blue_checkbox.setObjectName("colopicker_blue_checkbox")
        self.colorpicker_blue_label = QtWidgets.QLabel(PyGradeTool)
        self.colorpicker_blue_label.setGeometry(QtCore.QRect(670, 522, 20, 20))
        self.colorpicker_blue_label.setObjectName("color_blue_picker")

        self.colorpicker_pink_checkbox = QtWidgets.QCheckBox(PyGradeTool)
        self.colorpicker_pink_checkbox.setGeometry(QtCore.QRect(630, 550, 25, 25))
        self.colorpicker_pink_checkbox.setObjectName("colopicker_pink_checkbox")
        self.colorpicker_pink_label = QtWidgets.QLabel(PyGradeTool)
        self.colorpicker_pink_label.setGeometry(QtCore.QRect(670, 552, 20, 20))
        self.colorpicker_pink_label.setObjectName("color_pink_picker")


        

        # raise ----------------------------------------------
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


    def retranslateUi(self, PyGradeTool):
        _translate = QtCore.QCoreApplication.translate
        PyGradeTool.setWindowTitle(_translate("PyGradeTool", "PyGradeTool by MarcoPasta"))
        self.zu_bewerten.setText(_translate("PyGradeTool", "Zu bewertende Person"))
        self.bewertender.setText(_translate("PyGradeTool", "Bewertende Person"))
        self.file_dialog_label.setText(_translate("PyGradeTool", "PDF auswählen"))
        self.file_dialog.setIcon(self.style().standardIcon(QtWidgets.QStyle.SP_DialogOpenButton))
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
        self.compiler_fehler_label.setText(_translate("PyGradeTool", "Compiler Fehler"))
        self.bewertung_generieren.setText(_translate("PyGradeTool", "Bewertung generieren"))
        self.colorpicker_green_label.setStyleSheet("""  border: 3px solid #009879;
                                                        border-radius: 10px; 
                                                        background-color: #009879""")
        self.colorpicker_blue_label.setStyleSheet("""  border: 3px solid #04aed4;
                                                        border-radius: 10px; 
                                                        background-color: #04aed4""")
        self.colorpicker_pink_label.setStyleSheet("""  border: 3px solid #fc14da;
                                                        border-radius: 10px; 
                                                        background-color: #fc14da""")
        self.colorpicker_green_checkbox.setChecked(True)
        self.colorpicker_green_checkbox.stateChanged.connect(self.checkbox_handler)
        self.colorpicker_blue_checkbox.stateChanged.connect(self.checkbox_handler)
        self.colorpicker_pink_checkbox.stateChanged.connect(self.checkbox_handler)
        self.bewertung_generieren.clicked.connect(self.berechne_summe)
        self.bewertung_generieren.clicked.connect(self.create_html)
        self.file_dialog.clicked.connect(self.detect_from_pdf)


    def checkbox_handler(self):
        if self.sender() == self.colorpicker_green_checkbox:
            self.colorpicker_blue_checkbox.setChecked(False)
            self.colorpicker_pink_checkbox.setChecked(False)

        if self.sender() == self.colorpicker_blue_checkbox:
            self.colorpicker_green_checkbox.setChecked(False)
            self.colorpicker_pink_checkbox.setChecked(False)

        if self.sender() == self.colorpicker_pink_checkbox:
            self.colorpicker_blue_checkbox.setChecked(False)
            self.colorpicker_green_checkbox.setChecked(False)


    def get_color(self):
        if self.colorpicker_green_checkbox.isChecked():
            return "#009879"
        if self.colorpicker_blue_checkbox.isChecked():
            return "#04aed4"
        if self.colorpicker_pink_checkbox.isChecked():
            return "#fc14da"


    def open_file_dialog(self): 
        filename = QtWidgets.QFileDialog.getOpenFileName()
        path = filename[0]
        return path


    def detect_from_pdf(self): 
        """
        Oeffnet file dialog um Kriterien aus PDF zu kopieren
        """
        path = self.open_file_dialog()
        formatted_krits = auto_pdf.krit_list(path)
        i = 0
        for x in formatted_krits:
            self.krit[i].setText(x[0])
            self.krit_von[i].setText(x[1])
            i += 1


    def berechne_summe(self):
        """
        Berechne die Summe der übergebenen Punkte
        """
        self.number_in = 0
        self.number_von = 0

        for x in self.krit_in:
            if not x.text() == "":
                self.number_in = self.number_in + int(x.text())
        if self.compiler_fehler_checkbox.isChecked():
            self.number_in = 0
        self.summe_in.setText(str(self.number_in))

        for x in self.krit_von:
            if not x.text() == "":
                self.number_von = self.number_von + int(x.text())
        self.summe_von.setText(str(self.number_von))

        
    def create_html(self):
        """
        Erzeuge eine HTML Datei welche die Korrektur enthaelt 
        """
        program_name = self.zu_bewerten_in.text().replace(" ", "_")

        if not os.path.exists("html"):
            os.system("mkdir html")
        else:
            pass

        f = open("html/" + program_name + ".html", "w", encoding='utf8')

        # laesst sich nicht auslagern da QLineEdits anscheinend nicht gepassed werden koennen
        html_krit_list = []
        for x in range(0,8):
                html_krit = f"""<tr style="border-bottom: 1px solid #dddddd;">
                <td style="padding: 12px 15px;">{self.krit[x].text()}</td>
                <td style="padding: 12px 15px;">{self.krit_in[x].text()}/{self.krit_von[x].text()}</td>
                </tr>"""
                html_krit_list.append(html_krit)

        table_color = self.get_color()
        html_file_end = tmplt.html_end(self.compiler_fehler_checkbox.isChecked(), table_color, self.summe_in.text(),
                                       self.summe_von.text(), self.kommentar_in.toPlainText(), 
                                       self.hinweise_in.toPlainText(), self.musterloesung_in.text())

        html_file = tmplt.html_begin(table_color, self.bewertender_in.text(),
                                          self.zu_bewerten_in.text())

        # Jedes Kriterium hinzufuegen
        for x in range(0,8):
            if not (self.krit[x].text() and self.krit_in[x].text() and self.krit_von[x].text()) == "":
                html_file += html_krit_list[x]

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
