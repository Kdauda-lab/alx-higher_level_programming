#!/usr/bin/python3
if __name__ == '__main__':
    import hidden_4
    def_names = dir(hidden_4)
    for i in def_names:
        if def_names[:2] != '__':
            print(def_names)
