startTime=time.time()


st7=time.time()
name = 'pearson'
target = 'purchase_count'
pear = model(train_data_dummy, name, user_id, item_id, target, users_to_recommend, n_rec, n_display)
end7=time.time()

st8=time.time()
name = 'pearson'
target = 'purchase_dummy'
pear_dummy = model(train_data_dummy, name, user_id, item_id, target, users_to_recommend, n_rec, n_display)
end8=time.time()

st9=time.time()
name = 'pearson'
target = 'scaled_purchase_freq'
pear_norm = model(train_data_norm, name, user_id, item_id, target, users_to_recommend, n_rec, n_display)
end9=time.time()

cm7 = end7-st7
cm8 = end8-st8
cm9 = end9-st9

print (f'The pearson model with respect to purchase_count took {cm7} second !')
print (f'The pearson model with respect to purchase_dummy took {cm8} second !')
print (f'The pearson model with respect to scaled_purchase_frequency took {cm9} second !')
print ('The script took {0} second !'.format(time.time() - startTime))