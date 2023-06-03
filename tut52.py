import pickle

# Pickling a pyhon object

cars = ["audi","BMW","ferrari","scquarpio"]
file = "mycar.pkl"
fileobj = open(file,'wb')
pickle.dump(cars, fileobj)
fileobj.close()