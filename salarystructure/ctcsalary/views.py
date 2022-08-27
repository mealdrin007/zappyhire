from django.shortcuts import render
from django.views.generic import TemplateView
import openpyxl
class BaseView(TemplateView):
    template_name = "base.html"



def index(request):
    if "GET" == request.method:
        return render(request, 'index.html', {})
    else:
        excel_file = request.FILES["excel_file"]
        wb = openpyxl.load_workbook(excel_file)
        worksheet = wb["sheet1"]
        print(worksheet)
        excel_data = list()
        for row in worksheet.iter_rows():
            row_data = list()
            for cell in row:
                row_data.append(str(cell.value))
            excel_data.append(row_data)
        a=0
        m=0
        for i in excel_data:
            if i[0]=="Total Cost to Company" or i[0]=="CTC":
                a=i[1]
                break
            else:
                m+=1
        g=0
        for l in excel_data:
            if l[0] =="Salary Components":
                break
            else:
                g+=1
        v=[]
        b=[]
        for u in range(g+1,m):
                v.append(excel_data[u])
        for d in v:
            if d[0]!="None":
                b.append(d[0])
        c={}
        data = request.POST.get("ctc")
        if data=="":
            data="1"
        for j in b:
            for k in excel_data:
                if j==k[0] and k[1]!=0:
                    if k[1]!="None":
                        x=int(k[1])/int(a)
                        c[j]=round(x*int(data))
        return render(request, 'index.html', {"excel_data":c})
