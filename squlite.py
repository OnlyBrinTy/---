import sqlite3 
class AcPas: 
    def __init__(self, name): 
        self.name = name
        
con = sqlite3.connect(self.name) 
cur = con.cursor() 
result = cur.execute(f"""SELECT id FROM ships WHERE name = ?""", (ship,)).fetchone() 
id_ship = result[0] 
res = cur.execute(f"""SELECT * FROM accounting 
                    WHERE date = ? and ship_id = ?""", (date, id_ship)).fetchall()
con.close()
