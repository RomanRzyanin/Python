import pickle

__all__ = ['save_to_pickle']


def save_to_pickle(data, filename):
    with open(filename, 'wb') as pickle_f:
        pickle.dump(data, pickle_f)


if __name__ == '__main__':
    save_to_pickle()
