# SQL - More Queries

## Description
This repository contains SQL scripts focusing on various queries and database management tasks. These scripts were created as part of the "SQL - More Queries" project.

## Learning Objectives
By the end of this project, you should be able to:
- Create a new MySQL user and manage privileges for that user
- Understand concepts such as PRIMARY KEY, FOREIGN KEY, NOT NULL, and UNIQUE constraints
- Retrieve data from multiple tables using JOIN and UNION
- Utilize subqueries for complex queries
- Create and manage databases and tables
- Import and export SQL dumps

## Resources
To successfully complete this project, you should have a strong understanding of the following topics:
- Creating new users and granting permissions in MySQL
- Managing privileges using GRANT statements
- Understanding MySQL constraints
- Working with SQL techniques such as subqueries, joins, unions, and distinct keyword
- Utilizing MySQL cheat sheets and tutorials
- Additional resources on relational database model design, normalization, and ER modeling

## Requirements
- **Allowed Editors:** vi, vim, emacs
- **Operating System:** Ubuntu 20.04 LTS
- **MySQL Version:** 8.0.25
- All SQL queries should have comments just before them.
- File names should match the task numbers.
- All SQL keywords should be in uppercase.
- A README.md file is mandatory at the root of the project directory.

## Installation and Usage
1. **Install MySQL 8.0 on Ubuntu 20.04 LTS:**
$ sudo apt update
$ sudo apt install mysql-server

2. **Connect to MySQL server:**
$ sudo mysql

3. **Using the Sandbox:**
- Credentials: root/root
- Connect via SSH or Web terminal.
- Start MySQL server inside the container: `$ service mysql start`

4. **Import SQL Dump:**
$ echo "CREATE DATABASE hbtn_0d_tvshows;" | mysql -uroot -p
$ curl "https://s3.eu-west-3.amazonaws.com/hbtn.intranet.project.files/holbertonschool-higher-level_programming+/274/hbtn_0d_tvshows.sql" -s | mysql -uroot -p hbtn_0d_tvshows

markdown

5. **Running SQL Scripts:**
$ cat script_name.sql | mysql -hlocalhost -uroot -p database_name

## Tasks Overview
1. **0-privileges.sql:** Script to list all privileges of specified MySQL users.
2. **1-create_user.sql:** Script to create a new MySQL user with all privileges.
3. **2-create_read_user.sql:** Script to create a database and a user with read-only access.
4. **3-force_name.sql:** Script to create a table with a non-null name column.
5. **4-never_empty.sql:** Script to create a table with a non-null ID column and default value.
6. **5-unique_id.sql:** Script to create a table with a unique ID column.
7. **6-states.sql:** Script to create a database and a states table.
8. **7-cities.sql:** Script to create a database and a cities table with a foreign key constraint.
9. **8-cities_of_california_subquery.sql:** Script to list all cities of California without using JOIN.
10. **9-cities_by_state_join.sql:** Script to list all cities with their corresponding states using JOIN.
11. **10-genre_id_by_show.sql:** Script to list shows with at least one linked genre.
12. **11-genre_id_all_shows.sql:** Script to list all shows with their linked genres or NULL if none.
13. **12-no_genre.sql:** Script to list shows without any linked genre.
14. **13-count_shows_by_genre.sql:** Script to count shows by genre.
15. **14-my_genres.sql:** Script to list genres of a specific show.
16. **15-comedy_only.sql:** Script to list all Comedy shows.
17. **16-shows_by_genre.sql:** Script to list all shows and their linked genres.

## Authors
- Guillaume

## Acknowledgments
Special thanks to Holberton School for providing the necessary guidance and resources for this project.

## Tasks Overview
1. **0-privileges.sql:** Script to list all privileges of specified MySQL users.
2. **1-create_user.sql:** Script to create a new MySQL user with all privileges.
3. **2-create_read_user.sql:** Script to create a database and a user with read-only access.
4. **3-force_name.sql:** Script to create a table with a non-null name column.
5. **4-never_empty.sql:** Script to create a table with a non-null ID column and default value.
6. **5-unique_id.sql:** Script to create a table with a unique ID column.
7. **6-states.sql:** Script to create a database and a states table.
8. **7-cities.sql:** Script to create a database and a cities table with a foreign key constraint.
9. **8-cities_of_california_subquery.sql:** Script to list all cities of California without using JOIN.
10. **9-cities_by_state_join.sql:** Script to list all cities with their corresponding states using JOIN.
11. **10-genre_id_by_show.sql:** Script to list shows with at least one linked genre.
12. **11-genre_id_all_shows.sql:** Script to list all shows with their linked genres or NULL if none.
13. **12-no_genre.sql:** Script to list shows without any linked genre.
14. **13-count_shows_by_genre.sql:** Script to count shows by genre.
15. **14-my_genres.sql:** Script to list genres of a specific show.
16. **15-comedy_only.sql:** Script to list all Comedy shows.
17. **16-shows_by_genre.sql:** Script to list all shows and their linked genres.

## Authors
- Guillaume

## Acknowledgments
Special thanks to Holberton School for providing the necessary guidance and resources for this project.
