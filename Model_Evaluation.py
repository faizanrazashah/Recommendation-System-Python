models_w_counts = [cos]
models_w_dummy = [cos_dummy]
models_w_norm = [cos_norm]
names_w_counts = ['Cosine Similarity on Purchase Counts']
names_w_dummy = ['Cosine Similarity on Purchase Dummy']
names_w_norm = ['Cosine Similarity on Scaled Purchase Counts']

eval_counts = tc.recommender.util.compare_models(test_data_dummy, models_w_counts, model_names=names_w_counts)
eval_dummy = tc.recommender.util.compare_models(test_data_dummy, models_w_dummy, model_names=names_w_dummy)
eval_norm = tc.recommender.util.compare_models(test_data_norm, models_w_norm, model_names=names_w_norm)