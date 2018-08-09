"""
    global variable uber_database which will hold the drivers detatils
    initially  its empty.

"""
import re
class Usercredentials:
    """class method for modeling the  signup page"""

    def __init__(self, firstname,lastname,phonenumber,email):
        """creating class instances"""
        self.firstname = firstname
        self.lastname = lastname
        self.phonenumber =int(phonenumber)
        self.email = Usercredentials.isValidEmail(email)


    def fullname(self):
        """ Combines first and last name into a single name"""
        name = '{}  {}'.format(self.firstname, self.lastname)
        return name
        
    """ check if the email is in valid format"""
    @staticmethod
    def isValidEmail(email):
        validemail = re.compile(r"^[A-Za-z0-9_-]+@[A-Za-z0-9_-]+\.[a-zA-Z]*$")
        if not validemail.match(email):
            raise ValueError(" incorrect email")
            print ('something')
        else:
            return email
            print('nothong')


class Driver(Usercredentials):
     def __init__(self, firstname,lastname,phonenumber,password, number_plate, type_of_vehicle):
        super().__init__(firstname,lastname,phonenumber,password)

        self.number_plate = number_plate
        self.type_of_vehicle

    

