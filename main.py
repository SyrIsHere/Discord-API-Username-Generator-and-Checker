import requests
import random
import string
import time
import logging
from colorama import Fore, Back, Style, init

init(autoreset=True)

class DiscordRequest:
    """Class for handling Discord API requests."""
    
    def __init__(self, authorization_token, locale="it", timezone="Europe/Rome"):
        self.url = "https://discord.com/api/v9/users/@me/pomelo-attempt"
        self.headers = {
            "accept": "*/*",
            "accept-encoding": "gzip, deflate, br, zstd",
            "accept-language": "it-IT,it;q=0.9,en-US;q=0.8,en;q=0.7",
            "authorization": authorization_token,
            "content-type": "application/json",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36",
            "x-debug-options": "bugReporterEnabled",
            "x-discord-locale": locale,
            "x-discord-timezone": timezone,
        }

    def send_request(self, payload):
        """Send a POST request with the given payload."""
        try:
            response = requests.post(self.url, headers=self.headers, json=payload)
            response.raise_for_status()
            return response
        except requests.exceptions.RequestException as e:
            logging.error(f"{Fore.RED}[ERROR] Requests: {e}")
            return None

class UsernameGenerator:
    """Class for generating random usernames."""
    
    @staticmethod
    def generate_username(length=3):
        """Generate a random username with a defined number of letters."""
        letters = ''.join(random.choices(string.ascii_lowercase, k=length))
        return letters

class DiscordBot:
    """Main class to handle the logic of the token."""
    
    def __init__(self, authorization_token):
        self.discord_request = DiscordRequest(authorization_token)
        self.username_generator = UsernameGenerator()

    def run(self):
        """Start the infinite loop to send random usernames."""
        while True:
            username = self.username_generator.generate_username()
            payload = {"username": username}
            
            response = self.discord_request.send_request(payload)
            
            if response:
                logging.info(f"{Fore.GREEN}[INFO] Username: {username}")
                logging.info(f"{Fore.CYAN}[INFO] Response: {response.text}\n")
            else:
                logging.warning(f"{Fore.YELLOW}[WARNING] Username {username}")
            
            time.sleep(30)

def setup_logging():
    """Configure logging with professional colors."""
    logging.basicConfig(
        level=logging.DEBUG,
        format="%(asctime)s - %(message)s",
    )

    logging.getLogger().handlers[0].setFormatter(logging.Formatter('%(asctime)s - %(message)s'))
    logging.setLoggerClass(ColoredLogger)

class ColoredLogger(logging.Logger):
    """Custom logger that adds support for colors."""
    
    COLORS = {
        logging.DEBUG: Fore.BLUE,
        logging.INFO: Fore.GREEN,
        logging.WARNING: Fore.YELLOW,
        logging.ERROR: Fore.RED,
        logging.CRITICAL: Fore.MAGENTA,
    }
    
    def __init__(self, name):
        super().__init__(name)
    
    def log(self, level, msg, *args, **kwargs):
        color = self.COLORS.get(level, "")
        msg = f"{color}{msg}{Style.RESET_ALL}"
        super().log(level, msg, *args, **kwargs)

if __name__ == "__main__":
    setup_logging()
    authorization_token = "TOKEN HERE" # TOKEN HERE

    bot = DiscordBot(authorization_token)
    bot.run()
