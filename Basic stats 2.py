# -*- coding: utf-8 -*-
"""
Created on Thu Jan 30 07:18:20 2020

@author: srira
"""

emp_datacsv
emp_datacsv.columns
emp_datacsv.Salary_hike.skew()
emp_datacsv.Salary_hike.kurt()
emp_datacsv.Salary_hike.mean()
emp_datacsv.Salary_hike.median()
emp_datacsv.Churn_out_rate.mode()

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

plt.bar(height=emp_datacsv.Salary_hike, x=np.arange(1,12,1))

emp_datacsv.shape

emp_datacsv.describe()

plt.hist(emp_datacsv.Salary_hike)

plt.boxplot(emp_datacsv.Salary_hike)

plt.boxplot(emp_datacsv.Salary_hike, vert=0)

help(print)
help(plt.boxplot)
