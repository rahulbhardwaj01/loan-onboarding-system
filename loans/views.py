from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from django.template import loader
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Loan
from .serializers import LoanSerializer
from .transformer import transform_loan_data

# mixin/genericss : generics less codee they handle many things under teh hood 
class LoanCreateView(generics.CreateAPIView):
    queryset = Loan.objects.all()
    serializer_class = LoanSerializer

class LoanDetailView(generics.RetrieveAPIView):
    queryset = Loan.objects.all()
    serializer_class = LoanSerializer
    lookup_field = 'loan_number'  #primary key for single upd,del etc

class BaseLoanDataView(APIView):    
    def get_loan_data(self, loan_number):
        loan = get_object_or_404(Loan, loan_number=loan_number) 
        serializer = LoanSerializer(loan)
        return serializer.data

class LoanTransformedJSONView(BaseLoanDataView):        #inherited class
    def get(self, request, loan_number, format=None):
        raw_data = self.get_loan_data(loan_number)
        transformed_data = transform_loan_data(raw_data)
        if transformed_data:
            return Response(transformed_data)
        return Response({"error": "Failed to transform data"}, status=500)

class LoanXMLView(BaseLoanDataView):
    def get(self, request, loan_number, format=None):
        raw_data = self.get_loan_data(loan_number)
        transformed_data = transform_loan_data(raw_data)
        if not transformed_data:
            return Response({"error": "Failed to transform data for XML generation"}, status=500)
        template = loader.get_template('loan.xml')
        xml_content = template.render({'data': transformed_data})
        return HttpResponse(xml_content, content_type='application/xml')  
    
    
# content_type='application/xml', adds a header to the response that tells the browser, "The text I am sending you is an XML document, so please interpret it that way."
    # The .render() method essentially "fills in the blanks" in your template file.
# It Takes a "Context" Dictionary: You pass a dictionary to the .render() method. In our code, the context is {'data': transformed_data}. The keys in this dictionary (data) match the variables used in the template's placeholders (like {{ data.loanId }}).

# It Replaces Placeholders: The method goes through the template string and replaces every placeholder with the corresponding value from the context dictionary.

# It Returns a String: After all replacements are done, the method returns one complete string of text, which we assign to the xml_content variable. This string is the final XML document, ready to be sent in the HttpResponse.