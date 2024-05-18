import matplotlib.pyplot as plt

# plt.plot([1,3,5,7],[0,1,2,3],'ro-.')

plt.plot(['banana','apple','orange'],[10,19,15],"ro--",label="last year")
plt.bar(['banana','apple','orange'],[10,20,17],color="green",label="current year")

plt.legend()
plt.show()