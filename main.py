#!/usr/bin/python
from sheet.spreadsheet_controller import SpreadSheetController
from scrapper.product_scrapper import ProductDetailsScrapper

sheet_controller = SpreadSheetController(worksheet_index=0, sheet_name='ptzn_spec_test')
scrapper = ProductDetailsScrapper()


# Use only for debug purposes
def clear_spreadsheet():
    products_url_cells = sheet_controller.get_all_working_cells()
    for cell in products_url_cells:
        sheet_controller.update_product_name(cell, '')
        sheet_controller.update_product_image(cell, '')
        sheet_controller.update_product_price(cell, 0)


def update_spreadsheet():
    products_url_cells = sheet_controller.get_all_working_cells()
    for cell in products_url_cells:
        name = scrapper.get_product_name(cell.value)
        if name:
            sheet_controller.update_product_name(cell, name)

        image = scrapper.get_product_image(cell.value)
        if image:
            sheet_controller.update_product_image(cell, image)

        price = scrapper.get_product_price(cell.value)
        if price:
            sheet_controller.update_product_price(cell, price)


if __name__ == '__main__':
    update_spreadsheet()
    # clear_spreadsheet()
