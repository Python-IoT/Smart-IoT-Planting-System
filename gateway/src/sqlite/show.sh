#!/bin/sh
DBNAME="cpu.db"
echo 'all data in this database:'
sqlite3 $DBNAME "SELECT * FROM temps;"

echo 'Reverse chronological order:'
sqlite3 $DBNAME "select * from temps ORDER BY tdatetime DESC;"

echo 'latest 3 hours data:'
date
sqlite3 $DBNAME "SELECT * FROM temps
                where tdatetime > datetime('now', 'localtime', '-3 hours')
                ORDER BY tdatetime ASC;"
