## Task 3 – Streaming AI Chat Assistant

### Objective
Build an interactive chatbot using the Gemini API with streaming responses and chat history.

### Features
- Interactive command-line chatbot
- Chat history support
- Streaming responses (chunk-by-chunk)
- Exit command to end the chat

### Technologies Used
- Python
- Google Gemini API
- google-genai SDK

### Output
The chatbot successfully streams responses while maintaining conversation history.


## Task 4 – Token Usage and Cost Tracker

### Objective
Track prompt text, response text, estimated token usage, and estimated API cost.

### Features
- Logs prompt and response
- Estimates token usage
- Estimates API cost
- Saves logs to CSV
- Displays final usage report

### Output
A CSV file (`token_usage_log.csv`) is generated containing prompt, response, token count, and estimated cost. A final report displays total requests, total tokens, and total estimated cost.