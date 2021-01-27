from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel
from datetime import date

today = date.today()


class ExpenseEntry(BaseModel):
    hardware_id: str
    year: int
    month: int
    day: int
    amount: float
    description: Optional[str] = None
    category: Optional[str] = None

entry_a = {
        "hardware_id": "A76E533625E3FBD",
        "year": 2021,
        "month": 1,
        "day": 21,
        "amount": 997.56,
        "description": "A rocket. (Test entry)",
        "category": "Food",
    }
entry_b = {
    "hardware_id": "A76E533625E3FBD",
    "year": 2021,
    "month": 1,
    "day": 22,
    "amount": 50.22,
    "description": "A rocket. (Test entry)",
    "category": "Housing",
}




app = FastAPI()

@app.get("/entries/{hardware_id}/{from_y}/{from_m}/{from_d}/{to_y}/{to_m}/{to_d}")
async def entries(hardware_id: str = "A76E533625E3FBD", from_y: int = today.year, from_m: int = today.month, from_d: int = today.day,to_y: int = today.year, to_m: int = today.month, to_d: int = today.day):
    result = []
    result.append(entry_a)
    result.append(entry_b)
    return result

@app.get("/categories/{hardware_id}/")
async def categories(hardware_id: str = "A76E533625E3FBD",):
    result = (
        {
            "category_id": 1,
            "category_name": "Food",
        },
        {
            "category_id": 2,
            "category_name": "Housing",
        },
        {
            "category_id": 3,
            "category_name": "Transportation",
        },
    )
    return result


@app.get("/categories_pie/{hardware_id}/{from_y}/{from_m}/{from_d}/{to_y}/{to_m}/{to_d}")
async def categories_pie(hardware_id: str = "A76E533625E3FBD", from_y: int = today.year, from_m: int = today.month, from_d: int = today.day,to_y: int = today.year, to_m: int = today.month, to_d: int = today.day):
    return (
        {
            "category": "Food",
            "percentage": 20,
            "total": 2213.50,
        },
        {
            "category": "Housing",
            "percentage": 40,
            "total": 5000.50,
        },
        {
            "category": "Transportation",
            "percentage": 40,
            "total": 500.00,
        }
    )
    

@app.get("/monthly_trend/{hardware_id}/{from_y}/{from_m}/{to_y}/{to_m}")
async def monthly_trend(hardware_id: str = "A76E533625E3FBD", from_y: int = today.year, from_m: int = today.month, to_y: int = today.year, to_m: int = today.month):
    return (
        {
            "month": 202011,
            "amount": 11222.00,
        },
        {
            "month": 202012,
            "amount": 22222.00,
        },
        {
            "month": 202101,
            "amount": 15625.00,
        },
        {
            "month": 202102,
            "amount": 14325.00,
        },
    )

@app.post("/add_entry/")
async def add_entry(hardware_id: str, category: str, description: str, amount: float):
    return {
        "error_code": 0,
        "error_msg": f"Successfully added entry: {amount}"
    }

@app.post("/add_category/")
async def add_category(hardware_id: str, category: str):
    return {
        "error_code": -1,
        "error_msg": f"Failed to add category. Category {category} already exists."
    }

@app.put("/update_category/")
async def update_category(hardware_id: str, old_category: str, new_category: str):
    return {
        "error_code": 0,
        "error_msg": f"Successfully updated Category from {oldcategory} to {new_category}."
    }

@app.delete("/delete_category/}")
async def delete_category(hardware_id: str, category: str):
    return {
        "error_code": 0,
        "error_msg": f"Successfully deleted Category {category}."
    }

