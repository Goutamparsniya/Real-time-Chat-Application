import re

def find_urls(input_string):
    url_pattern = re.compile(r'https?://\S+|www\.\S+')
    urls = re.findall(url_pattern, input_string)
    return urls

input_text = "This is a sentence with a URL: https://www.example.com. Another URL is www.another-url.com."
found_urls = find_urls(input_text)
if found_urls:
    print("URLs found in the input:")
    for url in found_urls:
        print(url)
else:
    print("No URLs found in the input.")
