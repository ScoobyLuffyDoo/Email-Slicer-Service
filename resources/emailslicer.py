class EmailSlicer:   
    username :str
    domain:str 
    def sliceEmail(self,email):
        i_email = email.strip()
        self.username = i_email[:i_email.index('@')]
        self.domain = i_email[i_email.index('@') + 1:]
        return

    @staticmethod
    def checkEmailAddress(email):
        email = email
        return True