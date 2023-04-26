import json

class fetch:   
    def proxy() -> str: 
        config = open("./config.json"); data = json.load(config)
        proxy = data["Proxy"]
        
        config.close(); return proxy
