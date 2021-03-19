import os


def func(x):
    print('я - f()')
    raise ValueError('asdf')
    print('hoho')


def print_current_work_dir():
    print(os.path.curdir)
    print(os.path.abspath(os.path.curdir))
    func(0)
    print('ha-ha')


if __name__ == '__main__':
    print_current_work_dir()
