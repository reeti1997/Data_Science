dict1 = {'fname':'John', 'lname':'Miller', 'profession':'plumber', 'age':'32'}
#each eelemeent is in key-value form.
#key = fname, lname, etc.
#value = John, Miller, etc.

dict1
#sorted output
#o/p : {'age': '32', 'fname': 'John', 'lname': 'Miller', 'profession': 'plumber'}

dict1['city'] = 'Jaipur'
#o/p : {'age': '32','city': 'Jaipur','fname': 'John','lname': 'Miller','profession': 'plumber'}

del dict1['city']

dict1.has_key('lname')
#o/p : True