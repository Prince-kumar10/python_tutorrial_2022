import re
mystr = '''Tata Limited
Dr. David Landsman, executive director
18, Grosvenor Place
London SW1X 7HSc
Phone: +44 (20) 7235 8281
Fax: +44 (20) 7235 8727
Email: tata@tata.co.uk
Website: www.europe.tata.com
Directions: View map

Tata Sons, North America
1700 North Moore St, Suite 1520
Arlington, VA 22209-1911
USA
Phone: +1 (703) 243 9787
Fax: +1 (703) 243 9791
66-66
455-4545
Email: northamerica@tata.com 
Website: www.northamerica.tata.com
Directions: View map fass
harry bhai lekin 
babut hi badia aadmi aiiii   '''

# findall ,split ,search,sub,finditer

# patt = re.compile(r"fass")

# . Any character (except newline character)
# patt = re.compile(r".")

# ^ Starts with
# patt = re.compile(r"^Tata")

# $ Ends with
# patt = re.compile(r"aadmi$")

# * Zero or more occurrences
# patt = re.compile(r"a*i*")

# + One or more occurrences
# patt = re.compile(r"ai+")

# {} Exactly the specified number of occurrences
# patt = re.compile(r"ai{2}")

# | Either or
# patt = re.compile(r"ai{1}|fa")

# special sequence
# patt = re.compile(r'\ATata')
# patt = re.compile(r'27\b')
patt = re.compile(r'\d{5}-\d{4}')


matchas= patt.finditer(mystr)

for match in matchas:
    print(match)
    #span = print(mystr[448:452])
