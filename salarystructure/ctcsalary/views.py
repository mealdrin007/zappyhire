from django.shortcuts import render
from django.views.generic import TemplateView,CreateView
from ctcsalary.models import SalaryDetails
from ctcsalary.forms import SalaryDetailForm
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
        a=[]
        for i in excel_data:
            if i[3]!=""and i[3]!="None":
                a.append(i[3])

        return render(request, 'index.html', {"excel_data":excel_data})