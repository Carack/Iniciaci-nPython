with open (archivo) as fh:
    count = 0
text = fh.read()
for character intext:
    if character.isupper():
        count += 1

