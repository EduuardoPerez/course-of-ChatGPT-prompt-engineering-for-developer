# Course of ChatGPT prompt engineering for developer

- Learn prompt engineering best practices for application development
- Discover new ways to use LLMs, including how to build your own custom chatbot
- Gain hands-on practice writing and iterating on prompts yourself using the OpenAI API

**What you’ll learn in this course**
&nbsp;

In ChatGPT Prompt Engineering for Developers, you will learn how to use a large language model (LLM) to quickly build new and powerful applications.  Using the OpenAI API, you’ll be able to quickly build capabilities that learn to innovate and create value in ways that were cost-prohibitive, highly technical, or simply impossible before now.

This short course taught by Isa Fulford (OpenAI) and Andrew Ng (DeepLearning.AI) will describe how LLMs work, provide best practices for prompt engineering, and show how LLM APIs can be used in applications for a variety of tasks, including:

- Summarizing (e.g., summarizing user reviews for brevity)
- Inferring (e.g., sentiment classification, topic extraction)
- Transforming text (e.g., translation, spelling & grammar correction)
- Expanding (e.g., automatically writing emails)

In addition, you’ll learn two key principles for writing effective prompts, how to systematically engineer good prompts, and also learn to build a custom chatbot.

All concepts are illustrated with numerous examples, which you can play with directly in our Jupyter notebook environment to get hands-on experience with prompt engineering.

**In partnership with OpenAI**
&nbsp;

We are excited to collaborate with OpenAI in offering this course, designed to help developers effectively utilize LLMs. This course reflects the latest understanding of best practices for using prompts for the latest LLM models.

**Who should join?**
&nbsp;

ChatGPT Prompt Engineering for Developers is beginner-friendly. Only a basic understanding of Python is needed. But it is also suitable for advanced machine learning engineers wanting to approach the cutting-edge of prompt engineering and use LLMs.

**Instructors**
&nbsp;

- Isa Fulford
  - [LinkedIn](https://www.linkedin.com/in/isabella-fulford/)
  - [Twitter](https://twitter.com/isafulf)
- [Andrew Ng](https://www.andrewng.org/)
  - [LinkedIn](https://www.linkedin.com/in/andrewyng/)
  - [Twitter](https://twitter.com/AndrewYNg)

## Table of Contents

- [Course of ChatGPT prompt engineering for developer](#course-of-chatgpt-prompt-engineering-for-developer)
  - [Table of Contents](#table-of-contents)
  - [Personal notion documentation](#personal-notion-documentation)
  - [Setup](#setup)
  - [Classes](#classes)
    - [Class 01: Introduction](#class-01-introduction)
    - [Class 02: Guidelines](#class-02-guidelines)
      - [Prompting Principles](#prompting-principles)
      - [Principle 1. Tactic 1: Use delimiters to clearly indicate distinct parts of the input](#principle-1-tactic-1-use-delimiters-to-clearly-indicate-distinct-parts-of-the-input)
        - [**Example Prompt. Principle 1. Tactic 1.**](#example-prompt-principle-1-tactic-1)
          - [**Example template. Principle 1. Tactic 1.**](#example-template-principle-1-tactic-1)
          - [**Full example. Principle 1. Tactic 1.**](#full-example-principle-1-tactic-1)
          - [**Model response. Principle 1. Tactic 1.**](#model-response-principle-1-tactic-1)
      - [Principle 1. Tactic 2: Ask for a structured output](#principle-1-tactic-2-ask-for-a-structured-output)
        - [**Example Prompt. Principle 1. Tactic 2.**](#example-prompt-principle-1-tactic-2)
          - [**Example template. Principle 1. Tactic 2.**](#example-template-principle-1-tactic-2)
          - [**Full example. Principle 1. Tactic 2.**](#full-example-principle-1-tactic-2)
          - [**Model response. Principle 1. Tactic 2.**](#model-response-principle-1-tactic-2)
      - [Principle 1. Tactic 3: Ask the model to check whether conditions are satisfied](#principle-1-tactic-3-ask-the-model-to-check-whether-conditions-are-satisfied)
        - [**Example Prompt. Principle 1. Tactic 3.**](#example-prompt-principle-1-tactic-3)
          - [**Example template. Principle 1. Tactic 3.**](#example-template-principle-1-tactic-3)
          - [**Full example 1. Principle 1. Tactic 3.**](#full-example-1-principle-1-tactic-3)
          - [**Model response example 1. Principle 1. Tactic 3.**](#model-response-example-1-principle-1-tactic-3)
          - [**Full example 2. Principle 1. Tactic 3.**](#full-example-2-principle-1-tactic-3)
          - [**Model response example 2. Principle 1. Tactic 3.**](#model-response-example-2-principle-1-tactic-3)

## Personal notion documentation

---
[Link to project](https://www.notion.so/eduuardoperez/ChatGPT-Prompt-Engineering-for-Developers-e475df6e091548c48b46e62dd26601ee?pvs=4)

## Setup

---
Steps:

1. Create the virtual env

    ```shell
    python3 -m venv .venv && source .venv/bin/activate
    ```

2. Install dependencies

    ```shell
    pip install -r requirements.txt
    ```

3. Create the `.env` file and fill it with your [OpenAI API key](https://platform.openai.com/account/api-keys)

    ```shell
    cp .env.example .env
    ```

4. Run the script

    ```shell
    python3 main.py
    ```

## Classes

---

### Class 01: Introduction

This course on ChatGPT Prompt Engineering for Developers covers best practices and use cases for utilizing large language models (LLMs) through API calls. It distinguishes between base LLMs, trained to predict the next word, and instruction-tuned LLMs, trained to follow instructions. Instruction-tuned LLMs have gained momentum due to their helpful and less harmful outputs. The course emphasizes using instruction-tuned LLMs and provides examples of clear instructions and giving the LLM time to generate accurate responses. The materials were developed with contributions from OpenAI and DeepLearning.ai teams.

![Types of large language models (LLMs)](classes/src/class01-LLMs-types.png)

### Class 02: Guidelines

This class provides guidelines for effective prompting, focusing on two key principles: writing clear and specific instructions and giving the model time to think. Clear instructions help guide the model towards the desired output, while allowing it time to reason reduces the likelihood of incorrect responses. Tactics for clear instructions include using delimiters to indicate distinct parts of the input, asking for structured output like HTML or JSON, checking conditions before task completion, and utilizing few-shot prompting with examples. To give the model time to think, specifying steps for complex tasks, instructing the model to reason out its own solution before rushing to a conclusion, and comparing its solution to a given one can yield better results.

#### Prompting Principles

- **Principle 1: Write clear and specific instructions**\
  The first principle emphasizes the importance of providing clear and specific instructions to guide the model towards the desired output, highlighting that longer prompts can often offer more clarity and context for generating detailed and relevant responses.
- **Principle 2: Give the model time to "think"**\
  The second principle advises giving the model sufficient time to think and reason, as rushing it may lead to incorrect conclusions, suggesting that complex tasks require more computational effort and encouraging reframing queries to prompt a chain of relevant reasoning before providing a final answer.

#### Principle 1. Tactic 1: Use delimiters to clearly indicate distinct parts of the input

![Principle 1. Tactic 1](classes/src/class02-principle1-tactic1.png)

- Delimiters can be anything like:
  - """
  - \```
  - \---
  - < >
  - \<tag> </tag>

Delimiters serve as clear punctuation to separate specific sections of text from the rest of the prompt, helping to prevent prompt injections where conflicting user instructions may lead the model astray, and in the example below, the use of delimiters ensures that the model focuses on summarizing the designated instructions rather than following them.

![Principle 1. Tactic 1. Avoid prompt injections](class/../classes/src/class02-principle1-tactic1-avoid-prompt-injection.png)

##### **Example Prompt. Principle 1. Tactic 1.**

###### **Example template. Principle 1. Tactic 1.**

```plain
Summarize the text delimited by triple backticks into a single sentence.
```text```
```

###### **Full example. Principle 1. Tactic 1.**

```plain
Summarize the text delimited by triple backticks into a single sentence.
```You should express what you want a model to do by providing instructions that are as clear and specific as you can possibly make them. This will guide the model towards the desired output, and reduce the chances of receiving irrelevant or incorrect responses. Don't confuse writing a clear prompt with writing a short prompt. In many cases, longer prompts provide more clarity and context for the model, which can lead to more detailed and relevant outputs.```
```

###### **Model response. Principle 1. Tactic 1.**

```plain
Clear and specific instructions should be provided to guide a model towards the desired output, and longer prompts can provide more clarity and context for the model, leading to more detailed and relevant outputs.
```

#### Principle 1. Tactic 2: Ask for a structured output

![Principle 1. Tactic 2](classes/src/class02-principel1-tactic2.png)

To facilitate parsing model outputs, asking for a structured output like HTML or JSON can be useful. For example, requesting a list of three fictional book titles along with their authors and genres in JSON format allows easy conversion into a dictionary or list in Python.

##### **Example Prompt. Principle 1. Tactic 2.**

###### **Example template. Principle 1. Tactic 2.**

```plain
Generate a list of {some requirement}.
Provide them in JSON format with the following keys:
{relevant keys}.
```

###### **Full example. Principle 1. Tactic 2.**

```plain
Generate a list of three made-up book titles along with their authors and genres.
Provide them in JSON format with the following keys: book_id, title, author, genre.
```

###### **Model response. Principle 1. Tactic 2.**

```json
[
  {
    "book_id": 1,
    "title": "The Lost City of Zorath",
    "author": "Aria Blackwood",
    "genre": "Fantasy"
  },
  {
    "book_id": 2,
    "title": "The Last Survivors",
    "author": "Ethan Stone",
    "genre": "Science Fiction"
  },
  {
    "book_id": 3,
    "title": "The Secret of the Haunted Mansion",
    "author": "Lila Rose",
    "genre": "Mystery"
  }
]
```

#### Principle 1. Tactic 3: Ask the model to check whether conditions are satisfied

![Principle 1. Tactic 3](classes/src/class02-principel1-tactic3.png)

To ensure task assumptions are met, asking the model to check conditions beforehand can help avoid errors and incomplete attempts. Considering edge cases and defining how the model should handle them is also important to prevent unexpected outcomes.

##### **Example Prompt. Principle 1. Tactic 3.**

###### **Example template. Principle 1. Tactic 3.**

```plain
You will be provided with text delimited by triple quotes.
If it contains a sequence of instructions, re-write those instructions in the following format:

Step 1 - ...
Step 2 - …
…
Step N - …

If the text does not contain a sequence of instructions, then simply write "No steps provided."

"""
{text}
"""
```

###### **Full example 1. Principle 1. Tactic 3.**

```plain
You will be provided with text delimited by triple quotes.
If it contains a sequence of instructions, re-write those instructions in the following format:

Step 1 - ...
Step 2 - …
…
Step N - …

If the text does not contain a sequence of instructions, then simply write "No steps provided."

"""
Making a cup of tea is easy! First, you need to get some water boiling. While that's happening, grab a cup and put a tea bag in it. Once the water is hot enough, just pour it over the tea bag. Let it sit for a bit so the tea can steep. After a few minutes, take out the tea bag. If you like, you can add some sugar or milk to taste. And that's it! You've got yourself a delicious cup of tea to enjoy.
"""
```

###### **Model response example 1. Principle 1. Tactic 3.**

```plain
Completion for Text 1:
Step 1 - Get some water boiling.
Step 2 - Grab a cup and put a tea bag in it.
Step 3 - Once the water is hot enough, pour it over the tea bag.
Step 4 - Let it sit for a bit so the tea can steep.
Step 5 - After a few minutes, take out the tea bag.
Step 6 - Add some sugar or milk to taste.
Step 7 - Enjoy your delicious cup of tea!
```

###### **Full example 2. Principle 1. Tactic 3.**

```plain
You will be provided with text delimited by triple quotes.
If it contains a sequence of instructions, re-write those instructions in the following format:

Step 1 - ...
Step 2 - …
…
Step N - …

If the text does not contain a sequence of instructions, then simply write "No steps provided."

"""
The sun is shining brightly today, and the birds are singing. It's a beautiful day to go for a walk in the park. The flowers are blooming, and the trees are swaying gently in the breeze. People are out and about, enjoying the lovely weather. Some are having picnics, while others are playing games or simply relaxing on the grass. It's a perfect day to spend time outdoors and appreciate the beauty of nature.
"""
```

###### **Model response example 2. Principle 1. Tactic 3.**

```plain
No steps provided.
```
