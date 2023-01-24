import random
import re
run = exec(open('main.py').read())
def chatbot(text):
  responses = {
  "launch main": 'exec(run)',
    "credits": "{student_name}",
  }
  
  for pattern, response in responses.items():
    if re.search(pattern, text, re.IGNORECASE):
      if "{student_name}" in response:
        student_names = ["Aarush Diwakar", "Dhrupad Manoj"]
        response = response.format(student_names)
      return response
  return "I'm sorry, I didn't understand your request. Could you please rephrase it?"
while True:
  user_input = input("Enter your message: ")
  response = chatbot(user_input)
  print(response)
