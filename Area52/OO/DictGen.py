from string import ascii_lowercase as letters


class DictGen():
    d = {}

    def generator(self):
        for i in range(len(letters)):
            self.d[i] = letters[i]
        return self.d


obj = DictGen()
obj.generator()
