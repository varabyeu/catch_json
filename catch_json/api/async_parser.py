import asyncio
import aiohttp
from rest_framework import status

from .utils import get_valid_data


async def get_json_data(article):
    url = f"https://wbx-content-v2.wbstatic.net/ru/{article}.json"
    async with aiohttp.ClientSession() as session:
        json_product_data = []
        try:
            async with session.get(url) as response:
                if response.status == status.HTTP_200_OK:
                    response_data = await response.json()
                    valid_data = get_valid_data(response_data)
                    return valid_data
        except aiohttp.ClientError as error:
            return error


def distribute_tasks(data: list):
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    task_list = []
    for item in data:
        task_list.append(get_json_data(item))
    ran_tasks: list = loop.run_until_complete(asyncio.gather(*task_list))
    for result in ran_tasks:
        if result is None:
            ran_tasks.remove(result)
    return ran_tasks
