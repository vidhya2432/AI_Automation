import pandas as pd

df = pd.read_csv("Students Performance Dataset (1).csv")

total_students = len(df)

print("\nTotal Students:", total_students)

## MISSING VALUES 

missing_values = df.isnull().sum()

print(missing_values)

total_missing = df.isnull().sum().sum()

print("\nTotal Missing Values:", total_missing)

# FIND DUPLICATES

duplicate_count = df.duplicated().sum()

print("\nDuplicate Records:", duplicate_count)


# FIND INVALID MARKS

mark_columns = [
    "Midterm_Score",
    "Final_Score",
    "Assignments_Avg",
    "Quizzes_Avg",
    "Participation_Score",
    "Projects_Score",
    "Total_Score"
]


invalid_records = pd.Series(
    False,
    index=df.index
)


for column in mark_columns:

    invalid_records = invalid_records | (
        (df[column] < 0) |
        (df[column] > 100)
    )


invalid_count = invalid_records.sum()

print("\nInvalid Records:", invalid_count)

# CLEAN INVALID RECORDS

cleaned_df = df[~invalid_records].copy()

print(
    "\nRecords after removing invalid data:",
    len(cleaned_df)
)

# REMOVE DUPLICATES

cleaned_df = cleaned_df.drop_duplicates()

print(
    "Records after removing duplicates:",
    len(cleaned_df)
)

# FILL MISSING NUMERIC VALUES

numeric_columns = cleaned_df.select_dtypes(
    include="number"
).columns


for column in numeric_columns:

    cleaned_df[column] = cleaned_df[column].fillna(
        cleaned_df[column].median()
    )

# FILL MISSING TEXT VALUES

text_columns = cleaned_df.select_dtypes(
    include="object"
).columns


for column in text_columns:

    if cleaned_df[column].isnull().any():

        cleaned_df[column] = cleaned_df[column].fillna(
            cleaned_df[column].mode()[0]
        )


print("\nMissing values cleaned successfully.")

# FIND TOPPER

topper_index = cleaned_df["Total_Score"].idxmax()

topper_name = (
    cleaned_df.loc[topper_index, "First_Name"]
    + " "
    + cleaned_df.loc[topper_index, "Last_Name"]
)

topper_mark = cleaned_df.loc[
    topper_index,
    "Total_Score"
]

# FIND STATISTICS


highest_mark = cleaned_df["Total_Score"].max()

lowest_mark = cleaned_df["Total_Score"].min()

average_mark = cleaned_df["Total_Score"].mean()

# COUNT DEPARTMENTS

engineering_students = (
    cleaned_df["Department"] == "Engineering"
).sum()


cs_students = (
    cleaned_df["Department"] == "CS"
).sum()

#  DISPLAY FINAL RESULTS

print("Total Students:", len(cleaned_df))

print(
    "Average Mark:",
    round(average_mark, 2)
)

print(
    "Highest Mark:",
    highest_mark
)

print(
    "Lowest Mark:",
    lowest_mark
)

print(
    "Topper:",
    topper_name
)

print(
    "Topper Mark:",
    topper_mark
)

print(
    "Engineering Students:",
    engineering_students
)

print(
    "CS Students:",
    cs_students
)

print(
    "Invalid Records:",
    invalid_count
)

print(
    "Duplicate Records:",
    duplicate_count
)

# GENERATE TEXT REPORT

report = f"""
STUDENT PERFORMANCE REPORT
==========================

Total Students: {len(cleaned_df)}

Average Mark: {average_mark:.2f}

Highest Mark: {highest_mark}

Lowest Mark: {lowest_mark}

Topper: {topper_name}

Topper Mark: {topper_mark}

Engineering Students: {engineering_students}

CS Students: {cs_students}

Invalid Records: {invalid_count}

Duplicate Records: {duplicate_count}

Missing Values Found: {total_missing}
"""

# SAVE REPORT

with open(
    "student_performance_report.txt",
    "w"
) as file:

    file.write(report)


# SAVE CLEANED DATASET

cleaned_df.to_csv(
    "Students_Performance_Cleaned.csv",
    index=False
)



print("\n" + report)

print(
    "Report saved as: student_performance_report.txt"
)

print(
    "Cleaned dataset saved as: Students_Performance_Cleaned.csv"
)