import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm
from scipy import stats

"""
MATRIX: 654 × 6
0) age – a positive integer (years)
1) FEV1 – a continuous valued measurement (liter)
2) height – a continuous valued measurement (inches) • 
3) gender – binary (female: 0, male: 1)
4) smoking status – binary (non-smoker: 0, smoker: 1) • 
5) weight – a continuous valued measurement (kg)
"""

#EXERCISE 1

data = np.loadtxt("smoking.txt")

### Assigning values for smokers and non-smokers
smokers = data[(data[:,4] == 1)]
non_smokers = data[(data[:,4] == 0)]


### Function calculating mean

def meanFEV1(data_input):
    return np.mean(data_input)


### Checking mean lung capacity for smokers and non-smokers
smokers_FEV1 = smokers[:,1]
non_smokers_FEV1 = non_smokers[:,1]

smokers_FEV1_mean = meanFEV1(smokers_FEV1)
non_smokers_FEV1_mean = meanFEV1(non_smokers_FEV1)

print(smokers_FEV1_mean, "is the mean FEV1 of smokers.")
print(non_smokers_FEV1_mean, "is the mean FEV1 of non_smokers.")





#EXERCISE 2: Box plot for FEV1 for smokers and non-smokers
#https://matplotlib.org/gallery/pyplots/boxplot_demo_pyplot.html#sphx-glr-gallery-pyplots-boxplot-demo-pyplot-py


data_FEV1 = smokers_FEV1, non_smokers_FEV1
labels = ['smokers', 'non_smokers']
plt.figure()
plt.boxplot(data_FEV1, labels=labels)
plt.title('lung capacity for smokers and non_smokers')
plt.ylabel('continuous valued measurement in liter')




#EXERCISE 3: Degrees Of Freedom, and Student's T-Test

### Degrees of Freedom: Calculated with formula from Thomas' Slides

std1 = np.std(smokers_FEV1, ddof = 1) #ddof1 = unbiased
std2 = np.std(non_smokers_FEV1, ddof = 1) #ddof1 = unbiased

n_x = len(smokers_FEV1)
n_y = len(non_smokers_FEV1)

v_dof = ((std1**2/n_x) + (std2**2/n_y))**2
v_dof = v_dof / ((std1**4)/((n_x**2)*(n_x-1))) + ((std2**4)/((n_y**2)*(n_y-1)))
v_dof = np.floor(v_dof)
print('degrees of freedom: ', v_dof)


### This function computes Independent Samples t-test
### Returns t-statistic, p-value, and whether null hypothesis is accepted or rejected 

def hyptest(data1,data2):
  t,p = stats.ttest_ind(data1,data2)
  print('t-statistic: ',t) 
  print('p-value: ',p)
  
  a = 0.05

  if p > a:
    return 'Null hypothesis that smokers and non-smokers have the same fev1 mean is accepted'
  else:
    return 'Null hypothesis that smokers and non-smokers have the same fev1 mean is rejected'


print(hyptest(smokers_FEV1, non_smokers_FEV1))





#EXERCISE 4: 2D Plot And Correlation

### Scatter plot illustrating age versus FEV1

smokers_age = smokers[:,0]
non_smokers_age = non_smokers[:,0]

plt.figure()
plt.scatter(smokers_age,smokers_FEV1, label='smokers', s=25, alpha = 0.3)
plt.scatter(non_smokers_age,non_smokers_FEV1, label='non-smokers', s=25, alpha = 0.3)
plt.xlabel('age')
plt.ylabel('FEV1')
plt.title('Age versus FEV1')
plt.legend()


### Outputs correlation between age and FEV1

all_fev1 = data[:,1]
all_age = data[:,0]

print('correlation between age and FEV1: ', np.corrcoef(all_age, all_fev1))





#EXERCISE 5: Histogram

plt.figure()
plt.hist(non_smokers[:,0], 16, label="non-smokers")
plt.hist(smokers[:,0], 16, label="smokers")
plt.title("age distribution, non-smokers and smokers")
plt.xlabel("age")
plt.ylabel("participants")
plt.legend()

plt.show(block=False)
input("press <ENTER> to close window")







###################################### exercises to discuss data (not imporant for TA) ######################

#print(non_smokers.shape)
#print(smokers.shape)

#print(len(non_smokers), 'are non_smokers')
#print(len(smokers), 'are smokers')

#print(len(smokers[(smokers[:,3] == 0)]), "females are smokers")
#print(len(smokers[(smokers[:,3] == 1)]), "males are smokers")

#print(len(non_smokers[(non_smokers[:,3] == 0)]), "females are non-smokers")
#print(len(non_smokers[(non_smokers[:,3] == 1)]), "males are non-smokers")

#print(smokers[(smokers[:,0] == 9)], "are 9 years old")
