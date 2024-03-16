# SQL Introduction

## Description
This repository contains solutions to tasks related to SQL as part of the Holberton School curriculum.

## Concepts
For this project, we expect you to be familiar with the following concepts:
- Databases

## Resources
Read or watch:
- [What is Database & SQL?](https://www.youtube.com/watch?v=FR4QIeZaPeM)
- [Install MySQL (MySQL Server)](https://dev.mysql.com/doc/mysql-installation-excerpt/8.0/en/)
- [A Basic MySQL Tutorial](https://www.digitalocean.com/community/tutorials/a-basic-mysql-tutorial)
- [Basic SQL statements: DDL and DML](https://www.sqlservertutorial.net/sql-server-basics/sql-server-ddl-dml/)
- [Basic queries: SQL and RA](https://en.wikipedia.org/wiki/Relational_algebra)
- [SQL technique: functions](https://www.sqlshack.com/sql-functions/)
- [SQL technique: subqueries](https://www.mysqltutorial.org/mysql-subquery/)
- [What makes the big difference between a backtick and an apostrophe?](https://stackoverflow.com/questions/2940233/what-makes-the-big-difference-between-a-backtick-and-an-apostrophe)
- [MySQL Cheat Sheet](https://gist.github.com/bradtraversy/c831baaad44343cc945e76c2e30927b3)
- [MySQL 8.0 SQL Statement Syntax](https://dev.mysql.com/doc/refman/8.0/en/sql-syntax.html)

## Learning Objectives
At the end of this project, you are expected to be able to explain to anyone, without the help of Google:
- What’s a database?
- What’s a relational database?
- What does SQL stand for?
- What’s MySQL?
- How to create a database in MySQL?
- What does DDL and DML stand for?
- How to CREATE or ALTER a table?
- How to SELECT data from a table?
- How to INSERT, UPDATE or DELETE data?
- What are subqueries?
- How to use MySQL functions?

## Requirements
- Allowed editors: vi, vim, emacs
- All your files will be executed on Ubuntu 20.04 LTS using MySQL 8.0 (version 8.0.25)
- All your files should end with a new line
- All your SQL queries should have a comment just before (i.e. syntax above)
- All your files should start by a comment describing the task
- All SQL keywords should be in uppercase (SELECT, WHERE…)
- A `README.md` file, at the root of the folder of the project, is mandatory
- The length of your files will be tested using `wc`

## More Info
Comments for your SQL file:
```bash
$ cat my_script.sql
-- 3 first students in the Batch ID=3
-- because Batch 3 is the best!
SELECT id, name FROM students WHERE batch_id = 3 ORDER BY created_at DESC LIMIT 3;
$
$ sudo apt update
$ sudo apt install mysql-server
...
$ mysql --version
mysql  Ver 8.0.25-0ubuntu0.20.04.1 for Linux on x86_64 ((Ubuntu))
$
$ sudo mysql
Welcome to the MySQL monitor.  Commands end with ; or \g.
Your MySQL connection id is 11
Server version: 8.0.25-0ubuntu0.20.04.1 (Ubuntu)

Copyright (c) 2000, 2021, Oracle and/or its affiliates.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

mysql>
mysql> quit
Bye
$
Tasks
List databases

Write a script that lists all databases of your MySQL server.
0-list_databases.sql
Create a database

Write a script that creates the database hbtn_0c_0 in your MySQL server.
1-create_database_if_missing.sql
Delete a database

Write a script that deletes the database hbtn_0c_0 in your MySQL server.
2-remove_database.sql
List tables

Write a script that lists all the tables of a database in your MySQL server.
3-list_tables.sql
First table

Write a script that creates a table called first_table in the current database in your MySQL server.
4-first_table.sql
Full description

Write a script that prints the following description of the table first_table from the database hbtn_0c_0 in your MySQL server.
5-full_description.sql
List all in table

Write a script that lists all rows of the table first_table from the database hbtn_0c_0 in your MySQL server.
6-list_all_in_table.sql
First add

Write a script that inserts a new row in the table first_table (database hbtn_0c_0) in your MySQL server.
7-first_add.sql
Count 89

Write a script that displays the number of records with id = 89 in the table first_table of the database hbtn_0c_0 in your MySQL server.
8-count_89.sql
Full creation

Write a script that creates a table second_table in the database hbtn_0c_0 in your MySQL server and add multiple rows.
9-full_creation.sql
List by best

Write a script that lists all records of the table second_table of the database hbtn_0c_0 in your MySQL server.
10-list_by_best.sql
Select the best

Write a script that lists all records with a score >= 10 in the table second_table of the database hbtn_0c_0 in your MySQL server.
11-select_the_best.sql
Cheating is bad

Write a script that updates the score of Bob to 10 in the table second_table.
12-cheating_is_bad.sql
Score too low

Write a script that removes all records with a score <= 5 in the table second_table of the database hbtn_0c_0 in your MySQL server.
13-score_too_low.sql
Average

Write a script that computes the score average of all records in the table second_table of the database hbtn_0c_0 in your MySQL server.
14-average.sql
Number by score

Write a script that lists the number of records with the same score in the table second_table of the database hbtn_0c_0 in your MySQL server.
15-number_by_score.sql
Say my name

Write a script that lists all records of the table second_table of the database hbtn_0c_0 in your MySQL server.
16-say_my_name.sql