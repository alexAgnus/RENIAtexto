import psycopg2.extras
import psycopg2


hostname='localhost'
database='Renia_BD'
username='postgres'
pwd='12345678'
port_id=5432

conn=None
cur=None



try:
    conn = psycopg2.connect(
        host=hostname,
        dbname=database,
        user=username,
        password=pwd,
        port=port_id
    )
    cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)


    cur.execute('SELECT * FROM Persona')
    for record in cur.fetchall(): #fetchall, datos del DB
        #print(record[9])
        print( record[0],record[9])
        #print(record['idPrs'],record['apellidoPa'],record['senasParticulares'])
         #dato=record[9]
         #print(dato)
        #record[9]= record["senasParticulares']



    #cur.close()
    #conn.close()
except Exception as error:
    print(error)

#finally:
   # if cur is not None:
    #    conn.commit()
     #   cur.close()
    #if conn is not None:
     #   conn.commit()
      #  conn.close()


