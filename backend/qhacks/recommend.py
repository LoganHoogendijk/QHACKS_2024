import openai
from dotenv import load_dotenv
import os
from openai import OpenAI

# Load environment variables from .env file
load_dotenv()

# Get the OpenAI API key
openai_key = os.getenv("OPENAI_KEY")

def recommender(disease, plant):
    if disease == "":
        msg = f"Give me 5 recommendations on how to take care of my {plant} plant"
    else:
        msg = f"Give me a checklist (maximum 5 steps) on how to fix {disease} on {plant}s"
    client = OpenAI(
        # This is the default and can be omitted
        api_key=openai_key
    )

    # Make a request to the API
    response =  client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": msg,
            }
        ],
        model="gpt-3.5-turbo",
        # stream=True
    )

    #---------------------------------------
    # checklist = []
    # for chunk in response:
    #     if chunk.choices[0].delta.content is not None:
    #         a = chunk.choices[0].delta.content, end=""
    #         print(chunk.choices[0].delta.content, end="")
    #         # checklist.append(chunk.choices[0].delta.content, end="")
    # return checklist
    #----------------------------------
    # res = ""
    # print(response.choices[0].message.content)
    res = response.choices[0].message.content
    return res

if __name__ == '__main__':
    disease = "black rot"
    plant = "apple"
    # msg = "Say this is a test"
    checklist = recommender(disease, plant)
    # print(checklist)

    # Split the text into an array using newline as the separator
    instructions_array = checklist.split('\n')

    # Remove any empty strings from the array
    instructions_array = [instruction.strip() for instruction in instructions_array if instruction.strip()]

    # Print the resulting array
    # for index, instruction in enumerate(instructions_array, start=1):
    #     print(f"{index}. {instruction}")
    print(instructions_array)

    disease = ""
    checklist = recommender(disease, plant)

    instructions_array = checklist.split('\n')
    instructions_array = [instruction.strip() for instruction in instructions_array if instruction.strip()]
    print(instructions_array)
    

