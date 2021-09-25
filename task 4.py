print('Task 4')
d={"title":"Cake","price":100,"ingredients":["eggs","milk","flour","sugar"]}
d["description"]="Cake is a form of sweet food made from flour, sugar,and other ingredients, that is usually baked."
d["price"]=d["price"]+100
d["ingredients"]=d["ingredients"]+["chocolate"]
print(len(d["ingredients"]))
d.pop("description") 