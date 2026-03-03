#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  3 11:59:02 2026

@author: rumi
"""

import click

@click.command()
def greet():
    click.echo("Hello, World!")