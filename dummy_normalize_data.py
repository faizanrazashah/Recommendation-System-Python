startTime = time.time()

data.loc[data['Net_Amount'] <= 1, 'purchase_dummy'] = 0 
data.loc[data['Net_Amount'] > 1, 'purchase_dummy'] = 1
data_dummy=data
df_matrix = pd.pivot_table(data_dummy, values='purchase_count', index='Customer_Code', columns='Product_Code')
df_matrix_norm = (df_matrix-df_matrix.min())/(df_matrix.max()-df_matrix.min())
d = df_matrix_norm.reset_index() 
d.index.names = ['scaled_purchase_freq'] 
data_norm = pd.melt(d, id_vars=['Customer_Code'], value_name='scaled_purchase_freq').dropna()
print(data_norm.shape)
display(data_norm)

print ('The script took {0} second !'.format(time.time() - startTime))