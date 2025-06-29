import requests

def evaluate_text(text: str, method: str = "simple", host: str = "http://localhost:8000"):
    url = f"{host}/evaluate"
    response = requests.post(url, json={"text": text, "method": method})
    response.raise_for_status()
    return response.json()

if __name__ == "__main__":
    sample_text = "意味が潰れたあとに、声が残った。"
    result = evaluate_text(sample_text)
    print(result)
