#!/bin/sh
rm -f cpu.db
echo 'database init start'
sqlite3 cpu.db < db_init.sql
echo 'database init done'
