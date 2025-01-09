from fastapi import FastAPI
from datetime import datetime, date
from typing import Dict
import random

### Create FastAPI instance with custom docs and openapi url
app = FastAPI(docs_url="/api/py/docs", openapi_url="/api/py/openapi.json")

@app.get("/api/py/helloFastApi")
def hello_fast_api():
    return {"message": "Hello from FastAPI"}

@app.get("/api/py/ageCalculator/{birthday}")
def age_calculator(birthday: str) -> Dict[str, str]:
    """
    생년월일을 입력받아 만나이를 계산하는 API

    :param birthday: 생년월일 (형식: YYYY-MM-DD)
    :return: 생년월일 및 만나이를 포함한 JSON 응답
    """
    today = date.today()
    birth_date = datetime.strptime(birthday, "%Y-%m-%d").date()
    age = today.year - birth_date.year

    # 생일 반영 코드
    is_pre_birthday = today < birth_date.replace(year=today.year)
    if is_pre_birthday:
        age = age - 1

    return {
            "birthday": birthday,
            "age": str(age),
<<<<<<< HEAD
=======
=======
<<<<<<< HEAD
            "age": str(age),
=======
<<<<<<< HEAD
            "age": str(age),
=======
            "age": str(27),
>>>>>>> 07fcb3ee25bac5975a17b464fa9e36d4fbe138d0
>>>>>>> d8c78a38faf01a9d7e11222d52680b8d9759baa2
>>>>>>> 138c3576efeef0115d4234acfc49ec48a02814e4
>>>>>>> f875316b3c05c3cff290703708252787f897bb3b
            "basedate": str(today),
            "message": "Age calculated successfully!"
            }
