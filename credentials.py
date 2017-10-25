#!/usr/bin/env python


def load(filename):
    with open(filename) as creds_file:
        (u, p) = creds_file.read().splitlines()
        return (u, p)
