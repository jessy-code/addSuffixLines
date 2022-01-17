import argparse
import sys
from line_updates.AddSuffix import add_suffix


def get_user_inputs():
    """
    Function to get user inputs
    """
    # Input variable definition
    parser = argparse.ArgumentParser(formatter_class=argparse.RawTextHelpFormatter,
                                     description='Script which add a suffix to all lines of a given file.')
    parser.add_argument('suffix', help='suffix which will be added to each line', type=str)
    parser.add_argument('file_path', help='path of the file which need to be updated', type=str)
    parser.add_argument('-output_file', help='path where you want to store the result. If not defined, the output file '
                                            'will be the input file', type=str)
    return parser.parse_args()


def main(argv):
    user_inputs = get_user_inputs()
    suffix = user_inputs.suffix
    file_path = user_inputs.file_path
    output_file = user_inputs.output_file if user_inputs.output_file else ''

    add_suffix(suffix, file_path, output_file)


if __name__ == "__main__":
    main(sys.argv[1:])
