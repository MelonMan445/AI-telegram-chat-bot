Telegram AI Character Bot
---
This is a Python-based Telegram bot that lets users chat with AI-generated personas of various characters, such as Elon Musk, Donald Trump, and LeBron James. Users can interact with these characters and experience their distinct conversational styles.



---
Features:
---

- Chat with Famous Personas: Engage with predefined personas styled to emulate the conversational patterns of well-known figures.
- Customizable: Add new characters and define their unique personalities easily.
- Powered by Google Gemini AI: Leverages Google's Generative AI for dynamic and context-aware responses.
---


You need these packages :
---
- telebot
- google.generativeai

Run pip install pyTelegramBotAPI google-generativeai

---
Get token:
---
- A Telegram bot token from BotFather. text this bot on telegram https://telegram.me/BotFather 
- A Google Gemini API key from Google AI Studio. https://aistudio.google.com/app/apikey

---
Replace placeholders in the script with your credentials:
---
- YOUR BOT TOKEN: Your Telegram bot token.
- YOUR GOOGLE GMEINI API KEY: Your Google Gemini API key.
- YOUR LLM MODEL: The model you want to use (e.g., gemini-1.5-flash).

---
Running the Bot
---

Run the script and text the bot (very easy)

---
Customization
---
1. Update the CHARACTER_PROMPTS dictionary with the new character's name and persona description. For example:

"Albert Einstein": "You are Albert Einstein, a genius physicist. Respond with scientific insight and profound wisdom."

2. Add a button for the new character in the CHARACTER_BUTTONS list:

telebot.types.KeyboardButton("Albert Einstein")

---


Feel free to use this script as-is, customize it, or integrate it into larger projects.

