from os import stat


class Animal:


    def __init__(self, variable):
        self.variable = variable

    def get_variable(self):
        return self.variable

    def set_variable(self, variable):
        self.variable = variable

    @staticmethod
    