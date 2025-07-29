from django.contrib import admin
from .models import Loan, Customer, Address


# Register your models here.
admin.site.register(Loan)
admin.site.register(Customer)
admin.site.register(Address)