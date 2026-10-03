from sklearn import*
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

X=[[177,30],[180,82],[160,60],[175,80],[140,40],[200,100],[180,77],[1,99],[700,1],[168,80]]
y=['fausse','un homme','une femme','un homme','une femme','un homme','une femme','fausse','fausse','une femme']


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
model = DecisionTreeClassifier()


model.fit(X_train, y_train)
precision=accuracy_score(y_test, y_pred=model.predict(X_test))

teste_moi=[[1,75]]
phrase=[str(teste_moi).replace("[","").replace("]","").replace(","," et"), str(model.predict(teste_moi)).replace("[","").replace("]","").replace("'","").replace("'","")]

if precision==0:
    print(f"Je ne suis vraiment pas sûr pour ce coup...\nSelon moi, avec des mensurations de {phrase[0]}, la personne est {phrase[1]}... J'en suis sûr à {precision*100:.0f}%")
else:
    print(f"Selon moi, avec des mensurations de {phrase[0]}, la personne est {phrase[1]}... J'en suis sûr à {precision*100:.0f}%")