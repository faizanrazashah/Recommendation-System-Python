startTime=time.time()
# constant variables to define field names include:
user_id = 'Customer_Code'
item_id = 'Product_Code'
users_to_recommend = list(customer[user_id])
n_rec = 5 # number of items to recommend
n_display = 40 # to display the first few rows in an output dataset

def model(train_data_dummy, name, user_id, item_id, target, users_to_recommend, n_rec, n_display):
    if name == 'popularity':
        model = tc.popularity_recommender.create(train_data_dummy, 
                                                    user_id=user_id, 
                                                    item_id=item_id, 
                                                    target=target)
    elif name == 'cosine':
        model = tc.item_similarity_recommender.create(train_data_dummy, 
                                                    user_id=user_id, 
                                                    item_id=item_id, 
                                                    target=target, 
                                                    similarity_type='cosine')
    elif name == 'pearson':
        model = tc.item_similarity_recommender.create(train_data_dummy, 
                                                    user_id=user_id, 
                                                    item_id=item_id, 
                                                    target=target, 
                                                    similarity_type='pearson')
    
    #.drop_duplicates(subset=['customerId','productId'], keep='first')
    recom = model.recommend(users=users_to_recommend, k=n_rec)
    recom1=recom.drop_duplicates(subset=["Customer_Code","Product_Code","score","rank"])
    recom11=recom1.sort(["Customer_Code","rank"])
    recom11.print_rows(n_display)
    print(recom11)
    print(target)
    from turicreate import SFrame
    recom11=SFrame.to_dataframe(recom11)
    print(recom11)
    import sqlalchemy  # Package for accessing SQL databases via Python

    # Connect to database (Note: The package psychopg2 is required for Postgres to work with SQLAlchemy)
    engine = sqlalchemy.create_engine("postgresql://postgres:jhoncena619@localhost/RB_Recommendation_System")
    con = engine.connect()

    # Verify that there are no existing tables
    print(engine.table_names())

    
    #BBBB=recom11.lower()
    table_name = f'model_{name}{target}'
    recom11.to_sql(table_name, con, index=False, if_exists='replace')



    print(engine.table_names())

    con.close()
    return model

print ('The script took {0} second !'.format(time.time() - startTime))