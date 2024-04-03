import json


class Registration:
    def __init__(self, name: str, code: str, file='registration.json'):
        self.name = name
        self.code = code
        self.file = file



    def registration(self):
        try:
            with open(self.file, 'r', encoding='utf-8') as files:
                n = json.load(files)
                count = int(n["count"]) + 1
                if self.name not in n.keys() and self.code not in n.values():
                    if self.name != '' and self.code != '' and self.name[0] != ' ' and self.code[0] != ' ':
                        n[self.name] = self.code
                    else:
                        raise Exception('Имя или код заняты')
                else:
                    raise Exception('Имя или код заняты')
                n["count"] = str(count)
            with open(self.file, 'w+', encoding='utf-8') as files1:
                print(n)
                json.dump(n, files1)
        except Exception as e:
            print(e)



name = input()
code = input()
c = Registration(name, code)
c.registration()