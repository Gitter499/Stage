# Stage

A new way to develop and host

## Idea

Hosting can be pretty challenging sometimes and rather annoying. For Stage, 
I want to build a tool which uses a JSON build config and the GitHub API to
automatically deploy and host applications in the cloud. This includes automatic deploys
from GitHub and other DevOps features. However, this is not a hosting service. It is meant
to be self hosted on a VPS. 

## Architecture

I decided to use Python for this project given it's simple nature as well as
the extensive library support. Each application is going to be ran on a container. In 
order to build the container, the user will provide a simple build file (using JSON for now) 
to specify build instructions. On top of that, Stage will have automation tools like auto-deploy
from GitHub and much more.

## The challenge

Whilst I've been programming for a year now, I've been mostly doing JS/TS and Java projects. I know python
but am very much inexperienced with it. I am also new to the world of cloud computing, so this project
is going to involve a lot of learning.

## Road-map

- [ ] Run containers in the background and fetch stdout, stderr logs on command.
- [ ] Provide a command for stdin. 
- [ ] Basic container management commands, not meant to replace the docker CLI
- [ ] Code retrieval from GitHub API
- [ ] Interpreting stage.json to get container commands and build instructions
- [ ] More advanced GitHub API features for auto-deploying
- [ ] Configuring a environment variables through stage.json
- [ ] Advanced networking for adding automatic sub-domains (base domain is user provided)
- [ ] API for interacting with a frontend remotely
- [ ] Adding more features