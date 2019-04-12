# v1.0.0

from import_hedgehogs import *

def createTopLevelURLs(ticker):
    """
    
    forms the links needed to download data later on

    Arguments:
        ticker: specific company ticker to collect data

    Returns:
        list of top level links for specific ticker

    """
    top_level_links = []
    top_level_link = "https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=" + ticker + "&type=10-Q&dateb=&owner=exclude&count=4"
    tl_link = Link('top_level_link', top_level_link)
    pre_soup = tl_link.getHTML()
    soup = BeautifulSoup(pre_soup, 'lxml')
    print("Creating Top Level URLs...")
    for doc in soup.find_all('a', attrs={'id' : 'interactiveDataBtn'}):
        top_level_links.append(str(doc['href']))
    return top_level_links

def createParseableUrls(top_level_links):
    """

    uses BeautifulSoup to create links to place data into xlsx files

    Arguments:
        top_level_links: top level links which are utilized to download data

    Returns:
        list of links which are properly formatted to be downloaded

    """
    header_link = "https://www.sec.gov"
    return_list = []
    print("Creating Parseable URLs...")
    for link in top_level_links:
        q10_link = Link('link', header_link + link)
        pre_soup = q10_link.getHTML()
        soup = BeautifulSoup(pre_soup, 'lxml')
        for xlxs in soup.find_all('a', attrs={'class' : 'xbrlviewer'}):
            if(xlxs.contents[0] == 'View Excel Document'):
                return_list.append(header_link + str(xlxs['href']))
    return return_list

def downloadXlxs(xlxs_links, ticker):
    """
    
    uses xlxs links and downloads them locally and renames them in proper folders

    Arguments:
        xlxs_links: full links to download stock data
        ticker: specific company ticker which we are collecting data

    """
    print("Downloading .xlxs files...")
    os.chdir('fin_data')
    os.mkdir(ticker)
    os.chdir(ticker)
    counter = 0
    for i in range(0,len(xlxs_links)):
        file = wget.download(xlxs_links[i], "")
    for i in os.listdir('.'):
        name = str(counter) + '.xlsx'
        os.rename(i, name)
        counter +=1

def initializer():
    """
    
    function which handles main program flow


    """
    cli_parser = OptionParser(
        usage='usage: %prog <input.xlsx> [output.json]'
        )
    (options, args) = cli_parser.parse_args()
    # Input file checks
    if len(args) < 1:
        cli_parser.error("You have to supply at least 1 argument")
    print("Version 2.5.0")
    client = MongoClient('localhost', 12345)
    if(client):
        print("Connected to MonogClient: localhost port 12345")
    ticker = sys.argv[1]
    topLevelLinks = createTopLevelURLs(ticker)
    parseLinks = createParseableUrls(topLevelLinks)
    downloadXlxs(parseLinks, ticker)

if __name__ == '__main__':
    initializer()