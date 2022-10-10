import requests
import pickle
# r = requests.get("https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data")
# print(r.text)
# print(r.status_code)


with open("iris.txt","r")as f:
    f =f.read().splitlines()

file = "myiris.txt"
object = open(file ,"wb")

pickle.dump(f,object)
object.close()

file = "myiris.txt"

object2 = open(file,"rb")

sea = pickle.load(object2)
print(sea)

