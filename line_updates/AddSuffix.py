from os import rename, remove


def add_suffix(suffix, file_path, output_file=''):
    """
    Add a given suffix to each lines a given file

    Parameters
    __________
    suffix : suffix which will be added

    file_path : the file which needs to be updated

    output_file='' : the output file path if different of the input file path

    Raises
    ______
    FileNotFoundError : if file_path is not found

    """
    lines = []
    if output_file == '': output_file = file_path

    try:
        with open(file_path, mode='r', encoding='utf-8') as input_file:
            lines = input_file.readlines()
    except FileNotFoundError:
        print(file_path + " doesn't exist. Impossible to make the update.\n")
        raise FileNotFoundError

    with open(output_file + '_tmp', mode='w', encoding='utf8') as tmp_output_file:
        [tmp_output_file.write(line[:-1] + suffix + '\n') for line in lines]

    try:
        remove(output_file)
    except FileNotFoundError:
        pass

    rename(output_file + '_tmp', output_file)
