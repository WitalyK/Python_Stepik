import numpy as np

Z = np.zeros((5, 5))
Z += np.arange(5)
# Z = np.random.random_integers(0,5,(7,5))
Z = np.random.randint(0,5,(5,5))


if __name__ == '__main__':
    print(Z)
    print(np.array(list(np.ndenumerate(Z))))
    print(Z.argsort())
