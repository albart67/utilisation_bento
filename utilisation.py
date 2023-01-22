var1 = float(input('Mesure 1 : '))
var2 = float(input('Mesure 2 : '))
var3 = float(input('Mesure 3 : '))
var4 = float(input('Mesure 4 : '))

import bentoml

Model = bentoml.sklearn.get("iris_clf:latest").to_runner()
Model.init_local()
pred = Model.predict.run([[var1, var2, var3, var4]])
print(pred)

# Exemple de valeurs : 5.7, 2.6, 4.1, 1.3