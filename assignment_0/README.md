# Assignment 0

This is an introductory assignment and is meant to get you familiar with the structure of the upcoming challenges. Additionally, this assignment is a brief guide on performing actions that subsequent assignements will expect you to perform.

**To complete this assignment deploy the application with the pipeline and verify that the application is working**

In order to complete this task we first need to take a look at the assignment components:

- `app.py`: This is the Python application that we want to deploy and verify. Any changes to the application is made in this file.    
- `a0-pipeline.py`: This python script represents a CI/CD pipeline for automated deployments. In order to deploy the desired application we need to run this code or in other words the "pipeline". This python script builds and runs a container locally using the `app.py` as the source code.    
- `Dockerfile`: This file contains all the steps taken while the pipeline script is building the docker container.

Now that you have a bit of context regarding the important components, perform the following steps to complete this assignment:
1. Make sure that you are performing all the commands in the appropriate directory. In the case of this assignment make sure you are working in `(your_local_path_to)/assignment_0`.
2. Use the pipeline to deploy the application. To do this, run the pipline's python script by performing the command 
   
   ``` bash
   python a0_pipeline.py
   ```    
   or

    ``` bash
    python3 a0_pipeline.py
    ```    
3. After this pipeline has completed its task use the command `docker ps` to get an overview of currently running containers. You can also view this overview in Docker Desktop if you are using that tool. 
4. Once the previous steps have been successful, verify that the application's webpage up and running. The pipeline script runs the container locally and makes it accessible via port "5001". Open up your browser and enter the following in the search bar: `http://localhost:5001/`. If all went well you should see a green welcome page.

By following these steps you have successfully completed this assignemnt and can move on to the rest. Before moving on be sure stop and remove the container that you deployed.    

> [!NOTE]
> 1. The changes to the application can be seen at: `localhost:5001`. Port `5000` is the default port used by the application.  
> 2. The pipeline script always runs a container of the same name. This can lead to issues when trying to apply and deploy new chages to the application. Before applying changes to the application, by running the pipeline script, make sure that there's no existing container of the same name. You can remove existing containers by doing the following: 
> 
>    `docker container kill "name_of_container"` - to stop the desired container from running.\
>    `docker container rm "name_of_container"` - to remove the contianer entirely.  


