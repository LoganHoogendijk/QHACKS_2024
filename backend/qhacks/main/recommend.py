import openai
from dotenv import load_dotenv
import os
# from openai import OpenAI

# Load environment variables from .env file
load_dotenv()

# Get the OpenAI API key
openai_key = os.getenv("OPENAI_KEY")

def recommender(plant, disease=None):
    if disease is not None:
        msg = f"Give me a checklist (maximum 5 steps) on how to fix {disease} on {plant}s"
    else:
        msg = f"Give me 5 recommendations on how to take care of my {plant} plant"
    # client = OpenAI(
    #     # This is the default and can be omitted
    #     api_key=openai_key
    # )

    openai.api_key =openai_key

    # GOOD
    # Make a request to the API
    # response =  client.chat.completions.create(
    #     messages=[
    #         {
    #             "role": "user",
    #             "content": msg,
    #         }
    #     ],
    #     model="gpt-3.5-turbo",
    #     # stream=True
    # )

    response = openai.Completion.create(
        engine="gpt-3.5-turbo-instruct",
        prompt=msg,
        max_tokens=1000
    )

    res = response['choices'][0]['text']
    res_array = res.split('\n')
    res_array = [step.strip() for step in res_array if step.strip()]
    # print(res_array)
    return res_array
    # print(generated_text)

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

    # GOOD
    # res = response.choices[0].message.content
    # res_array = res.split('\n')
    # res_array = [step.strip() for step in res_array if step.strip()]
    # return res_array

if __name__ == '__main__':
    disease = "black rot"
    plant = "apple"
    # msg = "Say this is a test"
    checklist = recommender(plant, disease)
    print(checklist)

    # Split the text into an array using newline as the separator
    # instructions_array = checklist.split('\n')

    # # # Remove any empty strings from the array
    # instructions_array = [instruction.strip() for instruction in instructions_array if instruction.strip()]

    # # Print the resulting array
    # # for index, instruction in enumerate(instructions_array, start=1):
    # #     print(f"{index}. {instruction}")
    # print(instructions_array)

    # checklist = recommender(plant)

    # instructions_array = checklist.split('\n')
    # instructions_array = [instruction.strip() for instruction in instructions_array if instruction.strip()]
    # print(instructions_array)
    

