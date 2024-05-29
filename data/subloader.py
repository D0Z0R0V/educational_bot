import os
from ujson import loads
import aiofiles

async def get_json_data(filename: str) -> list:
    path1 = f"data/class/{filename}"
    path2 = f"data/application/{filename}"
    path3 = f"data/task/{filename}"
    
    if os.path.exists(path1):
        async with aiofiles.open(path1, "r", encoding="utf-8") as file:
            return loads(await file.read())
    elif os.path.exists(path2):
        async with aiofiles.open(path2, "r", encoding="utf-8") as file:
            return loads(await file.read())
    elif os.path.exists(path3):
        async with aiofiles.open(path3, "r", encoding="utf-8") as file:
            return loads(await file.read())
    return []