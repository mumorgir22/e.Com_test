import json
import requests


url = "http://127.0.0.1:8000/add_template/"

form = {
    "name": "New Feedback Form",
    "full_name": "text",
    "email": "email",
    "message": "text",
    "date": "date"
}


def add_template(api_url, data):
    response = requests.post(api_url, json=data).json()
    output = (
        json.dumps(response, indent=4, ensure_ascii=False)
        if isinstance(response, dict)
        else "\n".join(response)
    )
    return output


if __name__ == "__main__":
    print(add_template(url, form))
