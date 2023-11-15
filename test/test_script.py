import json
import random
import requests

from params import data_list

url = "http://127.0.0.1:8000/get_form/"


def test(api_url, data):
    params = random.choice(data)
    response = requests.post(api_url, params=params).json()
    output = (
        json.dumps(response, indent=4, ensure_ascii=False)
        if isinstance(response, dict)
        else "\n".join(response)
    )
    return output


if __name__ == "__main__":
    print(test(url, data_list))
