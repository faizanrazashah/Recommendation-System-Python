#CREATE DATAFRAME FOR DATE DIFFERENCE
shand=frames.groupby(['Customer_Code','Invoice_Date']).agg({'Invoice_Date':'count'}).rename(columns={'Invoice_Date':'Sales of products'})
shand.reset_index(inplace=True)
shand.sort_values(['Invoice_Date'],ascending=True)
display(shand)
#ordd=shand[shand['Route_Code']==bbbb]
ordd=shand
display(ordd)
ordd['diff'] = ordd.groupby(['Customer_Code'])['Invoice_Date'].apply(lambda x: x.diff()).dt.days
display(ordd)
orddaily=ordd[ordd['diff']==1.0]
display(orddaily)


#TAKING AVERAGE OF THE DIFFERENCE COlUMN 
ordavg=ordd.groupby(['Customer_Code']).agg({'diff':'mean'})
ordavg.reset_index(inplace=True)
ordavg1=ordavg.fillna(1.00)
ordavg1['diff']=ordavg1['diff'].astype('int')
display(ordavg1)
print(ordavg1.isnull().sum())


#MERGING DIFFERENCE COLUMN WITH NON_POP DATAFRAME
npo=pd.merge(nptest,ordavg1, on='Customer_Code')
print(npo.isnull().sum())
display(npo)


#RENAMING DIFF COLUMN AND SELECTING APPROPRIATE COLUMNS
npo_final=npo.rename(columns={'diff':'Expected_Difference_In_visits'})
npo_final.insert(12,'Product_Remarks','Non-Popular Product')
npo_final1=npo_final.iloc[:,[0,1,3,4,5,6,7,8,9,10,12]]
display(npo_final1)