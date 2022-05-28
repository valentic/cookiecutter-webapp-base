#!/bin/sh

./v1/sitecmd config \
    siteroot={{cookiecutter.siteroot}} \
    release={{cookiecutter.release}} \
    project={{cookiecutter.project_slug}} \
    port={{cookiecutter.development_port}}


