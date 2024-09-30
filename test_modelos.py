import numpy as np
from model_loader import carregar_modelo


# To run: pytest -v test_modelos.py

# Dados para testar o modelo
# O resultado desses dados é: [0, 1, 1]

data = {
    'Age': [70, 80, 85],
    'Gender': [0, 1, 0],
    'Ethnicity': [1, 2, 3],
    'EducationLevel': [2, 1, 3],
    'BMI': [23.5, 29.4, 20.1],
    'Smoking': [0, 1, 0],
    'AlcoholConsumption': [5.0, 2.0, 10.0],
    'PhysicalActivity': [7.5, 5.0, 6.0],
    'DietQuality': [3.0, 2.0, 4.0],
    'SleepQuality': [7.0, 5.0, 6.0],
    'FamilyHistoryAlzheimers': [1, 0, 1],
    'CardiovascularDisease': [1, 0, 0],
    'Diabetes': [0, 1, 0],
    'Depression': [1, 0, 1],
    'HeadInjury': [0, 1, 0],
    'Hypertension': [1, 1, 0],
    'SystolicBP': [120, 140, 130],
    'DiastolicBP': [80, 90, 85],
    'CholesterolTotal': [200, 250, 210],
    'CholesterolLDL': [100, 150, 120],
    'CholesterolHDL': [60, 55, 65],
    'CholesterolTriglycerides': [150, 180, 160],
    'MMSE': [28, 22, 18],
    'FunctionalAssessment': [2.0, 3.5, 1.5],
    'MemoryComplaints': [1, 1, 0],
    'BehavioralProblems': [0, 1, 1],
    'ADL': [5.0, 6.0, 4.0],
    'Confusion': [0, 1, 1],
    'Disorientation': [0, 1, 1],
    'PersonalityChanges': [1, 0, 1],
    'DifficultyCompletingTasks': [1, 1, 0],
    'Forgetfulness': [1, 1, 0]
}

# Função que organiza os dados no formato necessário para a predição


def preparar_dados(data):
    # Para cada paciente (índice i), extrai o valor correspondente de cada característica.
    return np.array([[
        data['Age'][i], data['Gender'][i], data['Ethnicity'][i], data['EducationLevel'][i],
        data['BMI'][i], data['Smoking'][i], data['AlcoholConsumption'][i], data['PhysicalActivity'][i],
        data['DietQuality'][i], data['SleepQuality'][i], data['FamilyHistoryAlzheimers'][i],
        data['CardiovascularDisease'][i], data['Diabetes'][i], data['Depression'][i], data['HeadInjury'][i],
        data['Hypertension'][i], data['SystolicBP'][i], data['DiastolicBP'][i], data['CholesterolTotal'][i],
        data['CholesterolLDL'][i], data['CholesterolHDL'][i], data['CholesterolTriglycerides'][i],
        data['MMSE'][i], data['FunctionalAssessment'][i], data['MemoryComplaints'][i],
        data['BehavioralProblems'][i], data['ADL'][i], data['Confusion'][i], data['Disorientation'][i],
        data['PersonalityChanges'][i], data['DifficultyCompletingTasks'][i], data['Forgetfulness'][i]
    ] for i in range(len(data['Age']))])  # O 'for' itera sobre a quantidade de pacientes, com base no tamanho da lista no primeiro campo

# Testando o modelo


def test_model():
    # Carrega o pipeline e a acurácia
    pipeline, accuracy = carregar_modelo()

    # Prepara os dados
    dados_paciente = preparar_dados(data)

    # Faz a predição
    predicoes = pipeline.predict(dados_paciente)

    # Verifica as predições esperadas
    esperado = [0., 1., 1.]  # Predições esperada

    # Verifica a acurácia
    assert accuracy > 0.9, f"Acurácia baixa: {accuracy}"

    # Verifica se as predições estão corretas
    assert np.array_equal(
        predicoes, esperado), f"Predições incorretas: {predicoes} != {esperado}"

    print(f"Predições: {predicoes}, Acurácia: {accuracy}")
