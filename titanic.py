import pandas as pd
import matplotlib.pyplot as plt
import math
import statistics
import numpy

train_df = pd.read_csv('./train.csv')
test_df = pd.read_csv('./test.csv')
combine = [train_df, test_df]


def q7(feature):
  # Remove invalid values
  feature = feature[~numpy.isnan(feature)]

  print(len(feature))
  print(statistics.mean(feature))
  print(statistics.stdev(feature))
  print(min(feature))
  print(numpy.percentile(feature, 25))
  print(numpy.percentile(feature, 50))
  print(numpy.percentile(feature, 75))
  print(max(feature))

def q8(feature):
  print(len(feature))
  print(len(set(feature)))
  featureList = feature.values.tolist()
  most = max(feature.values, key=featureList.count)
  print(most)
  print(featureList.count(most))


# q7(test_df['Age'])
# q7(test_df['SibSp'])
# q7(test_df['Parch'])
# q7(test_df['Fare'])

# q8(train_df['Survived'])

# print(train_df.corr())

#df = pd.DataFrame(train_df, columns=["Sex", "Survived"])
#df['Sex'] = numpy.where(df['Sex'] == 'female', 1, 0)
#print(df.corr())

#df = pd.DataFrame(train_df, columns=["Age", "Survived"])
#df_survived = df.loc[df['Survived'] == 1]
#df_died = df.loc[df['Survived'] == 0]

#hist = df_survived.hist(column="Age")
#plt.suptitle("Survived")
#plt.show()

#hist = df_died.hist(column="Age")
#plt.suptitle("Died")
#plt.show()

#df = pd.DataFrame(train_df, columns=["Embarked", "Sex", "Fare", "Survived"])
#df = df.loc[df['Embarked'] == 'Q']
#df = df.loc[df['Survived'] == 1]

#df_male = df.loc[df['Sex'] == 'male']
#male_fare = statistics.mean(df_male['Fare'])
#df_female = df.loc[df['Sex'] == 'female']
#female_fare = statistics.mean(df_female['Fare'])

#df2 = pd.DataFrame({'Sex': ["Male", "Female"], 'Fare': [male_fare, female_fare]})

#hist = df2.plot.bar(x="Sex", y="Fare")
#plt.suptitle("Embarked = Q | Survived = 1")
#plt.show()

# df['Fare'] = numpy.where(df['Fare'] > -0.001 and df['Fare'] <= 7.91 , 0)
# df['Fare'] = numpy.where(df['Fare'] > 7.91 and df['Fare'] <= 14.454 , 1)
# df['Fare'] = numpy.where(df['Fare'] > 14.454 and df['Fare'] <= 31 , 2)
# df['Fare'] = numpy.where(df['Fare'] > 31 and df['Fare'] <= 512.329 , 3)

# mode_fare = statistics.mode(test_df['Fare'])
# df['Fare'] = df['Fare'][mode_fare if numpy.isnan(df['Fare'])]

input("Press Enter to Exit")