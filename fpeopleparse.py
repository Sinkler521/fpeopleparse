from arguments_handler import ArgumentsHandler
from parser import FpeopleParser as Fparser

if __name__ == '__main__':
    # initialize argparse object
    argshndl = ArgumentsHandler()
    output_dir, argument_links = argshndl.handle_arguments()  # get links depending on arguments

    # initialize parser object
    parser = Fparser(output_dir)

    # parse information
    parser.parse_all_and_save(argument_links)
