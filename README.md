# Nebula_bot

Nebula is an AI telegram bot powered by many popular LLM tools like Gemini, Cohere's rerank, etc.

## Note:
I have used the tools that I prefer for that specific tasks. Like for embedding I prefer Cohere's embedding v3 model, for chat: Gemini, Vector DB: ChromaDB, etc.

### To use this Repo:
1. Clone the repo

2. create `.env` with the following API Keys:
```
TOKEN= <Telegram bot token>
GEMINI= <Gemini API_KEY>
HF_TOKEN= <HUGGINGFACE TOKEN>
COHERE_API= <COHERE API_KEY>
```

3. run the following command to install the packages:
`pip install requirements.txt`

4. run `python main.py`

5. (Optional) For hosting steps depends on the hosting service used.

This project is still under development. Currenly, RAG only supports for PDF. 

If you wish to contribute to this project. Feel free to do so. There is still room for lot of improvement. But do remember that everything works for free as this is a personal ai bot specifically for them.


### Bot commands
1. `/access <password>` : for a little security. (you can change the password from `main.py`).
2. After gaining access you can directly use the bot by sending it text messages of images.
3. `/image <prompt>` : to generate images.
4. `/pdf <question>` : to chat with pdf (upload a pdf before using this)