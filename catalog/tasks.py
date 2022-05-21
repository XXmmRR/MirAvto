from .models import Order


def total_price(request):
    total_bill = 0
    for key, value in request.session['cart'].items():
        total_bill = total_bill + (float(value['price']) * value['quantity'])
    return total_bill


def get_parts(request):
    dict = request.session['cart'].items()
    text = ''
    for i in dict:
        text += f"Поступил заказ Имя: {i[1]['name']}\nАртикул: {i[1]['article']}\nДополнительный артикул:{i[1]['article_second']}\n" \
               f"Количество:{i[1]['quantity']}"
    return text
