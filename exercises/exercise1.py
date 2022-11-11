import string
import re

regex = '/^[a-z0-9]+[\\._]?[a-z0-9]+[@]\\w+[.]\\w{2,3}$'

class Person:
    def __init__(self, name: string, email: str):
        self._name = name
        if(re.search(regex, email)):   
            self._email = email
        else:   
            raise ValueError('Invalid email!')

    def greet(self):
        return 'Hello!'



