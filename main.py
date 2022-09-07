import argparse as arg
import os
import functions as func

def main():
    parser = arg.ArgumentParser(description='Path to an image')

    parser.add_argument('-b', '--blur', help='Blur passed image', default='')
    parser.add_argument('-g', '--grayscale', help='Grayscale passed image', default='')
    parser.add_argument('-a', '--all-options', help='Blur and grayscale passed image', default='')

    args=parser.parse_args()

    blurPath = args.blur
    grayScalePath = args.grayscale
    allOptionsPath = args.all_options

    if os.path.exists(blurPath):
        func.blur(blurPath)

    if os.path.exists(grayScalePath):
        func.grayscale(grayScalePath)

    if os.path.exists(allOptionsPath):
        func.blur(allOptionsPath)
        func.grayscale(allOptionsPath)

if __name__ == '__main__':
    main()