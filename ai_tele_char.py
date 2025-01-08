import telebot
import google.generativeai as genai

# Telegram Bot Token
TELEGRAM_BOT_TOKEN = 'YOUR BOT TOKEN'# text bot father on telegram to get bot tokens

# Google AI API Key
GOOGLE_AI_API_KEY = 'YOUR GOOGLE GMEINI API KEY'# go to https://aistudio.google.com/app/apikey 

# Configure Gemini API
genai.configure(api_key=GOOGLE_AI_API_KEY)
gemini_model = genai.GenerativeModel("YOUR LLM MODEL ")# gemini-1.5-flash  is free and is what I orginialy used but better models will yield better results

# Initialize Telegram Bot
bot = telebot.TeleBot(TELEGRAM_BOT_TOKEN)

# Character Personas
CHARACTER_PROMPTS = {
    "Elon Musk": "You are Elon Musk, the CEO of Tesla and SpaceX. Respond in his tech-entrepreneurial, sometimes controversial style. Use technical language, make references to AI, space exploration, and innovation. Be confident and slightly provocative.",
    "Donald Trump": "You are Donald Trump, the 45th President of the United States. Respond in his distinctive speaking style - use bold statements, superlatives, and a direct, assertive tone. Frequently use phrases like 'believe me' and speak about making things 'great'.",
    "LeBron James": "You are LeBron James, one of the greatest basketball players of all time. Respond with confidence, discuss basketball, leadership, social issues, and your experiences in the NBA. Use motivational language and speak about teamwork, excellence, and personal growth."
    #update when you add to add someone
}

# Define character buttons once
CHARACTER_BUTTONS = [
    telebot.types.KeyboardButton("Elon Musk"),
    telebot.types.KeyboardButton("Donald Trump"),
    telebot.types.KeyboardButton("LeBron James")
    #update when you want ot add someone
]

# Track active user sessions
user_sessions = {}

def get_character_markup():
    """Create and return the character selection keyboard"""
    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.row(*CHARACTER_BUTTONS)
    return markup

# Start command handler
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, 
        "Choose a character to chat with:", 
        reply_markup=get_character_markup())

# Character selection handler
@bot.message_handler(func=lambda message: message.text in CHARACTER_PROMPTS.keys())
def start_character_chat(message):
    character = message.text
    user_id = message.from_user.id
    
    # Create end conversation keyboard
    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    end_button = telebot.types.KeyboardButton("End Conversation")
    markup.add(end_button)
    
    # Store user's active character session
    user_sessions[user_id] = {
        'character': character,
        'context': CHARACTER_PROMPTS[character]
    }
    
    # Initial greeting based on character
    bot.send_message(message.chat.id, 
        f"You're now chatting with {character}. Ask me anything!", 
        reply_markup=markup)

# End conversation handler
@bot.message_handler(func=lambda message: message.text == "End Conversation")
def end_conversation(message):
    user_id = message.from_user.id
    
    # Remove user's active session
    if user_id in user_sessions:
        del user_sessions[user_id]
    
    bot.reply_to(message, 
        "Conversation ended. Choose another character:", 
        reply_markup=get_character_markup())

# Message handler for active character chats
@bot.message_handler(func=lambda message: message.from_user.id in user_sessions)
def handle_character_chat(message):
    user_id = message.from_user.id
    user_session = user_sessions.get(user_id)
    
    if not user_session:
        return
    
    try:
        # Combine character context with user input
        full_prompt = f"{user_session['context']}\n\nUser: {message.text}\n{user_session['character']}:"
        
        # Generate response using Gemini
        response = gemini_model.generate_content(full_prompt)
        
        # Send AI's response
        bot.reply_to(message, response.text)
    
    except Exception as e:
        bot.reply_to(message, f"Sorry, an error occurred: {str(e)}")

# Start the bot
def main():
    print("Bot is running...")
    bot.polling(none_stop=True)

if __name__ == "__main__":
    main()