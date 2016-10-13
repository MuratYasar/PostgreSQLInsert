#!/usr/bin/python3

import psycopg2

__version__ = '1.0.0'


class myDatabase:
    def __init__(self, **kwargs):
        """
        :param kwargs:
        hostname = '192.168.1.1'
        username = 'postgres'
        password = 'pass'
        database = 'postgres'
        port = '5432'
        tablename = 'RegisteredCompanies'
        """

        self._hostname = kwargs.get('hostname')
        self._username = kwargs.get('username')
        self._password = kwargs.get('password')
        self._database = kwargs.get('database')
        self._port = kwargs.get('port')
        self._schemaname = kwargs.get('schemaname')
        self._tablename = kwargs.get('tablename')
        self._con = None

    # hostname property
    @property
    def hostname(self):
        return self._hostname

    @hostname.setter
    def hostname(self, hn):
        self._hostname = hn

    # username property
    @property
    def username(self):
        return self._username

    @username.setter
    def username(self, un):
        self._username = un

    # password property
    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, pw):
        self._password = pw

    # database property
    @property
    def database(self):
        return self._database

    @database.setter
    def database(self, dtb):
        self._database = dtb

    # port property
    @property
    def port(self):
        return self._port

    @port.setter
    def port(self, prt):
        self._port = prt

    # schemaname property
    @property
    def schemaname(self):
        return self._schemaname

    @schemaname.setter
    def schemaname(self, sn):
        self._schemaname = sn

    # tablename property
    @property
    def tablename(self):
        return self._tablename

    @tablename.setter
    def tablename(self, tn):
        self._tablename = tn

    def create_connection(self):
        self._con = psycopg2.connect(host=self._hostname, user=self._username, password=self._password,
                                     dbname=self._database, port=self._port)
        return self._con

    def close_connection(self):
        if self._con:
            self._con.close()

    def insert(self, rec):
        try:
            klist = sorted(rec.keys())
            values = [rec[v] for v in klist]
            q = 'INSERT INTO "{}"."{}" ({}) VALUES ({})'.format(
                self._schemaname,
                self._tablename,
                ', '.join(map(lambda x: '"' + x + '"', klist)),
                ', '.join('%s' for i in range(len(values)))
            )

            self.create_connection()
            cursr = self._con.cursor()
            cursr.execute(q, values)
            __statusmessage = cursr.statusmessage
            self._con.commit()
            cursr.close()

            print("Insert status: ", str(__statusmessage))

        except (Exception, psycopg2.DatabaseError) as err:
            if self._con:
                self._con.rollback()

            print("Database insert error : ", str(err))
        finally:
            if self._con:
                self._con.close()


def start():
    pass


if __name__ == "__main__":
    start()
