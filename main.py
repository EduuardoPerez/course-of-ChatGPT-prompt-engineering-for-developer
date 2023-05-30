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


# ** Tactic 3: Ask the model to check whether conditions are satisfied
text_2 = """
Making a cup of tea is easy! First, you need to get some \
water boiling. While that's happening, \
grab a cup and put a tea bag in it. Once the water is \
hot enough, just pour it over the tea bag. \
Let it sit for a bit so the tea can steep. After a \
few minutes, take out the tea bag. If you \
like, you can add some sugar or milk to taste. \
And that's it! You've got yourself a delicious \
cup of tea to enjoy.
"""
prompt_3 = """
You will be provided with text delimited by triple quotes.
If it contains a sequence of instructions, \
re-write those instructions in the following format:

Step 1 - ...
Step 2 - …
…
Step N - …

If the text does not contain a sequence of instructions, \
then simply write \"No steps provided.\"

\"\"\"{}\"\"\"

"""
response_3 = get_completion(prompt_3.format(text_2))
print("Completion for Text 2:")
print(response_3)
# response
# Completion for Text 1:
# Step 1 - Get some water boiling.
# Step 2 - Grab a cup and put a tea bag in it.
# Step 3 - Once the water is hot enough, pour it over the tea bag.
# Step 4 - Let it sit for a bit so the tea can steep.
# Step 5 - After a few minutes, take out the tea bag.
# Step 6 - Add some sugar or milk to taste.
# Step 7 - Enjoy your delicious cup of tea!

text_3 = """
The sun is shining brightly today, and the birds are \
singing. It's a beautiful day to go for a \
walk in the park. The flowers are blooming, and the \
trees are swaying gently in the breeze. People \
are out and about, enjoying the lovely weather. \
Some are having picnics, while others are playing \
games or simply relaxing on the grass. It's a \
perfect day to spend time outdoors and appreciate the \
beauty of nature.
"""
response = get_completion(prompt_3.format(text_3))
print("Completion for Text 2:")
print(response)
# response
# Completion for Text 2:
# No steps provided.

# ** Tactic 4: "Few-shot" prompting
prompt_4 = """
Your task is to answer in a consistent style.
<child>: Teach me about patience.

<grandparent>: The river that carves the deepest \
valley flows from a modest spring; the \
grandest symphony originates from a single note; \
the most intricate tapestry begins with a solitary thread.

<child>: Teach me about resilience.
"""
response_4 = get_completion(prompt_4)
print(response_4)
# response
# <grandparent>: Resilience is like a tree that bends with the wind but never breaks. It is the ability to bounce back
# from adversity and keep moving forward, even when things get tough. Just like a tree that grows stronger with each
# storm it weathers, resilience is a quality that can be developed and strengthened over time.
