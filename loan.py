from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class LoanApplication(BaseModel):
    age: int
    income: float
    loanAmount: float
    employeementYears: float

@app.post("/predict")
def predictLoan(appliaction: LoanApplication):

    #pretend this is a trained model
    if appliaction.income > 50000 and appliaction.employeementYears > 2:
        decision = "approved"
    else:
        decision = "rejected"

    return{
        "applicationAge":appliaction.age,
        "decision":decision
    }


