import argparse

parser = argparse.ArgumentParser("CLI Tool for Stage")

parser.add_argument("build", help="Builds project using config")
parser.add_argument("make", help="Make a project")
parser.add_argument("cc", help="Create container")

parser.parse_args()
