from scrapper.by import By

locators = {
    'bt.rozetka.com.ua': {
        'product_name': (
            By(tag_name='h1', container=By(tag_name='div', class_='detail-title-code')),
        ),
        'product_price': (
            By(tag_name='span', container=By(tag_name='div', class_='detail-buy-label')),
        ),
        'product_image': (
            By(tag_name='img', container=By(tag_name='pp-main-photo')),
        )
    },
    'ikea-club.com.ua': {
        'product_name': (
            By(tag_name='h1', container=By(tag_name='div', class_='product-name')),
        ),
        'product_price': (
            By(tag_name='span', container=By(tag_name='div', class_='product-price')),
        ),
        'product_image': (
            By(tag_name='img', id='cloudZoomImage', container=By(tag_name='div', id='sevenspikes-cloud-zoom')),
        )
    },
    'e27.com.ua': {
        'product_name': (
            By(tag_name='h1', container=By(tag_name='div', class_='product-name')),
        ),
        'product_price': (
            By(tag_name='span', class_='price', container=By(tag_name='div', class_='product-type-data')),
        ),
        'product_image': (
            By(tag_name='img', id='image-main', container=By(tag_name='div', class_='img-box')),
        )
    },
    'jysk.ua': {
        'product_name': (
            By(tag_name='h1', container=By(tag_name='div', class_='product-name-sku')),
        ),
        'product_price': (
            By(tag_name='span', class_='product-price', container=By(tag_name='div', class_='product-sumup')),
        ),
        'product_image': (
            By(tag_name='img', class_='image', container=By(tag_name='div', id='product-image-carousel')),
        )
    },
    'his.ua': {
        'product_name': (
            By(tag_name='span', container=By(tag_name='div', class_='product_layout_info'))
        ),
        'product_price': (
            By(tag_name='span', id='product_price')
        ),
        'product_image': (
            By(tag_name='img', container=By(tag_name='div', class_='product_left'))
        )
    }
}
