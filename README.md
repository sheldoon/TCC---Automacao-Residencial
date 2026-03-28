# 🤟 Automação Residencial para Acessibilidade de Pessoas com Deficiência na Fala

> Sistema de controle residencial por reconhecimento de gestos manuais — sem voz, sem toque.

---

## 📌 Sobre o Projeto

Pessoas com deficiência na fala enfrentam barreiras concretas para usar assistentes de voz (Alexa, Google Assistant, Siri) em sistemas de automação residencial. Este projeto resolve esse problema com visão computacional e machine learning: o usuário controla luzes, climatizadores, persianas e multimídia por meio de gestos simples capturados por câmera.

Desenvolvido como Trabalho de Conclusão de Curso em Engenharia de Controle e Automação no **Instituto Federal de Goiás (IFG)** — aprovado em banca em março de 2025.

---

## 🏗️ Arquitetura do Sistema

```
Câmera → MediaPipe (detecção de mão) → Extração de landmarks → Classificador SVM
                                                                        ↓
                                                           Comando via MQTT (WiFi)
                                                                        ↓
                                                    Raspberry Pi 4 → ESP32 → Dispositivos
```

O sistema opera em tempo real com três camadas integradas:
1. **Visão Computacional** — captura e extração de landmarks com MediaPipe (Python/OpenCV)
2. **Classificação ML** — modelo SVM treinado para identificar gestos específicos
3. **Comunicação IoT** — protocolo MQTT entre Raspberry Pi 4 e ESP32 via WiFi

---

## 🤖 Machine Learning — Comparação de Algoritmos

Quatro algoritmos foram treinados, validados e comparados por métricas de classificação:

| Algoritmo | Acurácia | Observação |
|---|---|---|
| **SVM** | **93%** | ✅ Escolhido — melhor F1-Score geral |
| Random Forest | ~88% | Boa generalização, maior custo computacional |
| KNN | ~85% | Sensível a variações de iluminação |
| Árvore de Decisão | ~80% | Menor robustez com dados desbalanceados |

**Processo completo de ML:**
- Coleta e criação de dataset próprio (imagens capturadas em diferentes condições)
- Normalização e balanceamento dos dados
- Extração de features via landmarks do MediaPipe
- Busca de hiperparâmetros (Grid Search)
- Avaliação por acurácia, precisão, recall e F1-Score
- Validação em diferentes distâncias e condições de iluminação

---

## 🛠️ Stack Técnico

| Camada | Tecnologias |
|---|---|
| Linguagem principal | Python, C++ |
| Visão computacional | OpenCV, MediaPipe |
| Machine Learning | Scikit-learn (SVM, Random Forest, KNN, Decision Tree) |
| Hardware | Raspberry Pi 4 Modelo B, ESP32 |
| Comunicação IoT | Protocolo MQTT (WiFi) |
| Interface mobile | Aplicativo de controle (Android) |
| Controle de versão | Git / GitHub |

---

## 📊 Resultados

- Acurácia de **93%** na classificação de gestos com SVM
- Reconhecimento estável em **diferentes distâncias e condições de iluminação**
- Comunicação MQTT com **baixa latência**, garantindo resposta imediata aos comandos
- Sistema validado em hardware real (Raspberry Pi + ESP32)
- Desafios superados: desbalanceamento de dataset, normalização de features, variações de ambiente

---

## 👥 Autores

- **João Pedro Ferreira Resende** — [LinkedIn](https://www.linkedin.com/in/joao-pedro-ferreira-resende) · [GitHub](https://github.com/sheldoon)
- Gustavo Borba Bessa
- Victor Hugo Marinho da Silva

**Orientador:** Prof. Dr. José Luiz Ferraz Barbosa — IFG Câmpus Goiânia

---

## 📄 Referência Acadêmica

> Bessa, Gustavo Borba.
Automação residencial aplicada na acessibilidade de pessoas com deficiência
na fala / Gustavo Borba Bessa, João Pedro Ferreira Resende, Victor Hugo
Marinho da Silva. – Goiânia: Instituto Federal de Educação, Ciência e Tecnologia
de Goiás, Câmpus Goiânia, 2025

