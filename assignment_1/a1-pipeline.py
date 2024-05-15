import subprocess

container_name = "assignment-1"


def docker_build():
    try:
        # Run 'docker build' command to build the Docker image from the current directory
        subprocess.run(["docker", "build", "-t", container_name, "."], check=True)
        print("Docker build successful.")
    except subprocess.CalledProcessError as e:
        print("Error: Docker build failed.")
        print(e)


def docker_run():
    try:
        # Run 'docker run' command to run the built Docker image
        subprocess.run(
            ["docker", "run","--name", container_name, "-p", "5001:5000", "-d", container_name], check=True
        )
    except subprocess.CalledProcessError as e:
        print("Error: Docker run failed.")
        print(e)


if __name__ == "__main__":

    print("Triggering deployment of application! :^) ")
    # Build the Docker image
    docker_build()

    # Run the Docker container
    docker_run()
