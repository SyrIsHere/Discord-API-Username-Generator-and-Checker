# Discord Bot Username Generator

This Python script automates the process of generating random usernames and sending requests to the [Discord API](https://discord.com/developers/docs/intro).

## Features:

- **Discord API Integration**: Interacts with Discord's API to send POST requests.
- **Dynamic Username Generation**: Automatically generates random usernames consisting of 3 lowercase letters.
- **Color-Coded Logging**: Utilizes `colorama` for colorized logs, making it easier to distinguish between log levels.
- **Modular Design**: The project is broken down into separate classes for clean, maintainable code.
- **Request Retry Mechanism**: Gracefully handles failed requests and logs error messages.
- **Infinite Loop**: The bot runs continuously, sending a new username every 30 seconds.
- **Custom Logging Configuration**: Professional, color-coded logs for better readability.
- **Localization and Timezone Support**: Adapts to different regions and time zones with flexible configuration.
- **Token Management**: Authenticates the bot using a provided Discord token.

## Setup

Install dependencies:
```bash
pip install requests colorama
```

## Disclaimer
I am not responsible for any damages, consequences, results, or account suspensions that may occur through the use of this tool. By running this tool, you acknowledge that it is entirely at your own risk and you take full responsibility for any actions or outcomes that result from its use.
