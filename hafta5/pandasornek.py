import pandas as pd

df = pd.read_csv("hafta5\people.csv")
print(df.head())

filtreleme = df[df["yas"]>30]
print(f"Yasi 30 dan buyuk olanlar:\n {filtreleme}")

sorted_df = df.sort_values(["maas"], ascending=False)
print(f"Maaşa göre siralama:\n {sorted_df}")

sorted_df_filtreleme= df.groupby("departman") ["maas"]. mean()
print(f"Departmanlarina göre ortalama maas siralamasi:\n {sorted_df_filtreleme}")

print(f"Dosyanin Null değerler: \n{df.isnull().sum()}")
df.fillna(0, inplace = True)