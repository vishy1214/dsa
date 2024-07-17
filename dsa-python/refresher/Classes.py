class AlphaNumeric(object):

    default_suffix = "your parent is alpha"

    def __init__(self,prefix=default_prefix,suffix=default_suffix):
        self.prefix = prefix
        self.suffix = suffix

    def printMe(self,x):
        print(self.prefix+" "+x+ " "+self.suffix)

class String(AlphaNumeric):
    custom_suffix = " your parent is a String"

    def printMe(self,x):
        print(self.prefix+" "+x+" "+String.custom_suffix)

class Number(AlphaNumeric):
    custom_suffix = " your parent is a Number"

    def printMe(self,x):
        print(self.prefix+" "+x+" "+Number.custom_suffix)

