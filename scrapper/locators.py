class Locator(object):
    def __init__(self, name, key='', value=''):
        self.name = name
        self.attrs = {key: value}


class DetailedLocator(object):
    def __init__(self, parent_locator, child_locator):
        self.parent_locator = parent_locator
        self.child_locator = child_locator


PRODUCT_NAME_LOCATORS = [
    # https://bt.rozetka.com.ua
    DetailedLocator(
        parent_locator=Locator(name='div', key='class_', value='detail-title-wrap'),
        child_locator=Locator(name='h1', key='class_', value='detail-title')
    ),
    # https://ikea-club.com.ua
    DetailedLocator(
        parent_locator=Locator(name='div', key='class_', value='product-name'),
        child_locator=Locator(name='h1')
    ),
    # https://e27.com.ua
    DetailedLocator(
        parent_locator=Locator(name='div', key='class_', value='product-name'),
        child_locator=Locator(name='h1')
    ),
    # https://jysk.ua
    DetailedLocator(
        parent_locator=Locator(name='div', key='class_', value='product-name-sku'),
        child_locator=Locator(name='h1')
    )
]

PRODUCT_IMAGE_LOCATORS = [
    # https://bt.rozetka.com.ua
    DetailedLocator(
        parent_locator=Locator(name='div', key='class_', value='responsive-img'),
        child_locator=Locator(name='img', key='id', value='base_image')
    ),
    # https://ikea-club.com.ua
    DetailedLocator(
        parent_locator=Locator(name='div', key='id', value='sevenspikes-cloud-zoom'),
        child_locator=Locator(name='img', key='id', value='cloudZoomImage')
    ),
    # https://e27.com.ua
    DetailedLocator(
        parent_locator=Locator(name='div', key='class_', value='img-box'),
        child_locator=Locator(name='img', key='id', value='image-main')
    ),
    # https://jysk.ua
    DetailedLocator(
        parent_locator=Locator(name='div', key='id', value='product-image-carousel'),
        child_locator=Locator(name='img', key='class_', value='image')
    )
]

PRODUCT_PRICE_LOCATORS = [
    # https://bt.rozetka.com.ua
    DetailedLocator(
        parent_locator=Locator(name='div', key='class_', value='detail-price-uah'),
        child_locator=Locator(name='meta', key='itemprop', value='price')
    ),
    # https://ikea-club.com.ua
    DetailedLocator(
        parent_locator=Locator(name='div', key='class_', value='product-price'),
        child_locator=Locator(name='span')
    ),
    # https://e27.com.ua
    DetailedLocator(
        parent_locator=Locator(name='div', key='class_', value='product-primary-column'),
        child_locator=Locator(name='meta', key='itemprop', value='price')
    ),
    # https://jysk.ua
    DetailedLocator(
        parent_locator=Locator(name='div', key='class_', value='product-sumup'),
        child_locator=Locator(name='span', key='class_', value='product-price')
    )
]
