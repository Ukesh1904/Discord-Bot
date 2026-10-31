# Discord Bot 

A personal Discord bot project built using Python and `discord.py`.

## About the Project

I started this project to learn Python and understand how Discord bots operate. I was interested in learning how bots communicate with Discord servers, how command and event handling work, and how to add different functionalities using Python.

Throughout the development process, I experimented with various features, including moderation commands, welcome messages, server information, embeds, and utility commands.

This project was primarily created for educational purposes and personal learning.

## 📁 Project Structure

```text
Discord Bot/
│
├── main/
│   ├── cogs/
│   │   ├── admin.py
│   │   └── embed.py
│   │
│   ├── main.py
│   └── requirements.txt
│
├── other/
│   ├── bleach.py
│   └── truthordare.py
│
├── README.md
└── .gitignore
```

## Main Bot Features

### Moderation
- Ban and unban members
- Kick members
- Timeout and remove timeout
- Clear messages
- Delete messages containing a specified word

### Server Information
- User information
- Server information
- Member count
- Role information
- Server roles
- Server booster information

### Fun Commands
- Random quotes
- Random jokes
- Rock Paper Scissors
- Coin flip

### Other Features
- Welcome messages through DMs
- Bot information
- Help command
- Custom Discord embeds

## Other Projects

The `other/` directory contains separate Discord bot experiments.

### Bleach Character Collection

A simple character-collection game inspired by the anime *Bleach*.

**Features:**
- Random character rolls
- Character information and images
- Character collection system
- Limited number of rolls per user

### Truth or Dare

A simple Discord Truth or Dare bot.

**Features:**
- Random truth questions
- Random dare prompts
- Help command

## Technologies Used

- Python
- discord.py
- Requests
- Discord API

## Project Status

This project was created quite some time ago while I was learning Python and Discord bot development.

I haven't worked on or updated this code in approximately 1–2 years. I'm keeping it as a record of what I learned and as an opportunity to revisit, understand, and improve my earlier code.

Some parts of the code may be outdated and might require updates to work with newer versions of Python and its dependencies.

## Learning Resources & Acknowledgements

I learned the fundamentals of Discord bot development through various YouTube tutorials.

Special thanks to the creators whose tutorials helped me throughout the learning process:

- **James S.** — [Discord.py Tutorial Playlist](https://www.youtube.com/watch?v=cCiqcu2NP8I&list=PL-7Dfw57ZZVRB4N7VWPjmT0Q-2FIMNBMP)
- **House of Code** — [Discord.py Tutorial Playlist](https://www.youtube.com/watch?v=x7oBQNcNGeM&list=PLwqYQaS6jxfk_NCetUOyNRDGAf9_kU90n)

Their tutorials helped me understand the basics and gave me the foundation to build my own Discord bots.

## Disclaimer

This repository is shared for educational purposes. It represents my previous learning experience with Python and Discord bot development. Some features may no longer work as originally intended due to changes in dependencies or Discord's API.
