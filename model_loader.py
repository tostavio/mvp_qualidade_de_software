import pickle


def carregar_modelo(filepath='./MachineLearning/models/model.pkl'):
    """
    Carrega o pipeline do modelo e a acurácia do arquivo .pkl.

    Args:
        filepath (str): Caminho do arquivo .pkl que contém o modelo e a acurácia.

    Returns:
        tuple: Retorna o pipeline carregado e a acurácia.
    """
    with open(filepath, 'rb') as f:
        model_data = pickle.load(f)
        pipeline = model_data['pipeline']
        accuracy = model_data['accuracy']
    return pipeline, accuracy
