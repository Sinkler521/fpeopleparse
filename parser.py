from bs4 import BeautifulSoup
import requests

class FpeopleParser:
    def __init__(self, output_dir: str):
        self.url = 'https://www.fastpeoplesearch.com/'
        self.output_dir = output_dir

    def get_page_text(self, url):
        response = requests.get(url)
        if response.status_code == 200:
            return response.text
        else:
            print(f"Failed to fetch page: {url}")
            return None

    def parse(self, link):
        final_url = self.url + link
        page_text = self.get_page_text(final_url)
        if page_text:
            soup = BeautifulSoup(page_text, 'html.parser')
            result = self.process_parsed_data(soup)
            return result
        else:
            return None

    def process_parsed_data(self, soup) -> list: # here should be all the data
        """
        :param soup:
        :return list:
        First Name                                                                      0
        Last Name                                                                       1
        Age                                                                             2
        Current Home Full Address including city, state, zip, street address            3
        Beds                                                                            4
        Baths                                                                           5
        SqFt                                                                            6
        Year home was built                                                             7
        Estimated Value                                                                 8
        Estimated Equity                                                                9
        Last Sale Date                                                                  10
        Primary Phone Number                                                            11
        Phone Type (wireless/landline)                                                  12
        Email                                                                           13
        Occupancy Type                                                                  14
        Ownership Type                                                                  15
        """
        ...

    def parse_all_and_save(self, links: list):
        results = []
        for link in links:
            result = self.parse(link)
            if result:
                results.append(result)

        self.save(results)
        return


    def save(self, data): # should save to output
        ...


