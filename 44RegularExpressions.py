import re

text = "The quicl brown for jumps over the lazy dog."

# match = re.search("brown",text)
# print(match)

# if match:
#     print("Match found")
#     print("Start index:" , match.start())
#     print(("End index:" , match.end()))

matches = re.findall("the",text,re.IGNORECASE)
print(matches)