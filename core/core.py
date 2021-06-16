import docker
import json
from github import Github
from datetime import datetime
import os

"""
Initialize docker
"""

client = docker.from_env()


def start_container(image="ubuntu"):
    client.containers.run(image, "echo hello world")


start_container()
