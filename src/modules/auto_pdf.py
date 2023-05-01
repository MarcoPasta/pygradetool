import PyPDF2 
import re

def krit_list(path): 
    pdf = PyPDF2.PdfReader(path)
    i = 0
    while(i < len(pdf.pages)):
        if not re.search("Bewertungsschema", pdf.pages[i].extract_text()):
            i += 1
        else:
            kritList = re.findall(".*[a-zA-Z]* [0-9]* P", pdf.pages[i].extract_text())
            break

    kritList.pop(0)
    formatted_krit = format_krit(kritList)
    return formatted_krit


def format_krit(krit_list):
        pattern = re.compile("(.+[a-zA-Z]*) ([0-9]*) P")
        krit_tuplist = []
        for x in krit_list:
            krit_tuplist.append(pattern.match(x).groups())
        krit_tuplist.pop()
        return krit_tuplist