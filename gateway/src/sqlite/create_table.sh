#!/bin/sh
rm -f cpu.db
echo 'insert data'
sqlite3 cpu.db < insert.sql
echo 'insert done'
