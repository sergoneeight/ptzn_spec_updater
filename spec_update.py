from sheet.spreadsheet_controller import SpreadSheetController

sheet_controller = SpreadSheetController(worksheet_index=0, sheet_name='ptzn_spec_test raq')

if __name__ == '__main__':
    sheet_controller.update()
    # sheet_controller.clear()
