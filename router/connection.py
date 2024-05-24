import mysql.connector
import time

class Connecter:
    def __init__(self) -> None:
        self.DB = mysql.connector.connect(
            host="182.213.254.158",
            port="3306",
            user="diddmstjr",
            password="soso0909@",
            database="User_DB"
        )
        self.token = []

    def Connection(self, SQL):
        cursor = self.DB.cursor()
        cursor.execute(SQL)
        result = cursor.fetchall()
        return result

    def sql_select(self, SQL):
        try:
            result = self.Connection(SQL)
            if len(result) > 0:
                return {"kind" : "ok", "msg" : "Search Passed", "val" : result} 
            else:
                return {"kind" : "fail", "msg" : "None Searched"}
        except:
            print("\033[1;31m" + "SQL SELECT - Error: " + "\033[0m" + SQL)
            return {"kind" : "fail", "msg" : "Query Error"}

    def thread_read_token(self):
        while True:
            SQL = f"SELECT Token FROM Token"
            res = self.sql_select(SQL)
            if res is not None and res["kind"] == "ok":
                self.token.append(res["val"])
                time.sleep(60)