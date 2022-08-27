from django import forms
from ctcsalary.models import SalaryDetails

class SalaryDetailForm(forms.ModelForm):
    class Meta:
        model=SalaryDetails
        fields=[
            "salary_structure",
        ]
        widgets={
            "salary_structure":forms.FileInput(attrs={"class":"form-control"}),
        }