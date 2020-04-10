from urllib.parse import urlparse

import cloudscraper
from bs4 import BeautifulSoup

from scrapper.locators import locators
from utils import logger
from utils.scrapper_utils import price_str_to_float

logger = logger.get_logger('scrapper.log')


class ProductDetailsScrapper(object):

    # @staticmethod
    # def get_html(url):
    #     logger.info('Getting data for {}'.format(url))
    #     urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
    #     # headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) '
    #     #                          'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
    #     header = {
    #         'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    #         # 'accept-encoding': 'gzip, deflate, br', # удалите эту строку
    #         'accept-language': 'en-US,en;q=0.8',
    #         'upgrade-insecure-requests': '1',
    #         'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'
    #     }
    #     # headers = {
    #     #     'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:75.0) Gecko/20100101 Firefox/75.0',
    #     #
    #     # }
    #     response = requests.get(url, headers=header, timeout=5, verify=False)
    #     if response.status_code == 503:
    #         response = requests.get(url, headers=header, timeout=5, verify=False)
    #     response.encoding = 'utf-8'
    #
    #     return response.text

    @staticmethod
    def get_html(url):
        logger.info('Getting data for {}'.format(url))
        scraper = cloudscraper.create_scraper()
        result = scraper.get(url)
        result.encoding = 'utf-8'
        return result.text

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
                logger.warning(
                    'CONTAINER - {} {} NOT FOUND'.format(locator.container.tag_name, locator.container.attrs))
            else:
                element = soup.find(name=locator.tag_name, **locator.attrs)
                if not element:
                    logger.warning('ELEMENT - {} {} NOT FOUND'.format(locator.tag_name, locator.attrs))
                return element

        return None

    def get_product_details(self, url):
        soup = BeautifulSoup(self.get_html(url), 'html.parser')
        locator_key = urlparse(url).netloc
        if locator_key.startswith('bt.'):
            locator_key = locator_key.replace('bt.', '')
        name_tag, price_tag, image_tag = None, None, None

        try:
            current = locators[locator_key]
            name_tag = self._find_element(soup, current['product_name'])
            price_tag = self._find_element(soup, current['product_price'])
            image_tag = self._find_element(soup, current['product_image'])
        except KeyError as e:
            logger.error('There is no available locators for {} key'.format(e))

        return Product(url, name_tag, price_tag, image_tag)


class Product(object):
    def __init__(self, url, name_tag, price_tag, image_tag):
        self._url = url
        self._name_tag = name_tag
        self._price_tag = price_tag
        self._image_tag = image_tag

    @property
    def name(self):
        name = ''
        if self._name_tag:
            name = self._name_tag.text.strip().split('+')[0]
        return name

    @property
    def price(self):
        price_str = ''
        if self._price_tag:
            try:
                price_str = self._price_tag['content']
            except KeyError as e:
                logger.error('There is no {} key in price tag'.format(e))
                price_str = self._price_tag.text

        return price_str_to_float(price_str)

    @property
    def image_url(self):
        image_url = ''
        if self._image_tag:
            image_url = self._image_tag.get('src') or self._image_tag.get('data-src')
            if image_url:
                if not image_url.startswith('http'):
                    parsed = urlparse(self._url)
                    image_url = '{}://{}{}'.format(parsed.scheme, parsed.netloc, image_url)
                logger.info('Retrieved image url - {}'.format(image_url))
            else:
                logger.error('Failed to locate image')
        return image_url
