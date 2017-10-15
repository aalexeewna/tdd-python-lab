import hashlib, sys


class Auth(object):
    """
    Auth class
    """

    def add_user(self, login, password):
        if login is not None and password is not None:
            try:
                file = open('app/users.txt', 'r')

                if_exist = False

                if file is not None:
                    for line in file:
                        user = line.split('/')
                        if login == user[0]:
                            if_exist = True
                            break

                if if_exist:
                    file.close()
                    return 1
                else:
                    file.close()
                    file = open('app/users.txt', 'a')
                    new_str = '{}/{}/'.format(login, self.get_md5(password))
                    file.write(new_str + '\n')
                    file.close()
                    return 0
            except IOError as e:
                print("Invalid file.", e)
                sys.exit()
        else:
            return 2

    def del_user(self, login, password):
        if login is not None and password is not None:
            try:
                file = open('app/users.txt', 'r')

                if_exist = False
                users = []

                if file is not None:
                    for line in file:
                        user = line.split('/')
                        if login == user[0] and self.get_md5(password) == user[1]:
                            if_exist = True
                        else:
                            users.append(line)

                if if_exist:
                    file.close()
                    file = open('app/users.txt', 'w')
                    file.writelines(users)
                    file.close()
                    return 0
                else:
                    file.close()
                    return 1
            except IOError as e:
                print("Invalid file.", e)
                sys.exit()
        else:
            return 2

    def check_user(self, login, password):
        try:
            file = open('app/users.txt', 'r')

            for line in file:
                user = line.split('/')

                if login == user[0]:
                    if self.get_md5(password) == user[1]:
                        file.close()
                        return 1
                    else:
                        print(self.get_md5(password), user[1])
                        file.close()
                        return 3
                else:
                    file.close()
                    return 2
        except IOError:
            print("Invalid file.")
            sys.exit()

    def get_md5(self, password):
        m = hashlib.md5()
        m.update(password.encode('utf-8'))
        return m.hexdigest()
