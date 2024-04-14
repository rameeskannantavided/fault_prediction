# # views.py
#
# from django.shortcuts import render
# from django.http import HttpResponse
# import pickle
# import numpy as np
#
# # Load the model
# model = pickle.load(open('rfc_fraud_model.pkl', 'rb'))
#
# # Define a function to handle the home page
# def home(request):
#     return render(request, 'home.html')
#
# # Define a function to handle the prediction
# def predict(request):
#     if request.method == 'POST':
#         # Retrieve user inputs from the form
#         transaction_amount = float(request.POST['transaction_amount'])
#         payment_method = int(request.POST['payment_method'])
#         product_category = int(request.POST['product_category'])
#         quantity = int(request.POST['quantity'])
#         customer_age = int(request.POST['customer_age'])
#         device_used = int(request.POST['device_used'])
#         address_match = int(request.POST['address_match'])
#         account_age_days = int(request.POST['account_age_days'])
#         transaction_hour = int(request.POST['transaction_hour'])
#
#         # Make prediction
#         input_data = np.array([[transaction_amount, payment_method, product_category, quantity,
#                                 customer_age, device_used, address_match, account_age_days, transaction_hour]])
#         prediction = model.predict(input_data)[0]
#
#         # Display the result
#         return render(request, 'result.html', {'prediction': prediction})
#     else:
#         return HttpResponse('Invalid request method')










# views.py

from django.shortcuts import render
from django.http import HttpResponse
import pickle
import numpy as np

# Load the model
model = pickle.load(open('rfc_fraud_model.pkl', 'rb'))

# Define a function to handle the home page
def home(request):
    return render(request, 'home.html')

# Define a function to handle the prediction
def predict(request):
    if request.method == 'POST':
        # Retrieve user inputs from the form and convert to appropriate data types
        try:
            transaction_amount = float(request.POST['transaction_amount'])
            payment_method = int(request.POST['payment_method'])
            product_category = int(request.POST['product_category'])
            quantity = float(request.POST['quantity'])
            customer_age = float(request.POST['customer_age'])
            device_used = int(request.POST['device_used'])
            address_match = int(request.POST['address_match'])
            account_age_days = float(request.POST['account_age_days'])
            transaction_hour = float(request.POST['transaction_hour'])
        except ValueError:
            return HttpResponse('Invalid input. Please enter numeric values for transaction details.')

        # Make prediction
        input_data = np.array([[transaction_amount, payment_method, product_category, quantity,
                                customer_age, device_used, address_match, account_age_days, transaction_hour]])
        prediction = model.predict(input_data)[0]
        print(input_data)
        # Display the result
        return render(request, 'result.html', {'prediction': prediction})
    else:
        return HttpResponse('Invalid request method')
