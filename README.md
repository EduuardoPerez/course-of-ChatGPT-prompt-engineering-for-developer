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
        - [Principle 1: Write clear and specific instructions](#principle-1-write-clear-and-specific-instructions)
        - [Principle 2: Give the model time to "think"](#principle-2-give-the-model-time-to-think)
      - [Principle 1. Tactic 1: Use delimiters to clearly indicate distinct parts of the input](#principle-1-tactic-1-use-delimiters-to-clearly-indicate-distinct-parts-of-the-input)
        - [Example Prompt. Principle 1. Tactic 1](#example-prompt-principle-1-tactic-1)
          - [Example template. Principle 1. Tactic 1](#example-template-principle-1-tactic-1)
          - [Full example. Principle 1. Tactic 1](#full-example-principle-1-tactic-1)
          - [Model response. Principle 1. Tactic 1](#model-response-principle-1-tactic-1)
      - [Principle 1. Tactic 2: Ask for a structured output](#principle-1-tactic-2-ask-for-a-structured-output)
        - [Example Prompt. Principle 1. Tactic 2](#example-prompt-principle-1-tactic-2)
          - [Example template. Principle 1. Tactic 2](#example-template-principle-1-tactic-2)
          - [Full example. Principle 1. Tactic 2](#full-example-principle-1-tactic-2)
          - [Model response. Principle 1. Tactic 2](#model-response-principle-1-tactic-2)
      - [Principle 1. Tactic 3: Ask the model to check whether conditions are satisfied](#principle-1-tactic-3-ask-the-model-to-check-whether-conditions-are-satisfied)
        - [Example Prompt. Principle 1. Tactic 3](#example-prompt-principle-1-tactic-3)
          - [Example template. Principle 1. Tactic 3](#example-template-principle-1-tactic-3)
          - [Full example 1. Principle 1. Tactic 3](#full-example-1-principle-1-tactic-3)
          - [Model response example 1. Principle 1. Tactic 3](#model-response-example-1-principle-1-tactic-3)
          - [Full example 2. Principle 1. Tactic 3](#full-example-2-principle-1-tactic-3)
          - [Model response example 2. Principle 1. Tactic 3](#model-response-example-2-principle-1-tactic-3)
      - [Principle 1. Tactic 4: "Few-shot" prompting](#principle-1-tactic-4-few-shot-prompting)
        - [Example Prompt. Principle 1. Tactic 4](#example-prompt-principle-1-tactic-4)
          - [Example. Principle 1. Tactic 4](#example-principle-1-tactic-4)
          - [Model response. Principle 1. Tactic 4](#model-response-principle-1-tactic-4)
      - [Principle 2. Tactic 1: Specify the steps required to complete a task](#principle-2-tactic-1-specify-the-steps-required-to-complete-a-task)
        - [Example Prompt. Principle 2. Tactic 1](#example-prompt-principle-2-tactic-1)
          - [Example template. Principle 2. Tactic 1](#example-template-principle-2-tactic-1)
          - [Full example 1. Principle 2. Tactic 1](#full-example-1-principle-2-tactic-1)
          - [Model response example 1. Principle 2. Tactic 1](#model-response-example-1-principle-2-tactic-1)
          - [Full example 2. Principle 2. Tactic 1. Ask for output in a specified format](#full-example-2-principle-2-tactic-1-ask-for-output-in-a-specified-format)
          - [Model response example 2. Principle 2. Tactic 1](#model-response-example-2-principle-2-tactic-1)
      - [Principle 2. Tactic 2: Instruct the model to work out its own solution before rushing to a conclusion](#principle-2-tactic-2-instruct-the-model-to-work-out-its-own-solution-before-rushing-to-a-conclusion)
        - [Example Prompt. Principle 2. Tactic 2](#example-prompt-principle-2-tactic-2)
          - [Model response. Principle 2. Tactic 2](#model-response-principle-2-tactic-2)
      - [Model Limitations: Hallucinations](#model-limitations-hallucinations)
        - [Example of an Hallucination of the LLM](#example-of-an-hallucination-of-the-llm)
    - [Class 03: Iterative](#class-03-iterative)
      - [Iterative Prompt Development](#iterative-prompt-development)
        - [Prompt guidelines](#prompt-guidelines)
          - [Expanding the prompt guidelines](#expanding-the-prompt-guidelines)
        - [Example summarizing a fact sheet for a chair for a marketing team](#example-summarizing-a-fact-sheet-for-a-chair-for-a-marketing-team)
          - [1st prompt: without any improvement](#1st-prompt-without-any-improvement)
          - [Model response. 1st prompt: without any improvement](#model-response-1st-prompt-without-any-improvement)
          - [2nd prompt: limiting the response](#2nd-prompt-limiting-the-response)
          - [Model response. 2nd prompt: limiting the response](#model-response-2nd-prompt-limiting-the-response)
          - [3rd prompt: specifying the tone of the response](#3rd-prompt-specifying-the-tone-of-the-response)
          - [Model response. 3rd prompt: specifying the tone of the response](#model-response-3rd-prompt-specifying-the-tone-of-the-response)
          - [4th prompt: asking to add specific details](#4th-prompt-asking-to-add-specific-details)
          - [Model response. 4th prompt: asking to add specific details](#model-response-4th-prompt-asking-to-add-specific-details)
          - [5th prompt: asking to organize the information](#5th-prompt-asking-to-organize-the-information)
          - [Model response. 5th prompt: asking to organize the information](#model-response-5th-prompt-asking-to-organize-the-information)
      - [Conclusion of iterative Prompt Development](#conclusion-of-iterative-prompt-development)
    - [Class 04: summarizing](#class-04-summarizing)
      - [Techniques to summarize text](#techniques-to-summarize-text)
        - [Summarize with a word/sentence/character limit](#summarize-with-a-wordsentencecharacter-limit)
          - [Model response. Summarize with a word/sentence/character limit](#model-response-summarize-with-a-wordsentencecharacter-limit)
        - [Summarize focusing on a specific objective](#summarize-focusing-on-a-specific-objective)
          - [Example prompt 1. Summarize with a focus on shipping and delivery](#example-prompt-1-summarize-with-a-focus-on-shipping-and-delivery)
          - [Model response. Example prompt 1. Summarize with a focus on shipping and delivery](#model-response-example-prompt-1-summarize-with-a-focus-on-shipping-and-delivery)
          - [Example prompt 2. Summarize with a focus on price and value](#example-prompt-2-summarize-with-a-focus-on-price-and-value)
          - [Model response. Example prompt 2. Summarize with a focus on price and value](#model-response-example-prompt-2-summarize-with-a-focus-on-price-and-value)
        - [Try "extract" instead of "summarize"](#try-extract-instead-of-summarize)
          - [Model response. Try "extract" instead of "summarize"](#model-response-try-extract-instead-of-summarize)

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

##### Principle 1: Write clear and specific instructions

  The first principle emphasizes the importance of providing clear and specific instructions to guide the model towards the desired output, highlighting that longer prompts can often offer more clarity and context for generating detailed and relevant responses.

##### Principle 2: Give the model time to "think"

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

##### Example Prompt. Principle 1. Tactic 1

###### Example template. Principle 1. Tactic 1

```plain
Summarize the text delimited by triple backticks into a single sentence.
```text```
```

###### Full example. Principle 1. Tactic 1

```plain
Summarize the text delimited by triple backticks into a single sentence.
```You should express what you want a model to do by providing instructions that are as clear and specific as you can possibly make them. This will guide the model towards the desired output, and reduce the chances of receiving irrelevant or incorrect responses. Don't confuse writing a clear prompt with writing a short prompt. In many cases, longer prompts provide more clarity and context for the model, which can lead to more detailed and relevant outputs.```
```

###### Model response. Principle 1. Tactic 1

```plain
Clear and specific instructions should be provided to guide a model towards the desired output, and longer prompts can provide more clarity and context for the model, leading to more detailed and relevant outputs.
```

#### Principle 1. Tactic 2: Ask for a structured output

![Principle 1. Tactic 2](classes/src/class02-principel1-tactic2.png)

To facilitate parsing model outputs, asking for a structured output like HTML or JSON can be useful. For example, requesting a list of three fictional book titles along with their authors and genres in JSON format allows easy conversion into a dictionary or list in Python.

##### Example Prompt. Principle 1. Tactic 2

###### Example template. Principle 1. Tactic 2

```plain
Generate a list of {some requirement}.
Provide them in JSON format with the following keys:
{relevant keys}.
```

###### Full example. Principle 1. Tactic 2

```plain
Generate a list of three made-up book titles along with their authors and genres.
Provide them in JSON format with the following keys: book_id, title, author, genre.
```

###### Model response. Principle 1. Tactic 2

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

##### Example Prompt. Principle 1. Tactic 3

###### Example template. Principle 1. Tactic 3

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

###### Full example 1. Principle 1. Tactic 3

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

###### Model response example 1. Principle 1. Tactic 3

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

###### Full example 2. Principle 1. Tactic 3

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

###### Model response example 2. Principle 1. Tactic 3

```plain
No steps provided.
```

#### Principle 1. Tactic 4: "Few-shot" prompting

![Principle 1. Tactic 4](classes/src/class02-principel1-tactic4.png)

The final tactic for this principle is using few-shot prompting, which involves providing examples of successful task executions before asking the model to perform the desired task.

##### Example Prompt. Principle 1. Tactic 4

The prompt instructs the model to answer in a consistent style by providing examples of a conversation between a child and a grandparent. The model is asked to teach about patience and then about resilience, and it responds in a similar tone, using metaphors to convey the desired message.

###### Example. Principle 1. Tactic 4

```plain
Your task is to answer in a consistent style.
<child>: Teach me about patience.

<grandparent>: The river that carves the deepest valley flows from a modest spring; the grandest symphony originates from a single note; the most intricate tapestry begins with a solitary thread.

<child>: Teach me about resilience.
```

###### Model response. Principle 1. Tactic 4

```plain
<grandparent>: Resilience is like a tree that bends with the wind but never breaks. It is the ability to bounce back from adversity and keep moving forward, even when things get tough. Just like a tree that grows stronger with each storm it weathers, resilience is a quality that can be developed and strengthened over time.
```

#### Principle 2. Tactic 1: Specify the steps required to complete a task

![Principle 2. Tactic 1](classes/src/class02-principle2-tactic1.png)

The first tactic of the second principle, is to provide specific instructions for a task, such as summarizing a text, translating it into French, listing names, and outputting a JSON object with specific keys, while separating the answers with line breaks.

##### Example Prompt. Principle 2. Tactic 1

###### Example template. Principle 2. Tactic 1

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

###### Full example 1. Principle 2. Tactic 1

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

###### Model response example 1. Principle 2. Tactic 1

```plain
Two siblings, Jack and Jill, go on a quest to fetch water from a well on a hilltop, but misfortune strikes and they both tumble down the hill, returning home slightly battered but with their adventurous spirits undimmed.

Deux frères et sœurs, Jack et Jill, partent en quête d'eau d'un puits sur une colline, mais un malheur frappe et ils tombent tous les deux de la colline, rentrant chez eux légèrement meurtris mais avec leurs esprits aventureux intacts. Noms: Jack, Jill.

{
  "french_summary": "Deux frères et sœurs, Jack et Jill, partent en quête d'eau d'un puits sur une colline, mais un malheur frappe et ils tombent tous les deux de la colline, rentrant chez eux légèrement meurtris mais avec leurs esprits aventureux intacts.",
  "num_names": 2,
}
```

###### Full example 2. Principle 2. Tactic 1. Ask for output in a specified format

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

###### Model response example 2. Principle 2. Tactic 1

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

##### Example Prompt. Principle 2. Tactic 2

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

###### Model response. Principle 2. Tactic 2

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

#### Model Limitations: Hallucinations

![Model Limitations: Hallucinations](classes/src/class02-model-limitations-hallucinations.png)

To mitigate the issue of model limitations and prevent the generation of fabricated ideas or "hallucinations," it is important to consider the model's knowledge boundaries when developing applications with large language models (LLMs). One approach to reduce hallucinations is to ask the model to provide answers based on relevant quotes from a text source, ensuring that the generated answers can be traced back to their original context.

##### Example of an Hallucination of the LLM

In an example illustrating model hallucination, the model generates a fabricated description for a fictional product name, despite referencing a real toothbrush company.

**Prompt:**

```plain
Tell me about AeroGlide UltraSlim Smart Toothbrush by Boie
```

Boie is a real company, but, the product name is not real.

**Model response:**

```plain
The AeroGlide UltraSlim Smart Toothbrush by Boie is a high-tech toothbrush that uses advanced sonic technology to provide a deep and thorough clean. It features a slim and sleek design that makes it easy to hold and maneuver, and it comes with a range of smart features that help you optimize your brushing routine.

One of the key features of the AeroGlide UltraSlim Smart Toothbrush is its advanced sonic technology, which uses high-frequency vibrations to break up plaque and bacteria on your teeth and gums. This technology is highly effective at removing even the toughest stains and buildup, leaving your teeth feeling clean and refreshed.

In addition to its sonic technology, the AeroGlide UltraSlim Smart Toothbrush also comes with a range of smart features that help you optimize your brushing routine. These include a built-in timer that ensures you brush for the recommended two minutes, as well as a pressure sensor that alerts you if you're brushing too hard.

Overall, the AeroGlide UltraSlim Smart Toothbrush by Boie is a highly advanced and effective toothbrush that is perfect for anyone looking to take their oral hygiene to the next level. With its advanced sonic technology and smart features, it provides a deep and thorough clean that leaves your teeth feeling fresh and healthy.
```

The model is giving us a pretty realistic sounding description of a fictitious product. This can be potentially misleading, highlighting the importance of employing techniques discussed until now to mitigate such risks.

### Class 03: Iterative

The process of building applications with large language models (LLMs) involves iterative improvement of prompts to find what works best for the intended task, as the initial prompt rarely yields optimal results. The key is to focus on refining the prompt through an effective process rather than relying on the first attempt, as the ultimate goal is to find prompts that are well-suited for the application at hand.

#### Iterative Prompt Development

![Iterative Prompt Development](classes/src/class03-iterative-prompt-development.png)

When developing prompts for applications using a LLM, it's beneficial to follow an iterative process. Similar to the development of machine learning models, you start with an idea, implement it by writing the code and obtaining data, train the model, and analyze the experimental results. Through this analysis, you can identify areas of improvement, adjust your approach or problem statement, modify the implementation, and run further experiments. The process continues iteratively until you achieve an effective prompt that works well for your specific application. The focus should be on refining the prompt based on the feedback received rather than seeking a single "perfect" prompt. Having a well-defined process for developing suitable prompts is key for successful application development with large language models (LLMs).

##### Prompt guidelines

- Be clear and specific
- Analyze why result does not give desired output.
- Refine the idea and the prompt
- Repeat

###### Expanding the prompt guidelines

- Prompt development for large language models (LLMS) is an iterative process.
- The initial prompt can be refined based on the desired length or specific characteristics of the output.
- Modifying the prompt allows for control over the output and tailoring it to the intended audience.
- Including additional instructions in the prompt can yield more specific results, such as generating tables or formatting output.
- The process of prompt development involves testing different variations and refining the prompt based on the desired outcomes.
- Evaluating prompts against a larger set of examples can be useful for mature applications to assess performance and drive prompt improvement.

##### Example summarizing a fact sheet for a chair for a marketing team

Text to summarize

```plain
OVERVIEW
- Part of a beautiful family of mid-century inspired office furniture,
including filing cabinets, desks, bookcases, meeting tables, and more.
- Several options of shell color and base finishes.
- Available with plastic back and front upholstery (SWC-100)
or full upholstery (SWC-110) in 10 fabric and 6 leather options.
- Base finish options are: stainless steel, matte black,
gloss white, or chrome.
- Chair is available with or without armrests.
- Suitable for home or business settings.
- Qualified for contract use.

CONSTRUCTION
- 5-wheel plastic coated aluminum base.
- Pneumatic chair adjust for easy raise/lower action.

DIMENSIONS
- WIDTH 53 CM | 20.87”
- DEPTH 51 CM | 20.08”
- HEIGHT 80 CM | 31.50”
- SEAT HEIGHT 44 CM | 17.32”
- SEAT DEPTH 41 CM | 16.14”

OPTIONS
- Soft or hard-floor caster options.
- Two choices of seat foam densities:
medium (1.8 lb/ft3) or high (2.8 lb/ft3)
- Armless or 8 position PU armrests

MATERIALS
SHELL BASE GLIDER
- Cast Aluminum with modified nylon PA6/PA66 coating.
- Shell thickness: 10 mm.
SEAT
- HD36 foam

COUNTRY OF ORIGIN
- Italy
```

###### 1st prompt: without any improvement

This is the first prompt without specify anything special, just to get the LLM response

```plain
Your task is to help a marketing team create a
description for a retail website of a product based
on a technical fact sheet.

Write a product description based on the information
provided in the technical specifications delimited by
triple backticks.

Technical specifications:
```OVERVIEW
- Part of a beautiful family of mid-century inspired office furniture,
including filing cabinets, desks, bookcases, meeting tables, and more.
- Several options of shell color and base finishes.
- Available with plastic back and front upholstery (SWC-100)
or full upholstery (SWC-110) in 10 fabric and 6 leather options.
- Base finish options are: stainless steel, matte black,
gloss white, or chrome.
- Chair is available with or without armrests.
- Suitable for home or business settings.
- Qualified for contract use.

CONSTRUCTION
- 5-wheel plastic coated aluminum base.
- Pneumatic chair adjust for easy raise/lower action.

DIMENSIONS
- WIDTH 53 CM | 20.87”
- DEPTH 51 CM | 20.08”
- HEIGHT 80 CM | 31.50”
- SEAT HEIGHT 44 CM | 17.32”
- SEAT DEPTH 41 CM | 16.14”

OPTIONS
- Soft or hard-floor caster options.
- Two choices of seat foam densities:
medium (1.8 lb/ft3) or high (2.8 lb/ft3)
- Armless or 8 position PU armrests

MATERIALS
SHELL BASE GLIDER
- Cast Aluminum with modified nylon PA6/PA66 coating.
- Shell thickness: 10 mm.
SEAT
- HD36 foam

COUNTRY OF ORIGIN
- Italy```
```

###### Model response. 1st prompt: without any improvement

```plain
Introducing our stunning mid-century inspired office chair, the perfect addition to any home or business setting. Part of a beautiful family of office furniture, including filing cabinets, desks, bookcases, meeting tables, and more, this chair is available in several options of shell color and base finishes to suit your style. Choose from plastic back and front upholstery (SWC-100) or full upholstery (SWC-110) in 10 fabric and 6 leather options.

The chair is constructed with a 5-wheel plastic coated aluminum base and features a pneumatic chair adjust for easy raise/lower action. It is available with or without armrests and is qualified for contract use. The base finish options are stainless steel, matte black, gloss white, or chrome.

Measuring at a width of 53 cm, depth of 51 cm, and height of 80 cm, with a seat height of 44 cm and seat depth of 41 cm, this chair is designed for ultimate comfort. You can also choose between soft or hard-floor caster options and two choices of seat foam densities: medium (1.8 lb/ft3) or high (2.8 lb/ft3). The armrests are available in either an armless or 8 position PU option.

The materials used in the construction of this chair are of the highest quality. The shell base glider is made of cast aluminum with modified nylon PA6/PA66 coating and has a shell thickness of 10 mm. The seat is made of HD36 foam, ensuring maximum comfort and durability.

This chair is made in Italy and is the perfect combination of style and functionality. Upgrade your workspace with our mid-century inspired office chair today!
```

###### 2nd prompt: limiting the response

Limit the number of words/sentences/characters, to solve the first issue we got, the text is too long.

```plain
Your task is to help a marketing team create a
description for a retail website of a product based
on a technical fact sheet.

Write a product description based on the information
provided in the technical specifications delimited by
triple backticks.

Use at most 50 words.

Technical specifications:
```OVERVIEW
- Part of a beautiful family of mid-century inspired office furniture,
including filing cabinets, desks, bookcases, meeting tables, and more.
- Several options of shell color and base finishes.
- Available with plastic back and front upholstery (SWC-100)
or full upholstery (SWC-110) in 10 fabric and 6 leather options.
- Base finish options are: stainless steel, matte black,
gloss white, or chrome.
- Chair is available with or without armrests.
- Suitable for home or business settings.
- Qualified for contract use.

CONSTRUCTION
- 5-wheel plastic coated aluminum base.
- Pneumatic chair adjust for easy raise/lower action.

DIMENSIONS
- WIDTH 53 CM | 20.87”
- DEPTH 51 CM | 20.08”
- HEIGHT 80 CM | 31.50”
- SEAT HEIGHT 44 CM | 17.32”
- SEAT DEPTH 41 CM | 16.14”

OPTIONS
- Soft or hard-floor caster options.
- Two choices of seat foam densities:
medium (1.8 lb/ft3) or high (2.8 lb/ft3)
- Armless or 8 position PU armrests

MATERIALS
SHELL BASE GLIDER
- Cast Aluminum with modified nylon PA6/PA66 coating.
- Shell thickness: 10 mm.
SEAT
- HD36 foam

COUNTRY OF ORIGIN
- Italy```
```

###### Model response. 2nd prompt: limiting the response

```plain
Introducing our mid-century inspired office chair, perfect for home or business settings. Available in a range of shell colors and base finishes, with or without armrests. Choose from 10 fabric and 6 leather options for full or plastic upholstery. With a 5-wheel base and pneumatic chair adjust, it's both stylish and functional. Made in Italy.
```

###### 3rd prompt: specifying the tone of the response

Ask it to focus on the aspects that are relevant to the intended audience, to solve the second issue we got, the text is focuses on the wrong details.

```plain
Your task is to help a marketing team create a
description for a retail website of a product based
on a technical fact sheet.

Write a product description based on the information
provided in the technical specifications delimited by
triple backticks.

The description is intended for furniture retailers,
so should be technical in nature and focus on the
materials the product is constructed from.

Use at most 50 words.

Technical specifications:
```OVERVIEW
- Part of a beautiful family of mid-century inspired office furniture,
including filing cabinets, desks, bookcases, meeting tables, and more.
- Several options of shell color and base finishes.
- Available with plastic back and front upholstery (SWC-100)
or full upholstery (SWC-110) in 10 fabric and 6 leather options.
- Base finish options are: stainless steel, matte black,
gloss white, or chrome.
- Chair is available with or without armrests.
- Suitable for home or business settings.
- Qualified for contract use.

CONSTRUCTION
- 5-wheel plastic coated aluminum base.
- Pneumatic chair adjust for easy raise/lower action.

DIMENSIONS
- WIDTH 53 CM | 20.87”
- DEPTH 51 CM | 20.08”
- HEIGHT 80 CM | 31.50”
- SEAT HEIGHT 44 CM | 17.32”
- SEAT DEPTH 41 CM | 16.14”

OPTIONS
- Soft or hard-floor caster options.
- Two choices of seat foam densities:
medium (1.8 lb/ft3) or high (2.8 lb/ft3)
- Armless or 8 position PU armrests

MATERIALS
SHELL BASE GLIDER
- Cast Aluminum with modified nylon PA6/PA66 coating.
- Shell thickness: 10 mm.
SEAT
- HD36 foam

COUNTRY OF ORIGIN
- Italy```
```

###### Model response. 3rd prompt: specifying the tone of the response

```plain
Introducing our mid-century inspired office chair, perfect for both home and business settings. With a range of shell colors and base finishes, including stainless steel and matte black, this chair is available with or without armrests. The 5-wheel plastic coated aluminum base and pneumatic chair adjust make it easy to move and adjust to your desired height. Made with high-quality materials, including a cast aluminum shell and HD36 foam seat, this chair is built to last.
```

###### 4th prompt: asking to add specific details

Ask it to add specific details from the text provided

```plain
Your task is to help a marketing team create a
description for a retail website of a product based
on a technical fact sheet.

Write a product description based on the information
provided in the technical specifications delimited by
triple backticks.

The description is intended for furniture retailers,
so should be technical in nature and focus on the
materials the product is constructed from.

At the end of the description, include every 7-character
Product ID in the technical specification.

Use at most 50 words.

Technical specifications:
```OVERVIEW
- Part of a beautiful family of mid-century inspired office furniture,
including filing cabinets, desks, bookcases, meeting tables, and more.
- Several options of shell color and base finishes.
- Available with plastic back and front upholstery (SWC-100)
or full upholstery (SWC-110) in 10 fabric and 6 leather options.
- Base finish options are: stainless steel, matte black,
gloss white, or chrome.
- Chair is available with or without armrests.
- Suitable for home or business settings.
- Qualified for contract use.

CONSTRUCTION
- 5-wheel plastic coated aluminum base.
- Pneumatic chair adjust for easy raise/lower action.

DIMENSIONS
- WIDTH 53 CM | 20.87”
- DEPTH 51 CM | 20.08”
- HEIGHT 80 CM | 31.50”
- SEAT HEIGHT 44 CM | 17.32”
- SEAT DEPTH 41 CM | 16.14”

OPTIONS
- Soft or hard-floor caster options.
- Two choices of seat foam densities:
medium (1.8 lb/ft3) or high (2.8 lb/ft3)
- Armless or 8 position PU armrests

MATERIALS
SHELL BASE GLIDER
- Cast Aluminum with modified nylon PA6/PA66 coating.
- Shell thickness: 10 mm.
SEAT
- HD36 foam

COUNTRY OF ORIGIN
- Italy```
```

###### Model response. 4th prompt: asking to add specific details

```plain
Introducing our mid-century inspired office chair, perfect for home or business settings. With a range of shell colors and base finishes, and the option of plastic or full upholstery, this chair is both stylish and comfortable. Constructed with a 5-wheel plastic coated aluminum base and pneumatic chair adjust, it's also practical. Available with or without armrests and suitable for contract use. Product ID: SWC-100, SWC-110.
```

###### 5th prompt: asking to organize the information

Ask it to extract information and organize it in a table, it could also be requested to organize the information in a JSON format, or any other useful format for your case. This is intending to solved the third issue we got, the description needs a table of dimensions.

```plain
Your task is to help a marketing team create a
description for a retail website of a product based
on a technical fact sheet.

Write a product description based on the information
provided in the technical specifications delimited by
triple backticks.

The description is intended for furniture retailers,
so should be technical in nature and focus on the
materials the product is constructed from.

At the end of the description, include every 7-character
Product ID in the technical specification.

After the description, include a table that gives the
product's dimensions. The table should have two columns.
In the first column include the name of the dimension.
In the second column include the measurements in inches only.

Give the table the title 'Product Dimensions'.

Format everything as HTML that can be used in a website.
Place the description in a <div> element.

Technical specifications:
```OVERVIEW
- Part of a beautiful family of mid-century inspired office furniture,
including filing cabinets, desks, bookcases, meeting tables, and more.
- Several options of shell color and base finishes.
- Available with plastic back and front upholstery (SWC-100)
or full upholstery (SWC-110) in 10 fabric and 6 leather options.
- Base finish options are: stainless steel, matte black,
gloss white, or chrome.
- Chair is available with or without armrests.
- Suitable for home or business settings.
- Qualified for contract use.

CONSTRUCTION
- 5-wheel plastic coated aluminum base.
- Pneumatic chair adjust for easy raise/lower action.

DIMENSIONS
- WIDTH 53 CM | 20.87”
- DEPTH 51 CM | 20.08”
- HEIGHT 80 CM | 31.50”
- SEAT HEIGHT 44 CM | 17.32”
- SEAT DEPTH 41 CM | 16.14”

OPTIONS
- Soft or hard-floor caster options.
- Two choices of seat foam densities:
medium (1.8 lb/ft3) or high (2.8 lb/ft3)
- Armless or 8 position PU armrests

MATERIALS
SHELL BASE GLIDER
- Cast Aluminum with modified nylon PA6/PA66 coating.
- Shell thickness: 10 mm.
SEAT
- HD36 foam

COUNTRY OF ORIGIN
- Italy```
```

###### Model response. 5th prompt: asking to organize the information

```plain
<div>
  <h2>Mid-Century Inspired Office Chair</h2>
  <p>
    Introducing our mid-century inspired office chair, part of a beautiful family of office furniture that includes filing cabinets, desks, bookcases, meeting tables, and more. This chair is available in several options of shell color and base finishes, allowing you to customize it to your liking. You can choose between plastic back and front upholstery or full upholstery in 10 fabric and 6 leather options. The base finish options are stainless steel, matte black, gloss white, or chrome. The chair is also available with or without armrests, making it suitable for both home and business settings. Plus, it's qualified for contract use, so you can trust its durability and quality.
  </p>
  <h3>Construction</h3>
  <p>
    The chair features a 5-wheel plastic coated aluminum base and a pneumatic chair adjust for easy raise/lower action. You can choose between soft or hard-floor caster options and two choices of seat foam densities: medium (1.8 lb/ft3) or high (2.8 lb/ft3). The chair is also available with armless or 8 position PU armrests.
  </p>
  <h3>Materials</h3>
  <p>
    The shell base glider is made of cast aluminum with modified nylon PA6/PA66 coating, and the shell thickness is 10 mm. The seat is made of HD36 foam, ensuring comfort and support.
  </p>
  <h3>Product Dimensions</h3>
  <table>
  <tr>
      <td>Width</td>
      <td>53 cm | 20.87"</td>
  </tr>
  <tr>
      <td>Depth</td>
      <td>51 cm | 20.08"</td>
  </tr>
  <tr>
      <td>Height</td>
      <td>80 cm | 31.50"</td>
  </tr>
  <tr>
      <td>Seat Height</td>
      <td>44 cm | 17.32"</td>
  </tr>
  <tr>
      <td>Seat Depth</td>
      <td>41 cm | 16.14"</td>
  </tr>
  </table>
  <h3>Product ID</h3>
  <p>SWC-100, SWC-110</p>
</div>
```

This is how the HTML model response looks like:
![HTML model response](classes/src/class03-HMTL-model-response.png)

#### Conclusion of iterative Prompt Development

![Conclusion of iterative Prompt Development](classes/src/class03-iterative-prompt-development-conclusion.png)

Whe we are talking about the iterative process of prompt development, we should emphasizes the importance of trying different approaches, evaluating their effectiveness, and refining instructions to achieve the desired results. The key to being an effective prompt engineer lies in having a good process for developing prompts tailored to the specific application. While initially, one example may suffice, for more sophisticated applications, multiple examples and iterative development are recommended. Evaluating prompts against a larger set of examples becomes valuable in the later stages of application development to assess average or worst-case performance and drive incremental prompt improvement.

### Class 04: summarizing

Large language models like chatGPT can be used to summarize text, allowing users to quickly understand the content of articles and read more efficiently, either through the web interface or programmatically.

#### Techniques to summarize text

##### Summarize with a word/sentence/character limit

Request to summarize limiting by the quantity of words, sentence or character.

```plain
Your task is to generate a short summary of a product review from an ecommerce site.

Summarize the review below, delimited by triple backticks, in at most 30 words.

Review:
```Got this panda plush toy for my daughter's birthday, who loves it and takes it everywhere. It's soft and super cute, and its face has a friendly look. It's a bit small for what I paid though. I think there might be other options that are bigger for the same price. It arrived a day earlier than expected, so I got to play with it myself before I gave it to her.```
```

###### Model response. Summarize with a word/sentence/character limit

```plain
Soft and cute panda plush toy loved by daughter, but a bit small for the price. Arrived early.
```

##### Summarize focusing on a specific objective

Modifying the prompt when creating a summary allows for generating more targeted and applicable summaries based on specific purposes, such as providing feedback to different departments within a business. By adjusting the prompt to focus on aspects related to shipping or pricing, the generated summaries highlight relevant information for those departments, providing more specific insights.

Request to get focus on specific details.

###### Example prompt 1. Summarize with a focus on shipping and delivery

```plain
Your task is to generate a short summary of a product review from an ecommerce site to give feedback to the Shipping department.

Summarize the review below, delimited by triple backticks, in at most 30 words, and focusing on any aspects that mention shipping and delivery of the product.

Review:
```Got this panda plush toy for my daughter's birthday, who loves it and takes it everywhere. It's soft and super cute, and its face has a friendly look. It's a bit small for what I paid though. I think there might be other options that are bigger for the same price. It arrived a day earlier than expected, so I got to play with it myself before I gave it to her.```
```

###### Model response. Example prompt 1. Summarize with a focus on shipping and delivery

```plain
The panda plush toy arrived a day earlier than expected, but the customer felt it was a bit small for the price paid.
```

###### Example prompt 2. Summarize with a focus on price and value

```plain
Your task is to generate a short summary of a product review from an ecommerce site to give feedback to the Shipping department.

Summarize the review below, delimited by triple backticks, in at most 30 words, and focusing on any aspects that are relevant to the price and perceived value.

Review:
```Got this panda plush toy for my daughter's birthday, who loves it and takes it everywhere. It's soft and super cute, and its face has a friendly look. It's a bit small for what I paid though. I think there might be other options that are bigger for the same price. It arrived a day earlier than expected, so I got to play with it myself before I gave it to her.```
```

###### Model response. Example prompt 2. Summarize with a focus on price and value

```plain
The panda plush toy is soft, cute, and loved by the recipient, but the price may be too high for its size.
```

##### Try "extract" instead of "summarize"

By modifying the prompt to extract relevant information instead of summarizing it, a more focused output can be generated. For example, when tasked with providing feedback to the shipping department, the prompt can be adjusted to extract specific details, such as the product arriving a day earlier than expected, without including additional information that may be useful for a general summary but less relevant to the shipping department's specific needs.

```plain
Your task is to extract relevant information from a product review from an ecommerce site to give feedback to the Shipping department.

From the review below, delimited by triple quotes extract the information relevant to shipping and delivery. Limit to 30 words.

Review:
```Got this panda plush toy for my daughter's birthday, who loves it and takes it everywhere. It's soft and super cute, and its face has a friendly look. It's a bit small for what I paid though. I think there might be other options that are bigger for the same price. It arrived a day earlier than expected, so I got to play with it myself before I gave it to her.```
```

###### Model response. Try "extract" instead of "summarize"

```plain
The product arrived a day earlier than expected.
```
