# CODTECH Internship - Task 1
# Big Data Analysis using Pure Python
# No external libraries required

import csv

file_name = "sales_data1.csv"

total_sales = 0
sales_count = 0
category_sales = {}

print("\nBIG DATA ANALYSIS USING PURE PYTHON\n")

with open(file_name, 'r') as file:
    reader = csv.DictReader(file)

    for row in reader:
        sales = float(row["Sales"])
        category = row["Category"]

        total_sales += sales
        sales_count += 1

        if category in category_sales:
            category_sales[category] += sales
        else:
            category_sales[category] = sales

print("Total Records Processed:", sales_count)

print("\nTotal Sales by Category:")
for cat, value in category_sales.items():
    print(cat, ":", value)

average_sales = total_sales / sales_count
print("\nAverage Sales:", round(average_sales, 2))

print("\nAnalysis Completed Successfully!")
