import uuid
import pandas as pd
import time

from utils.config_utils import load_config
from utils.prompt_utils import load_prompt
from utils.api_utils import send_request, print_response

config = load_config()
API_KEY = config["api"]["api_key"]
API_URL = config["api"]["api_url"]

REASONING = config["model"]["reasoning"]
MAX_TOKENS = config["model"]["max_new_tokens"]
TEMPERATURE = config["model"]["temperature"]
REPETITION_PENALTY = config["model"]["repetition_penalty"]


SYSTEM_PROMPT = load_prompt("prompts/system_prompt_v2.txt")
DEVELOPER_PROMPT = load_prompt("prompts/developer_prompt_v3.txt")

# Single
# question = input("Question :")
question = "Have I maxed out my out-of-pocket costs for in-plan-network facilities?"
question_id = f"q-{uuid.uuid4()}"
USER_PROMPT = f"Here is the user question:\n{question}"

payload = {
    "messages": [
        {
            "role": "user",
            "content": USER_PROMPT,
            "system": SYSTEM_PROMPT,
            "developer": DEVELOPER_PROMPT,
            "question_id": question_id
        }
    ],
    "reasoning": REASONING,
    "max_new_tokens": MAX_TOKENS,
    "temperature": TEMPERATURE,
    "repetition_penalty": REPETITION_PENALTY
}

start_time = time.time()
resp = send_request(API_URL, API_KEY, payload)
end_time = time.time()
print_response(resp, (end_time - start_time), question)


# # Bulk
# file_name = "ground_truth/GT_Demo_Day.xlsx"
# output = "outputs/llm_response.xlsx"
# data = pd.read_excel(file_name)

# # Select relevant columns
# questions = data[["Question", "EB Codes", "Phrases"]].copy()

# # Add empty columns
# questions["Response"] = ""
# questions["Query ID"] = ""
# questions["Total Time (API)"] = 0.0

# # Loop through each row
# for idx, row in questions.iterrows():
#     q_text = row["Question"]

#     USER_PROMPT = f"Here is the user question:\n{q_text}"
#     question_id = f"q-{uuid.uuid4()}"

#     payload = {
#         "messages": [
#             {
#                 "role": "user",
#                 "content": USER_PROMPT,
#                 "system": SYSTEM_PROMPT,
#                 "developer": DEVELOPER_PROMPT,
#                 "question_id": question_id
#             }
#         ],
#         "reasoning": REASONING,
#         "max_new_tokens": MAX_TOKENS,
#         "temperature": TEMPERATURE,
#         "repetition_penalty": REPETITION_PENALTY
#     }

#     start_time = time.time()
#     resp = send_request(API_URL, API_KEY, payload)
#     end_time = time.time()

#     # Insert results back into the same dataframe
#     questions.at[idx, "Response"] = resp.get("generated_text")
#     questions.at[idx, "Query ID"] = resp.get("query_id")
#     questions.at[idx, "Total Time (API)"] = end_time - start_time

#     print_response(resp, (end_time - start_time), q_text)

# # Save updated DataFrame
# questions.to_excel(output, index=False)
# print(f"Saved to {output}")
