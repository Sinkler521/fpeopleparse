from requests_html import HTMLSession
from bs4 import BeautifulSoup


class FpeopleParser:
    def __init__(self, output_dir: str):
        self.url = 'https://www.fastpeoplesearch.com/'
        self.output_dir = output_dir

    def process_parsed_data(self, soup) -> list: # here should be all the data processing
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
            result_html = self.get_html_js(link)  # run all js code and receive html
            if result_html:
                result = self.parse(result_html)  # try to parse all data
                if result:
                    results.append(result)

        self.save(results)
        return

    def get_html_js(self, url):
        session = HTMLSession()
        try:
            response = session.get(url)
            response.html.render()  # run js
            return response.html.html
        except Exception as e:
            print(f"Error: {e}")
            return None

    def parse(self, html_text): # here should be parsing of all existing webpages by calling self.process_parsed_data
        ...

    def parse_example_page(self): # test func
        url = 'https://www.fastpeoplesearch.com/573-291-7083'
        html_text = self.get_html_js(url)
        soup = BeautifulSoup(html_text, 'html.parser')

    def save(self, data):  # should save to output
        ...
