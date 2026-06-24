# blinds-sales-analytics
An end-to-end BI project modeling custom window blinds &amp; curtains business data with PostgreSQL, Python, and Power BI, integrated into a React dashboard.

# Blinds Sales Analytics Dashboard

## Overview

This project demonstrates an end-to-end Business Intelligence solution built using PostgreSQL, Python, Power BI, and React.

The goal was to simulate a real-world blinds and curtains business environment and build a complete analytics workflow from data generation to dashboard reporting.

---

## Business Problem

Management needs visibility into:

* Revenue performance
* Profitability trends
* Product performance
* Employee sales performance
* Installer productivity
* Customer activity

This dashboard provides key insights to support business decision-making.

---

## Technology Stack

* PostgreSQL
* Python
* Power BI
* React
* GitHub

---

## Data Warehouse Design

Star Schema Model

Fact Tables:

* fact_sales
* fact_quotes

Dimension Tables:

* dim_customer
* dim_product
* dim_date
* dim_employee
* dim_installer
* dim_manufacturer

---

## Data Generation

Synthetic business data was generated using Python.

Generated datasets include:

* Customers
* Products
* Manufacturers
* Employees
* Installers
* Quotes
* Sales Transactions

Total records generated:

* 15,000 Sales Records
* 20,000 Quote Records
* 1,000 Customers

---

## Dashboard Features

### KPI Monitoring

* Total Revenue
* Total Profit
* Total Orders
* Profit Margin

### Sales Analysis

* Revenue Trend
* Monthly Performance
* Product Contribution

### Employee Analysis

* Revenue by Employee
* Profit by Employee

### Installer Analysis

* Installation Performance
* Job Volume Analysis

### Manufacturer Analysis

* Revenue by Manufacturer
* Profit by Manufacturer

---

## Project Workflow

Python Data Generation

↓

CSV Export

↓

PostgreSQL Data Warehouse

↓

Power BI Dashboard

↓

React Portfolio Website

---

## Dashboard Preview

See screenshots/dashboard.png

---

## Author

Kyu Jeon

Brisbane, Australia
