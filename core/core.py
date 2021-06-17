import docker
import json

from github import Github
from datetime import datetime
import os

import tarfile
from io import BytesIO

from dotenv import load_dotenv

# Loading .env
load_dotenv()

"""
Initialize docker
"""

client = docker.from_env()

VERSION = client.version()

separator = "------------------------"

"""
Getting files from GitHub
"""


def get_files_from_repo(repo_name):
    g = Github()
    repo = g.get_repo(repo_name)


"""
Tar stuff for inserting files into container
"""


def create_tar_archive():
    tar_stream = BytesIO()

    tar = tarfile.TarFile(fileobj=tar_stream, mode='w')

    info = tarfile.TarInfo()


# All the functions necessary for running stage


def start_container(image="ubuntu", **kwargs):
    detach_opt = False
    if kwargs["daemon"]:
        detach_opt = True
    return client.containers.run(image, kwargs["commands"], detach=detach_opt, hostname=kwargs["hostname"],
                                 ports=kwargs["port"],
                                 user="stage", name=kwargs["name"])


def create_container(image="ubuntu", **kwargs):
    detach_opt = False
    if kwargs["detach"]:
        detach_opt = True
    return client.containers.create(image, kwargs["commands"], detach=detach_opt, hostname=kwargs["hostname"],
                                    ports=kwargs["port"],
                                    user="stage", name=kwargs["name"])


def list_containers():
    containers = client.containers.list(all=True)
    for container in containers:
        print(container.name)
        print(container.status)
        print(separator)


def prune_containers(filters):
    return client.containers.prune(filters=filters)


def add_files_to_container(container):
    container.put_archive('')


# Container manipulation methods, has to take in a container object
def get_container_output(container):
    return container.logs(stream=True)


def get_container_info(container):
    info = {
        "name": container.name,
        "image": container.image,
        "status": container.status
    }
    return info


def pause_container(container):
    container.pause()


def unpause_container(container):
    container.unpause()


def restart_container(container):
    container.restart(timeout=15)


def kill_container(container):
    container.kill()


# Stage functions

def create_stage():
    pass
