from scrapper.by import By

locators = {
    'rozetka.com.ua': {
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
            By(tag_name='span', container=By(tag_name='div', class_='product_layout_info')),
        ),
        'product_price': (
            By(tag_name='span', id='product_price'),
        ),
        'product_image': (
            By(tag_name='img', container=By(tag_name='div', class_='product_left')),
        )
    },
    'designloft.com.ua': {
        'product_name': (
            By(tag_name='h1', container=By(tag_name='div', class_='right')),
        ),
        'product_price': (
            By(tag_name='span', container=By(tag_name='span', itemprop='offerDetails')),
        ),
        'product_image': (
            By(tag_name='img', id='image', container=By(tag_name='div', class_='left')),
        )
    },
    'lustra-style.com.ua': {
        'product_name': (
            By(tag_name='h1', container=By(tag_name='ul', class_='product-info')),
        ),
        'product_price': (
            By(tag_name='div', itemprop='price', container=By(tag_name='div', class_='product-price')),
        ),
        'product_image': (
            By(tag_name='img', container=By(tag_name='div', class_='product-info-image')),
        )
    },
    'thexata.com': {
        'product_name': (
            By(tag_name='h1', container=By(tag_name='div', class_='product-name')),
        ),
        'product_price': (
            By(tag_name='span', class_='number', container=By(tag_name='div', class_='product-information')),
        ),
        'product_image': (
            By(tag_name='img', container=By(tag_name='div', class_='main-image')),
        )
    },
    'kupistul.ua': {
        'product_name': (
            By(tag_name='h1', container=By(tag_name='div', class_='product-main__content')),
        ),
        'product_price': (
            By(tag_name='span', itemprop='price',
               container=By(tag_name='span', class_='product-main__actions-price-count')),
        ),
        'product_image': (
            By(tag_name='img', container=By(tag_name='div', class_='product-main__gallery-img')),
        )
    },
    'shoploft.com.ua': {
        'product_name': (
            By(tag_name='h1', container=By(tag_name='div', class_='top_products-block')),
        ),
        'product_price': (
            By(tag_name='div', class_='price', container=By(tag_name='div', class_='info_block_product')),
        ),
        'product_image': (
            By(tag_name='img', container=By(tag_name='div', class_='slider_image_product')),
        )
    },
    'shop.agromat.ua': {
        'product_name': (
            By(tag_name='h1', container=By(tag_name='div', class_='prod-name')),
        ),
        'product_price': (
            By(tag_name='span', itemprop='price', container=By(tag_name='div', class_='to-cart-line')),
        ),
        'product_image': (
            By(tag_name='img', container=By(tag_name='div', class_='prod-slider')),
        )
    }
}
