model_list = [[cm1, cm2, cm3]]
f_mod = pd.DataFrame(model_list, columns=['duration_of_cosine_purchase_count',
                                        'duration_of_cosine_purchase_dummy',
                                        'duration_of_cosine_scaled_purchase_frequency'])
f_mod = f_mod.round(decimals = 2)
display(f_mod)                                        