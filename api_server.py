from fastapi import FastAPI
from pydantic import BaseModel
from evaluator import evaluate  # shared_core直下ならこれでOK

app = FastAPI(title="Syntax Evaluator API")

class TextInput(BaseModel):
    text: str
    method: str = "simple"

@app.post("/evaluate")
def evaluate_endpoint(input_data: TextInput):
    """
    KZHX評価API
    """
    result = evaluate(input_data.text, input_data.method)
    return result

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("api_server:app", host="0.0.0.0", port=8000, reload=True)
