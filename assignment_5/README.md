# Assignment 5 #
In this excercise we want you to replace PostgreSQL by MariaDB.

Some pointers:

- You will need to rebuild the Dockerfile with the additional MariaDB Connector/C package
- You will need to rebuild the app.py script to use MariaDB and not PostgreSQL
- You will need to rebuild the test_db.sql file as it is PostgreSQL specific
- You will need to rebuild the docker-compose.yml file to remove PostgreSQL and add MariaDB
- You will need to rebuild the requirements.txt file to use mariadb instead of the psycopg2-binary

Run the pipeline to deploy these applications and troubleshoot and solve any issues that you encounter.

> [!NOTE]
> `docker-compose down -v` - use this command to completely remove all applications deployed via docker-compose. Especially if you're running into issues running the pipeline consecutively.  


> [!TIP]
You live the DevOps\
You breathe the DevOps 


```
 
 __     __                               _____    ______     _     _                  _____                    ____                  _ 
 \ \   / /                       /\     |  __ \  |  ____|   | |   | |                |  __ \                  / __ \                | |
  \ \_/ /    ___    _   _       /  \    | |__) | | |__      | |_  | |__     ___      | |  | |   ___  __   __ | |  | |  _ __    ___  | |
   \   /    / _ \  | | | |     / /\ \   |  _  /  |  __|     | __| | '_ \   / _ \     | |  | |  / _ \ \ \ / / | |  | | | '_ \  / __| | |
    | |    | (_) | | |_| |    / ____ \  | | \ \  | |____    | |_  | | | | |  __/     | |__| | |  __/  \ V /  | |__| | | |_) | \__ \ |_|
    |_|     \___/   \__,_|   /_/    \_\ |_|  \_\ |______|    \__| |_| |_|  \___|     |_____/   \___|   \_/    \____/  | .__/  |___/ (_)
                                                                                                                      | |              
                                                                                                                      |_|
