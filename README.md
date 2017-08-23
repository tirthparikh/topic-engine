# Content Finder

In SEO, it’s important to write good content and signal to the search engines what your article or page is about.
One way to ensure that is by focusing your content on the core topics. This engine will take any URL and identify the
most relevant topics on the page.

## My Approach

* From what I have researched, almost all webpages love to be seen in top of 
SERP. For that, they try to signal the websites by injecting keywords and Relevant content in the HTML tags such as 
```<meta name="description" /> , <title>, <h1>-<h3>, <span>, <strong> ,<img alt="">, <link title="">```
and more like that. 

* Along with that , the webpage content are written such that the relevant keywords are place strategically and repeated
 as much as logically
 possible in the article or description.

* The goal of my program was to collect all the details from the tags responsible for holding 
relevant content information and also extract the data from the article . 
This text data, or documents are then passed to the engine, where it uses the 
```nltk``` library to judge the type of keywords in the documents and count the number of
times the keyword appears. 

* There was no need to include a list of stopwords because ```nltk``` already rejects that by judging them for what type
 of words they are

* My program has two important files
    * crawler.py
        * this module handles the ```http requests``` to the web page using the ```check_connection()``` , parses the 
        html content using the ```get_relevant_data()```
        and returns the list of text data.
    * engine.py
        * This module accepts the list of texts fetched from the html tags and main content and calculate the word 
        density, return the list of top n terms 
        with the help of ```top_n_terms(n)```

* Though this is not the only factor used by the search engines to rank the webpages. But this approach can be a start.
## Getting Started

To run the Program, please run the TopicEngine/topic-engine/run.py.
Once you run the program , it will will guide you on it's own

```
(venv) tirthparikh$ python TopicEngine/topic-engine/run.py 
```

### Prerequisites

The requirements are mentioned in the requirements.txt
```
beautifulsoup4==4.6.0
boilerpipe==1.3.0.0
JPype1==0.6.2
nltk==3.2.4
numpy==1.13.1
pytest==3.1.3
requests==2.18.2
```

### Installing

A step by step series of examples that tell you have to get a development env running

Install a Virtual Environment to get started.

```
$ virtualenv venv
```

Install the dependencies using pip
```
pip install -r requirements.txt
```

And copy the files to any directory and run the program from there

## Built With

* [Pycharm] - The IDE for python from Jetbrains
* [Pip] - Dependency Management
* [BeautifulSoup] - Used to Parse HTMl
* [Requests] - Used to make http requests
* [NLTK] - Used for Natural Language processing

## Authors

* **Tirthkumar Parikh** - *Initial work* 
**tirthmparikh@gmail.com**
#

