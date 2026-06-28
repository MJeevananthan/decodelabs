from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
# Load Dataset
iris = load_iris()
X = iris.data
y = iris.target
# Split Dataset
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)
# Create Model
model = DecisionTreeClassifier()
# Train Model
model.fit(X_train, y_train)
# Test Model
y_pred = model.predict(X_test)

# Accuracy
accuracy = accuracy_score(y_test, y_pred)

print("=" * 50)
print("🌸 Iris Flower Classification")
print("=" * 50)
print("Accuracy:", round(accuracy * 100, 2), "%")

# User Prediction
print("\nEnter Flower Details")

sepal_length = float(input("Sepal Length: "))
sepal_width = float(input("Sepal Width: "))
petal_length = float(input("Petal Length: "))
petal_width = float(input("Petal Width: "))

prediction = model.predict([[sepal_length, sepal_width, petal_length, petal_width]])

print()

if prediction[0] == 0:
    print("Predicted Flower : Setosa 🌼")
elif prediction[0] == 1:
    print("Predicted Flower : Versicolor 🌺")
else:
    print("Predicted Flower : Virginica 🌸")