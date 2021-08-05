# url handling module

# ! urllib.request for
# ? opening and reading.
import urllib.request
# request_url  = urllib.request.urlopen('https://www.geeksforgeeks.org/')
# print(request_url.read())

#! urllib.parse for
# ? parsing URLs

from urllib.parse import urlparse,urlunparse,parse_qs,parse_qsl
parsed_url = urlparse('https://www.f3motorauctions.com.au/simulcast.aspx')
print('parsed_url',parsed_url)

# now we will discuss urlunparse

unparsed_url = urlunparse(parsed_url)
print('unparsed_url',unparsed_url)


#! parse_qs,parse_qsl
t = parse_qs('https://www.carrefouruae.com/api/v5/zones/072/search/categories/F1600000?filter=&sortBy=relevance&currentPage=1&pageSize=60&areaCode=Dubai%20Festival%20City%20-%20Dubai&lang=en&expressPos=003&displayCurr=AED')
print(t)

t = parse_qsl('https://www.carrefouruae.com/api/v5/zones/072/search/categories/F1600000?filter=&sortBy=relevance&currentPage=1&pageSize=60&areaCode=Dubai%20Festival%20City%20-%20Dubai&lang=en&expressPos=003&displayCurr=AED')
print(t)

# !URL split, urlunsplit,  