from QueryADlibrary import SearchAD
import pprint

username = "BCRInformatics"

results = SearchAD(username)

for x in results:
    print(x)

pprint.pprint(results)
