import psycopg2
conn = psycopg2.connect(host="localhost", port = 5432, database="RB_Recommendation_System", user="postgres", password="jhoncena619")
cur = conn.cursor()
def create_pandas_table(sql_query, database = conn):

    table = pd.read_sql_query(sql_query, database)

    return table

if dist_name == 'PREMIER SALES (PRIVATE) LIMITED':

    #R_plan=pd.read_excel('/mnt/c/Users/ITSM/Downloads/Route Plan MT-KHI.xlsx', sheet_name='Sheet5')


    R_plan = create_pandas_table("SELECT * FROM routeplan_premier ")
    R_plan1=R_plan.rename(columns={'Cust Code':'Customer_Code','Customer Name':'Customer_Name',
                             'Salesman Code':'Route_Code'})
    #,[2,3,5,7]
    R_plan12=R_plan1

    dd1="ENTER DAY ACCORDING TO ROUTE PLAN: "
    dd2="\033[1m" + dd1 + "\033[0m"
    #fh=h.BOLD()
    days=str(input(dd2))

    R_plan12=R_plan12[['Customer_Code','Customer_Name','Route_Code',days]]
    display(R_plan12)

    route=frames['Route_Code'].drop_duplicates()
    display(route)
    hh1="ENTER Route Code: "
    h2="\033[1m" + hh1 + "\033[0m"
    #fh=h.BOLD()
    bbbb=str(input(h2))


    r_code=R_plan12[R_plan12['Route_Code']==bbbb]
    display(r_code)
    r_code1=r_code.iloc[:,[0,2,3]]
    display(r_code1)


    day_ytt=r_code1[r_code1[days]=='Y']
    day_ytt.reset_index(drop=True,inplace=True)
    display(day_ytt)


    rrrr = final_concat12["Customer_Code"].isin(day_ytt['Customer_Code'])
    fin_results=final_concat12[rrrr]
    fin_results.insert(11,'Day',days)
    fin_results.insert(0,'Route_Code',bbbb)
    #fin_results=fin_results.drop_duplicates(subset=['Customer_Code','Customer_Name','Product_Code'])
    display(fin_results)

elif dist_name == 'SHAN DISTRIBUTION SERVICES (PVT) LIMITED':
    route=frames['Route_Code'].drop_duplicates()
    display(route)
    hh1="ENTER Route Code: "
    h2="\033[1m" + hh1 + "\033[0m"
    #fh=h.BOLD()
    bbbb=str(input(h2))

    R_plan = create_pandas_table("SELECT * FROM routeplan_shan ")
    #R_plan=pd.read_excel('/mnt/c/Users/ITSM/Downloads/Weekly Routes (1).xlsx', sheet_name='Sheet1')
    R_plan1=R_plan.rename(columns={'Tree Code':'Tree_Code','Node Code':'Node_Code',
                              'POP_Code':'Customer_Code','Outlet':'Customer_Name',
                             'Route Plan Code':'Route_Plan_Code','Route Code':'Route_Code'})
    R_plan12=R_plan1.iloc[:,[1,0,5]]
    display(R_plan12)
    R_plan122=R_plan12[R_plan12['Route_Code']==bbbb]
    display(R_plan122)

    days1=R_plan12['Days'].drop_duplicates()
    print(days1)

    dd1="ENTER DAY ACCORDING TO ROUTE PLAN: "
    dd2="\033[1m" + dd1 + "\033[0m"
    #fh=h.BOLD()
    days=str(input(dd2))



    final_resultShan=R_plan122[R_plan122['Days']==days]
    display(final_resultShan)




    rrrr = final_concat12["Customer_Code"].isin(final_resultShan['Customer_Code'])
    fin_results=final_concat12[rrrr]
    fin_results.insert(11,'Day',days)
    fin_results.insert(0,'Route_Code',bbbb)
    fin_results=fin_results.drop_duplicates()
    display(fin_results)
