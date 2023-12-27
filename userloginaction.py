

class UserLoginCheck:

    def datacheck(self,uid,pwd):
        if uid == "" and pwd == "":
            return True
        else:
            return False
    @staticmethod
    def logincheck(uid,pwd):
        if uid == "user" and pwd == "user":
            return True
        else:
            return False
