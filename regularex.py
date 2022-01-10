
import re

# pattern=r"ab+" //starts with ab
# pattern=r"ab$" //Ends with ab
# pattern=r"^ab" //starts with ab
# * meabs 0 or more
# + means one or more
# ? means 0 or one
pattern=r"[a-z]" # contains small character
match=re.match(pattern,"Z")
if match:
    print("Match")
else:
    print("Not match")