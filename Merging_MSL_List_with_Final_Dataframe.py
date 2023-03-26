msl=pd.read_excel('/mnt/c/Users/ITSM/Downloads/MSL SKU.xlsx' , sheet_name='MSL SKU')
msl=msl.rename(columns={'Product SKU Code':'Product_Code','Product SKU Description':'Product_Description'})
msl.insert(2,'MSL_List','MSL Product')
msl=msl.iloc[:,[0,2]]
msl['Product_Code']=msl['Product_Code'].astype('str')
fin_results['Product_Code']=fin_results['Product_Code'].astype('str')
display(msl)
fin_results1 = fin_results.merge(msl, on='Product_Code', how='left')
fin_results1=fin_results1.drop(columns=['MSL_List_x'])
fin_results1=fin_results1.rename(columns={'MSL_List_y':'MSL_List'})

if dist_name == "SHAN DISTRIBUTION SERVICES (PVT) LIMITED":
    test_code=fin_results1['Customer_Code'].drop_duplicates()
    print(len(test_code))
    print(test_code)

    testcode1=final_resultShan['Customer_Code'].drop_duplicates()
    print(len(testcode1))
    print(testcode1)

    inter=set(final_resultShan['Customer_Code']).intersection(set(fin_results1['Customer_Code']))
    print(len(inter))
    display(inter)

    display(fin_results1)

elif dist_name == "PREMIER SALES (PRIVATE) LIMITED":    
    tts1=r_code1[r_code1[days]=='Y']
    tts12=tts1['Customer_Code'].drop_duplicates()


    intermsl=set(fin_results1['Product_Code']).intersection(set(msl['Product_Code']))
    print(len(intermsl))
    display(intermsl)

    test_code=fin_results1['Customer_Code'].drop_duplicates()
    print(len(test_code))
    print(test_code)

    print(len(tts12))
    print(tts12)

    inter=set(fin_results1['Customer_Code']).intersection(set(tts1['Customer_Code']))
    print(len(inter))
    display(inter)

    display(fin_results1)
