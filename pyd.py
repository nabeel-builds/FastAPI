from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class LoanApplication(BaseModel):
    name: str
    age: int
    income: float
    loanAmount: float
    employeementYears: int

@app.post("/predict")
def predict_loan(application: LoanApplication):
    #model logic
    approved = (
        application.income > 50000 and
        application.employeementYears > 2 and
        application.age >= 21
    )

    return{
        "Applicant Name": application.name,
        "Loan Amount": application.loanAmount,
        "Decision": "approved" if approved else "rejected",
        "Reviewed Income": application.income
    }