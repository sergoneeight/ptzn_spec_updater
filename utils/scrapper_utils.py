def price_str_to_float(price_str):
    price_str = price_str.replace(',', '.')
    formatted_price = ''.join(i for i in price_str if i.isdigit() or i == '.')
    if formatted_price.endswith('.'):
        formatted_price = formatted_price[:-1]
    try:
        price = float(''.join(formatted_price))
    except ValueError:
        price = 0
    return price
