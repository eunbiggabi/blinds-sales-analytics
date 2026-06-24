import pandas as pd
import random

random.seed(42)

# -------------------------
# Customers
# -------------------------

suburbs = [
    "Sunnybank",
    "Calamvale",
    "Eight Mile Plains",
    "Carindale",
    "Chermside",
    "Indooroopilly",
    "Toowong",
    "Springfield",
    "Forest Lake",
    "Redcliffe"
]

customers = []

for i in range(1, 1001):

    customer_type = random.choices(
        ["Residential", "Commercial"],
        weights=[80, 20]
    )[0]

    customers.append([
        f"C{i:04}",
        f"Customer {i}",
        customer_type,
        random.choice(suburbs),
        "QLD"
    ])

customers_df = pd.DataFrame(
    customers,
    columns=[
        "CustomerID",
        "CustomerName",
        "CustomerType",
        "Suburb",
        "State"
    ]
)

# -------------------------
# Products
# -------------------------

products = [
("P001","Roller Standard","Roller"),
("P002","Roller Blockout","Roller"),
("P003","Zebra Basic","Zebra"),
("P004","Zebra Premium","Zebra"),
("P005","PVC Shutter","Shutter"),
("P006","Basswood Shutter","Shutter"),
("P007","Premium Shutter","Shutter"),
("P008","Curtain Sheer","Curtains"),
("P009","Curtain Blockout","Curtains"),
("P010","Venetian Aluminium","Venetian"),
("P011","Venetian Timber","Venetian"),
("P012","Outdoor Zip Screen","Roller"),
("P013","Awning","Roller"),
("P014","Roman Blind","Roller"),
("P015","Security Screen","Roller")
]

products_df = pd.DataFrame(
    products,
    columns=[
        "ProductID",
        "ProductName",
        "Category"
    ]
)

# -------------------------
# Manufacturers
# -------------------------

manufacturers = [
("M001","Norman"),
("M002","Luxaflex"),
("M003","Hunter Douglas"),
("M004","Vertilux"),
("M005","Shaw"),
("M006","Wilson"),
("M007","Sunteca"),
("M008","Decor Systems")
]

manufacturers_df = pd.DataFrame(
    manufacturers,
    columns=[
        "ManufacturerID",
        "ManufacturerName"
    ]
)

# -------------------------
# Employees
# -------------------------

employees = [
("E001","Kai",1.30),
("E002","Brandon",1.10),
("E003","Chris",1.00),
("E004","Paul",0.90),
("E005","Alex",1.20),
("E006","Daniel",1.05),
("E007","Tom",0.95),
("E008","James",1.15),
("E009","Luke",1.00),
("E010","Henry",0.85)
]

employees_df = pd.DataFrame(
    employees,
    columns=[
        "EmployeeID",
        "EmployeeName",
        "SkillFactor"
    ]
)

# -------------------------
# Installers
# -------------------------

installers = []

for i in range(1, 6):

    installers.append([
        f"I{i:03}",
        f"Team {chr(64+i)}"
    ])

installers_df = pd.DataFrame(
    installers,
    columns=[
        "InstallerID",
        "InstallerTeam"
    ]
)

# -------------------------
# Date Table
# -------------------------

dates = []

date_range = pd.date_range(
    start="2024-01-01",
    end="2026-12-31"
)

for d in date_range:

    dates.append([
        d.strftime("%Y%m%d"),
        d.date(),
        d.year,
        d.month,
        d.quarter
    ])

dates_df = pd.DataFrame(
    dates,
    columns=[
        "DateID",
        "FullDate",
        "Year",
        "Month",
        "Quarter"
    ]
)

# -------------------------
# Product Pricing
# -------------------------

def generate_sale(category):

    if category == "Roller":
        revenue = random.randint(500, 1800)
        margin = 0.35

    elif category == "Zebra":
        revenue = random.randint(1200, 3000)
        margin = 0.40

    elif category == "Shutter":
        revenue = random.randint(2500, 8000)
        margin = 0.55

    elif category == "Curtains":
        revenue = random.randint(1500, 6000)
        margin = 0.45

    else:
        revenue = random.randint(800, 2500)
        margin = 0.35

    cost = round(revenue * (1-margin),2)
    profit = round(revenue - cost,2)

    return revenue, cost, profit

# -------------------------
# Sales
# -------------------------

sales = []

for i in range(1,15001):

    product = random.choice(products)

    revenue, cost, profit = generate_sale(
        product[2]
    )

    sales.append([
        f"S{i:06}",
        random.choice(dates_df["DateID"]),
        random.choice(customers_df["CustomerID"]),
        product[0],
        random.choice(manufacturers_df["ManufacturerID"]),
        random.choice(employees_df["EmployeeID"]),
        random.choice(installers_df["InstallerID"]),
        random.randint(1,5),
        revenue,
        cost,
        profit
    ])

sales_df = pd.DataFrame(
    sales,
    columns=[
        "SaleID",
        "DateID",
        "CustomerID",
        "ProductID",
        "ManufacturerID",
        "EmployeeID",
        "InstallerID",
        "Quantity",
        "Revenue",
        "Cost",
        "Profit"
    ]
)

# -------------------------
# Quotes
# -------------------------

quotes = []

for i in range(1,20001):

    quotes.append([
        f"Q{i:06}",
        random.choice(dates_df["DateID"]),
        random.choice(customers_df["CustomerID"]),
        random.choice(products_df["ProductID"]),
        random.randint(500,10000),
        random.choices(
            ["Won","Lost","Pending"],
            weights=[55,30,15]
        )[0]
    ])

quotes_df = pd.DataFrame(
    quotes,
    columns=[
        "QuoteID",
        "DateID",
        "CustomerID",
        "ProductID",
        "QuoteValue",
        "Status"
    ]
)

# -------------------------
# Export CSV
# -------------------------

customers_df.to_csv("customers.csv", index=False)
products_df.to_csv("products.csv", index=False)
manufacturers_df.to_csv("manufacturers.csv", index=False)
employees_df.to_csv("employees.csv", index=False)
installers_df.to_csv("installers.csv", index=False)
dates_df.to_csv("dates.csv", index=False)
sales_df.to_csv("sales.csv", index=False)
quotes_df.to_csv("quotes.csv", index=False)

print("CSV files created successfully!")