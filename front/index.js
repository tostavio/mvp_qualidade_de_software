async function submitForm(event) {
  event.preventDefault();

  const form = document.getElementById("predictionForm");
  const modalBody = document.getElementById("modalBody");

  modalBody.textContent = "";
  modalBody.classList.remove("text-danger", "text-success");

  const formData = new FormData(form);

  const keysToConvert = [
    "Age",
    "Gender",
    "Ethnicity",
    "EducationLevel",
    "BMI",
    "Smoking",
    "AlcoholConsumption",
    "PhysicalActivity",
    "DietQuality",
    "SleepQuality",
    "FamilyHistoryAlzheimers",
    "CardiovascularDisease",
    "Diabetes",
    "Depression",
    "HeadInjury",
    "Hypertension",
    "SystolicBP",
    "DiastolicBP",
    "CholesterolTotal",
    "CholesterolLDL",
    "CholesterolHDL",
    "CholesterolTriglycerides",
    "MMSE",
    "FunctionalAssessment",
    "MemoryComplaints",
    "BehavioralProblems",
    "ADL",
    "Confusion",
    "Disorientation",
    "PersonalityChanges",
    "DifficultyCompletingTasks",
    "Forgetfulness",
  ];

  const formDataEntries = Array.from(formData.entries());
  const data = formDataEntries.reduce((acc, [key, value]) => {
    acc[key] = keysToConvert.includes(key) ? parseFloat(value) : value;
    return acc;
  }, {});

  console.log(data);

  try {
    const response = await fetch("http://localhost:5000/predict", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(data),
    });

    if (response.ok) {
      const result = await response.json();
      console.log(result);

      if (result.prediction === 1) {
        modalBody.textContent = "O paciente tem Alzheimer.";
        modalBody.classList.add("text-danger");
      }
      if (result.prediction === 0) {
        modalBody.textContent = "O paciente não tem Alzheimer.";
        modalBody.classList.add("text-success");
      }

      const accuracyInfo = document.createElement("p");
      accuracyInfo.textContent = `Acurácia do modelo: ${result.accuracy}`;
      modalBody.appendChild(accuracyInfo);
    } else {
      modalBody.textContent =
        "Erro ao realizar a predição. Verifique os dados inseridos.";
      modalBody.classList.add("text-danger");
    }
  } catch (error) {
    modalBody.textContent = "Erro ao conectar com o servidor.";
    modalBody.classList.add("text-danger");
  }

  const resultModal = new bootstrap.Modal(
    document.getElementById("resultModal")
  );
  resultModal.show();
}
