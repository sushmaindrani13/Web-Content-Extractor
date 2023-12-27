
import validators
import re
import socket

class URLCheck:
    @staticmethod
    def validation(urlvar):
        res=validators.url(urlvar)
        return res


if __name__=="__main__":
    print("main")
    u=URLCheck()
    print(URLCheck.validation("https://stackoverflow.com"))

