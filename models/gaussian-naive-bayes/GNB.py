import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

from sklearn.naive_bayes import GaussianNB
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix, ConfusionMatrixDisplay

DATA = Path(__file__).resolve().parents[2] / "data" / "raw" / "email_phishing_data.csv"
emails = pd.read_csv(DATA).dropna()

print(emails.shape)
print(emails["label"].value_counts())

X = emails.drop(columns = ["label"])
y = emails["label"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 42, stratify = y)

model = GaussianNB()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)
print("Accuracy:", accuracy_score(y_test, y_pred))
print(classification_report(y_test, y_pred))

#graphs generated with claude
# Chart 1: confusion matrix
cm = confusion_matrix(y_test, y_pred)
ConfusionMatrixDisplay(cm, display_labels=model.classes_).plot(cmap="Blues")
plt.title("Phishing email detection: confusion matrix")
plt.savefig("confusion_matrix.png", dpi=150, bbox_inches="tight")
plt.show()

# Chart 2: average of each feature by class, scaled so every feature fits on one axis
means = emails.groupby("label").mean()
(means / means.max()).T.plot(kind="barh", figsize=(8, 5))
plt.xlabel("Average value (scaled to the larger class = 1)")
plt.title("Which features differ between the classes?")
plt.tight_layout()
plt.savefig("feature_means.png", dpi=150, bbox_inches="tight")
plt.show()