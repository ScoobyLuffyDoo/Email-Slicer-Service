class EmailSlicer:   
    def sliceEmail(self,email):
        i_email = email.strip()
        username= i_email[:i_email.index('@')]
        domain = i_email[i_email.index('@') + 1:]
        return{'username':username, 'domain':domain}

    @staticmethod
    def checkEmailAddress(email):
        email = email
        return True