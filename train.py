#!/usr/bin/env python3
"""Train a model."""

from sys import path
from configparser import ConfigParser

from train_cli import parse_arguments

path.append('/app')


if __name__ == '__main__':
    args = parse_arguments()
    config_file = ConfigParser()
    config_file.read(args.config_file)
