from recsys.algorithm.factorize import SVD
svd = SVD()
svd.load_data(filename='./data/recsys/ratings.dat', sep='::', format={'col':0, 'row':1, 'value':2, 'ids': int})
svd.compute(k=100, min_values=10, pre_normalize=None, mean_center=True, post_normalize=True, savefile='./tmp/movielens')