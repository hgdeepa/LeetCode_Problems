# Write your MySQL query statement below
select Product.product_name, year, price from sales, Product
where sales.product_id = Product.product_id