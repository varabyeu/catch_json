from openpyxl import load_workbook
from pydantic import BaseModel, ValidationError


class ProductData(BaseModel):
    nm_id: int
    brand_name: str
    imt_name: str

    def __init__(self, **kwargs):
        kwargs['brand_name'] = kwargs.get('selling').get('brand_name')
        super().__init__(**kwargs)


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
        valid_data = ProductDataList.parse_obj(response)
        return valid_data
    except ValidationError as ve:
        print(f'Validation error during processing {response}')


def get_needed_data(json):
    print(json)
    return None
