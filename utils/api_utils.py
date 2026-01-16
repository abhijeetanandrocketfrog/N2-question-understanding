import requests

def send_request(api_url, api_key, payload):
    headers = {
        "x-api-key": api_key,
        "Content-Type": "application/json"
    }
    response = requests.post(api_url, headers=headers, json=payload)
    try:
        return response.json()

    except Exception:
        print("\nError: Failed to decode JSON from API response.")
        print("Response status code:", response.status_code)

        # Try to extract error_code if present in the raw response
        raw_text = response.text.strip()
        print("Raw response:", raw_text)

        raise RuntimeError("Non-JSON response received from API.")

def print_response(resp, time, question):
    print("\n"+"-"*80)
    print("Question: ", question)
    print("Query ID:", resp.get("query_id"))
    print("Response Time:", time)
    print("\nGenerated Text:")
    print(resp.get("generated_text"))
    print("-"*80)

def clean_text(text: str) -> str:
    cleaned = text.replace("\\", "")
    cleaned = cleaned.replace("\n", " ")
    cleaned = " ".join(cleaned.split())
    return cleaned

