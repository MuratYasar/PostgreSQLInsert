#!/usr/bin/python3

import Database
import ReadExcel


def doJob():
    db = Database.myDatabase(hostname='127.0.0.1', username='postgres', password='muratyasar', database='postgres',
                             port=5432, schemaname='Test', tablename='RegisteredCompanies')
    db.create_connection()

    for index, line in enumerate(ReadExcel.readexcel()):
        db.insert(line)


if __name__ == '__main__':
    doJob()
