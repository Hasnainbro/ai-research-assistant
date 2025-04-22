
# Deep Research AI Assistant

This is a conversational AI assistant that can chat casually **and** provide real-time researched answers to user queries using LangGraph, Tavily API, and OpenRouter (Google Gemini). The app has a user-friendly interface built with HTML/CSS and communicates with the Flask backend via a simple `/ask` API.

---

## Features

-  **Real-time information retrieval** using Tavily search.
-  **Answer synthesis** via OpenRouter's Gemini model using LangChain.
-  **Conversational tone** – responds casually to greetings and seriously to queries.
-  **Cross-Origin API support** with Flask-CORS.
-  Minimal, clean chat UI with responsive layout.

---

##  Tech Stack

| Layer       | Technology                      | Description                                 |
|------------|----------------------------------|---------------------------------------------|
| Backend     | Flask                            | Web server handling routing and AI logic     |
| AI Workflow | LangGraph + LangChain            | Workflow manager and LLM integration         |
| AI Model    | OpenRouter (Gemini 2.0 Flash)    | Language model for generating responses      |
| Research    | Tavily API                       | Real-time search for factual information     |
| Frontend    | HTML + CSS + JavaScript          | Chat UI using native web technologies        |

---

##  Project Structure

```
 your-ai-app/
├── app.py                        # Flask app and API routes
├── templates/
│   └── index.html                # Chat UI
├── static/
│   └── style.css                 # UI styling
├── agents/
│   ├── research_agent.py         # Tavily-based web search
│   └── answer_agent.py           # Gemini-based response generator
├── graphs/
│   └── langgraph_flow.py         # Controls query handling flow
├── utils/
│   └── prompts.py                # Prompt templates
└── .env                          # Environment variables
```

---

## 🛠️ Installation & Setup

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/ai-research-assistant.git
cd ai-research-assistant
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

Example `requirements.txt`:

```txt
flask
flask-cors
python-dotenv
tavily-python
langchain
```

### 3. Configure `.env`

Create a `.env` file and add:

```
TAVILY_API_KEY=your_tavily_api_key
OPENROUTER_API=your_openrouter_api_key
```

> You can get your Tavily key from [Tavily.com](https://www.tavily.com/) and OpenRouter key from [OpenRouter.ai](https://openrouter.ai/).

### 4. Run the Flask app

```bash
python app.py
```

Then open `http://127.0.0.1:5000/` in your browser 🚀

---

##  How It Works

1. User types a message in the chat UI.
2. The message is sent to the `/ask` Flask route.
3. The backend checks if it's a casual greeting:
    - If yes → responds with a friendly message.
    - If no → it uses:
    - `research_agent.py` to fetch relevant info using Tavily.
    - `answer_agent.py` to summarize & format the answer via Gemini.
4. The final response is sent back to the frontend and displayed.

---

##  Example Queries

- "What's the latest news on AI regulation?"
- "Summarize the top 5 benefits of a plant-based diet."
- "Hey!" → Casual AI reply

---

##  Future Improvements

- Add support for voice input and TTS output.
- Deploy to Vercel (frontend) and Render (backend) or use Docker.
- Add chat history and authentication for saved sessions.

---

##  Contributing

Pull requests are welcome! For major changes, open an issue first to discuss what you'd like to change.

---

## Credits

- [Tavily](https://www.tavily.com/) for search APIs
- [OpenRouter](https://openrouter.ai/) for model access
- [LangChain](https://www.langchain.com/) for prompt tooling
