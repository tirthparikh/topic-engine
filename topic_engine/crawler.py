import requests
from bs4 import BeautifulSoup
from boilerpipe.extract import Extractor

class Crawler:
    """Crawler is used to parse the html page and collect the data on which analysis can be done to find the topic"""

    def __init__(self, url):
        self.url = url
        self.res = None
        self.list_of_documents = []
        self.soup = None
    ##

    def check_connection(self, stream=False):
        """checks if the connection is made and returns the response, along with status as either True os False"""
        try:
            headers = {  # Some website threw 503 error codes as the user agent was not a browser
                'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 '
                              'Safari/537.36',
            }
            self.res = requests.get(self.url, stream=stream, headers=headers)
            self.res.raise_for_status()
            # Loading the parser with Html content
            self.soup = BeautifulSoup(self.res.text, 'html.parser')
            return True, self.res
        except requests.exceptions.MissingSchema:
            error = "Invalid URL " + self.url + ", Please remember to add http:// or the domain name "
        except requests.exceptions.HTTPError:
            error = "HTTPError :" + str(self.res.status_code)
        except requests.exceptions.Timeout:
            error = "Connection Timeout! Please retry."
        except requests.exceptions.TooManyRedirects:
            error = "Too Many Redirects! Please refresh check the URL"
        except requests.exceptions.ConnectionError:
            error = "Connection Error! PLease check you Connections"
        return False, error

    ##
    def extract_text(self, list_of_tags):
        return [t.getText() for t in list_of_tags]

    def get_title(self):
        """gets the text from the <title> tag"""
        if self.soup is None:
            raise NotImplementedError('Error: Parser has no Html , please check the ')

        title = self.soup.select('title')
        return self.extract_text(title)

    def get_metas(self):
        """Get the information from the <meta> which are specifically designed for signalling the
           search engines
        """
        if self.soup is None:
            raise NotImplementedError('Error: Parser has no Html , please check the ')

        metas = self.soup.select('meta[name="description"]')
        metas.extend(self.soup.select('meta[name="keywords"]'))
        metas = [t["content"] for t in metas]
        return metas

    def get_headings(self):
        if self.soup is None:
            raise NotImplementedError('Error: Parser has no Html , please check the ')

        headings = self.soup.find_all('h1')
        headings.extend(self.soup.find_all('h2'))
        headings.extend(self.soup.find_all('h3'))
        return self.extract_text(headings)

    def extract_main_text(self):
        if self.res is None:
            return None

        extractor = Extractor(  # extractor='ArticleExtractor',
                              url=self.url)
        return [extractor.getText()]

    def get_relevant_data(self):
        """This method finds data from the html tags which mostly contains data signaling the search engine about their
        content. Along with the tags , it will also try to extract other important piece of information ,
        like article or a blog so that later on , word frequency can be calculated"""
        if self.res is None:
            return None

        # -------------------------------------------------
        # Get Data from tags which are places as a signal
        # -------------------------------------------------
        self.list_of_documents.extend(self.get_title())
        self.list_of_documents.extend(self.get_metas())
        self.list_of_documents.extend(self.get_headings())

        # -------------------------------------------------
        # Get text from the most important content/article/
        # description
        # -------------------------------------------------
        self.list_of_documents.extend((self.extract_main_text()))
        return self.list_of_documents
