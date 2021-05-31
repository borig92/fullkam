import pickle
with open('plazmatvs.pickle', 'rb') as f:
    tv_lista = pickle.load(f)

print(tv_lista[-1])