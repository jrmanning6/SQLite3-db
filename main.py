import sqlite3

from sqlite3 import Error

con = sqlite3.connect('printers1.db')
c = con.cursor()

# def sql_printers_table(con):

#     c = con.cursor()

#     c.execute("CREATE TABLE printer(id integer INT_AUTOINCREMENT PRIMARY KEY, printer_name text, printer_status text)")

#     con.commit()

# def sql_printables_table(con):
#     c = con.cursor()
#     c.execute("CREATE TABLE printables(id integer PRIMARY KEY, printable_name text, volume real, FOREIGN KEY (id) REFERENCES printer(printer_status))")
#     con.commit()

# sql_printers_table(con)
# sql_printables_table(con)

# many_printers = [ (1, 'Lulzbot', 'Ready'),
#                    (2, 'Makerbot', 'Ready'),
#                    (3, 'Creality', 'Busy'),
#                    (4, 'Prusa','Ready'),
#                    (5, 'Geetech', 'Busy')
#                  ]

# c.executemany("INSERT INTO printer VALUES(?, ?, ?)", many_printers)

# many_printables =[
#                      (1,'3D Benchy', 100),
#                      (2,'V29 Whistle', 300),
#                      (3,'Digital Sundial', 500),
#                      (4,'Modular Hex Drawer', 600),
#                      (5,'Baby Yoda', 1000)
#                  ]
# c.executemany("INSERT INTO printables VALUES(?, ?, ?)", many_printables)

# c.execute('SELECT * FROM printer JOIN printables')
# rows = c.fetchall()
# for row in rows:
#     print(row)

def main():
    while True:
        action = input("What action would you like to perform? ")
    
        if action == "Add":
            sql_insert()
    
        elif action == "Delete":
            _id = input("Enter the id for the printer you wish to delete: ")
            sql_delete(_id)
    
        elif action == "Update":
            _id = input("Enter the id of the printer you wish to update: ")
            _status = input("What is the status of the printer? ")
            sql_update(_id, _status)
    
        elif action == "Search":
            input_variable = int(input("Enter an id to search for: "))
            _id = input_variable - 1
            sql_search_by_id(_id)

        elif action == "Db":
            c.execute('SELECT * FROM printer JOIN printables')
            rows = c.fetchall()
            for row in rows:
                print(row)
        
        if action == "Print":
            sql_print_printable()
           
        else:
            print("Invalid action entered")
        
        return 0

def sql_insert():
    printer_id_input = input("What is the id of the printer: ")
    printer_name_input = input("What is the name of the printer: ")
    printer_status_input = input("what is the status of the printer: ")
    c.execute("INSERT INTO printer VALUES(?, ?, ?)", (printer_id_input, printer_name_input, printer_status_input))
    con.commit()
    print("Printer added")

def sql_update(_id, _status):
    c.execute("UPDATE printer SET printer_status = (?) WHERE id = (?)", (_status, _id))
    con.commit()
    print("Printer updated")

def sql_delete(_id):
    c.execute("DELETE FROM printer WHERE id =(?)", (_id))
    con.commit()
    print("Printer deleted")

def sql_search_by_id(_id):
    c.execute('SELECT * FROM printer')
    rows = c.fetchall()
    print(rows[_id])

def sql_print_printable():
    c.execute('SELECT id, printer_name FROM printer WHERE printer_status !="Busy"') 
    #WHERE printer_status != "Busy"')
    rows = c.fetchall()
    print("Available printers:")
    for row in rows:
        print(row)

    c.execute('SELECT id, printable_name FROM printables')
    printables = c.fetchall()
    print("Available printables:")
    for row in printables:
        print(row)
    
    printable_input = int(input("Enter the id for the printable you wish to print: "))
    printer_input = int(input("Enter the id for the printer you wish to use: "))
    printable_input_int = printable_input - 1
    printer_input_int = printer_input - 1
    printer_id = str(printer_input_int)
    printer_id_ = str(printer_input)
    print("Printing: ")
    c.execute('SELECT printable_name FROM printables')
    logs1 = c.fetchall()
    print(logs1[printable_input_int])
    c.execute('SELECT printer_name FROM printer')
    logs = c.fetchall()
    print(logs[printer_input_int])
    _status = "Busy"
    con.commit()    
    return auto_update(printer_id_, _status)


def auto_update(_id, _status):
    # _id_int = int(_id + 1)
    # _id_str = str(_id_int)
    _status = "Busy"
    c.execute("UPDATE printer SET printer_status = (?) WHERE id = (?)", (_status, _id))
    con.commit()

while True:
    main()

con.commit()
