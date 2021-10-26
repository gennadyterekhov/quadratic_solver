from src import Kernel
import sys


def main():
    result = None
    try:
        kernel = Kernel.Kernel(sys.argv)
        result = kernel.perform()
    except Exception as exception:
        print('An Error ocurred\n', exception)

    print(result)


if __name__ == '__main__':
    main()