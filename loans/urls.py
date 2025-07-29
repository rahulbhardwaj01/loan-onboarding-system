from django.urls import path
from . import views

urlpatterns = [
    path('loans/', views.LoanCreateView.as_view(), name='loan-create'),   #used uuid for uniqueness same like mern
    path('loans/<uuid:loan_number>/', views.LoanDetailView.as_view(), name='loan-detail'),
    path('loans/<uuid:loan_number>/json/', views.LoanTransformedJSONView.as_view(), name='loan-json'),
    path('loans/<uuid:loan_number>/xml/', views.LoanXMLView.as_view(), name='loan-xml'),
]