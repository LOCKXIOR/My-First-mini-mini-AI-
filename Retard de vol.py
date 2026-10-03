from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

# X : [Distance (km), Heure de départ, Nb passagers]
X = [
    [500, 8.0, 150],
    [1200, 18.5, 220],
    [300, 21.0, 80],
    [2500, 14.0, 300],
    [800, 7.5, 120],
    [1500, 19.0, 250],
    [400, 9.0, 90],
    [3000, 22.5, 280],
    [600, 11.0, 110],
    [1800, 20.0, 210]
]

# y : 1 = Retardé, 0 = À l'heure
y = [0, 1, 0, 1, 0, 1, 0, 1, 0, 1]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)

model=DecisionTreeClassifier()

model.fit(X_train,y_train)

pertinence=accuracy_score(y_test, y_pred=model.predict(X_test))
ped=[[1400,19.5,200]]

def event(n):
    if n[0] == 0:
        return "à l'heure"
    else : 
        return "retardé"

print(f"Voilà ce que je pense : le vol étudié est {event(model.predict(ped))}, j'en suis sûr à {pertinence*100:.0f}%")