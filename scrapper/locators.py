class By(object):
    def __init__(self, tag_name=None, class_=None, id=None, container=None):
        self.tag_name = tag_name
        self.container = container
        self.__class = class_
        self.__id = id

    @property
    def attrs(self):
        if self.__class:
            return {'class_': self.__class}
        elif self.__id:
            return {'id': self.__id}
        else:
            return {}


PRODUCT_NAME_LOCATORS = [
    # https://bt.rozetka.com.ua
    By(tag_name='h1', class_='detail-title', container=By(tag_name='div', class_='detail-title-wrap')),
    # https://ikea-club.com.ua
    By(tag_name='h1', container=By(tag_name='div', class_='product-name')),
    # https://e27.com.ua
    By(tag_name='h1', container=By(tag_name='div', class_='product-name')),
    # https://jysk.ua
    By(tag_name='h1', container=By(tag_name='div', class_='product-name-sku'))
]

PRODUCT_IMAGE_LOCATORS = [
    # https://bt.rozetka.com.ua
    By(tag_name='img', id='base_image', container=By(tag_name='div', class_='responsive-img')),
    # https://ikea-club.com.ua
    By(tag_name='img', id='cloudZoomImage', container=By(tag_name='div', id='sevenspikes-cloud-zoom')),
    # https://e27.com.ua
    By(tag_name='img', id='image-main', container=By(tag_name='div', class_='img-box')),
    # https://jysk.ua
    By(tag_name='img', class_='image', container=By(tag_name='div', id='product-image-carousel'))
]

PRODUCT_PRICE_LOCATORS = [
    # https://bt.rozetka.com.ua
    By(tag_name='meta', container=By(tag_name='div', class_='detail-price-uah')),
    # https://ikea-club.com.ua
    By(tag_name='span', container=By(tag_name='div', class_='product-price')),
    # https://e27.com.ua
    By(tag_name='span', class_='price', container=By(tag_name='div', class_='product-type-data')),
    # https://jysk.ua
    By(tag_name='span', class_='product-price', container=By(tag_name='div', class_='product-sumup'))
]
