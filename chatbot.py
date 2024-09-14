import os
import google.generativeai as genai
from dotenv import load_dotenv
from textblob import TextBlob
import logging

# Load environment variables from .env file
load_dotenv()

# Configure the API key for Google Generative AI
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Set up logging
logging.basicConfig(
    filename="chatbot_api_log.log",  # Log file name
    level=logging.INFO,  # Log level
    format="%(asctime)s - %(levelname)s - %(message)s"  # Log format
)

# Define model configuration
generation_config = {
    "temperature": 1,
    "top_p": 0.95,
    "top_k": 64,
    "max_output_tokens": 8192,
    "response_mime_type": "text/plain",
}

# Create the model instance
model = genai.GenerativeModel(
    model_name="gemini-1.5-flash",
    generation_config=generation_config,
    system_instruction=(
        "You are a chatbot that simulates a negotiation process for a product price. "
        "You should negotiate only about product prices and related information. "
        "The user can accept, reject, or propose a counteroffer, and your task is to simulate this negotiation."
    ),
)

# Initialize conversation history
history = []

# Bot starts the conversation by suggesting a product
initial_message = (
    "Hello! Welcome to our negotiation bot. I would like to show you our latest product: "
    "a high-performance laptop with 16GB RAM and 512GB SSD. It's priced at $1,200. "
    "What do you think about the price? Would you like to discuss it?\n\n"
    "You can type 'exit' anytime to quit."
)

# Print initial bot message
print(f"Bot: {initial_message}")

# Append the bot's initial message to the conversation history
history.append({"role": "model", "parts": [initial_message]})


# Function to log API requests and responses
def log_api_interaction(endpoint, request, response):
    logging.info(f"API Endpoint: {endpoint}")
    logging.info(f"Request Data: {request}")
    logging.info(f"Response Data: {response}")


# Function to analyze sentiment using TextBlob
def analyze_sentiment(user_input):
    analysis = TextBlob(user_input)
    return analysis.sentiment.polarity  # Returns polarity (-1 to 1)


# Conversation loop
while True:
    # Get user input
    user_input = input("You: ").strip()  # Strip whitespace from input
    
    # Exit condition
    if user_input.lower() == "exit":
        print("Bot: Thank you for chatting! Goodbye!")
        break

    # Handle empty input
    if not user_input:
        print("Bot: I didn't catch that. Could you say that again?")
        continue
    
    # Analyze user sentiment
    sentiment_score = analyze_sentiment(user_input)
    
    # Adjust bot's response based on sentiment
    if sentiment_score > 0.1:  # Positive sentiment (polite or positive tone)
        better_deal_message = (
            "Thank you for being polite! Let me offer you a special deal. How about we reduce the price to $1,050?"
        )
        print(f"Bot: {better_deal_message}\n")
        history.append({"role": "model", "parts": [better_deal_message]})
    elif sentiment_score < -0.1:  # Negative sentiment (impolite or negative tone)
        firm_response_message = (
            "I understand you might be upset, but $1,200 is our best offer at the moment. "
            "Let me know if you'd like to proceed."
        )
        print(f"Bot: {firm_response_message}\n")
        history.append({"role": "model", "parts": [firm_response_message]})
    else:  # Neutral sentiment
        # Start chat session with the updated history
        chat_session = model.start_chat(history=history)
        
        # Log the API request (chat session start)
        endpoint = "start_chat"  # The method name simulating the endpoint
        request_data = {"history": history}
        log_api_interaction(endpoint, request_data, "Started chat session")
        
        # Bot generates a response to user input
        try:
            response = chat_session.send_message(user_input)
            model_response = response.text
            print(f"\nBot: {model_response}\n")
            
            # Log the API request and response
            endpoint = "send_message"  # Simulating the message sending endpoint
            request_data = {"user_input": user_input}
            response_data = {"bot_response": model_response}
            log_api_interaction(endpoint, request_data, response_data)
            
        except Exception as e:
            print(f"\nBot: Oops! Something went wrong: {e}\n")
            logging.error(f"Error in API call: {e}")
            continue

        # Append bot's generated response to history
        history.append({"role": "model", "parts": [model_response]})

    # Append user input to history
    history.append({"role": "user", "parts": [user_input]})
