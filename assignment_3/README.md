# Assignment 3
For this assignment `docker-compose` is used (by the pipeline) to deploy the `app.py` application along with a Postgresql database as it's dependency. This application simply displays the content of the database after a successful connection. 

Run the pipeline to deploy these applications and troubleshoot and solve any issues that you may encounter.
> [!NOTE]
> `docker-compose down -v` - use this command to completely remove all applications deployed via docker-compose. Especially if you're running into issues running the pipeline consecutively.  


> [!TIP]
> Take a look at `docker-compose.yml` \
> Take a look at `app.py`