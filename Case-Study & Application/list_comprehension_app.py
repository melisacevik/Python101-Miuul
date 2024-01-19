#################
# Görev 1) List Comprehension yapısı kullanarak car_crashes verisindeki numeric değişkenlerin isimlerini
# büyük harfe çeviriniz ve başına NUM ekleyiniz.
#################

import seaborn as sns
df = sns.load_dataset("car_crashes")
df.columns

["NUM_" + col.upper() for col in df.columns if df[col].dtype != 'O']

#################
# Görev 2) List Comprehensions yapısı kullanarak car_crashers verisinde isminde "no" barındırmayan
# değişkenlerin sonuna FLAG ekleyiniz.
#################

import seaborn as sns
df = sns.load_dataset("car_crashes")
df.columns

[col + "_FLAG" if 'no' not in str(df[col]) else col for col in df.columns]
