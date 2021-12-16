class House:
    def __init__(self, name, windows, doors, has_garage):
        self.exists = True
        self.name = name.lower().title()
        self.windows = windows
        self.doors = doors
        self.has_garage = has_garage

    def get_existence(self):
        return_string = 'The house has been built'
        return return_string

    def get_name(self):
        return_string = 'The name of the house is ' + self.name
        return return_string

    def get_windows(self):
        return_string = self.name + ' has ' + str(self.windows) + ' window'
        if self.windows != 1:
            return_string += 's'
        return return_string

    def set_windows(self, windows):
        self.windows = windows

    def get_doors(self):
        return_string = self.name + ' has ' + str(self.doors) + ' door'
        if self.doors != 1:
            return_string += 's'
        return return_string

    def get_has_garage(self):
        return_string = self.name + ' '
        if not self.has_garage:
            return_string += "doesn't "
        return_string += 'has a garage'
        return return_string
    
    def get_basic_information(self):
        print(self.get_existence())
        print(self.get_name())
        print(self.get_windows())
        print(self.get_doors())
        print(self.get_has_garage())