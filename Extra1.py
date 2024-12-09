l = {'తల్లి':'mother', 'నాన్న':'father', 'చెల్లెలు':'sister', 'బావ':'brother', 'కుటుంబం' :'family', 'తాతయ్య':'grandpa', 'నాన్న':'grandma', 'దుకాణం':'shop', 'మంచి':'good'}
key = input("Enter a word to check (in Telugu script): ")
if key in l.keys():
    print(f"The translation is: {l[key]}")
else:
    print("The word is not present in the dictionary")