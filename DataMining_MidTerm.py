#!/usr/bin/env python
# coding: utf-8

# ## Creating csv files

# ### No need to run if csv files are downloaded already

# In[ ]:


#Amazon Transactions
data = [
    {"Transaction ID": "Trans1", "Books": "A Beginner’s Guide, Java: The Complete Reference, Java For Dummies, Android Programming: The Big Nerd Ranch"},
    {"Transaction ID": "Trans2", "Books": "A Beginner’s Guide, Java: The Complete Reference, Java For Dummies"},
    {"Transaction ID": "Trans3", "Books": "A Beginner’s Guide, Java: The Complete Reference, Java For Dummies, Android Programming: The Big Nerd Ranch, Head First Java 2nd Edition"},
    {"Transaction ID": "Trans4", "Books": "Android Programming: The Big Nerd Ranch, Head First Java 2nd Edition, Beginning Programming with Java"},
    {"Transaction ID": "Trans5", "Books": "Android Programming: The Big Nerd Ranch, Beginning Programming with Java, Java 8 Pocket Guide"},
    {"Transaction ID": "Trans6", "Books": "A Beginner’s Guide, Android Programming: The Big Nerd Ranch, Head First Java 2nd Edition"},
    {"Transaction ID": "Trans7", "Books": "A Beginner’s Guide, Head First Java 2nd Edition, Beginning Programming with Java"},
    {"Transaction ID": "Trans8", "Books": "Java: The Complete Reference, Java For Dummies, Android Programming: The Big Nerd Ranch"},
    {"Transaction ID": "Trans9", "Books": "Java For Dummies, Android Programming: The Big Nerd Ranch, Head First Java 2nd Edition, Beginning Programming with Java"},
    {"Transaction ID": "Trans10", "Books": "Beginning Programming with Java, Java 8 Pocket Guide, C++ Programming in Easy Steps"},
    {"Transaction ID": "Trans11", "Books": "A Beginner’s Guide, Java: The Complete Reference, Java For Dummies, Android Programming: The Big Nerd Ranch"},
    {"Transaction ID": "Trans12", "Books": "A Beginner’s Guide, Java: The Complete Reference, Java For Dummies, HTML and CSS: Design and Build Websites"},
    {"Transaction ID": "Trans13", "Books": "A Beginner’s Guide, Java: The Complete Reference, Java For Dummies, Java 8 Pocket Guide, HTML and CSS: Design and Build Websites"},
    {"Transaction ID": "Trans14", "Books": "Java For Dummies, Android Programming: The Big Nerd Ranch, Head First Java 2nd Edition"},
    {"Transaction ID": "Trans15", "Books": "Java For Dummies, Android Programming: The Big Nerd Ranch"},
    {"Transaction ID": "Trans16", "Books": "A Beginner’s Guide, Java: The Complete Reference, Java For Dummies, Android Programming: The Big Nerd Ranch"},
    {"Transaction ID": "Trans17", "Books": "A Beginner’s Guide, Java: The Complete Reference, Java For Dummies, Android Programming: The Big Nerd Ranch"},
    {"Transaction ID": "Trans18", "Books": "Head First Java 2nd Edition, Beginning Programming with Java, Java 8 Pocket Guide"},
    {"Transaction ID": "Trans19", "Books": "Android Programming: The Big Nerd Ranch, Head First Java 2nd Edition"},
    {"Transaction ID": "Trans20", "Books": "A Beginner’s Guide, Java: The Complete Reference, Java For Dummies"}
]

# Define the CSV file path
csv_file = "amazon.csv"

# Write the data to the CSV file
with open(csv_file, mode='w', newline='') as file:
    fieldnames = ['Transaction ID', 'Books']
    writer = csv.DictWriter(file, fieldnames=fieldnames)

    writer.writeheader()
    for row in data:
        writer.writerow(row)

print(f"CSV file '{csv_file}' has been created.")


# In[ ]:


#BestBuy Transactions
data1 = [
    {"Transaction ID": "Trans1", "Items": "Desk Top, Printer, Flash Drive, Microsoft Office, Speakers, Anti-Virus"},
    {"Transaction ID": "Trans2", "Items": "Lab Top, Flash Drive, Microsoft Office, Lab Top Case, Anti-Virus"},
    {"Transaction ID": "Trans3", "Items": "Lab Top, Printer, Flash Drive, Microsoft Office, Anti-Virus, Lab Top Case, External Hard-Drive"},
    {"Transaction ID": "Trans4", "Items": "Lab Top, Printer, Flash Drive, Anti-Virus, External Hard-Drive, Lab Top Case"},
    {"Transaction ID": "Trans5", "Items": "Lab Top, Flash Drive, Lab Top Case, Anti-Virus"},
    {"Transaction ID": "Trans6", "Items": "Lab Top, Printer, Flash Drive, Microsoft Office"},
    {"Transaction ID": "Trans7", "Items": "Desk Top, Printer, Flash Drive, Microsoft Office"},
    {"Transaction ID": "Trans8", "Items": "Lab Top, External Hard-Drive, Anti-Virus"},
    {"Transaction ID": "Trans9", "Items": "Desk Top, Printer, Flash Drive, Microsoft Office, Lab Top Case, Anti-Virus, Speakers, External Hard-Drive"},
    {"Transaction ID": "Trans10", "Items": "Digital Camera, Lab Top, Desk Top, Printer, Flash Drive, Microsoft Office, Lab Top Case, Anti-Virus, External Hard-Drive, Speakers"},
    {"Transaction ID": "Trans11", "Items": "Lab Top, Desk Top, Lab Top Case, External Hard-Drive, Speakers, Anti-Virus"},
    {"Transaction ID": "Trans12", "Items": "Digital Camera, Lab Top, Lab Top Case, External Hard-Drive, Anti-Virus, Speakers"},
    {"Transaction ID": "Trans13", "Items": "Digital Camera, Speakers"},
    {"Transaction ID": "Trans14", "Items": "Digital Camera, Desk Top, Printer, Flash Drive, Microsoft Office"},
    {"Transaction ID": "Trans15", "Items": "Printer, Flash Drive, Microsoft Office, Anti-Virus, Lab Top Case, Speakers, External Hard-Drive"},
    {"Transaction ID": "Trans16", "Items": "Digital Camera, Flash Drive, Microsoft Office, Anti-Virus, Lab Top Case, External Hard-Drive, Speakers"},
    {"Transaction ID": "Trans17", "Items": "Digital Camera, Lab Top, Lab Top Case"},
    {"Transaction ID": "Trans18", "Items": "Digital Camera, Lab Top Case, Speakers"},
    {"Transaction ID": "Trans19", "Items": "Digital Camera, Lab Top, Printer, Flash Drive, Microsoft Office, Speakers, Lab Top Case, Anti-Virus"},
    {"Transaction ID": "Trans20", "Items": "Digital Camera, Lab Top, Speakers, Anti-Virus, Lab Top Case"}
]

# Define the CSV file path for Transaction Type 1
csv_file1 = "BestBuy.csv"

# Write the data to the CSV file for Transaction Type 1
with open(csv_file1, mode='w', newline='') as file1:
    fieldnames1 = ['Transaction ID', 'Items']
    writer1 = csv.DictWriter(file1, fieldnames=fieldnames1)

    writer1.writeheader()
    for row1 in data1:
        writer1.writerow(row1)

print(f"CSV file '{csv_file1}' for BestBuy Transactions has been created.")


# In[ ]:


#Kmart Transactions

data2 = [
    {"Transaction ID": "Trans1", "Items": "Decorative Pillows, Quilts, Embroidered Bedspread"},
    {"Transaction ID": "Trans2", "Items": "Embroidered Bedspread, Shams, Kids Bedding, Bedding Collections, Bed Skirts, Bedspreads, Sheets"},
    {"Transaction ID": "Trans3", "Items": "Decorative Pillows, Quilts, Embroidered Bedspread, Shams, Kids Bedding, Bedding Collections"},
    {"Transaction ID": "Trans4", "Items": "Kids Bedding, Bedding Collections, Sheets, Bedspreads, Bed Skirts"},
    {"Transaction ID": "Trans5", "Items": "Decorative Pillows, Kids Bedding, Bedding Collections, Sheets, Bed Skirts, Bedspreads"},
    {"Transaction ID": "Trans6", "Items": "Bedding Collections, Bedspreads, Bed Skirts, Sheets, Shams, Kids Bedding"},
    {"Transaction ID": "Trans7", "Items": "Decorative Pillows, Quilts"},
    {"Transaction ID": "Trans8", "Items": "Decorative Pillows, Quilts, Embroidered Bedspread"},
    {"Transaction ID": "Trans9", "Items": "Bedspreads, Bed Skirts, Shams, Kids Bedding, Sheets"},
    {"Transaction ID": "Trans10", "Items": "Quilts, Embroidered Bedspread, Bedding Collections"},
    {"Transaction ID": "Trans11", "Items": "Bedding Collections, Bedspreads, Bed Skirts, Kids Bedding, Shams, Sheets"},
    {"Transaction ID": "Trans12", "Items": "Decorative Pillows, Quilts"},
    {"Transaction ID": "Trans13", "Items": "Embroidered Bedspread, Shams"},
    {"Transaction ID": "Trans14", "Items": "Sheets, Shams, Bed Skirts, Kids Bedding"},
    {"Transaction ID": "Trans15", "Items": "Decorative Pillows, Quilts"},
    {"Transaction ID": "Trans16", "Items": "Decorative Pillows, Kids Bedding, Bed Skirts, Shams"},
    {"Transaction ID": "Trans17", "Items": "Decorative Pillows, Shams, Bed Skirts"},
    {"Transaction ID": "Trans18", "Items": "Quilts, Sheets, Kids Bedding"},
    {"Transaction ID": "Trans19", "Items": "Shams, Bed Skirts, Kids Bedding, Sheets"},
    {"Transaction ID": "Trans20", "Items": "Decorative Pillows, Bedspreads, Shams, Sheets, Bed Skirts, Kids Bedding"}
]

# Define the CSV file path for Transaction Type 2
csv_file2 = "Kmart.csv"

# Write the data to the CSV file for Transaction Type 2
with open(csv_file2, mode='w', newline='') as file2:
    fieldnames2 = ['Transaction ID', 'Items']
    writer2 = csv.DictWriter(file2, fieldnames=fieldnames2)

    writer2.writeheader()
    for row2 in data2:
        writer2.writerow(row2)

print(f"CSV file '{csv_file2}' for Kmart Transactions has been created.")


# In[ ]:


#nike transactions

data3 = [
    {"Transaction ID": "Trans1", "Items": "Running Shoe, Socks, Sweatshirts, Modern Pants"},
    {"Transaction ID": "Trans2", "Items": "Running Shoe, Socks, Sweatshirts"},
    {"Transaction ID": "Trans3", "Items": "Running Shoe, Socks, Sweatshirts, Modern Pants"},
    {"Transaction ID": "Trans4", "Items": "Running Shoe, Sweatshirts, Modern Pants"},
    {"Transaction ID": "Trans5", "Items": "Running Shoe, Socks, Sweatshirts, Modern Pants, Soccer Shoe"},
    {"Transaction ID": "Trans6", "Items": "Running Shoe, Socks, Sweatshirts"},
    {"Transaction ID": "Trans7", "Items": "Running Shoe, Socks, Sweatshirts, Modern Pants, Tech Pants, Rash Guard, Hoodies"},
    {"Transaction ID": "Trans8", "Items": "Swimming Shirt, Socks, Sweatshirts"},
    {"Transaction ID": "Trans9", "Items": "Swimming Shirt, Rash Guard, Dry Fit V-Nick, Hoodies, Tech Pants"},
    {"Transaction ID": "Trans10", "Items": "Swimming Shirt, Rash Guard, Dry"},
    {"Transaction ID": "Trans11", "Items": "Swimming Shirt, Rash Guard, Dry Fit V-Nick"},
    {"Transaction ID": "Trans12", "Items": "Running Shoe, Swimming Shirt, Socks, Sweatshirts, Modern Pants, Soccer Shoe, Rash Guard, Hoodies, Tech Pants, Dry Fit V-Nick"},
    {"Transaction ID": "Trans13", "Items": "Running Shoe, Swimming Shirt, Socks, Sweatshirts, Modern Pants, Soccer Shoe, Rash Guard, Tech Pants, Dry Fit V-Nick, Hoodies"},
    {"Transaction ID": "Trans14", "Items": "Running Shoe, Swimming Shirt, Rash Guard, Tech Pants, Hoodies, Dry Fit V-Nick"},
    {"Transaction ID": "Trans15", "Items": "Running Shoe, Swimming Shirt, Socks, Sweatshirts, Modern Pants, Dry Fit V-Nick, Rash Guard, Tech Pants"},
    {"Transaction ID": "Trans16", "Items": "Swimming Shirt, Soccer Shoe, Hoodies, Dry Fit V-Nick, Tech Pants, Rash Guard"},
    {"Transaction ID": "Trans17", "Items": "Running Shoe, Socks"},
    {"Transaction ID": "Trans18", "Items": "Socks, Sweatshirts, Modern Pants, Soccer Shoe, Hoodies, Rash Guard, Tech Pants, Dry Fit V-Nick"},
    {"Transaction ID": "Trans19", "Items": "Running Shoe, Swimming Shirt, Rash Guard"},
    {"Transaction ID": "Trans20", "Items": "Running Shoe, Swimming Shirt, Socks, Sweatshirts, Modern Pants, Soccer Shoe, Hoodies, Tech Pants, Rash Guard, Dry Fit V-Nick"}
]

# Define the CSV file path for Transaction Type 3
csv_file3 = "nike.csv"

# Write the data to the CSV file for Transaction Type 3
with open(csv_file3, mode='w', newline='') as file3:
    fieldnames3 = ['Transaction ID', 'Items']
    writer3 = csv.DictWriter(file3, fieldnames=fieldnames3)

    writer3.writeheader()
    for row3 in data3:
        writer3.writerow(row3)

print(f"CSV file '{csv_file3}' for nike Transaction has been created.")


# In[ ]:


# Generic Transactions
data4 = [
    {"Transaction ID": "Trans1", "Items": "A, B, C"},
    {"Transaction ID": "Trans2", "Items": "A, B, C"},
    {"Transaction ID": "Trans3", "Items": "A, B, C, D"},
    {"Transaction ID": "Trans4", "Items": "A, B, C, D, E"},
    {"Transaction ID": "Trans5", "Items": "A, B, D, E"},
    {"Transaction ID": "Trans6", "Items": "A, D, E"},
    {"Transaction ID": "Trans7", "Items": "A, E"},
    {"Transaction ID": "Trans8", "Items": "A, E"},
    {"Transaction ID": "Trans9", "Items": "A, C, E"},
    {"Transaction ID": "Trans10", "Items": "A, C, E"},
    {"Transaction ID": "Trans11", "Items": "A, C, E"}
]

# Define the CSV file path for Transaction Type 4
csv_file4 = "Generic.csv"

# Write the data to the CSV file for Transaction Type 4
with open(csv_file4, mode='w', newline='') as file4:
    fieldnames4 = ['Transaction ID', 'Items']
    writer4 = csv.DictWriter(file4, fieldnames=fieldnames4)

    writer4.writeheader()
    for row4 in data4:
        writer4.writerow(row4)

print(f"CSV file '{csv_file4}' for Generic Transaction has been created.")


# ## Implementation of algorithms

# In[10]:


import csv
import itertools
import time
from mlxtend.preprocessing import TransactionEncoder
from mlxtend.frequent_patterns import apriori, association_rules, fpgrowth
import pandas as pd

#Brute Force
def brute_force(transactions, min_support, min_confidence):
    items = set(item for transaction in transactions for item in transaction)
    itemsets = []
    for i in range(1, len(items) + 1):
        itemsets.extend(itertools.combinations(items, i))
    frequent_itemsets = {}
    for itemset in itemsets:
        frequency = sum(1 for transaction in transactions if set(itemset).issubset(transaction))
        if frequency / len(transactions) >= min_support:
            frequent_itemsets[itemset] = frequency
    return generate_association_rules(frequent_itemsets, transactions, min_confidence)

def generate_association_rules(frequent_itemsets, transactions, min_confidence):
    rules = []
    for itemset, frequency in frequent_itemsets.items():
        for i in range(1, len(itemset)):
            for antecedent in itertools.combinations(itemset, i):
                consequent = set(itemset) - set(antecedent)
                antecedent_transactions = sum(1 for transaction in transactions if set(antecedent).issubset(transaction))
                if antecedent_transactions > 0:
                    confidence = frequency / antecedent_transactions
                    if confidence >= min_confidence:
                        rules.append((antecedent, consequent, confidence))
    return rules

def read_data(filename):
    transactions = []
    with open(filename, 'r') as file:
        csv_reader = csv.reader(file)
        next(csv_reader)  # Skip header row
        for row in csv_reader:
            transactions.append(row[1].split(", "))
    return transactions

def print_rules(rules, method):
    print(f"{method} Association Rules:")
    for rule in rules:
        antecedents = ', '.join(rule[0])
        consequents = ', '.join(rule[1])
        print(f"{antecedents} -> {consequents}, Confidence: {rule[2]:.2f}")
    print("\n")

def run_apriori_fpgrowth(transactions, min_support, min_confidence):
    te = TransactionEncoder()
    te_ary = te.fit(transactions).transform(transactions)
    df = pd.DataFrame(te_ary, columns=te.columns_)

    #Apriori
    
    start_time = time.time()
    frequent_itemsets_apriori = apriori(df, min_support=min_support, use_colnames=True)
    rules_apriori = association_rules(frequent_itemsets_apriori, metric="confidence", min_threshold=min_confidence)
    end_time = time.time()
    print(f"Apriori Execution Time: {end_time - start_time} seconds")
    if not rules_apriori.empty:
        for index, row in rules_apriori.iterrows():
            print(f"{' , '.join(row['antecedents'])} -> {' , '.join(row['consequents'])}, Confidence: {row['confidence']:.2f}")
    else:
        print("No association rules found.")
    print("\n")

    # FP-Growth
    
    start_time = time.time()
    frequent_itemsets_fp = fpgrowth(df, min_support=min_support, use_colnames=True)
    rules_fp = association_rules(frequent_itemsets_fp, metric="confidence", min_threshold=min_confidence)
    end_time = time.time()
    print(f"FP-Growth Execution Time: {end_time - start_time} seconds")
    if not rules_fp.empty:
        for index, row in rules_fp.iterrows():
            print(f"{' , '.join(row['antecedents'])} -> {' , '.join(row['consequents'])}, Confidence: {row['confidence']:.2f}")
    else:
        print("No association rules found.")
    print("\n")

def main():
    datasets = ["amazon.csv", "BestBuy.csv", "Kmart.csv", "nike.csv", "Generic.csv"]
    dataset_choice = int(input("Choose a dataset (1-5): \n1.Amazon\n2.BestBuy\n3.Kmart\n4.Nike\n5.Generic\n"))
    min_support = float(input("Enter minimum support (as a decimal): "))
    min_confidence = float(input("Enter minimum confidence (as a decimal): "))

    transactions = read_data(datasets[dataset_choice - 1])

    # Brute Force
    start_time = time.time()
    rules_brute_force = brute_force(transactions, min_support, min_confidence)
    end_time = time.time()
    print(f"\nBrute Force Execution Time: {end_time - start_time} seconds")
    print_rules(rules_brute_force, "Brute Force")

    # Apriori and FP-Growth
    run_apriori_fpgrowth(transactions, min_support, min_confidence)

if __name__ == "__main__":
    main()


# In[ ]:




