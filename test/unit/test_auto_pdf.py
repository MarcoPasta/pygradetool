import os
import pytest

import modules.auto_pdf as auto_pdf

@pytest.fixture
def pdf_files():
    files = [
        "prog1-p02d-Schleifen-Buchstaben-weich-hart-Quersumme.pdf",
        "Prog1-p05c-Rekursion_Fakul_Exp_Fibo.pdf"
    ]
    files = [os.path.join(os.path.dirname(__file__), "data", file) for file in files]
    return files

@pytest.fixture
def pdf_criteria():
    return ([
        [('Codeformatierung', '3'), ('sinnvolle Kommentare', '3'), ('Hauptschleife Einlesen / Ausgeben', '4'), ('Zähler der 2 Konsonanten-Gruppen ermitteln und ausgeben', '4'), ('Quersumme berechnen und ausgeben', '6')],
        [('Codeformatierung', '3'), ('sinnvolle Kommentare', '3'), ('fakul()-Funktion', '4'), ('power()-Funktion ', '4'), ('summe()-Funktion', '3'), ('Hauptprogramm, Ein-/Ausgaben', '3')]
    ])
    


def test_auto_pdf(pdf_files, pdf_criteria):
    format_krit_list = []
    for x in pdf_files:
        format_krit_list.append(auto_pdf.krit_list(x))
    assert format_krit_list == pdf_criteria