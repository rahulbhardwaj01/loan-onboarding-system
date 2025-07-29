import jmespath
#Transforms loan data using a JMESPath express renames field,exxtracts, combines values ,filters out fields
def transform_loan_data(data):
    
    # compacting the data !!!!!!!!
    expression = """
    {
      loanId: loan_number,
      principal: amount,
      loanTermMonths: term,
      borrower: {
        fullName: join(' ', [customers[0].first_name, customers[0].last_name]),
        contactEmail: customers[0].email,
        fullAddress: join(', ', [customers[0].address.street, customers[0].address.city, join(' ', [customers[0].address.state, customers[0].address.zip_code])])
      }
    }
    """
    try:
        # Use jmespath to apply the expression to the input data
        transformed_data = jmespath.search(expression, data)
        return transformed_data
    except Exception as e:
        # Handle potential errors if the data doesn't match the expression
        print(f"Error during JSON transformation: {e}")
        return None
    
    # This transformer acts as an adapter,((imptttt)) 
    # converting your internl data format into the formt the external system reuireeee.
    # /////////////////////////////////////////////////////////////////////////////////////////
    # /////////////////////////////////////////////////////////////////////////////////////////
    # LoanSerializer produces a detailed JSON that mirrors your database structure, 
    # including a list of customers with nested addresses. The transformed JSON is much simpler. 
    # It flattens the structure and combines fields (like creating fullName and fullAddress), 
    # making it easier for the receiving system to process.
# /////////////////////////////////////////////////////////////////////////////////////////
# /////////////////////////////////////////////////////////////////////////////////////////
  # The jmespath.search() function takes two arguments: the expression (our set of rules) and the data (the input dictionary).

# It applies the rules to the data and returns the resulting new dictionary, 
# which is then stored in the transformed_data variable.