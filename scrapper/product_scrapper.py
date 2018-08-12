import requests
from bs4 import BeautifulSoup

from scrapper.locators import PRODUCT_NAME_LOCATORS, PRODUCT_IMAGE_LOCATORS, PRODUCT_PRICE_LOCATORS


class ProductDetailsScrapper(object):

    @staticmethod
    def get_html(url):
        return requests.get(url, verify=False).text

    @classmethod
    def __price_converter(cls, price_tag):
        """
        Converts product price string to float
        :param price_tag: is soup html tag which contains product price
        :return: float product price
        """
        try:
            price = price_tag['content']
        except KeyError as e:
            print('There is no {} key in price tag'.format(e))
            price = price_tag.text

        if price:
            price = ''.join(i for i in price if i.isdigit() or i == ',' or i == '.')
            price = float(price)

        return price

    def get_product_price(self, url):
        soup = BeautifulSoup(self.get_html(url), 'html.parser')
        for name_locator in PRODUCT_PRICE_LOCATORS:
            parent = soup.find(name=name_locator.parent_locator.name, **name_locator.parent_locator.attrs)
            if parent:
                price = parent.find(name_locator.child_locator.name, **name_locator.child_locator.attrs)
                if price:
                    return self.__price_converter(price)
        return None

    def get_product_image(self, url):
        soup = BeautifulSoup(self.get_html(url), 'html.parser')
        for name_locator in PRODUCT_IMAGE_LOCATORS:
            parent = soup.find(name=name_locator.parent_locator.name, **name_locator.parent_locator.attrs)
            if parent:
                image = parent.find(name_locator.child_locator.name, **name_locator.child_locator.attrs)
                if image:
                    return image['src']
        return None

    def get_product_name(self, url):
        soup = BeautifulSoup(self.get_html(url), 'html.parser')
        for name_locator in PRODUCT_NAME_LOCATORS:
            parent = soup.find(name=name_locator.parent_locator.name, **name_locator.parent_locator.attrs)
            if parent:
                name = parent.find(name_locator.child_locator.name, **name_locator.child_locator.attrs)
                if name:
                    name = str(name.text).strip().split('+')[0]
                    return name
        return None
