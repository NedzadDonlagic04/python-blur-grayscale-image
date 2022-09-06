import argparse as arg
import os
import functions as func

def main():
    parser = arg.ArgumentParser(description='Path to an image')

    parser.add_argument('-b', '--blur', help='Blur passed image', default=None)
    parser.add_argument('-g', '--grayscale', help='Grayscale passed image', default='')
    parser.add_argument('-a', '--all-options', help='Blur and grayscale passed image', default='')

    args=parser.parse_args()

    blurPath = args.blur
    grayScalePath = args.grayscale
    allOptionsPath = args.all_options

    if os.path.exists(blurPath):
        print('Exists')

    if os.path.exists(grayScalePath):
        print('Exists')

    if os.path.exists(allOptionsPath):
        print('Exists')
    print(args)

if __name__ == '__main__':
    main()