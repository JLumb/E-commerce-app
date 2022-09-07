from django.shortcuts import render, reverse, redirect
from django.contrib import messages
from .forms import OrderForm


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request,'There is nothing in your bag')
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51LfPLQGR8l6JzE0N1Px4bWn80iAMuAGEncmIfvpXl7GVtC9QOHy7NlJl2aMDricqVUN8c0eHb2nHhj0uBrJLqzfg00NiXa1rxD',
        'client_secret': 'test client secret'
    }

    return render(request, template, context)
