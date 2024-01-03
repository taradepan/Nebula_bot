import google.generativeai as genai
import PIL.Image
import io
import os
import dotenv
dotenv.load_dotenv()

messages = []

genai.configure(api_key=os.environ.get('GEMINI')) 
def gchat(prompt):
    model = genai.GenerativeModel('gemini-pro')
    if messages and messages[-1]['role'] == "user":
        messages.append(
        {'role':'model',
         'parts': ["there was an error"]}
    )
    messages.append(
    {'role':'user',
     'parts': [prompt]+["(keep the response as short as possible)"]}
)
    response=model.generate_content(messages)
    response.resolve()
    messages.append({'role':'model',
                 'parts':[response.text]})
    print(messages[-2],messages[-1])
    return response.text
    
    

def gimg(prompt, file):
    model = genai.GenerativeModel('gemini-pro-vision')
    file_content = file.download_as_bytearray()
    img = PIL.Image.open(io.BytesIO(file_content))
    prompt = "If user doesn't give any prompt then explain what you see in the image in detail. Prompt: "+str(prompt)
    response = model.generate_content([prompt, img], stream=True)
    response.resolve()
    if messages and messages[-1]['role'] == "user":
        messages.append(
        {'role':'model',
         'parts': ["there was an error"]}
    )
    messages.append(
    {'role':'user',
     'parts': ["image"]}
    )
    messages.append(
    {'role':'model',
     'parts': [response.text]}
    )
    print(response.text)
    return response.text