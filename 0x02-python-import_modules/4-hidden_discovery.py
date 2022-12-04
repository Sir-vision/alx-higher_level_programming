#!/usr/bin/python3
if __name__ == '__main__':
    import hidden_4.pyc
    name_list = dir('hidden_4.pyc')
    for name in name_list:
        if name[0:2] != "__":
            print(f"{name}", end='')
