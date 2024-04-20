import json


class Admin_registration:
    def __init__(self, admin_name: str, id_admin: str, file_admin_registration='admin_registration.json'):
        self.admin_name = admin_name
        self.id_admin = id_admin
        self.file_admin_registration = file_admin_registration

    def registration_admin(self):
        try:
            with open(self.file_admin_registration, 'r', encoding='utf-8') as files_read:
                flag = False
                dict_registration = json.load(files_read)
                count = int(dict_registration["count_admins"]) + 1
                if self.admin_name not in dict_registration.keys() and self.id_admin not in dict_registration.values():
                    if self.admin_name != '' and self.id_admin != '' and self.admin_name[0] != ' ':
                        if self.id_admin[0] != ' ':
                            dict_registration[self.admin_name] = self.id_admin
                            flag = True
                if flag:
                    dict_registration["count_admins"] = str(count)
            with open(self.file_admin_registration, 'w+', encoding='utf-8') as files_write:
                json.dump(dict_registration, files_write, indent=2)
        except BaseException:
            return False

    def checking_for_admin(self) -> bool:
        with open(self.file_admin_registration, 'r', encoding='utf-8') as files:
            dict_registration_1 = json.load(files)
            if self.admin_name not in dict_registration_1.keys() and self.id_admin not in dict_registration_1.values():
                return True
            return False

    def is_checking_for_admin(self) -> bool:
        with open(self.file_admin_registration, 'r', encoding='utf-8') as is_files:
            dict_registration_2 = json.load(is_files)
            if self.admin_name in dict_registration_2.keys() and self.id_admin in dict_registration_2.values():
                return True
            return False