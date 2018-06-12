# @file
# Implements Docker Engine API.
# @refs
# - https://github.com/docker/docker-py

import docker

class DockerEngine():
    client = None

    # Constructor.
    def __init__(self):
        self.client = docker.from_env()

    # Run container.
    def containerRun(self, image, cmd, opts=None):
        return self.client.containers.run(image, cmd, opts)

    # Get container.
    def containerGet(self, id):
        return self.client.containers.get(id)

    # List containers
    def containerList(self):
        return self.client.client.containers.list()

    # Pull container image.
    def imagePull(self, name):
        return self.client.images.pull(name)

    # List container images.
    def imageList(self):
        return self.client.images.list()