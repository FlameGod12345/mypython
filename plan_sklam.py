info = (1, u'GGS-04', u'John', u'Smith', 9, u'0')

for result in info:
    ln           = str(result[0])
    ggs          = str(result[1])
    first_name   = str(result[2])
    last_name    = str(result[3])
    dob          = str(result[4])
    spend        = str(result[5])
while True:
    res = raw_input("Enter points to add: ")
    try:
        int(res)
        break
    except:
        print("Please enter a number...")
        pass
spend = str(int(spend) + int(res))
db_curs.execute("UPDATE '" + db_name + "' (cID, first_name, last_name, date_of_birth, spend) VALUES ('" + srce + "', '" + first_name + "', '" + last_name + "', '" + dob + "' WHERE '" + spend + "')")
db_connection.commit()
