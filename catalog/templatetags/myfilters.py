from django import template
from cart.cart import Cart

register = template.Library()


@register.simple_tag(takes_context=True)
def cart_total_amount(context):
    request = context['request']
    if request.user.is_authenticated:
        cart = Cart(request)
        total_bill = 0.0
        for key,value in request.session['cart'].items():
            total_bill = total_bill + (float(value['price']) * value['quantity'])
        return total_bill
    else:
        return 0


@register.simple_tag()
def get_price(price):
    price = str(price)
    tail = price[-6:]
    text=''
    new_price = price[:-6]
    steps = len(price[:-6]) // 3
    for i in range(steps):
        text += ' ' + new_price[-3:]
        price = new_price[:-3]
    new = price+text + ' ' + tail
    return new

@register.simple_tag()
def get_price_sum(price):
    price = str(price)
    tail = price[-5:]
    text=''
    new_price = price[:-5]
    steps = len(price[:-5]) // 3
    for i in range(steps):
        text += ' ' + new_price[-3:]
        price = new_price[:-3]
    new = price+text + ' ' + tail
    return new


@register.simple_tag(takes_context=True)
def cart_total_amount_space(context):
    request = context['request']
    if request.user.is_authenticated:
        cart = Cart(request)
        total_bill = 0.0
        for key,value in request.session['cart'].items():
            total_bill = total_bill + (float(value['price']) * value['quantity'])
        return get_price_sum(total_bill)
    else:
        return 0
