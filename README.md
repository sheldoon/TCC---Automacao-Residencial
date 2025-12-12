# TCC---Automacao-Residencial
Trabalho de Conclusão de Curso - Automação Residencial Aplicada na Acessibilidade de Pessoas com Deficiência na Fala

Para acesso ao trabalho completo, abra o PDF.

Resumo:

O avanço tecnológico possibilitou a utilização de equipamentos eletrônicos interconectados em uma residência, facilitando o controle desses dispositivos e proporcionando maior
conforto. O acionamento e controle por voz de dispositivos inteligentes – como smart
TVs, climatizadores, lâmpadas e robôs aspiradores têm-se tornado realidade por meio de
assistentes virtuais, como Alexa, Google Assistant e Siri. A domótica contribui para o
bem-estar dos residentes, otimizando o tempo gasto em tarefas rotineiras. Contudo, pessoas com deficiência na fala enfrentam barreiras para utilizar os assistentes de voz na
interação com os sistemas de automação residencial. Este trabalho propõe o desenvolvimento de um sistema de integração que permita a esses usuários acionar comandos por
meio do reconhecimento de gestos manuais, utilizando visão computacional para interpretar movimentos simples e naturais. A proposta integra visão computacional, aprendizado
de máquina e comunicação via WiFi, a fim de criar uma interface intuitiva e inclusiva,
e é estruturada em três etapas: reconhecimento de gestos, treinamento de inteligência
artificial e integração hardware/software. Foram testados quatro algoritmos e seus resultados foram avaliados por meio de métricas a fim de escolher qual seria o mais adequado
para aplicação no problema. O algoritmo SVM foi escolhido por apresentar maior precisão
na classificação (acurácia de 93%). Os resultados obtidos indicam alto desempenho com
o algoritmo escolhido, evidenciado pelo reconhecimento de gestos com elevada precisão
em diferentes distâncias e condições de iluminação. A comunicação MQTT entre Raspberry Pi e ESP32 demonstrou baixa latência, garantindo resposta imediata aos comandos.
O sistema mostrou-se eficaz na promoção da acessibilidade, permitindo o controle residencial sem dependência da fala ou contato físico. A combinação do uso de SVM para
classificação e MQTT para comunicação IoT assegurou robustez e replicabilidade, sendo
superados desafios como o equilíbrio e a normalização do conjunto de dados, o que validou
a abordagem técnica adotada.
