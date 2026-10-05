from fastapi import FastAPI

app = FastAPI()

all_customers = [
    {"id": 101, "name": "Ravi", "city": "Delhi", "risk": "low"},
    {"id": 102, "name": "Om", "city": "Mumbai", "risk": "high"},
    {"id": 103, "name": "Prakash", "city": "UP", "risk": "medium"},
    {"id": 104, "name": "Kishan", "city": "Pune", "risk": "low"},
    {"id": 105, "name": "Karan", "city": "noida", "risk": "high"}
]

@app.get("/customers")
def get_customers(city: str, risk: str):
    filtered = [
        c for c in all_customers
        if c["city"] == city and c["risk"] == risk
    ]

    return{
        "city": city,
        "risk": risk,
        "count": len(filtered),
        "result": filtered
    }