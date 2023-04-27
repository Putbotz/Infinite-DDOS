import random

from typing import Union

user_agent_list: list = ["Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36"]

class UserAgent:
    def random() -> Union[str, None]:
        try:
            return random.choice(user_agent_list)
        except:
            return None