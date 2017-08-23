import sys

import crawler
import engine


def main():
    # ----------------------------
    # Welcome Screen
    # ----------------------------
    left_width = 40
    print("-" * left_width)
    print("|" + "Topic Engine".center(left_width - 2, " ") + "|")
    print("-" * left_width)
    print("This engine will take any URL and identify the most relevant topics on the page.\n"
          "Please enter a valid URL below to get proper results\n"
          "Example: http://www.google.com \n\n")

    url = input("Enter the Url or press q/Q to quit: ")

    # Check for empty url
    while not url:
        print("Please enter some address to a webpage, Empty Url are not valid")
        url = input("Enter the Url or press q/Q to quit: ")

    if url == "q" or url == "Q":
            sys.exit(1)

    # ----------------------------
    # Creating Crawler object
    # ----------------------------
    crawl_obj = crawler.Crawler(url)

    print("Attempting to connect {}".format(url))
    connected, response = crawl_obj.check_connection(url)
    if not connected:
        print("An Error occurred!")
        print(response)

        # Code to retry for a finite number of attempts

        sys.exit(1)

    # Connection successful, pass the response content to the parser to get the list of the topic
    # supporting only text/html for now
    content_type = response.headers['content-type'].split(";")[0]
    if content_type != 'text/html':
        print("Sorry, "+content_type+" is not supported right now")
        sys.exit(1)

    # Fetching potentially useful texts to finally analyze important topics
    list_of_documents = crawl_obj.get_relevant_data()
    eng = engine.Engine(list_of_documents)

    relevant_content = eng.top_n_terms(4)

    print("The relevant terms are : ")
    for terms in relevant_content:
        print(terms)


if __name__ == '__main__':
    main()
