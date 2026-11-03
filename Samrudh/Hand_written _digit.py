
from sklearn.datasets import load_digits
import matplotlib.pyplot as plt

digits = load_digits()
# print(digits[1])


# for i in range(4):
#     plt.matshow(digits.images[i])
#     plt.show()

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

X = digits.data
y = digits.target

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model =  LogisticRegression(max_iter=10000)
model.fit(X_train, y_train) # training of machine

print(model.score(X_test, y_test))
