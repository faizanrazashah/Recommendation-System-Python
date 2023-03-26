df_rec = recom11.to_dataframe()
print(df_rec.shape)
df_rec.set_index('rank', inplace=True)
df_rec1=df_rec.iloc[:,[1,0]]
df_rec1.reset_index(inplace=True)
df_rec1=df_rec1.rename(columns={'rank':'Rank'})


ordr=frames.groupby(['Customer_Code','Customer_Name']).agg({'Customer_Code':'count'}).rename(columns={
    'Customer_Code':'Salesman'})
ordr.reset_index(inplace=True)
ordrs=ordr.iloc[:,[0,1,2]]


ordrm=pd.merge(df_rec1,ordrs, on='Customer_Code')
ordrm=ordrm[['Customer_Code', 'Customer_Name','Rank','Product_Code']]


trans=frames.groupby(['Product_Code', 'Product_Description']).agg({'List_Price':'mean','Quantity_EA':'mean',
                                            'Net_Amount':'mean'}).rename(columns={'Quantity_EA':'Expected_Quantity_EA'})
trans['Expected_Quantity_EA']=trans['Expected_Quantity_EA'].astype('int')
trans['Expected_Amount']=trans['List_Price']*trans['Expected_Quantity_EA']
trans.reset_index(inplace=True)


nptest=pd.merge(ordrm,trans, on='Product_Code')
nptest=nptest.sort_values(['Customer_Code','Rank'], ascending=True)
nptest.reset_index(drop=True, inplace=True)
nptest.insert(8,'MSL_List',np.nan)
nptest.insert(9,'PROMO_List',np.nan)
h=f'THE NON-POPULAR Recommended PRODUCT CODE FOR Route_Code: across each Customer Code is'
fh="\033[1m" + h + "\033[0m"
print('\n\n')
print('\t\t\t')
print(fh)
display(nptest)


              #POPULAR PRODUCTS
pop=frames.groupby(['Customer_Code', 'Customer_Name','Product_Code', 'Product_Description']).agg({
    'Product_Code':'count','List_Price':'mean','Quantity_EA':'mean','Net_Amount':'mean'}).rename(columns={
    'Product_Code':'Purchase_Count','Quantity_EA':'Expected_Quantity_EA'
})
pop.reset_index(inplace=True)
popRoute=pop.sort_values(['Customer_Code','Purchase_Count'], ascending=False)
popRoute['Expected_Quantity_EA']=popRoute['Expected_Quantity_EA'].astype('int')
popRoute['Expected_Amount']=popRoute['Expected_Quantity_EA']*popRoute['List_Price']
popRoute=popRoute.iloc[:,[0,1,2,3,5,6,7,8]]
popRoute.reset_index(drop=True,inplace=True)
popRoute.insert(7,'MSL_List', np.nan)
popRoute.insert(8,'PROMO_List', np.nan)
h22=f'THE POPULAR RECOMMENDED PRODUCT CODE & THEIR EXPECTED IMS FOR Route Code: across each Customer Code is '

popRoute_list=popRoute['Customer_Code'].drop_duplicates()
popRoute_list1=popRoute_list.tolist()
popRoute_list1


pop_df_list=[]
for x in popRoute_list1:
    f3x=popRoute[popRoute['Customer_Code']==x]
    popRoute1=f3x.head(10)
    pop_df_list.append(popRoute1)
    
    
pop_df=pd.concat(pop_df_list)

fh1="\033[1m" + h22 + "\033[0m"
print(fh1)
display(pop_df)