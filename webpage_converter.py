import pdfkit
config = pdfkit.configuration(wkhtmltopdf = r"C:\\Program Files\\wkhtmltopdf\\bin\\wkhtmltopdf.exe") 

in_url = input("Paste url here : ") 

url_split = in_url.split(".")
web_name = url_split[1]

pdfkit.from_url(in_url,'.\webpage_to_pdf\\Output\\' + web_name +'.pdf', configuration = config) 