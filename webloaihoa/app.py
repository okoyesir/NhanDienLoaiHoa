from flask import Flask, render_template, request
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
import seaborn as sns
import matplotlib.pyplot as plt
import os

# --- Load dữ liệu & huấn luyện model ---
df = pd.read_csv("Iris.csv")
X = df.drop(["Id", "Species"], axis=1)
y = df["Species"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
knn = KNeighborsClassifier(n_neighbors=5)
knn.fit(X_train, y_train)

# --- Đánh giá mô hình ---
y_pred = knn.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
report = classification_report(y_test, y_pred, output_dict=True)
matrix = confusion_matrix(y_test, y_pred)

# Vẽ confusion matrix và lưu ảnh
plt.figure(figsize=(4,3))
sns.heatmap(matrix, annot=True, cmap="Blues", fmt="d",
            xticklabels=knn.classes_, yticklabels=knn.classes_)
plt.title("Confusion Matrix")
plt.ylabel("Thực tế")
plt.xlabel("Dự đoán")
if not os.path.exists("static"):
    os.mkdir("static")
plt.savefig("static/confusion_matrix.png")
plt.close()

# --- Flask app ---
app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    prediction = None
    if request.method == "POST":
        try:
            sl = float(request.form["sepal_length"])
            sw = float(request.form["sepal_width"])
            pl = float(request.form["petal_length"])
            pw = float(request.form["petal_width"])
            sample = [[sl, sw, pl, pw]]
            prediction = knn.predict(sample)[0]
        except:
            prediction = "❌ Lỗi nhập dữ liệu!"
    return render_template("index.html", 
                           prediction=prediction,
                           accuracy=round(accuracy*100,2),
                           report=report,
                           image_path="static/confusion_matrix.png")

if __name__ == "__main__":
    app.run(debug=True)
