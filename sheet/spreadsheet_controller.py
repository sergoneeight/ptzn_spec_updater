import re

import gspread
from oauth2client.service_account import ServiceAccountCredentials

from scrapper.product_scrapper import ProductDetailsScrapper


class SpreadSheetController(object):
    SCOPE = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
    URL_COLUMN_INDEX = 4
    CLIENT_SECRET_PATH = 'misc/ptzn_client_secret.json'
    COLUMN_PRODUCT_NAME_INDEX = 3
    COLUMN_PRODUCT_IMAGE_INDEX = 2
    COLUMN_PRODUCT_PRICE_INDEX = 6
    scrapper = ProductDetailsScrapper()

    def __init__(self, worksheet_index, sheet_name):
        self.__credentials = ServiceAccountCredentials.from_json_keyfile_name(self.CLIENT_SECRET_PATH, self.SCOPE)
        self.__client = gspread.authorize(self.__credentials)
        self.sheet = self.__client.open(sheet_name).get_worksheet(worksheet_index)

    def _get_all_working_cells(self):
        search_criteria = re.compile(r'(http|https)')
        return self.sheet.findall(search_criteria)

    def _update_product_name(self, cell, name):
        self.sheet.update_cell(cell.row, self.COLUMN_PRODUCT_NAME_INDEX, name)

    def _update_product_image(self, cell, image_url):
        self.sheet.update_cell(cell.row, self.COLUMN_PRODUCT_IMAGE_INDEX, '=image("{url}")'.format(url=image_url))

    def _update_product_price(self, cell, price):
        self.sheet.update_cell(cell.row, self.COLUMN_PRODUCT_PRICE_INDEX, price)

    def clear(self):
        products_url_cells = self._get_all_working_cells()
        for cell in products_url_cells:
            self._update_product_name(cell, '')
            self._update_product_image(cell, '')
            self._update_product_price(cell, 0)

    def update(self):
        products_url_cells = self._get_all_working_cells()
        for cell in products_url_cells:
            product = self.scrapper.get_product_details(cell.value)
            if product.name:
                self._update_product_name(cell, product.name)
            if product.price:
                self._update_product_price(cell, product.price)
            if product.image_url:
                self._update_product_image(cell, product.image_url)
