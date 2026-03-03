
import numpy as np
import pandas as pd
import click

taskDf=pd.DataFrame(data={"task":["Task","None","None2"],"status":[True,False,False],"due_time":["now","None","None2"]},columns=["task","status","due_time"])

@click.command()
def list():
    print(taskDf[taskDf.status==True])

@click.command()
def input():
    status=input("What is the status of your task? ")
    due_time=input("When is the task due? ")

def _addTask():
    task=input("Add task:")
    # True for unfinished
    taskDf.loc[len(taskDf)]=["a","b"]



    

# def _markDone():
    
