import pandas
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import pickle


student_data=pandas.read_excel("student_data.xlsx", sheet_name="Sheet1")

student=student_data.iloc[:, 0:32]
student_target=student_data['G3']


X_train, X_test, y_train, y_test=train_test_split(student, student_target, random_state=0)
reg=LinearRegression()
reg.fit(X_train, y_train)

pickle.dump(reg, open('model.pkl','wb'))