#MERGING POPULAR PRODUCT DATAFRAME WITH DATE DIFF DATAFRAME
popo=pd.merge(pop_df,ordavg1, on='Customer_Code')
print(pop.isnull().sum())
display(popo)


#RENAMING DIFF COLUMN AND SELECTING APPROPRIATE COLUMNS
popo_final=popo.rename(columns={'diff':'Expected_Difference_In_visits'})
popo_final.insert(11,'Product_Remarks','Popular Product')
popo_final1=popo_final.iloc[:,[0,1,2,3,4,5,6,7,8,9,11]]
display(popo_final1)


#CONCAT BOTH NON_POP & POP DATAFRAMES
final_concat=pd.concat([popo_final1, npo_final1])
final_concat1=final_concat.sort_values(['Customer_Code', 'Product_Remarks'], ascending=False)
final_concat12=final_concat1.iloc[:,[0,1,2,3,4,5,6,7,8,9,10]]
final_concat12.reset_index(drop=True, inplace=True)
final_concat12