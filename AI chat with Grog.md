# 🤖 Project: Chat AI with Groq API

![Groq Logo](https://cdn.asp.events/CLIENT_Informa__AADDE28D_5056_B739_5481D63BF875B0DF/sites/ai-summit-NY-2022/media/libraries/exhibitors/0b84f0a6-3bbd-11ee-bff906bd0f937899-cover-image.png/fit-in/1500x9999/filters:no_upscale())

Welcome, Students! 🐍 In this project, you'll create a chat application that utilizes the Groq API to generate AI responses. Instead of a graphical interface, you will modify the existing code to run directly in your IDE and display responses in the console. Let's dive in! 🚀

### Purpose of This Project

By completing this project, you will:
- Learn how to connect to and use an external API in Python.
- Replace a GUI with console-based interaction.
- Improve your understanding of error handling in API requests.
- Work with your own API key, gaining hands-on experience in API integration.

### Get Your API Key

To use the Groq API, you need an API key. Follow these steps:
1. Go to the [Groq website](https://groq.com/) and sign up for an account. 🌐
2. Once registered, retrieve your API key from your account dashboard. Keep this key secure!

### Modify the Provided Code

Below is the original code modified for console interaction. Replace the existing Tkinter code with the following:

```python
from groq import Groq

# Initialize Groq API client
client = Groq(
    api_key='YOUR_API_KEY_HERE',  # Replace with your own API key
)

# Function to get chat completion from Groq API
def get_ai_response(user_input):
    try:
        chat_completion = client.chat.completions.create(
            messages=[
                {"role": "user", "content": user_input}
            ],
            model="llama3-8b-8192",
        )
        return chat_completion.choices[0].message.content
    except Exception as e:
        return f"Error: {e}"

# Main loop for user input
while True:
    user_input = input("You: ")
    if user_input.lower() in ["exit", "quit"]:
        print("Goodbye! 👋")
        break
    response = get_ai_response(user_input)
    print("AI: " + response)
```

### Task Requirements
1. Replace `'YOUR_API_KEY_HERE'` with your actual Groq API key.
2. Run the modified code in your IDE and interact with the AI via console input.
3. Implement error handling to manage invalid inputs gracefully.

### Additional Features to Implement
- **Chat History**: Save chat history to a text file.
- **Multi-turn Conversations**: Allow for a back-and-forth conversation without restarting the program.
- **Different AI Models**: Provide an option to select different models from Groq.

### Additional Resources
- [Groq API Documentation](https://console.groq.com/docs/quickstart)
- [Python Documentation](https://docs.python.org/3/)

### Points Breakdown
| Task                                      | Points |
|-------------------------------------------|--------|
| Successful API integration                | 30     |
| Error handling implementation              | 20     |
| Console-based interaction                 | 20     |
| Additional features implemented            | 30     |

---

This project is an exciting way to enhance your coding skills and learn about API integration! Get creative and have fun! 🎉💻

Happy Coding! 🚀🌟

--- 
