from google import generativeai as genai 
import dotenv
import os 
import google.generativeai as genai
dotenv.load_dotenv()

genai.configure(api_key=os.environ["AI_API_key"])

generation_config = {
  "temperature": 0.5,
  "top_p": 0.95,
  "top_k": 40,
  "max_output_tokens": 48,
  "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
  model_name="gemini-1.5-pro",
  generation_config=generation_config,
)
chat_session = model.start_chat(
  history=[
    {
      "role": "user",
      "parts": [
        "You are running in someone's system and they need help,   they will tell you what they need and you have to provide them with the command to do it on PowerShell Windows,   Tell them only the command and nothing else,  also make sure the command is safe, Do not provide any special symbols with the command like backticks\n, Here is thir systam info {}.\n",
      ],
    },
    {
      "role": "model",
      "parts": [
        "Okay.  I'm ready.\n",
      ],
    },
    {
      "role": "user",
      "parts": [
        "make me a file called hello_world",
      ],
    },
    {
      "role": "model",
      "parts": [
        "`New-Item -Path \".\\hello_world\" -ItemType File`\n",
      ],
    },
  ]
)

running = True 

while running:
    prompt = input("AISH > ")
    if prompt == "":
        continue
    if prompt == "exit":
        print("Bye :)")
        running = False
    else:
        command = chat_session.send_message(prompt).text.strip("`")
        print(command)
        os.system(f"powershell -c {command}")
        