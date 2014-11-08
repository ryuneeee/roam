import os


_NOT_SUPPORTED = 'Not supported yet.'
_SYNO_LOGIN_OK = 'LOGIN OK.'
_SYNO_LOGIN_FAILED = 'LOGIN failed.'
_SYNO_GROUP_OK = 'Group Name: [%s]\nGroup Type: [AUTH_LOCAL]\nGroup ID:   [65536]\nGroup Members: '
_SYNO_GROUP_NOT_FOUND = 'Lastest SynoErr=[group_db_get.c:37]\nSYNOGroupGet failed, synoerr=0x1800'
_SYNO_USER_NOT_FOUND = 'synouser.c:357 SYNOUserGet failed. synoerr=[0x1D00]'


class FakeSyno:

    groups = {}
    users = {}

    def __init__(self):
        self.override_popen()

    def __init__(self, user, password, group=None):
        self.users[user] = password
        self.groups[user] = group
        self.result = None

        # Overriding for fake test
        self.override_popen()

    def add_user(self, user, password, group=None):
        self.users[user] = password
        self.groups[user] = group
        print(self.users, self.groups)

    def override_popen(self):
        self.popen = os.popen
        os.popen = self.fake_syno_shell

    def rollback_popen(self):
        os.popen = self.popen

    def fake_syno_shell(self, cmd):

        cmds = cmd.split(' ')
        command, func = cmds[:2]

        if command == 'synouser':
            self.synouser(func, user=cmds[2], password=cmds[3])
        elif command == 'synogroup':
            self.synogroup(func, group=cmds[2])
        else:
            raise Exception(_NOT_SUPPORTED)
        return self

    def synouser(self, func, user, password):
        if func == '--login':
            if self.users.get(user) is None:
                self.result = _SYNO_USER_NOT_FOUND
                return self

            if self.users[user] == password:
                self.result = _SYNO_LOGIN_OK
            else:
                self.result = _SYNO_LOGIN_FAILED
        else:
            raise Exception(_NOT_SUPPORTED)

    def synogroup(self, func, group):
        #synogroup --get ryunbox
        if func == '--get':
            users = [k for k, v in self.groups.items() if v == group]

            if len(users):
                user_str = ''
                for user in users:
                    user_str += '\n%s:[%s]' % (users.index(user), user)
                self.result = _SYNO_GROUP_OK % group + user_str + "\n"
            else:
                self.result = _SYNO_GROUP_NOT_FOUND
        else:
            raise Exception(_NOT_SUPPORTED)

    def read(self):
        return self.result