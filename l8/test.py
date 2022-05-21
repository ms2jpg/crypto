def split_shares(img: npt.NDArray):
    height, width = img.shape
    frag1, frag2 = np.zeros((2, height, width, 2))
    m = np.random.rand(height, width) > 0.5
    x = (img == 1) & (m == 0)
    frag1[x] = [1, 0]
    frag2[x] = [1, 0]

    x = (img == 1) & (m == 1)
    frag1[x] = [0, 1]
    frag2[x] = [0, 1]

    x = (img == 0) & (m == 0)
    frag1[x] = [1, 0]
    frag2[x] = [0, 1]

    x = (img == 0) & (m == 1)
    frag1[x] = [0, 1]
    frag2[x] = [1, 0]

    frag1 = frag1.reshape(height, 2 * width).astype(bool)
    frag2 = frag2.reshape(height, 2 * width).astype(bool)
    return frag1, frag2


def join_shares(x, y):
    return x == y