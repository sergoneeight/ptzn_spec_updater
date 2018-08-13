import requests
from bs4 import BeautifulSoup

from scrapper.locators import PRODUCT_NAME_LOCATORS, PRODUCT_IMAGE_LOCATORS, PRODUCT_PRICE_LOCATORS


class ProductDetailsScrapper(object):

    @staticmethod
    def get_html(url):
        return requests.get(url, verify=False).text

    @staticmethod
    def __price_converter(price_tag):
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

    @staticmethod
    def __find_element(soup, locators):
        for locator in locators:
            if locator.parent:
                parent = soup.find(name=locator.parent.tag_name, **locator.parent.attrs)
                if parent:
                    element = parent.find(name=locator.tag_name, **locator.attrs)
                    if element:
                        return parent.find(name=locator.tag_name, **locator.attrs)
            else:
                element = soup.find(name=locator.tag_name, **locator.attrs)
                if element:
                    return element
        return None

    def get_product_price(self, url):
        soup = BeautifulSoup(self.get_html(url), 'html.parser')
        price = self.__find_element(soup, PRODUCT_PRICE_LOCATORS)
        if price:
            return self.__price_converter(price)
        return None

    def get_product_image(self, url):
        soup = BeautifulSoup(self.get_html(url), 'html.parser')
        image_tag = self.__find_element(soup, PRODUCT_IMAGE_LOCATORS)
        if image_tag:
            return image_tag['src']
        return None

    def get_product_name(self, url):
        soup = BeautifulSoup(self.get_html(url), 'html.parser')
        name_tag = self.__find_element(soup, PRODUCT_NAME_LOCATORS)
        if name_tag:
            return str(name_tag.text).strip().split('+')[0]
        return None
