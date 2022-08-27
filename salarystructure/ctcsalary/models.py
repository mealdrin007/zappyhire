from django.db import models

class SalaryDetails(models.Model):
    salary_structure = models.FileField(upload_to="excel", null=True)