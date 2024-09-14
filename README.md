# negotiation-Chatbot
This project implements a negotiation chatbot using Google Generative AI (Gemini) for product price negotiation. It simulates a conversation between a chatbot (representing a seller) and a user (acting as the buyer). The chatbot offers dynamic responses based on the user's sentiment and logs API interactions for further analysis.

Key Components
Google Generative AI for Chat Responses:
The chatbot uses Google's Generative AI (google-generativeai SDK) to provide dynamic and context-aware responses to the user's input.
Sentiment Analysis:
The sentiment of the user’s input is analyzed using TextBlob. Depending on whether the sentiment is positive, negative, or neutral, the chatbot adapts its responses, offering better deals to polite users.
API Endpoint Logging:
Every API interaction is logged to track endpoints and facilitate debugging or analysis of API usage.

