import os
import sys
from importlib import import_module

import openai
from dotenv import find_dotenv, load_dotenv

_ = load_dotenv(find_dotenv())

openai.api_key = os.getenv("OPENAI_API_KEY")


def get_completion(prompt, model="gpt-3.5-turbo", temperature=0):
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
        temperature=temperature,  # this is the degree of randomness of the model's output
    )
    return response.choices[0].message["content"]


def display_menu():
    """
    Display a command line menu and execute Python scripts based on user input.
    """
    script_files = sorted(os.listdir("classes"))
    script_files = [f for f in script_files if f.endswith(".py")]

    script_names = [os.path.splitext(f)[0].replace("_", " ").title() for f in script_files]

    print("")
    print("ChatGPT prompt engineering for developers course!")
    print("Please select a script class to execute:")
    print("")
    for i, name in enumerate(script_names):
        print(f"{i+1}) {name}")
    print("")

    while True:
        try:
            choice = int(input("Enter the number of the script to execute (0 to exit): "))
            if choice == 0:
                print("Closing the script...")
                sys.exit()
            elif choice in range(1, len(script_files) + 1):
                module_name = os.path.splitext(script_files[choice - 1])[0]
                module = import_module(f"classes.{module_name}")
                if hasattr(module, "execute"):
                    print("")
                    module.execute()
                    print("")
                else:
                    print("The selected script does not have an 'execute' function.")
            else:
                print("Invalid input. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a number.")


if __name__ == "__main__":
    display_menu()
