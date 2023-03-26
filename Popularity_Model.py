startTime=time.time()

st4=time.time()
name = 'popularity'
target = 'purchase_count'
popularity = model(train_data_dummy, name, user_id, item_id, target, users_to_recommend, n_rec, n_display)
end4=time.time()

st5=time.time()
name = 'popularity'
target = 'purchase_dummy'
pop_dummy = model(train_data_dummy, name, user_id, item_id, target, users_to_recommend, n_rec, n_display)
end5=time.time()

st6=time.time()
name = 'popularity'
target = 'scaled_purchase_freq'
pop_norm = model(train_data_norm, name, user_id, item_id, target, users_to_recommend, n_rec, n_display)
end6=time.time()

cm4 = end4-st4
cm5 = end5-st5
cm6 = end6-st6

print (f'The popularity model with respect to purchase_count took {cm4} second !')
print (f'The popularity model with respect to purchase_dummy took {cm5} second !')
print (f'The popularity model with respect to scaled_purchase_frequency took {cm6} second !')
print ('The script took {0} second !'.format(time.time() - startTime))