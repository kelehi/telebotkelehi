class Write:
    def __init__(self, code: str, file='history_users.txt'):
        self.code = code
        self.file = file

    def request_write(self):
        with open(self.file, 'a+', encoding='utf-8') as file_write:
            string_info = self.code + '\n'
            file_write.write(string_info)

    def request_read(self):
        with open(self.file, 'r', encoding='utf-8') as file_read:
            read_admin = file_read.read()
            return read_admin


