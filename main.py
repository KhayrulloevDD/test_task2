from fastapi import FastAPI
import re

app = FastAPI()


@app.get("/check_inn/{inn}")
def read_item(inn):
    pattern = re.compile("[0-9]{10}")
    inn_is_valid = False
    if pattern.match(inn):
        inn_is_valid = True

    return {
        "inn": inn,
        "inn_is_valid": inn_is_valid
    }
