frames=pd.read_csv('/mnt/d/faizan/Project RB/Data Files/RB NewsPage Data/TestShanRBnewspage2019-2020.csv', engine='python')
frames.drop('Unnamed: 0', axis=1, inplace=True)
pd.set_option("display.max_columns", None)

frames['Year'] = frames['Year'].astype('str')
frames['Distributor'] = frames['Distributor'].astype('str')
frames['Product_Code'] = frames['Product_Code'].astype('str')
#frames['Quantity_EA'] = frames['Quantity_EA'].astype('int')
import datetime
frames['Invoice_Date']=pd.to_datetime(frames['Invoice_Date'],format='%Y%m%d')

display(frames)

print(frames.isnull().sum())