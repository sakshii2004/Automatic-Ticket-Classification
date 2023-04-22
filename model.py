import pandas
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import seaborn as sb
import matplotlib.pyplot as plt
import sklearn.metrics as sm


student_data=pandas.read_excel("student_data.xlsx", sheet_name="Sheet1")
print(student_data.head())

student=student_data.iloc[:, 0:32]
student_target=student_data['G3']

#print(student_target.head())
#print(student.head())


#help(plt.figure)
#fig1=plt.figure(figsize=(30,30))
#help(sb.heatmap)
#heatmap=sb.heatmap(student_data.corr(), cbar=True, annot=True)
#plt.show()

X_train, X_test, y_train, y_test=train_test_split(student, student_target, random_state=0)

#print(X_train.shape, X_test.shape)

reg=LinearRegression()
reg.fit(X_train, y_train)

y_pred=reg.predict(X_test)

y_pred_df=pandas.DataFrame(y_pred)

#y_pred_new=np.round_(y_pred, decimals=0)

print(y_test)
print(y_pred_df)

coefficients=pandas.DataFrame(reg.coef_)
coefficients.index=student.columns



print(coefficients)

print("The intercept is: ",reg.intercept_)


print("R2 score =", round(sm.r2_score(y_test, y_pred), 2))
