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
        - [**Principle 1: Write clear and specific instructions**](#principle-1-write-clear-and-specific-instructions)
        - [**Principle 2: Give the model time to "think"**](#principle-2-give-the-model-time-to-think)
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
      - [Principle 1. Tactic 4: "Few-shot" prompting](#principle-1-tactic-4-few-shot-prompting)
        - [**Example Prompt. Principle 1. Tactic 4.**](#example-prompt-principle-1-tactic-4)
          - [**Example. Principle 1. Tactic 4.**](#example-principle-1-tactic-4)
          - [**Model response. Principle 1. Tactic 4.**](#model-response-principle-1-tactic-4)
      - [Principle 2. Tactic 1: Specify the steps required to complete a task](#principle-2-tactic-1-specify-the-steps-required-to-complete-a-task)
        - [**Example Prompt. Principle 2. Tactic 1.**](#example-prompt-principle-2-tactic-1)
          - [**Example template. Principle 2. Tactic 1.**](#example-template-principle-2-tactic-1)
          - [**Full example 1. Principle 2. Tactic 1.**](#full-example-1-principle-2-tactic-1)
          - [**Model response example 1. Principle 2. Tactic 1.**](#model-response-example-1-principle-2-tactic-1)
          - [**Full example 2. Principle 2. Tactic 1. Ask for output in a specified format**](#full-example-2-principle-2-tactic-1-ask-for-output-in-a-specified-format)
          - [**Model response example 2. Principle 2. Tactic 1.**](#model-response-example-2-principle-2-tactic-1)
      - [Principle 2. Tactic 2: Instruct the model to work out its own solution before rushing to a conclusion](#principle-2-tactic-2-instruct-the-model-to-work-out-its-own-solution-before-rushing-to-a-conclusion)
        - [**Example Prompt. Principle 2. Tactic 2.**](#example-prompt-principle-2-tactic-2)
          - [**Model response. Principle 2. Tactic 2.**](#model-response-principle-2-tactic-2)

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

##### **Principle 1: Write clear and specific instructions**

  The first principle emphasizes the importance of providing clear and specific instructions to guide the model towards the desired output, highlighting that longer prompts can often offer more clarity and context for generating detailed and relevant responses.

##### **Principle 2: Give the model time to "think"**

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

#### Principle 1. Tactic 4: "Few-shot" prompting

![Principle 1. Tactic 4](classes/src/class02-principel1-tactic4.png)

The final tactic for this principle is using few-shot prompting, which involves providing examples of successful task executions before asking the model to perform the desired task.

##### **Example Prompt. Principle 1. Tactic 4.**

The prompt instructs the model to answer in a consistent style by providing examples of a conversation between a child and a grandparent. The model is asked to teach about patience and then about resilience, and it responds in a similar tone, using metaphors to convey the desired message.

###### **Example. Principle 1. Tactic 4.**

```plain
Your task is to answer in a consistent style.
<child>: Teach me about patience.

<grandparent>: The river that carves the deepest valley flows from a modest spring; the grandest symphony originates from a single note; the most intricate tapestry begins with a solitary thread.

<child>: Teach me about resilience.
```

###### **Model response. Principle 1. Tactic 4.**

```plain
<grandparent>: Resilience is like a tree that bends with the wind but never breaks. It is the ability to bounce back from adversity and keep moving forward, even when things get tough. Just like a tree that grows stronger with each storm it weathers, resilience is a quality that can be developed and strengthened over time.
```

#### Principle 2. Tactic 1: Specify the steps required to complete a task

![Principle 2. Tactic 1](classes/src/class02-principle2-tactic1.png)

The first tactic of the second principle, is to provide specific instructions for a task, such as summarizing a text, translating it into French, listing names, and outputting a JSON object with specific keys, while separating the answers with line breaks.

##### **Example Prompt. Principle 2. Tactic 1.**

###### **Example template. Principle 2. Tactic 1.**

```plain
Perform the following actions:
Step 1: ...
Step 2: ...
...
Step N: ...

Separate your answers with line breaks.

Text:
```{text}```
```

###### **Full example 1. Principle 2. Tactic 1.**

```plain
Perform the following actions:
1 - Summarize the following text delimited by triple backticks with 1 sentence.
2 - Translate the summary into French.
3 - List each name in the French summary.
4 - Output a json object that contains the following keys: french_summary, num_names.

Separate your answers with line breaks.

Text:
```In a charming village, siblings Jack and Jill set out on a quest to fetch water from a hilltop well. As they climbed, singing joyfully, misfortune struck—Jack tripped on a stone and tumbled down the hill, with Jill following suit. Though slightly battered, the pair returned home to comforting embraces. Despite the mishap, their adventurous spirits remained undimmed, and they continued exploring with delight.```
```

###### **Model response example 1. Principle 2. Tactic 1.**

```plain
Two siblings, Jack and Jill, go on a quest to fetch water from a well on a hilltop, but misfortune strikes and they both tumble down the hill, returning home slightly battered but with their adventurous spirits undimmed.

Deux frères et sœurs, Jack et Jill, partent en quête d'eau d'un puits sur une colline, mais un malheur frappe et ils tombent tous les deux de la colline, rentrant chez eux légèrement meurtris mais avec leurs esprits aventureux intacts. Noms: Jack, Jill.

{
  "french_summary": "Deux frères et sœurs, Jack et Jill, partent en quête d'eau d'un puits sur une colline, mais un malheur frappe et ils tombent tous les deux de la colline, rentrant chez eux légèrement meurtris mais avec leurs esprits aventureux intacts.",
  "num_names": 2,
}
```

###### **Full example 2. Principle 2. Tactic 1. Ask for output in a specified format**

```plain
Your task is to perform the following actions:
1 - Summarize the following text delimited by <> with 1 sentence.
2 - Translate the summary into French.
3 - List each name in the French summary.
4 - Output a json object that contains the following keys: french_summary, num_names.

Use the following format:
Text: <text to summarize>

Summary: <summary>

Translation: <summary translation>

Names: <list of names in Italian summary>

Output JSON: <json with summary and num_names>

Text: <In a charming village, siblings Jack and Jill set out on a quest to fetch water from a hilltop well. As they climbed, singing joyfully, misfortune struck—Jack tripped on a stone and tumbled down the hill, with Jill following suit. Though slightly battered, the pair returned home to comforting embraces. Despite the mishap, their adventurous spirits remained undimmed, and they continued exploring with delight.>
```

###### **Model response example 2. Principle 2. Tactic 1.**

```plain
Summary: Jack and Jill, siblings from a charming village, embarked on a quest to fetch water but encountered misfortune along the way. Despite the mishap, their adventurous spirits persisted.

Translation: Jack et Jill, frère et sœur d'un charmant village, se sont lancés dans une quête pour chercher de l'eau mais ont rencontré des malheurs en cours de route. Malgré cet incident, leur esprit d'aventure persistait.

Names: Jack, Jill

Output JSON:
{
"french_summary": "Jack et Jill, frère et sœur d'un charmant village, se sont lancés dans une quête pour chercher de l'eau mais ont rencontré des malheurs en cours de route. Malgré cet incident, leur esprit d'aventure persistait.",
"num_names": 2
}
```

#### Principle 2. Tactic 2: Instruct the model to work out its own solution before rushing to a conclusion

![Principle 2. Tactic 2](classes/src/class02-principel1-tactic2.png)

Instructing the model to reason and work out its own solution before reaching a conclusion can lead to better results, similar to giving the model time to think and allowing it to mimic human judgment in evaluating the correctness of a student's solution.

##### **Example Prompt. Principle 2. Tactic 2.**

The prompt instructs the model to determine if the student's solution is correct by first working out its own solution to the problem, comparing it to the student's solution, and evaluating their correctness. The format includes the question, student's solution, actual solution, agreement status (yes or no), and the student's grade (correct or incorrect). By breaking down the task and giving the model more time to think, it can provide accurate evaluations and assessments.

```plain
Your task is to determine if the student's solution is correct or not.

To solve the problem do the following:
- First, work out your own solution to the problem.
- Then compare your solution to the student's solution and evaluate if the student's solution is correct or not. Don't decide if the student's solution is correct until you have done the problem yourself.

Use the following format:

Question:
"""
question here
"""
Student's solution:
"""
student's solution here
"""
Actual solution:
"""
steps to work out the solution and your solution here
"""
Is the student's solution the same as actual solution just calculated:
"""
yes or no
"""
Student grade:
"""
correct or incorrect
"""

Question:
"""
I'm building a solar power installation and I need help working out the financials.
- Land costs $100 / square foot
- I can buy solar panels for $250 / square foot
- I negotiated a contract for maintenance that will cost me a flat $100k per year, and an additional $10 / square foot
What is the total cost for the first year of operations as a function of the number of square feet.
"""

Student's solution:
"""
Let x be the size of the installation in square feet.
Costs:
1. Land cost: 100x
2. Solar panel cost: 250x
3. Maintenance cost: 100,000 + 100x
Total cost: 100x + 250x + 100,000 + 100x = 450x + 100,000
"""

Actual solution:
```

###### **Model response. Principle 2. Tactic 2.**

```plain
Question:
"""
I'm building a solar power installation and I need help working out the financials.

Land costs $100 / square foot
I can buy solar panels for $250 / square foot
I negotiated a contract for maintenance that will cost me a flat $100k per year, and an additional $10 / square foot
What is the total cost for the first year of operations as a function of the number of square feet?
"""
Student's solution:
"""
Let x be the size of the installation in square feet.
Costs:

Land cost: 100x
Solar panel cost: 250x
Maintenance cost: 100,000 + 100x
Total cost: 100x + 250x + 100,000 + 100x = 450x + 100,000
"""
Actual solution:
"""
To calculate the total cost for the first year of operations, we need to add up the costs for land, solar panels, and maintenance.

Land cost: $100 * x square feet
Solar panel cost: $250 * x square feet
Maintenance cost: $100,000 (flat fee) + $10 * x square feet
Total cost: 100x + 250x + 100,000 + 10x = 360x + 100,000
"""
Is the student's solution the same as the actual solution just calculated?
"""
No
"""

Student grade:
"""
Incorrect
"""
```
