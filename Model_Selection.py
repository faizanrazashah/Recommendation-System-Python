final_model = tc.item_similarity_recommender.create(tc.SFrame(data_dummy), 
                                            user_id=user_id, 
                                            item_id=item_id, 
                                            target='purchase_dummy', similarity_type='cosine')
recom = final_model.recommend(users=users_to_recommend, k=n_rec)
recom1=recom.drop_duplicates(subset=["Customer_Code","Product_Code","score","rank"])
recom11=recom1.sort(["Customer_Code","rank"])
recom11.print_rows(n_display)