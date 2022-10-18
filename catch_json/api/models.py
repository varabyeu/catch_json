from pydantic import BaseModel


class ProductData(BaseModel):
    nm_id: int
    brand_name: str
    imt_name: str

    def __init__(self, **kwargs):
        kwargs['brand_name'] = kwargs.get('selling').get('brand_name')
        super().__init__(**kwargs)

    def __getitem__(self, item):
        return getattr(self, item)
