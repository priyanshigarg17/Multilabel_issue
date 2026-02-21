from sklearn.metrics import accuracy_score, f1_score, hamming_loss

def evaluate_model(y_test, y_pred):

    print("Exact Match Accuracy:",
          accuracy_score(y_test, y_pred))

    print("Hamming Loss:",
          hamming_loss(y_test, y_pred))

    print("Micro F1 Score:",
          f1_score(y_test, y_pred, average='micro'))