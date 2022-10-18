import asyncio
import aiohttp
from rest_framework import status

from .utils import get_needed_data


async def get_json_data(article):
    url = f"https://wbx-content-v2.wbstatic.net/ru/{article}.json"
    async with aiohttp.ClientSession() as session:
        json_product_data = []
        try:
            async with session.get(url) as response:
                if response.status == status.HTTP_200_OK:
                    full_product_data = await response.json()
                    json_product_data.append(get_needed_data(full_product_data))
            return json_product_data
        except aiohttp.ClientError as error:
            return error


def distribute_tasks(data: list):
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    task_list = []
    for item in data:
        task_list.append(get_json_data(item))
    ran_tasks = loop.run_until_complete(asyncio.gather(*task_list))
    return ran_tasks
