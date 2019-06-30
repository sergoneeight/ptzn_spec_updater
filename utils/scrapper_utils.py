def get_price(price_str):
    result = []
    if price_str:
        price_str = price_str.replace(',', '.')
        for c in price_str:
            if c.isalpha():
                break
            if c.isdigit() or c == '.':
                result.append(c)
    try:
        price = float(''.join(result))
    except ValueError:
        price = 0
    return price
