from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return{"message":"My first API is working"}

@app.get("/about")
def about():
    return{"Project": "loan risk model", "version": "1.0"}

@app.get("/customers")
def getCustomers(customer_id: int):
    return{
        "customerId": customer_id,
        "name": "Ravi",
        "status": "Active"
    }