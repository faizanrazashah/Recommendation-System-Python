startTime=time.time()


st1=time.time()
name = 'cosine'
target = 'purchase_count'
cos = model(train_data_dummy, name, user_id, item_id, target, users_to_recommend, n_rec, n_display)
end1=time.time()

st2=time.time()
name = 'cosine'
target = 'purchase_dummy'
cos_dummy = model(train_data_dummy, name, user_id, item_id, target, users_to_recommend, n_rec, n_display)
end2=time.time()

st3=time.time()
name = 'cosine' 
target = 'scaled_purchase_freq' 
cos_norm = model(train_data_norm, name, user_id, item_id, target, users_to_recommend, n_rec, n_display)
end3=time.time()

cm1 = end1-st1
cm2 = end2-st2
cm3 = end3-st3

print (f'The cosine model with respect to purchase_count took {cm1} second !')
print (f'The cosine model with respect to purchase_dummy took {cm2} second !')
print (f'The cosine model with respect to scaled_purchase_frequency took {cm3} second !')


# import sqlalchemy  # Package for accessing SQL databases via Python

# # Connect to database (Note: The package psychopg2 is required for Postgres to work with SQLAlchemy)
# engine = sqlalchemy.create_engine("postgresql://postgres:jhoncena619@localhost/RB_Recommendation_System")
# con = engine.connect()

# # Verify that there are no existing tables
# print(engine.table_names())

# hhre="ENTER Recommendation Date: "
# h23="\033[1m" + hhre + "\033[0m"
# #fh=h.BOLD()
# recom_date=str(input(h23))
# BBBB=bbbb.lower()
# table_name = f'recom_for_{BBBB}{recom_date}'
# fin_results1.to_sql(table_name, con, index=False, if_exists='replace')



# print(engine.table_names())

# con.close()


print ('The script took {0} second !'.format(time.time() - startTime))