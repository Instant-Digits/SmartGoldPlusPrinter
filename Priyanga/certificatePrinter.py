import os
from fpdf import FPDF, HTMLMixin

class PDF(FPDF, HTMLMixin):
    pass


def SetPrintingJobCertificate(printData):
    # class PDF(FPDF, HTMLMixin):
    #     pass

    data = (
        ("ELEMENT", "CONC %", ),
        ("Gold (Au)",'               '+printData['Au']+'%',),
        ("Copper (Cu)", '               '+printData['Cu']+'%', ),
        ("Silver (Ag)", '               '+printData['Ag']+'%', ),
        ("Indium (In)", '               '+printData['In']+'%', ),
        ("Zinc (Zn)", '               '+printData['Zn']+'%', ),

    )
    pdf = PDF()
    pdf.set_font("Arial", size = 15)

    pdf.add_page()
    pdf.cell(0, 12, txt="" ,ln=1,align='L')
    pdf.cell(0, 9, txt="" ,ln=1,align='L')


    pdf.set_left_margin(32)

    pdf.write_html(
        f"""<table border="1" ><thead><tr>
        <th width="40%">{data[0][0]}</th>
        <th width="25%">{data[0][1]}</th>    
    </tr></thead><tbody><tr>
        <td>{'</td><td>'.join(data[1])}</td>
    </tr><tr>
        <td>{'</td><td>'.join(data[2])}</td>
    </tr><tr>
        <td>{'</td><td>'.join(data[3])}</td>
    </tr><tr>
        <td>{'</td><td>'.join(data[4])}</td>
    </tr><tr>
        <td>{'</td><td>'.join(data[5])}</td>
    </tr>
    </tbody></table""",
    )
    pdf.set_left_margin(23)
    pdf.cell(0, 5, txt="Weight      : "+printData['weight']+"g,    Karat : "+printData['karad']+'K',ln=1,align='L')
    pdf.set_left_margin(23)
    pdf.cell(0, 5, txt="{:<10} {:<40} ".format('Date   ' , "   : "+printData['date']) ,ln=1,align='L')
    pdf.cell(0, 5, txt="{:<10} {:<40} ".format('Time  ' , "  : "+printData['time']) ,ln=1,align='L')
    pdf.cell(0, 5, txt="{:<10} {:<40} ".format('Name  ' , " : "+printData['name']),ln=1,align='L')
    pdf.cell(0, 5, txt="{:<10} {:<40} ".format('Sample' , " : "+printData['sample']),ln=1,align='L')
    pdf.output('table.pdf', 'F')
    os.system('lp ./table.pdf')

# SetPrintingJobCertificate({'date':'10-21',
#                            'time':'20-33',
#                             'name':'SHaganan', 
#                             'sample':'Good',
#                             "Au":'10%',
#                             "Cu":'10%',
#                             "Ag":'10%',
#                             "In":'10%',
#                             "Zn":'10%',
#                             "weight":"10",
#                             "karad":"22.5"
#                             })

