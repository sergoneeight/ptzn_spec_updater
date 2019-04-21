from scrapper.by import By

PRODUCT_NAME_LOCATORS = [
    # https://bt.rozetka.com.ua
    By(tag_name='h1', container=By(tag_name='div', class_='detail-title-code')),
    # https://ikea-club.com.ua
    By(tag_name='h1', container=By(tag_name='div', class_='product-name')),
    # https://e27.com.ua
    By(tag_name='h1', container=By(tag_name='div', class_='product-name')),
    # https://jysk.ua
    By(tag_name='h1', container=By(tag_name='div', class_='product-name-sku')),
    # his.ua
    By(tag_name='span', container=By(tag_name='div', class_='product_layout_info'))
]

PRODUCT_IMAGE_LOCATORS = [
    # https://bt.rozetka.com.ua
    By(tag_name='img', container=By(tag_name='pp-main-photo')),
    # https://ikea-club.com.ua
    By(tag_name='img', id='cloudZoomImage', container=By(tag_name='div', id='sevenspikes-cloud-zoom')),
    # https://e27.com.ua
    By(tag_name='img', id='image-main', container=By(tag_name='div', class_='img-box')),
    # https://jysk.ua
    By(tag_name='img', class_='image', container=By(tag_name='div', id='product-image-carousel')),
    # his.ua
    By(tag_name='img', container=By(tag_name='div', class_='product_left'))
]

PRODUCT_PRICE_LOCATORS = [
    # https://bt.rozetka.com.ua
    By(tag_name='span', container=By(tag_name='div', class_='detail-buy-label')),
    # https://ikea-club.com.ua
    By(tag_name='span', container=By(tag_name='div', class_='product-price')),
    # https://e27.com.ua
    By(tag_name='span', class_='price', container=By(tag_name='div', class_='product-type-data')),
    # https://jysk.ua
    By(tag_name='span', class_='product-price', container=By(tag_name='div', class_='product-sumup')),
    # his.ua
    By(tag_name='span', id='product_price')
]
