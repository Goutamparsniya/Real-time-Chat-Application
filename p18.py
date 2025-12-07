import re
def extract_dates(paragraph):
    date_pattern = r'\b(\d{1,2}/\d{1,2}/\d{4})\b'
    dates = re.findall(date_pattern, paragraph)
    return dates

paragraph = input("Enter a paragraph: ")
dates_found = extract_dates(paragraph)
if dates_found:
    print("Dates found in the paragraph:")
    for date in dates_found:
        print(date)
else:
    print("No dates found in the paragraph.")
