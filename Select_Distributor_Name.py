startTime = time.time()

print('DISTRIBUTOR LIST','\n')
dist_list=T_frames['Distributor_Name'].drop_duplicates()
display(dist_list)
dist_name=input('Enter Distributor Name From the Above Distributor List: ')

frames=T_frames[T_frames['Distributor_Name']==dist_name]
frames.reset_index(drop=True,inplace=True)
display(frames)

print ('The script took {0} second !'.format(time.time() - startTime))