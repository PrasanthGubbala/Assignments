import cgi

from flask import Flask, render_template, request
import PyPDF2
import re


app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('dashboard.html')

@app.route('/vol1')
def vol1():
    pdfFileObj = open('static/pdf_files/VOLUME_01.pdf', 'rb')
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
    pageObj = pdfReader.getPage(0)
    text = pageObj.extractText()
    pdfFileObj.close()
    return render_template('dashboard.html',data = text)

@app.route('/vol2')
def vol2():
    pdfFileObj = open('static/pdf_files/VOLUME_02.pdf', 'rb')
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
    pageObj = pdfReader.getPage(0)
    text = pageObj.extractText()
    pdfFileObj.close()
    return render_template('dashboard.html',data = text)

@app.route('/vol3')
def vol3():
    pdfFileObj = open('static/pdf_files/VOLUME_03.pdf', 'rb')
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
    pageObj = pdfReader.getPage(0)
    text = pageObj.extractText()
    pdfFileObj.close()
    return render_template('dashboard.html',data = text)

@app.route('/vol4')
def vol4():
    pdfFileObj = open('static/pdf_files/VOLUME_04.pdf', 'rb')
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
    pageObj = pdfReader.getPage(0)
    text = pageObj.extractText()
    pdfFileObj.close()
    return render_template('dashboard.html',data = text)

@app.route('/vol5')
def vol5():
    pdfFileObj = open('static/pdf_files/VOLUME_05.pdf', 'rb')
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
    pageObj = pdfReader.getPage(0)
    text = pageObj.extractText()
    pdfFileObj.close()
    return render_template('dashboard.html',data = text)

@app.route('/vol6')
def vol6():
    pdfFileObj = open('static/pdf_files/VOLUME_06.pdf', 'rb')
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
    pageObj = pdfReader.getPage(0)
    text = pageObj.extractText()
    pdfFileObj.close()
    return render_template('dashboard.html',data = text)

@app.route('/vol7')
def vol7():
    pdfFileObj = open('static/pdf_files/VOLUME_07.pdf', 'rb')
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
    pageObj = pdfReader.getPage(0)
    text = pageObj.extractText()
    pdfFileObj.close()
    return render_template('dashboard.html',data = text)

@app.route('/vol8')
def vol8():
    pdfFileObj = open('static/pdf_files/VOLUME_08.pdf', 'rb')
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
    pageObj = pdfReader.getPage(0)
    text = pageObj.extractText()
    pdfFileObj.close()
    return render_template('dashboard.html',data = text)

@app.route('/vol9')
def vol9():
    pdfFileObj = open('static/pdf_files/VOLUME_09.pdf', 'rb')
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
    pageObj = pdfReader.getPage(0)
    text = pageObj.extractText()
    pdfFileObj.close()
    return render_template('dashboard.html',data = text)

@app.route('/vol10')
def vol10():
    pdfFileObj = open('static/pdf_files/VOLUME_10.pdf', 'rb')
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
    pageObj = pdfReader.getPage(0)
    text = pageObj.extractText()
    pdfFileObj.close()
    return render_template('dashboard.html',data = text)

@app.route('/vol11')
def vol11():
    pdfFileObj = open('static/pdf_files/VOLUME_11.pdf', 'rb')
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
    pageObj = pdfReader.getPage(0)
    text = pageObj.extractText()
    pdfFileObj.close()
    return render_template('dashboard.html',data = text)

@app.route('/vol12')
def vol12():
    pdfFileObj = open('static/pdf_files/VOLUME_12.pdf', 'rb')
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
    pageObj = pdfReader.getPage(0)
    text = pageObj.extractText()
    pdfFileObj.close()
    return render_template('dashboard.html',data = text)

@app.route('/vol13')
def vol13():
    pdfFileObj = open('static/pdf_files/VOLUME_13.pdf', 'rb')
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
    pageObj = pdfReader.getPage(0)
    text = pageObj.extractText()
    pdfFileObj.close()
    return render_template('dashboard.html',data = text)

@app.route('/vol14')
def vol14():
    pdfFileObj = open('static/pdf_files/VOLUME_14.pdf', 'rb')
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
    pageObj = pdfReader.getPage(0)
    text = pageObj.extractText()
    pdfFileObj.close()
    return render_template('dashboard.html',data = text)

@app.route('/vol15')
def vol15():
    pdfFileObj = open('static/pdf_files/VOLUME_15.pdf', 'rb')
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
    pageObj = pdfReader.getPage(0)
    text = pageObj.extractText()
    pdfFileObj.close()
    return render_template('dashboard.html',data = text)

@app.route('/vol16')
def vol16():
    pdfFileObj = open('static/pdf_files/VOLUME_16.pdf', 'rb')
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
    pageObj = pdfReader.getPage(0)
    text = pageObj.extractText()
    pdfFileObj.close()
    return render_template('dashboard.html',data = text)

@app.route('/vol17')
def vol17():
    pdfFileObj = open('static/pdf_files/VOLUME_17.pdf', 'rb')
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
    pageObj = pdfReader.getPage(0)
    text = pageObj.extractText()
    pdfFileObj.close()
    return render_template('dashboard.html',data = text)

@app.route('/vol18')
def vol18():
    pdfFileObj = open('static/pdf_files/VOLUME_18.pdf', 'rb')
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
    pageObj = pdfReader.getPage(0)
    text = pageObj.extractText()
    pdfFileObj.close()
    return render_template('dashboard.html',data = text)

@app.route('/vol19')
def vol19():
    pdfFileObj = open('static/pdf_files/VOLUME_19.pdf', 'rb')
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
    pageObj = pdfReader.getPage(0)
    text = pageObj.extractText()
    pdfFileObj.close()
    return render_template('dashboard.html',data = text)


@app.route('/sec1')
def sec1():
    object = PyPDF2.PdfFileReader("static/pdf_files/VOLUME_01.pdf")
    NumPages = object.getNumPages()
    String = "Contract Agreement"
    for i in range(0, NumPages):
        PageObj = object.getPage(i)
        Text = PageObj.extractText()
        ResSearch = re.search(String, Text)
        if ResSearch:
            return render_template('dashboard.html',data=ResSearch.string)

@app.route('/sec2')
def sec2():
    object = PyPDF2.PdfFileReader("static/pdf_files/VOLUME_02.pdf")
    NumPages = object.getNumPages()
    String = "Letter of Award"
    for i in range(0, NumPages):
        PageObj = object.getPage(i)
        Text = PageObj.extractText()
        ResSearch = re.search(String, Text)
        if ResSearch:
            return render_template('dashboard.html',data=ResSearch.string)

@app.route('/sec3')
def sec3():
    object = PyPDF2.PdfFileReader("static/pdf_files/VOLUME_03.pdf")
    NumPages = object.getNumPages()
    String = "Letter of Confirmation"
    for i in range(0, NumPages):
        PageObj = object.getPage(i)
        Text = PageObj.extractText()
        ResSearch = re.search(String, Text)
        if ResSearch:
            return render_template('dashboard.html',data=ResSearch.string)

@app.route('/sec4')
def sec4():
    object = PyPDF2.PdfFileReader("static/pdf_files/VOLUME_04.pdf")
    NumPages = object.getNumPages()
    String = "Secrecy Declaration"
    for i in range(0, NumPages):
        PageObj = object.getPage(i)
        Text = PageObj.extractText()
        ResSearch = re.search(String, Text)
        if ResSearch:
            return render_template('dashboard.html',data=ResSearch.string)

@app.route('/sec5')
def sec5():
    object = PyPDF2.PdfFileReader("static/pdf_files/VOLUME_05.pdf")
    NumPages = object.getNumPages()
    String = "Performance Bond"
    for i in range(0, NumPages):
        PageObj = object.getPage(i)
        Text = PageObj.extractText()
        ResSearch = re.search(String, Text)
        if ResSearch:
            return render_template('dashboard.html',data=ResSearch.string)

@app.route('/sec6')
def sec6():
    object = PyPDF2.PdfFileReader("static/pdf_files/VOLUME_06.pdf")
    NumPages = object.getNumPages()
    String = "Commercial Registration and Power of Attorney"
    for i in range(0, NumPages):
        PageObj = object.getPage(i)
        Text = PageObj.extractText()
        ResSearch = re.search(String, Text)
        if ResSearch:
            return render_template('dashboard.html',data=ResSearch.string)

@app.route('/sec7')
def sec7():
    object = PyPDF2.PdfFileReader("static/pdf_files/VOLUME_07.pdf")
    NumPages = object.getNumPages()
    String = "Summary of Contract"
    for i in range(0, NumPages):
        PageObj = object.getPage(i)
        Text = PageObj.extractText()
        ResSearch = re.search(String, Text)
        if ResSearch:
            return render_template('dashboard.html',data=ResSearch.string)

@app.route('/sec8')
def sec8():
    object = PyPDF2.PdfFileReader("static/pdf_files/VOLUME_08.pdf")
    NumPages = object.getNumPages()
    String = "General Conditions of Contracts"
    for i in range(0, NumPages):
        PageObj = object.getPage(i)
        Text = PageObj.extractText()
        ResSearch = re.search(String, Text)
        if ResSearch:
            return render_template('dashboard.html',data=ResSearch.string)

@app.route('/sec9')
def sec9():
    object = PyPDF2.PdfFileReader("static/pdf_files/VOLUME_09.pdf")
    NumPages = object.getNumPages()
    String = "Appendix A: Scope of Work and Specifications"
    for i in range(0, NumPages):
        PageObj = object.getPage(i)
        Text = PageObj.extractText()
        ResSearch = re.search(String, Text)
        if ResSearch:
            return render_template('dashboard.html',data=ResSearch.string)

@app.route('/sec10')
def sec10():
    object = PyPDF2.PdfFileReader("static/pdf_files/VOLUME_10.pdf")
    NumPages = object.getNumPages()
    String = "Appendix 8 : Schedule of Prices"
    for i in range(0, NumPages):
        PageObj = object.getPage(i)
        Text = PageObj.extractText()
        ResSearch = re.search(String, Text)
        if ResSearch:
            return render_template('dashboard.html',data=ResSearch.string)

@app.route('/sec11')
def sec11():
    object = PyPDF2.PdfFileReader("static/pdf_files/VOLUME_11.pdf")
    NumPages = object.getNumPages()
    String = "Appendix C: Insurance"
    for i in range(0, NumPages):
        PageObj = object.getPage(i)
        Text = PageObj.extractText()
        ResSearch = re.search(String, Text)
        if ResSearch:
            return render_template('dashboard.html',data=ResSearch.string)

@app.route('/sec12')
def sec12():
    object = PyPDF2.PdfFileReader("static/pdf_files/VOLUME_12.pdf")
    NumPages = object.getNumPages()
    String = "Appendix D Administration Instructions"
    for i in range(0, NumPages):
        PageObj = object.getPage(i)
        Text = PageObj.extractText()
        ResSearch = re.search(String, Text)
        if ResSearch:
            return render_template('dashboard.html',data=ResSearch.string)

@app.route('/sec13')
def sec13():
    object = PyPDF2.PdfFileReader("static/pdf_files/VOLUME_13.pdf")
    NumPages = object.getNumPages()
    String = "Appendix E Contractor Resources"
    for i in range(0, NumPages):
        PageObj = object.getPage(i)
        Text = PageObj.extractText()
        ResSearch = re.search(String, Text)
        if ResSearch:
            return render_template('dashboard.html',data=ResSearch.string)

@app.route('/sec14')
def sec14():
    object = PyPDF2.PdfFileReader("static/pdf_files/VOLUME_14.pdf")
    NumPages = object.getNumPages()
    String = "Appendix F Drawings"
    for i in range(0, NumPages):
        PageObj = object.getPage(i)
        Text = PageObj.extractText()
        ResSearch = re.search(String, Text)
        if ResSearch:
            return render_template('dashboard.html',data=ResSearch.string)

@app.route('/sec15')
def sec15():
    object = PyPDF2.PdfFileReader("static/pdf_files/VOLUME_15.pdf")
    NumPages = object.getNumPages()
    String = "Appendix G Material Equipment Supplied by KAHRAMAA"
    for i in range(0, NumPages):
        PageObj = object.getPage(i)
        Text = PageObj.extractText()
        ResSearch = re.search(String, Text)
        if ResSearch:
            return render_template('dashboard.html',data=ResSearch.string)

@app.route('/sec16')
def sec16():
    object = PyPDF2.PdfFileReader("static/pdf_files/VOLUME_16.pdf")
    NumPages = object.getNumPages()
    String = "Appendix H Contract Execution Plan"
    for i in range(0, NumPages):
        PageObj = object.getPage(i)
        Text = PageObj.extractText()
        ResSearch = re.search(String, Text)
        if ResSearch:
            return render_template('dashboard.html',data=ResSearch.string)

@app.route('/sec17')
def sec17():
    object = PyPDF2.PdfFileReader("static/pdf_files/VOLUME_17.pdf")
    NumPages = object.getNumPages()
    String = "Appendix I Materials Supplied by the Contractor"
    for i in range(0, NumPages):
        PageObj = object.getPage(i)
        Text = PageObj.extractText()
        ResSearch = re.search(String, Text)
        if ResSearch:
            return render_template('dashboard.html',data=ResSearch.string)

@app.route('/sec18')
def sec18():
    object = PyPDF2.PdfFileReader("static/pdf_files/VOLUME_18.pdf")
    NumPages = object.getNumPages()
    String = "Appendix J General Safety Requirements"
    for i in range(0, NumPages):
        PageObj = object.getPage(i)
        Text = PageObj.extractText()
        ResSearch = re.search(String, Text)
        if ResSearch:
            return render_template('dashboard.html',data=ResSearch.string)

@app.route('/sec19')
def sec19():
    object = PyPDF2.PdfFileReader("static/pdf_files/VOLUME_19.pdf")
    NumPages = object.getNumPages()
    String = "Appendix K Departure from or Qualification to the Specification"
    for i in range(0, NumPages):
        PageObj = object.getPage(i)
        Text = PageObj.extractText()
        ResSearch = re.search(String, Text)
        if ResSearch:
            return render_template('dashboard.html',data=ResSearch.string)

@app.route('/sec20')
def sec20():
    object = PyPDF2.PdfFileReader("static/pdf_files/VOLUME_19.pdf")
    NumPages = object.getNumPages()
    String = "Acknowledgement of Receipt of Tender Documents"
    for i in range(0, NumPages):
        PageObj = object.getPage(i)
        Text = PageObj.extractText()
        ResSearch = re.search(String, Text)
        if ResSearch:
            return render_template('dashboard.html',data=ResSearch.string)

@app.route('/sec21')
def sec21():
    object = PyPDF2.PdfFileReader("static/pdf_files/VOLUME_19.pdf")
    NumPages = object.getNumPages()
    String = "Commercial Offer BOQ"
    for i in range(0, NumPages):
        PageObj = object.getPage(i)
        Text = PageObj.extractText()
        ResSearch = re.search(String, Text)
        if ResSearch:
            return render_template('dashboard.html',data=ResSearch.string)


@app.route('/search',methods=['POST'])
def search():
    try:
        keyword = request.form.get("t1")
        print(keyword)
        object = PyPDF2.PdfFileReader("static/pdf_files/VOLUME_01.pdf")
        NumPages = object.getNumPages()
        String = keyword
        for i in range(0, NumPages):
            PageObj = object.getPage(i)
            Text = PageObj.extractText()
            ResSearch = re.search(String, Text)
            if ResSearch:
                return render_template('dashboard.html', data=ResSearch.string)

    except:
        return render_template('dashboard.html',data='invalid')



if __name__ == '__main__':
    app.run(debug=True)
