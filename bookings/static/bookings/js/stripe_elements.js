/*
    Core logic/paymenr flow for the comes from here:
    https://stripe.com/docs/payments/quickstart

    CSS from here:
    https://stripe.com/docs/payments/elements

*/

var stripe_public_key = $('#id_stripe_public_key').text().slice(1, -1);
var client_secret = $('#id_client_secret').text().slice(1, -1);
var stripe = Stripe(stripe_public_key)
var elements = stripe.elements();
var style = {
    base: {
        color: '#32325d',
        fontFamily: '"Helvetica Neue", Helvetica, sans-serif',
        fontSmoothing: 'antialiased',
        fontSize: '16px',
        '::placeholder': {
            color: '#aab7c4'
        }
    },
    invalid: {
        color: '#dc3545',
        iconColor: '#dc3545'
    }
};
var card = elements.create('card', {hidePostalCode: true, style: style});
card.mount('#card-element');

//Handle realtime validation errors on the card element
card.addEventListener('change', function(event){
    var errorDiv = document.getElementById('card-errors');
    if(event.error){
        var html = `
            <span class="icon" role=alert>
                <i class="fa-solid fa-exclamation"></i>
            </span>
            <span>${event.error.message}</span>
        `;
        $(errorDiv).html(html);
    }else{
        errorDiv.textContent = '';
    }
});