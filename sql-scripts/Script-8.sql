select distinct Date, (Unit_sale_price * Quantity) as ricavo, Retailer_code , Product_number 
from go_daily_sales gds, go_products gp, go_retailers gr
where gds.Product_number = gp.Product_number 
	and gds.Retailer_code = gr.Retailer_code
	and (Product_brand = COALESCE(%s, Product_brand))
	and (year(Date) = COALESCE(%s, year(Date))
	and (Retailer_code = coalesce(%s, Retailer_code))
order by ricavo desc
limit 5