from pyzipcode import ZipCodeDatabase
zcdb = ZipCodeDatabase()
print [z.zip for z in zcdb.get_zipcodes_around_radius('91010', 5)]