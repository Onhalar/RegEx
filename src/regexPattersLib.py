import re

URL = r"(https?:\/\/)?(www\.)?([a-z0-9^\s]+){1}(\.[a-z]+){1}(\/[^\/\s]+)*"
EMAIL = r"([^A-Z\s]+)@([^A-U\s\.]+)(\.[a-z]+)"
TIME = r"(([0-1][0-9]):([0-5][0-9])\s?(PM|AM){1})|(([0-2][0-9]):([0-5][0-9]))"

class IsValid:
    def URL(toCheck: str):
        return re.match(URL, toCheck) is not None
    
    def Email(toCheck: str):
        return re.match(EMAIL, toCheck) is not None
    
    def Time(toCheck: str):
        return re.match(TIME, toCheck) is not None
    
if __name__ == '__main__':
    pass