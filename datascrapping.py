from urllib.request import urlopen
url = "http://olympus.realpython.org/profiles/aphrodite"
page = urlopen(url)
html_bytes = page.read()
html = html_bytes.decode("utf-8")
print(html)

# extraction using string method
title_index = html.find("<title>")
print(title_index)

# to get the index of title itself
start_index = title_index + len("<title>")
print(start_index)

# index of closing tag 
end_index = html.find("</title>")
print(end_index)

# extracting the title
title = html[start_index:end_index]
print(title)
