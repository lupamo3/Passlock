class Login:
    """
    Class that generates username, email and password
    """

    login_list=[] #Empty login list 

    def __init__(self, username, email, password):
        '''
        __init__ method helps us to define our properties
        '''
        self.username=username
        self.email=email
        self.password=password

    def usercreation(self):
        '''
        usercreation method saves usercreation objects into usercreation_method
        '''
        Login.login_list.append(self)

    @classmethod
    def loginverify(cls, name, key):
        '''
        Authenticates login details,
        '''
        for user in cls.login_list:
            if user.email==name and user.password==key:
                #print(user.username)
                return user
        return 0

class Pword:
    """
    Class that stores password and user ids
    """
    pword_list=[] #Empty pword list

    def __init__(self, userid, website, webkey):
        '''
        __init__ method helps us to store user details
        '''
        self.userid=userid
        self.website=website
        self.webkey=webkey

    def addpassword (self):
        """
        creating a method that creates username and password
        """
        Pword.pword_list.append(self)

    @classmethod
    def display_data(cls, number, count):
        '''
        display all passwords generated by user
        '''
        for password in cls.pword_list:
            if password.userid==number:
                if password.webkey==count:
                    return password

    @classmethod
    def existing_data(cls, number):
        '''
        Checks if data exists in the profile
        '''
        for data in cls.pword_list:
            if data.userid==number:
                return True
        return False

    @classmethod
    def copy_password(cls, number, count)
        found_password=Pword.display_data(number, count)
        pyperclip.copy(found_password.webkey)