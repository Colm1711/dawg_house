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
            content=f'Webhoook received: {event["type"]}',
            status=200)
