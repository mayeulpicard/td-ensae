def random_sparse_matrix(shape, ratio_sparse=0.2):
    rnd = numpy.random.rand(shape[0] * shape[1])
    sparse = 0
    for i in range(0, len(rnd)):
        x = random.random()
        if x <= ratio_sparse - sparse:
            sparse += 1 - ratio_sparse
        else:
            rnd[i] = 0
            sparse -= ratio_sparse
    rnd.resize(shape[0], shape[1])
    return scipy.sparse.csr_matrix(rnd)