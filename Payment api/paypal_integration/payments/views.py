from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from paypalrestsdk import Payment

class ExecutePaymentView(APIView):
    def get(self, request):
        payment_id = request.GET.get('paymentId')
        payer_id = request.GET.get('PayerID')
        
        payment = Payment.find(payment_id)
        
        if payment.execute({"payer_id": payer_id}):
            # Payment successful, you can process the order here
            return Response({"message": "Payment executed successfully!"}, status=status.HTTP_200_OK)
        else:
            return Response({"error": "Payment execution failed"}, status=status.HTTP_400_BAD_REQUEST)


# Create the Execute Payment View#
#When the user is redirected to PayPal and approves the payment, they will be redirected to the return_url you've provided. You can create a new API endpoint to handle the execution of the payment.#.
