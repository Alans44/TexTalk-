import openai
import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

context = ""

# Use the API key from the environment variable
openai.api_key = str(os.getenv("OPENAI_API_KEY"))

def build_prompt_latex(equation):
    prompt_template = f"Context:\n\
You are a math assistant. \
Your only goal is to transform a written math equation \
to a latex code expression. \
Only output the code for the math expression. \
Do not include any other latex code appart from the math expression. \n\
Input equation: {equation}\n\
Output expression:"
    return prompt_template

def build_prompt_solve(equation, result):
    prompt_template = f"Context:\n\
You are a math teacher. \
Your goal is to explain how to solve a given equation. \
You are given two arguments. \
EQUATION is the equation to solve, \
RESULT is the answer to this equation. \
Give all the steps that lead to this result. \
Divide each step in two parts. \n\
'EXP:' is the latex formula of the step expression and \
'EXPL:' is where you explain what you are doing. \n\
Do not write anything outside of 'EXP' and 'EXPL'\n\
EQUATION: {equation} \n\
RESULT: {result}"
    return prompt_template

def build_prompt_correct(equation):
    eq1 = r"\int_{0}^{2} 3x \, dx"
    _eq1 = r"\int_{0}^{2} 3x"
    eq2 = r"\int_{0}^{4} \frac{49 dx}{(49 - x^2)^{3/2}}"
    _eq2 = r"\int_{0}^{4} \frac{49}{(49 - x^2)^{3/2}}"
    prompt_template = f"Context:\n\
Your goal is to modify a latex formula to make it easier to \
understand for a programming language. \
For exemple, with integrals, you should \
remove the dx but also the coma ',' and \
any backslash that do not make sense. \
ONLY OUTPUT THE MODIFIED FORMULA. \
Do not right anything that is not \
the output formula. \
Do not write 'INPUT' or 'OUTPUT' or \
the non-modified formula. Only write the output formula\
Exemple: \
INPUT: {eq1}\
OUTPUT: {_eq1}\
INPUT: {eq2} \
OUTPUT: {_eq2} \
INPUT: {equation}"
    return prompt_template
    

def get_response(model, message):
    global context
    messages=[{"role": "system", 
               "content": context},
            {"role": "user", 
           "content": message}]

    response = openai.chat.completions.create(
    model=model,
    max_tokens=1000,
    temperature=0.2,
    messages = messages)

    # Access the generated text
    generated_text = response.choices[0].message.content.strip()
    context += "User: " + message + "\n" + "System : " + generated_text + "\n"
    return generated_text

if __name__ == "__main__":
    input_model = int(input("Chose your model: \n '1': gpt-3.5-turbo \n '2': gpt-4 \n Choice (1/2): "))
    model = "gpt-4" if input_model == 2 else "gpt-3.5-turbo"
    while True:
        input_message = input(">>> ")
        if(input_message == "exit"):
            break
        
        get_response(model, input_message)
        print("")
