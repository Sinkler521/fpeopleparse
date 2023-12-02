import argparse
from input.phone_codes import phone_codes


class ArgumentsHandler:
    def __init__(self):
        self.arghandler = argparse.ArgumentParser(description='To run program with arguments')
        self.__initialize_arguments(self.arghandler)

    def __initialize_arguments(self, arghandler):
        arghandler.add_argument('outdir') # output file path, starts with folder 'output'
        arghandler.add_argument(
            '--name',
            type=str,
            help='Search optional argument, if we want to search by name',
        )
        arghandler.add_argument(
            '--surname',
            type=str,
            help='Search optional argument, if we want to search by surname',
        )
        arghandler.add_argument(
            '--phone',
            type=str,
            help='Search optional argument, if we want to search by phone (state code specifically)'
        )

    def handle_arguments(self) -> tuple: # first argument is path to output dir and second is data
        args = self.arghandler.parse_args()

        if args.phone:
            state_name = args.phone
            result = self.search_by_phone(state_name)
            print('Phones numbers generated')
            return f'output/{args.outdir}', result

        # TODO continue if statement for name and surname. Search can be either or, so do not use both name-surname and phone

    def __generate_numbers_partial(self, area_code):
        result_list = []
        for middle in range(100, 120):
            for last in range(10000):
                formatted_number = f"{area_code}-{str(middle).zfill(3)}-{str(last).zfill(4)}"
                result_list.append(formatted_number)
        return result_list

    def search_by_phone(self, state_name: str) -> list: # example 907-501-9766
        result_list = []
        area_codes = phone_codes.get(state_name.capitalize(), [])
        for area_code in area_codes:
            partial_numbers = self.__generate_numbers_partial(area_code)
            result_list.extend(partial_numbers)
        return result_list
