from django.urls import path
from ctcsalary import views
urlpatterns = [
    # path("",views.BaseView.as_view(),name="base"),
    # path("form/",views.SalaryDetailFormView.as_view(),name="input"),
    path("data/",views.index),
]