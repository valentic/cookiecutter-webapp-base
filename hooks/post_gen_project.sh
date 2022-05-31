#!/bin/sh

./v1/sitecmd config \
    siteroot={{cookiecutter.siteroot}} \
    branch={{cookiecutter.project_branch}} \
    release={{cookiecutter.release}} \
    project={{cookiecutter.project_slug}} \
    port={{cookiecutter.development_port}}


