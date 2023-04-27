from fake_useragent import UserAgent

class useragent:
    def random() -> str: 
        ua: object = UserAgent()
        return ua.random