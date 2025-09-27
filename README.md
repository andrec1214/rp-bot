# RP Bot CLI

A command-line roleplay chatbot application that allows users to create and interact with AI characters through conversational sessions. Built with Flask, SQLAlchemy, and the Anthropic Claude API.

## Features

- **User Management**: Secure user registration and authentication with password hashing
- **Character Creation**: Create detailed characters with personality, backstory, world info, goals, and relationships
- **Session Management**: Organize conversations into sessions with custom titles
- **Intelligent Conversation**: Powered by Claude Sonnet 4 for natural, in-character responses
- **Context Management**: Automatic conversation summarization to maintain long-term context
- **Database Support**: Compatible with both SQLite (development) and PostgreSQL (production)

## Tech Stack

- **Backend**: Flask, SQLAlchemy
- **Database**: PostgreSQL/SQLite
- **AI**: Anthropic Claude API
- **Authentication**: Werkzeug password hashing
- **Environment**: Python 3.12+

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd rp-bot-cli
```

2. Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Set up environment variables:
```bash
# Create a .env file with:
DATABASE_URL=postgresql://username:password@localhost:5432/rpbot_db
```

5. Set up your database:
```bash
# Make sure PostgreSQL is running and create the database
createdb rpbot_db
```

## Usage

1. Run the application:
```bash
cd backend
python chat.py
```

2. Follow the prompts to:
   - Create a user account or log in
   - Enter your Anthropic API key
   - Create a character or select an existing one
   - Start chatting!

3. Type "exit" to end the conversation

## Database Schema

- **Users**: Store user accounts with hashed passwords
- **Characters**: Character profiles with personality traits and background
- **Sessions**: Conversation sessions between users and characters
- **Messages**: Individual messages with automatic summarization support

## Key Components

- `models.py` - Database models and relationships
- `app.py` - Flask application configuration
- `init.py` - User setup and character selection logic
- `chat.py` - Main chat interface and conversation loop
- `utils.py` - Claude API integration and context management

## Features in Detail

### Context Management
The application automatically manages conversation context by:
- Keeping recent messages in active memory
- Summarizing older conversations to maintain continuity
- Merging multiple summaries for long-term sessions

### Character System
Characters can be defined with:
- **Name**: Character identifier
- **Personality**: Core personality traits
- **Backstory**: Character history and background
- **World Info**: Setting and world details
- **Goals**: Character motivations
- **Relationships**: Connections to other characters

### Security
- Passwords are hashed using Werkzeug's secure password hashing
- API keys are not stored in the database
- User sessions are isolated and secure

## Contributing

This is a personal project for portfolio demonstration. Feel free to fork and modify for your own use.

## License

This project is for educational and portfolio purposes.