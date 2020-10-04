def fileToByteStr(fileName):
    path = '/var/www/sitioweb/public_html/'+fileName
    try:
        flhand = open (path,'rb')
        str = flhand.read()
        #print(str)
        return [str]
    except:
        print('error reading file path: '+ path)

def select_BBDD(table_select):
# Connect to the database.
    import pymysql
    conn = pymysql.connect(
        db='BBDD_PANES',
        user='panes',
        passwd='password',
        host='localhost')
    c = conn.cursor()
# Print the contents of the database.
    string_select = 'SELECT * FROM ' + table_select
    c.execute(string_select)
    #records = c.fetchall()
    #print([(row[0], row[1]) for row in records])
    row = c.fetchone()
    value = row [1]
    #print (value)
    return [value]
