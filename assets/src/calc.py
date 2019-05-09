import fire

class Calc:

    def add(self, *args):
        print(sum(args))

    def double(self, *args):
        print(' '.join(f'{i * 2}' for i in args))


if __name__ == '__main__':
    fire.Fire(Calc)
