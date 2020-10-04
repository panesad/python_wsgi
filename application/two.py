def gen_html():
# Open file
    path = '/var/www/sitioweb/public_html/two.html'
    flhand = open (path,'r')
    str = flhand.read()

# Connect to the database.
    import pymysql
    conn = pymysql.connect(
        db='BBDD_PANES',
        user='panes',
        passwd='password',
        host='localhost')
    c = conn.cursor()

# Get Name
    string_select = 'SELECT * FROM tabla_1' 
    c.execute(string_select)
    #records = c.fetchall()
    #print([(row[0], row[1]) for row in records])
    row = c.fetchone()
    value = row [1]
    output = str % (value)
    output = bytes(output, encoding='utf-8')
    print (output)
    return [output]
