import pandas as pd


df = pd.read_csv("titanic.csv")

print("Original Dataset:")

print("\nDataset Shape:")
print(df.shape)

print("\nColumn Names:")
print(df.columns)

print("\nDataset Information:")
df.info()



print("\nMissing Values Before Cleaning:")
print(df.isnull().sum())

df["Age"] = df["Age"].fillna(df["Age"].median())

df["Fare"] = df["Fare"].fillna(df["Fare"].median())

df["Embarked"] = df["Embarked"].fillna(df["Embarked"].mode()[0])

df["Name"] = df["Name"].fillna("Unknown")
df["Ticket"] = df["Ticket"].fillna("Unknown")
df["Cabin"] = df["Cabin"].fillna("Unknown")

duplicates = df.duplicated().sum()

print("\nNumber of Duplicate Rows:", duplicates)

df = df.drop_duplicates()


df["Age"] = df["Age"].astype(float)
df["Fare"] = df["Fare"].astype(float)
df["Survived"] = df["Survived"].astype(int)
df["Pclass"] = df["Pclass"].astype(int)


df["Sex"] = df["Sex"].str.strip().str.lower()
df["Embarked"] = df["Embarked"].str.strip().str.upper()


print("\nMissing Values After Cleaning:")
print(df.isnull().sum())


print("\nCleaned Dataset:")
print(df.head())


df.to_csv("titanic_cleaned.csv", index=False)

print("\nCleaned dataset saved as titanic_cleaned.csv")