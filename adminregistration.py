import json


class Admin_registration:
    def __init__(self, admin_name: str, id_admin: str, file_admin_registration='admin_registration.json'):
        self.admin_name = admin_name
        self.id_admin = id_admin
        self.file_admin_registration = file_admin_registration

    def registration_admin(self):
        try:
            with open(self.file_admin_registration, 'r', encoding='utf-8') as files:
                flag = False
                n = json.load(files)
                count = int(n["count_admins"]) + 1
                if self.admin_name not in n.keys() and self.id_admin not in n.values():
                    if self.admin_name != '' and self.id_admin != '' and self.admin_name[0] != ' ' and self.id_admin[0] != ' ':
                        n[self.admin_name] = self.id_admin
                        flag = True
                if flag:
                    n["count_admins"] = str(count)
            with open(self.file_admin_registration, 'w+', encoding='utf-8') as files1:
                print(n)
                json.dump(n, files1, indent=2)
        except BaseException:
            return False

    def checking_for_admin(self):
        with open(self.file_admin_registration, 'r', encoding='utf-8') as files:
            n = json.load(files)
            if self.admin_name not in n.keys() and self.id_admin not in n.values():
                return True
            return False


