exec(open('/home/faizan/pre venv/Function_file_RB/libraries.py').read())
exec(open('/mnt/d/Rb Suggested Ordering System/injest_by_postgresql.py').read())
a=0
while a>=0:
    exec(open('/mnt/d/Rb Suggested Ordering System/Select_Distributor_Name.py').read())
    exec(open('/mnt/d/Rb Suggested Ordering System/cust_transaction.py').read())
    exec(open('/mnt/d/Rb Suggested Ordering System/dummy_normalize_data.py').read())
    exec(open('/mnt/d/Rb Suggested Ordering System/Split_data.py').read())
    exec(open('/mnt/d/Rb Suggested Ordering System/Cisone_Similarity_Model.py').read())
    exec(open('/mnt/d/Rb Suggested Ordering System/Model_Evaluation.py').read())
    exec(open('/mnt/d/Rb Suggested Ordering System/Model_Selection.py').read())
    exec(open('/mnt/d/Rb Suggested Ordering System/Popular_and_Non_Popular_dataframe.py').read())
    exec(open('/mnt/d/Rb Suggested Ordering System/Date_Difference_Dataframe.py').read())
    exec(open('/mnt/d/Rb Suggested Ordering System/Merging_Popular_and_Non_Popular.py').read())

    b=0
    while b>=0:
        
        rr=str(input("Continue for same distribution? y/n: "))
        if rr=="n":
            break
        elif rr=="y":
            exec(open('/mnt/d/Rb Suggested Ordering System/Merging_Route_plan_with_Final_Dataframe.py').read())
            exec(open('/mnt/d/Rb Suggested Ordering System/Merging_MSL_List_with_Final_Dataframe.py').read())
            exec(open('/mnt/d/Rb Suggested Ordering System/recom_database.py').read())
        