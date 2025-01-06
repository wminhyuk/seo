from fastapi import FastAPI
from datetime import datetime, date
from typing import Dict

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
    try:
        # 생년월일을 datetime 객체로 변환
        birth_date = datetime.strptime(birthday, "%Y-%m-%d").date()
        today = date.today()

        # 만나이 계산
        age = today.year - birth_date.year
        
        # 생일이 이미 지났으면 연도 차이만 사용, 아니면 1년을 뺌
        if today < birth_date.replace(year=today.year):
            age = age - 1
            
        return {
            "birthday": birthday,
            "age": str(age),
            "basedate": str(today),
            "message": "Age calculated successfully!"
        }
    except ValueError:
        return {
            "error": "Invalid date format. Use 'YYYY-MM-DD'."
        }