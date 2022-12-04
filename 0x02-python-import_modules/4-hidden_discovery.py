#!/usr/bin/python3
if __name__ == '__main__':
    import hidden_4.pyc
    name_list = dir(hidden_4.pyc)
        if name_list[0:2] != "__":
            print("{name_list}", end='')
