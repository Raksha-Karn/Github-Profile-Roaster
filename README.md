
# GitHub Profile Roaster 🔥

Welcome to **GitHub Profile Roaster**! This is a fun and snarky app designed to roast GitHub profiles using data fetched from the GitHub API and the power of AI. Want to roast yourself or your friends' GitHub profiles? Get ready for some uncensored, dark-humor-filled commentary about repos, stars, bios, and more.

## Features

- **Roast GitHub Profiles**: Simply enter a GitHub username and get a stand-up comedy-style roast.
- **AI-Powered Roasting**: Uses the [Ollama Gemma2:2b](https://ollama.com/) LLM to generate custom roasts.
- **Handles Profile and Repo Data**: Fetches user information, repositories, stars, followers, and even the user's `README.md`.
- **Saves Roasts**: Automatically saves the roast to a `.txt` file for you to enjoy later!

## How It Works

1. **Enter GitHub Username**: Input any GitHub username.
2. **Fetch Data**: The app fetches profile and repository information from the GitHub API.
3. **AI Roast**: It uses AI to craft a dark-humored roast based on the fetched data.
4. **Save Roast**: Roasts are saved to a `roasts` folder as a `.txt` file for easy reference.

## Getting Started

### Prerequisites

To run this project locally, you will need:

- **Python 3.7+**
- An API token from GitHub (stored in an `.env` file)
- Access to the [Ollama](https://ollama.com/) AI model