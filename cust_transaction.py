startTime = time.time()


customer=frames.iloc[:,[5,6]]
transactions=frames.iloc[:,[4,5,6,7,8,9,10,11,12,13,14,15]]
test = transactions.groupby(['Customer_Code','Customer_Name', 'Route_Code', 'Route_Name', 'Product_Code','List_Price']).agg({ 'Quantity_EA':'sum', 'Net_Amount' : 'sum', 'Product_Code': 'count'}).rename(columns={'Product_Code': 'purchase_count'}) 
data=test.reset_index()
display(data)

print ('The script took {0} second !'.format(time.time() - startTime))