import sys
from urllib.parse import urlparse, parse_qs

def extract_params(url):
    parsed_url = urlparse(url)
    query_params = parse_qs(parsed_url.query)
    filtered_params = {key: ''.join(filter(str.isalpha, value[0])) for key, value in query_params.items() if key in ['p', 'l']}
    return filtered_params

if len(sys.argv) != 2:
    print("Ange endast en URL som ett argument.")
    sys.exit(1)
    
url = sys.argv[1]
params = extract_params(url)
print("occupation_field: ", params["p"])
print("kommun: ", params["l"])
