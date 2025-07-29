from rest_framework import serializers
from .models import Loan, Customer, Address

class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = ['street', 'city', 'state', 'zip_code']

class CustomerSerializer(serializers.ModelSerializer):
    address = AddressSerializer()  #vissible at drf page for nestinmg so that whole object visible not simple id!

    class Meta:
        model = Customer
        fields = ['first_name', 'last_name', 'email', 'address']

class LoanSerializer(serializers.ModelSerializer):
    customers = CustomerSerializer(many=True)

    class Meta:
        model = Loan
        fields = ['loan_number', 'amount', 'term', 'status', 'customers']

    def create(self, validated_data):          # responsible for creation of all its nested children (Customer and Address)
        customers_data = validated_data.pop('customers')
        loan = Loan.objects.create(**validated_data)  #** like we do ... in mern
        for customer_data in customers_data:
            address_data = customer_data.pop('address')
            address = Address.objects.create(**address_data)
            customer = Customer.objects.create(address=address, **customer_data)
            loan.customers.add(customer)
        return loan
    
    # .add(customer): This is a special method provided by the ManyToManyField manager. 
    # It takes a Customer object and adds a record to the hidden "join table" 
    # that Django uses to track which customers belong to which loans.


    # The Loan.objects.create() method doesn't accept a dictionary as a single argument. 
    # It expects the models fields to be passed as individual keyword arguments.