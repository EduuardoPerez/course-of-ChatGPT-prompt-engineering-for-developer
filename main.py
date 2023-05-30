import os

import openai
from dotenv import find_dotenv, load_dotenv

_ = load_dotenv(find_dotenv())

openai.api_key = os.getenv("OPENAI_API_KEY")


def get_completion(prompt, model="gpt-3.5-turbo"):
    """
    Generates a completion based on the given prompt using OpenAI's ChatCompletion API.

    Args:
        prompt (str): The user's input prompt.
        model (str): (Optional) The model to use for generating the completion. Defaults to "gpt-3.5-turbo".

    Returns:
        str: The generated completion as a response to the prompt.
    """
    messages = [{"role": "user", "content": prompt}]
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=0,  # this is the degree of randomness of the model's output
    )
    return response.choices[0].message["content"]


# ** Principle 1
# ** Write clear and specific instructions
# ** Tactic 1: Use delimiters to clearly indicate distinct parts of the input
text_1 = """
You should express what you want a model to do by \
providing instructions that are as clear and \
specific as you can possibly make them. \
This will guide the model towards the desired output, \
and reduce the chances of receiving irrelevant \
or incorrect responses. Don't confuse writing a \
clear prompt with writing a short prompt. \
In many cases, longer prompts provide more clarity \
and context for the model, which can lead to \
more detailed and relevant outputs.
"""
prompt_1 = f"""
Summarize the text delimited by triple backticks \
into a single sentence.
```{text_1}```
"""
response_1 = get_completion(prompt_1)
print(response_1)
# response
# Clear and specific instructions should be provided to guide a model towards the desired output, and longer
# prompts can provide more clarity and context for the model, leading to more detailed and relevant outputs.


# ** Tactic 2: Ask for a structured output
prompt_2 = """
Generate a list of three made-up book titles along \
with their authors and genres.
Provide them in JSON format with the following keys:
book_id, title, author, genre.
"""
response_2 = get_completion(prompt_2)
print(response_2)
# response
# [
#     {"book_id": 1, "title": "The Lost City of Zorath", "author": "Aria Blackwood", "genre": "Fantasy"},
#     {"book_id": 2, "title": "The Last Survivors", "author": "Ethan Stone", "genre": "Science Fiction"},
#     {"book_id": 3, "title": "The Secret of the Haunted Mansion", "author": "Lila Rose", "genre": "Mystery"},
# ]
