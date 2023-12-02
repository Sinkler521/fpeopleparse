Install such libraries via pip install:
1) bs4
2) requests-html
3) argparse

Program should be using with "python fpeopleparse.py [output file] [--arg]"

output file - filename. File will be created at output folder. Required argument
optional arguments:
1) --phone state_name (for example --phone alaska). Takes all the phone numbers depending on state code
2) --name name (for example --name John)
3) --surname surname (same)

For developers:
input/phone_codes.py contains dict with phone states as keys and list with phone codes as values
arguments_handler.py - argparse usage to 'read' and handle arguments. Now only --phone case is described. Returns urls to use in parser
parser.py - here should be parsing process of any page using url that we received with arguments_handler.py

So the algorithm is:
1) read arguments user used in command line
2) create urls using arguments_handler.py
3) parse these pages and save in .csv file

Task:
1) only --phone case creates links now, --name and --surname left. I have not found any open-source database of citizens, but maybe
any name and surname lists can be used to create combinations
2) parser does not work properly because of Cloudflare protection on this website
3) add library to work with csv files and use in parser

