import unittest
from os import getcwd, chdir, remove
from line_updates.AddSuffix import add_suffix
from shutil import copyfile


class AddSuffixTestCase(unittest.TestCase):

    def test_input_neq_output(self):
        """
        Test add_suffix function if the input file is different of output file
        """
        if not getcwd().split('\\').__contains__('tests'):
            chdir("tests")
        add_suffix('_suffix', 'input.txt', 'output.txt')

        with open('input.txt', mode='r', encoding='utf-8') as input_file:
            input_lines = input_file.readlines()

        with open('output.txt', mode='r', encoding='utf-8') as input_file:
            output_lines = input_file.readlines()

        remove('output.txt')
        self.assertListEqual([line[:-1] + '_suffix\n' for line in input_lines], output_lines)

    def test_input_eq_output(self):
        """
        Test add_suffix function if the input and the output file are the same
        """
        if not getcwd().split('\\').__contains__('tests'):
            chdir("tests")

        copyfile('input.txt', 'input_test.txt')

        with open('input_test.txt', mode='r', encoding='utf-8') as input_file:
            input_lines = input_file.readlines()

        add_suffix('_suffix', 'input_test.txt')

        with open('input_test.txt', mode='r', encoding='utf-8') as input_file:
            output_lines = input_file.readlines()

        remove('input_test.txt')
        self.assertListEqual([line[:-1] + '_suffix\n' for line in input_lines], output_lines)

    def test_unexisting_input_file(self):
        """
        Test add_suffix function if the input file is not found
        """
        if not getcwd().split('\\').__contains__('tests'):
            chdir("tests")

        with self.assertRaises(FileNotFoundError):
            add_suffix('_suffix', 'unexisting_file.txt')


if __name__ == '__main__':
    unittest.main()
