# Assignment 1

For this assignment, modify the application to display any word of your choice on the webpage. Once you have modified the application code, deploy the changes by running the pipline and verify that the application's webpage is up and running. 

> [!NOTE]
> 1. The changes to the application can be seen at: `localhost:5001`. Port `5000` is the default port used by the application.  
> 2. The pipeline script always runs a container of the same name. This can lead to issues when trying to apply and deploy new chages to the application. Before applying changes to the application, by running the pipeline script, make sure that there's no existing container of the same name. You can remove existing containers by doing the following: 
> 
>    `docker container kill "name_of_container"` - to stop the desired container from running.\
>    `docker container rm "name_of_container"` - to remove the contianer entirely.  


> [!TIP]
> Take a look at `app.py`
