# Chatbot using Google Generative AI with Sentiment Analysis

This Python project implements a negotiation chatbot using **Google Generative AI (Gemini)**. The chatbot engages in dynamic price negotiations, offering customized responses based on user input. The main features include sentiment analysis and API endpoint logging for monitoring interactions.

## Features
- **Dynamic Negotiation**: The chatbot simulates a negotiation process for product pricing. It provides flexible responses, enabling users to accept, reject, or make counteroffers.
- **Sentiment-Based Interaction**: The bot adjusts its responses based on the sentiment of the user's input using `TextBlob` for sentiment analysis. Users with polite input receive better offers, while negative or impolite inputs are handled more firmly.
- **Logging of API Endpoints**: The project logs API interactions using Python's `logging` module, tracking which endpoints were hit during each conversation.

## Technologies Used
- **Python**: The core programming language.
- **Google Generative AI**: For generating context-aware responses based on user interaction.
- **TextBlob**: For performing sentiment analysis on user input.
- **dotenv**: For securely managing API keys using environment variables.
- **Logging**: To track API endpoint interactions and responses.

## Setup

1. Install the necessary dependencies:
   ```bash
   pip install google-generativeai textblob python-dotenv

2. Generate the API key from Google`s gemini AI site:
- **API initialization**: create a new .env file and save the api key

3. Run and retrive the logs:
  **API log access**: API logs are created seperately in the directory and api calls are logged as the conversation moves

