class By(object):
    def __init__(self, tag_name=None, class_=None, id=None, parent=None):
        self.tag_name = tag_name
        self.parent = parent
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
    By(tag_name='h1', class_='detail-title', parent=By(tag_name='div', class_='detail-title-wrap')),
    # https://ikea-club.com.ua
    By(tag_name='h1', parent=By(tag_name='div', class_='product-name')),
    # https://e27.com.ua
    By(tag_name='h1', parent=By(tag_name='div', class_='product-name')),
    # https://jysk.ua
    By(tag_name='h1', parent=By(tag_name='div', class_='product-name-sku'))
]

PRODUCT_IMAGE_LOCATORS = [
    # https://bt.rozetka.com.ua
    By(tag_name='img', id='base_image', parent=By(tag_name='div', class_='responsive-img')),
    # https://ikea-club.com.ua
    By(tag_name='img', id='cloudZoomImage', parent=By(tag_name='div', id='sevenspikes-cloud-zoom')),
    # https://e27.com.ua
    By(tag_name='img', id='image-main', parent=By(tag_name='div', class_='img-box')),
    # https://jysk.ua
    By(tag_name='img', class_='image', parent=By(tag_name='div', id='product-image-carousel'))
]

PRODUCT_PRICE_LOCATORS = [
    # https://bt.rozetka.com.ua
    By(tag_name='meta', parent=By(tag_name='div', class_='detail-price-uah')),
    # https://ikea-club.com.ua
    By(tag_name='span', parent=By(tag_name='div', class_='product-price')),
    # https://e27.com.ua
    By(tag_name='span', class_='price', parent=By(tag_name='div', class_='product-type-data')),
    # https://jysk.ua
    By(tag_name='span', class_='product-price', parent=By(tag_name='div', class_='product-sumup'))
]
