import re

import gspread
from oauth2client.service_account import ServiceAccountCredentials


class SpreadSheetController(object):
    SCOPE = ['https://spreadsheets.google.com/feeds',
             'https://www.googleapis.com/auth/drive']
    URL_COLUMN_INDEX = 4
    CLIENT_SECRET_PATH = 'misc/ptzn_client_secret.json'
    COLUMN_PRODUCT_NAME_INDEX = 3
    COLUMN_PRODUCT_IMAGE_INDEX = 2
    COLUMN_PRODUCT_PRICE_INDEX = 6

    def __init__(self, worksheet_index, sheet_name):
        self.__credentials = ServiceAccountCredentials.from_json_keyfile_name(self.CLIENT_SECRET_PATH, self.SCOPE)
        self.__client = gspread.authorize(self.__credentials)
        self.working_sheet = self.__client.open(sheet_name).get_worksheet(worksheet_index)

    def get_all_working_cells(self):
        search_criteria = re.compile(r'(http|https)')
        return self.working_sheet.findall(search_criteria)

    def update_product_name(self, cell, name):
        self.working_sheet.update_cell(cell.row, self.COLUMN_PRODUCT_NAME_INDEX, name)

    def update_product_image(self, cell, image_url):
        self.working_sheet.update_cell(cell.row, self.COLUMN_PRODUCT_IMAGE_INDEX, '=image("{url}")'.format(url=image_url))

    def update_product_price(self, cell, price):
        self.working_sheet.update_cell(cell.row, self.COLUMN_PRODUCT_PRICE_INDEX, price)
