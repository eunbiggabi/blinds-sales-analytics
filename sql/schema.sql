
-- =====================================
-- DIMENSION TABLES
-- =====================================

CREATE TABLE dim_customer (
    customer_id VARCHAR(10) PRIMARY KEY,
    customer_name VARCHAR(100),
    customer_type VARCHAR(50),
    suburb VARCHAR(100),
    state VARCHAR(20)
);

CREATE TABLE dim_product (
    product_id VARCHAR(10) PRIMARY KEY,
    product_name VARCHAR(100),
    category VARCHAR(50)
);

CREATE TABLE dim_manufacturer (
    manufacturer_id VARCHAR(10) PRIMARY KEY,
    manufacturer_name VARCHAR(100)
);

CREATE TABLE dim_employee (
    employee_id VARCHAR(10) PRIMARY KEY,
    employee_name VARCHAR(100),
    skill_factor NUMERIC(4,2)
);

CREATE TABLE dim_installer (
    installer_id VARCHAR(10) PRIMARY KEY,
    installer_team VARCHAR(100)
);

CREATE TABLE dim_date (
    date_id VARCHAR(10) PRIMARY KEY,
    full_date DATE,
    year INTEGER,
    month INTEGER,
    quarter INTEGER
);

-- =====================================
-- FACT TABLES
-- =====================================

CREATE TABLE fact_sales (
    sale_id VARCHAR(10) PRIMARY KEY,

    date_id VARCHAR(10),
    customer_id VARCHAR(10),
    product_id VARCHAR(10),
    manufacturer_id VARCHAR(10),
    employee_id VARCHAR(10),
    installer_id VARCHAR(10),

    quantity INTEGER,
    revenue NUMERIC(12,2),
    cost NUMERIC(12,2),
    profit NUMERIC(12,2),

    CONSTRAINT fk_sales_date
        FOREIGN KEY (date_id)
        REFERENCES dim_date(date_id),

    CONSTRAINT fk_sales_customer
        FOREIGN KEY (customer_id)
        REFERENCES dim_customer(customer_id),

    CONSTRAINT fk_sales_product
        FOREIGN KEY (product_id)
        REFERENCES dim_product(product_id),

    CONSTRAINT fk_sales_manufacturer
        FOREIGN KEY (manufacturer_id)
        REFERENCES dim_manufacturer(manufacturer_id),

    CONSTRAINT fk_sales_employee
        FOREIGN KEY (employee_id)
        REFERENCES dim_employee(employee_id),

    CONSTRAINT fk_sales_installer
        FOREIGN KEY (installer_id)
        REFERENCES dim_installer(installer_id)
);

CREATE TABLE fact_quotes (
    quote_id VARCHAR(10) PRIMARY KEY,

    date_id VARCHAR(10),
    customer_id VARCHAR(10),
    product_id VARCHAR(10),

    quote_value NUMERIC(12,2),
    status VARCHAR(20),

    CONSTRAINT fk_quotes_date
        FOREIGN KEY (date_id)
        REFERENCES dim_date(date_id),

    CONSTRAINT fk_quotes_customer
        FOREIGN KEY (customer_id)
        REFERENCES dim_customer(customer_id),

    CONSTRAINT fk_quotes_product
        FOREIGN KEY (product_id)
        REFERENCES dim_product(product_id)
);
