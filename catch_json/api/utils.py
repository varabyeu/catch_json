from openpyxl import load_workbook

from .models import ProductData


def get_articles(file):
    workbook = load_workbook(filename=file).active
    list_articles = []
    list_error_articles = []
    row = 1

    while True:
        cell = workbook.cell(row=row, column=1)
        if cell.value:
            if isinstance(cell.value, int):
                list_articles.append(cell.value)
            else:
                list_error_articles.append(cell.value)
            row += 1
        else:
            break
    return tuple(list_articles), tuple(list_error_articles)


def get_valid_data(response):
    try:
        valid_data = ProductData.parse_obj(response)
        return {
            'article': valid_data['nm_id'],
            'brand': valid_data['brand_name'],
            'title': valid_data['imt_name']
        }
    except ValidationError as ve:
        print(f'Validation error during processing {response}')
