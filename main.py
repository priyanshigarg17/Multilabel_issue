from src.data_loader import load_data
from src.preprocess import preprocess_data
from src.model import build_model
from src.evaluate import evaluate_model

def main():

    df = load_data("data/multilabel_ecommerce_dataset.csv")

    X_train, X_test, y_train, y_test = preprocess_data(df)

    model = build_model()

    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)

    evaluate_model(y_test, y_pred)

if __name__ == "__main__":
    main()