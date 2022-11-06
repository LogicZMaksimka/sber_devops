#!/bin/sh
sleep 2
PGPASSWORD=123456 psql -h "db" -U postgres -a -f /postgres_setup/fill.sql