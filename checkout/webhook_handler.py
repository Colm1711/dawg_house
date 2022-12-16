# Imports

# Django Imports
from django.http import HttpResponse


class StripeWH_Handler:
    """Handle Stripe webhooks"""

    def __int__(self, request):
        self.request = request

    def handle_event(self, event):
        """
        Handle a generic/unknown/unexpected webook event
        """
        return HttpResponse(
            content=f'Unhandled webhoook received: {event["type"]}',
            status=200)

    def handle_payment_intent_succeeded(self, event):
        """
        Handle the payment_intent.succeeded webhook from stripe
        """
        intent = event.data.object
        return HttpResponse(
            content=f'Webbhook received: {event["type"]}',
            status=200)

    def handle_payment_intent_failed(self, event):
        """
        Handle the payment_intent.faled webhook from stripe
        """
        return HttpResponse(
            content=f'Webbhook received: {event["type"]}',
            status=200)
