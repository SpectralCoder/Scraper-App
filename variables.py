import os
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())

## TODO Need to look for env-variables first
def get_var(var_name):
    temp_var = os.getenv(var_name)
    if (temp_var == None): temp_var = 'Missing'
    return temp_var