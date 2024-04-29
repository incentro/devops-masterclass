# Devops Masterclass
This repositories contains all the assignments meant to accompany the Devops masterclass for the collaboration between DXT and BA.

## Explanation of Assignments 
In this repository you will find several assignments meant to simulate the Devops experience when working with CI/CD automation along with its possible challenges. You can expect the challenge of these assignments to progressively increase as you work through them. 

Each assignment contains the following files:
- ***Pipeline Script***: meant to simulate automated deployments.
- ***Application Script***: meant to be the codebase for the deployment
- ***Dockerfile***: the docker file used to build application locally as containers. 

The applications as well as the pipeline scripts are all written in Python. The pipeline scripts have been written this way in order to mitigate OS compatibility issues. 

Before you begin, take a good look at the requirements and pipeline instructions below and ensure that you have all the necessary installations.  

## Requirements 

### Hardware Requirements

You will need a Windows, MacOS or Linux based system with at least `8GB RAM` and `10GB of free disk space` available.

### Software Requirements

- If you don't already have it installed make sure to install [git](https://git-scm.com/downloads) in order to clone this repository to your local machine. It doesn't really matter what tool you use for this just make sure that you have some way of working with git.   

- You will need also need to install [docker](https://docs.docker.com/engine/install/) and [docker compose](https://docs.docker.com/compose/install/) if not already installed to be able to run Docker containers.

- To use the exercise files and make modifications, you will need an IDE or text editor like [Visual Studio Code](https://code.visualstudio.com/download) or [Vim](https://www.vim.org/download.php)

- Make sure that you have [Python](https://wiki.python.org/moin/BeginnersGuide/Download) installed on your local machine. 


## Running the Pipelines
As mentioned above, the pipelines are all Python scripts. Run the following command to perform a pipeline deployment:`python pipeline_name.py`

> [!NOTE] 
> Each assignment can be found in their own directory. When running the pipeline scripts, make sure that you are running it from within in the correct assingment directory.  


> [!TIP]
If you already have Python on your machine and would like to perform these assignments wihtin an isolated environmnt, follow these steps: 
>  ### Install and create environment
> Run `pip install virtualenv` \
> then `virtualenv venv`
>
> ### Activate environment
> Windows - `venv\Scripts\activate` \
> Linux - `source ./venv/bin/activate`
