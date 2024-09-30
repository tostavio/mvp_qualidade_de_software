
from flask_openapi3 import OpenAPI, Info, Tag
from flask import redirect, request, jsonify
import numpy as np
from logger import logger
from flask_cors import CORS

from model_loader import carregar_modelo
from schemas import *

# Instanciando o objeto OpenAPI
info = Info(title="API de Predição de Alzheimer", version="1.0.0")
app = OpenAPI(__name__, info=info)
CORS(app)

# Definindo tags para agrupamento das rotas
home_tag = Tag(name="Documentação",
               description="Seleção de documentação: Swagger, Redoc ou RapiDoc")
predicao_tag = Tag(
    name="Predição", description="Realiza a predição de Alzheimer com base nos dados fornecidos")

# Rota home


@app.get('/', tags=[home_tag])
def home():
    """Redireciona para /openapi, tela que permite a escolha do estilo de documentação."""
    return redirect('/openapi')


# Rota de predição
@app.post('/predict', tags=[predicao_tag],
          responses={"200": PacientePredictionSchema, "404": ErrorSchema})
def predict():
    """
    Realiza a predição de Alzheimer com base nos dados do paciente.

    Args:
        Age (int): Idade do paciente.
        Gender (int): Gênero: 0 para Masculino, 1 para Feminino.
        Ethnicity (int): Etnia: 0 para Caucasiano, 1 para Afroamericano, 2 para Asiático, 3 para Outros.
        EducationLevel (int): Nível educacional: 0 para Nenhum, 1 para Ensino Médio, 2 para Graduação, 3 para Pós-graduação.
        BMI (float): Índice de Massa Corporal (IMC).
        Smoking (int): Fumante: 0 para Não, 1 para Sim.
        AlcoholConsumption (float): Consumo de álcool semanal (em unidades).
        PhysicalActivity (float): Atividade física semanal (em horas).
        DietQuality (float): Qualidade da dieta (0 a 10).
        SleepQuality (float): Qualidade do sono (0 a 10).
        FamilyHistoryAlzheimers (int): Histórico familiar de Alzheimer: 0 para Não, 1 para Sim.
        CardiovascularDisease (int): Doença cardiovascular: 0 para Não, 1 para Sim.
        Diabetes (int): Presença de diabetes: 0 para Não, 1 para Sim.
        Depression (int): Presença de depressão: 0 para Não, 1 para Sim.
        HeadInjury (int): Lesão na cabeça: 0 para Não, 1 para Sim.
        Hypertension (int): Hipertensão: 0 para Não, 1 para Sim.
        SystolicBP (int): Pressão arterial sistólica (mmHg).
        DiastolicBP (int): Pressão arterial diastólica (mmHg).
        CholesterolTotal (int): Colesterol total (mg/dL).
        CholesterolLDL (int): Colesterol LDL (mg/dL).
        CholesterolHDL (int): Colesterol HDL (mg/dL).
        CholesterolTriglycerides (int): Triglicerídeos (mg/dL).
        MMSE (int): Mini Mental State Examination (MMSE) (0 a 30).
        FunctionalAssessment (float): Avaliação funcional (0 a 10).
        MemoryComplaints (int): Queixas de memória: 0 para Não, 1 para Sim.
        BehavioralProblems (int): Problemas comportamentais: 0 para Não, 1 para Sim.
        ADL (float): Atividades de vida diária (ADL) (0 a 10).
        Confusion (int): Presença de confusão: 0 para Não, 1 para Sim.
        Disorientation (int): Desorientação: 0 para Não, 1 para Sim.
        PersonalityChanges (int): Mudanças de personalidade: 0 para Não, 1 para Sim.
        DifficultyCompletingTasks (int): Dificuldade em completar tarefas: 0 para Não, 1 para Sim.
        Forgetfulness (int): Esquecimento: 0 para Não, 1 para Sim.

    Returns:
        Um dicionário contendo:
        prediction (int): O resultado da predição (1 para positivo, 0 para negativo).
        accuracy (float): A acurácia do modelo de predição.
    """
    try:
        # Carregar o modelo e a acurácia
        pipeline, accuracy = carregar_modelo()

        # Recebe os dados do paciente no formato JSON
        dados_paciente = request.json

        # Valida os dados com o Pydantic, que agora aceita os campos UpperCamelCase
        paciente = PacienteSchema(**dados_paciente)

        # Converte os dados do paciente em um array NumPy
        paciente_np = np.array([[
            paciente.Age, paciente.Gender, paciente.Ethnicity, paciente.EducationLevel,
            paciente.BMI, paciente.Smoking, paciente.AlcoholConsumption,
            paciente.PhysicalActivity, paciente.DietQuality, paciente.SleepQuality,
            paciente.FamilyHistoryAlzheimers, paciente.CardiovascularDisease,
            paciente.Diabetes, paciente.Depression, paciente.HeadInjury,
            paciente.Hypertension, paciente.SystolicBP, paciente.DiastolicBP,
            paciente.CholesterolTotal, paciente.CholesterolLDL,
            paciente.CholesterolHDL, paciente.CholesterolTriglycerides,
            paciente.MMSE, paciente.FunctionalAssessment,
            paciente.MemoryComplaints, paciente.BehavioralProblems, paciente.ADL,
            paciente.Confusion, paciente.Disorientation, paciente.PersonalityChanges,
            paciente.DifficultyCompletingTasks, paciente.Forgetfulness
        ]])

        # Faz a predição usando o modelo carregado
        prediction = pipeline.predict(paciente_np)
        logger.info(f"Predição realizada com sucesso: {prediction[0]}")

        # Formata a resposta usando PacientePredictionSchema
        resultado = apresenta_predicao(prediction[0], accuracy)

        return jsonify(resultado), 200

    except Exception as e:
        print(e)
        return jsonify({"error": str(e)}), 400


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
