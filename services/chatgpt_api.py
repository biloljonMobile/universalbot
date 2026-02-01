# from openai import OpenAI
# from config import OPENIA_API

# client = OpenAI(
#     api_key=OPENIA_API
# )


# def chatgpt_answer(text: str) -> str:
#     response = client.chat.completions.create(
#         model="gpt-4o-mini",
#         messages=[
#             {"role": "user", "content": text}
#         ]
#     )
#     return response.choices[0].message.content
