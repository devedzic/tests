#!/usr/bin/env python
# coding: utf-8

# # Import functions from another notebook

# Test different external packages recommended on Stackoverflow for this functionality, and the assumption that "if \_\_name__ == '\_\_main__'" is necessary in the external .ipynb file in order to make the  import in the desired way.

# In[1]:


# # This does not work in JupyterLab, only in Jupyter Notebook
# %run external_test_functions.ipynb

# # This does not work in JupyterLab, only in Jupyter Notebook
# !pip install nbimporter
# import nbimporter
# from external_test_functions.ipynb import return_1
# from external_test_functions import return_1

# # This does not work in JupyterLab, only in Jupyter Notebook
# !pip install import-ipynb
# import import_ipynb
# from external_test_functions.ipynb import return_1
# from external_test_functions import return_1


# In[2]:


# This works in both JupyterLab and Jupyter Notebook
get_ipython().system('pip install ipynb')


# In[3]:


from ipynb.fs.full.external_test_functions import *  # imports functions and top-level variables from an external script AND runs the external script 
                                                     # (so it is necessary to have   if __name__ == '__main__' in the external script)
# from ipynb.fs.full.external_test_functions import return_1  # imports a function AND runs the external script (so it is necessary to have   if __name__ == '__main__' in the external script)
# from ipynb.fs.defs.external_test_functions import return_1  # just imports class and function definitions from the external script
# import ipynb.fs.full.external_test_functions  # just imports the external script NAME, so running a function from that script must be of the form <script name>.<function>


# In[4]:


# ipynb.fs.full.external_test_functions.return_1()

# print(return_1())
# print(EXTERNAL)
EXTERNAL


# # Test debugger

# In[5]:


def return_sum(a, b):
    sum = a + b
    return sum


# In[6]:


a = 5
b = 6
c = 7
sum = return_sum(a, b)


# # # Test magic functions
#
# # In[7]:
#
#
# get_ipython().run_line_magic('pinfo', '%magic')
#
#
# # In[8]:
#
#
# get_ipython().run_line_magic('magic', '')
#
#
# # In[9]:
#
#
# get_ipython().run_line_magic('pinfo', '%%writefile')
#
#
# # In[10]:
#
#
# get_ipython().run_cell_magic('writefile', 't1.py', "'''Testing %%writefile\n'''\n\n\ndef return_1():\n    '''A simple function\n    '''\n    \n    return 1\n")
#
#
# # In[11]:
#
#
# get_ipython().run_cell_magic('writefile', '-a t1.py', "\n\ndef return_2():\n    '''Another simple function\n    '''\n    \n    return 2\n")
#
