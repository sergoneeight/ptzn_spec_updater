import requests
import urllib3
from bs4 import BeautifulSoup

from scrapper.locators import PRODUCT_NAME_LOCATORS, PRODUCT_IMAGE_LOCATORS, PRODUCT_PRICE_LOCATORS
from utils import logger

logger = logger.get_logger('scrapper.log')


class ProductDetailsScrapper(object):

    @staticmethod
    def get_html(url):
        logger.info('Getting data for {}\n'.format(url))
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        return requests.get(url, verify=False).text

    @staticmethod
    def _find_element(soup, locators):
        for locator in locators:
            if locator.container:
                msg = 'Searching for an element - {} {} in container - {} {}'.format(
                    locator.tag_name, locator.attrs, locator.container.tag_name, locator.container.attrs)
                logger.info(msg)
                parent = soup.find(name=locator.container.tag_name, **locator.container.attrs)
                if parent:
                    element = parent.find(name=locator.tag_name, **locator.attrs)
                    if not element:
                        logger.warning('ELEMENT - {} {} NOT FOUND'.format(locator.tag_name, locator.attrs))
                    return element
                logger.warning('CONTAINER - {} {} NOT FOUND'.format(locator.container.tag_name, locator.container.attrs))
            else:
                element = soup.find(name=locator.tag_name, **locator.attrs)
                if not element:
                    logger.warning('ELEMENT - {} {} NOT FOUND'.format(locator.tag_name, locator.attrs))
                return element

        return None

    def get_product_details(self, url):
        soup = BeautifulSoup(self.get_html(url), 'html.parser')
        name_tag = self._find_element(soup, PRODUCT_NAME_LOCATORS)
        price_tag = self._find_element(soup, PRODUCT_PRICE_LOCATORS)
        image_tag = self._find_element(soup, PRODUCT_IMAGE_LOCATORS)
        return Product(name_tag, price_tag, image_tag)


class Product(object):
    def __init__(self, name_tag, price_tag, image_tag):
        self._name_tag = name_tag
        self._price_tag = price_tag
        self._image_tag = image_tag

    @property
    def name(self):
        name = None
        if self._name_tag:
            name = self._name_tag.text.strip().split('+')[0]
        return name

    @property
    def price(self):
        price = None
        if self._price_tag:
            try:
                price = self._price_tag['content']
            except KeyError as e:
                print('There is no {} key in price tag'.format(e))
                price = self._price_tag.text

        if price:
            price = ''.join(i for i in price if i.isdigit() or i == ',' or i == '.')
            price = float(price)
        return price

    @property
    def image_url(self):
        image_url = None
        if self._image_tag:
            image_url = self._image_tag['src']
        return image_url
