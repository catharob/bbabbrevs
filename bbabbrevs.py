import csv

while True:
    with open('abbrevs.csv', 'rU') as csvfile:
        reader = csv.reader(csvfile)
        mydict = {rows[0]:rows[1] for rows in reader} # reads csv into a dictionary

    full_name = raw_input('Enter a thing you want to abbreviate: ')

    if full_name in mydict:
        print mydict[full_name] # match input with key in dictionary
    else:
        print "Oops, that's not in my abbreviation dictionary."
    
    while True: # now we want it to loop back to the start, in case we want to abbrev something else
        answer = raw_input('Want to abbreviate something else? (y/n): ')
        if answer in ('y', 'n'):
            break
        print "Oops, I didn't catch that. Try 'y' or 'n'."
    if answer == 'y':
        continue
    else:
        print 'Thanks, and have a great day!'
        break