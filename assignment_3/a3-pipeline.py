import subprocess


def docker_compose():
    try:
        print("Performing docker compose deployments")
        
        # Run 'docker compose' command to build the Docker image from the current directory
        subprocess.run(["docker-compose", "up", "--build"], check=True)
    except subprocess.CalledProcessError as e:
        print("Error: Docker compose failed.")
        print(e)


if __name__ == "__main__":

    print("Triggering deployment of applications! :^) ")
    # Build the Docker image
    docker_compose()
