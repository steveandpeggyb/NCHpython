from QueryADlibrary import SearchAD
username = "BCRInformatics"
SearchResults = SearchAD(username)
for row in SearchResults:
    print(row)
