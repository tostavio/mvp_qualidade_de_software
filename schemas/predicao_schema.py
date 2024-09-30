from pydantic import BaseModel

# Schema para a predição de um paciente

# UpperCamelCase utilizado para manter a compatibilidade com o
# modelo de predição, que espera os dados em UpperCamelCase


class PacienteSchema(BaseModel):
    """ Define como um paciente à ser predito deve ser representado.
    """
    Age: int  # Idade
    Gender: int  # Gênero
    Ethnicity: int  # Etnia
    EducationLevel: int  # Nível Educacional
    BMI: float  # Índice de Massa Corporal (IMC)
    Smoking: int  # Fumante
    AlcoholConsumption: float  # Consumo de Álcool
    PhysicalActivity: float  # Atividade Física
    DietQuality: float  # Qualidade da Dieta
    SleepQuality: float  # Qualidade do Sono
    FamilyHistoryAlzheimers: int  # Histórico Familiar de Alzheimer
    CardiovascularDisease: int  # Doença Cardiovascular
    Diabetes: int  # Diabetes
    Depression: int  # Depressão
    HeadInjury: int  # Lesão na Cabeça
    Hypertension: int  # Hipertensão
    SystolicBP: int  # Pressão Sistólica
    DiastolicBP: int  # Pressão Diastólica
    CholesterolTotal: int  # Colesterol Total
    CholesterolLDL: int  # Colesterol LDL
    CholesterolHDL: int  # Colesterol HDL
    CholesterolTriglycerides: int  # Triglicerídeos
    MMSE: int  # Mini Mental State Examination
    FunctionalAssessment: float  # Avaliação Funcional
    MemoryComplaints: int  # Queixas de Memória
    BehavioralProblems: int  # Problemas Comportamentais
    ADL: float  # Atividades de Vida Diária (ADL)
    Confusion: int  # Confusão
    Disorientation: int  # Desorientação
    PersonalityChanges: int  # Mudanças de Personalidade
    DifficultyCompletingTasks: int  # Dificuldade em Completar Tarefas
    Forgetfulness: int  # Esquecimento


class PacientePredictionSchema(BaseModel):
    """Define o retorno da predição de um paciente.
    """
    prediction: int = None  # Predição do modelo (resultado)
    accuracy: float = None  # Acurácia do modelo para o conjunto de testes


def apresenta_predicao(prediction: int, accuracy: float) -> dict:
    """ Retorna uma representação do paciente seguindo o schema definido em
        PacienteViewSchema, incluindo a predição e a acurácia.
    """
    return {
        "prediction": prediction,  # Incluindo predição
        "accuracy": accuracy  # Incluindo acurácia
    }
