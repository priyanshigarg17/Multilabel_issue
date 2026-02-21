from sklearn.model_selection import train_test_split
from config.config import TEST_SIZE, RANDOM_STATE

def preprocess_data(df):

    X = df[["age", "annual_income",
            "purchase_frequency",
            "time_spent_on_app",
            "is_premium_user"]]

    y = df[["label_fashion",
            "label_electronics",
            "label_home_decor",
            "label_sports",
            "label_books"]]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y,
        test_size=TEST_SIZE,
        random_state=RANDOM_STATE
    )

    return X_train, X_test, y_train, y_test