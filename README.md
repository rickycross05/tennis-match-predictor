# 🎾 ATP Tennis Match Predictor

Questo progetto implementa modelli di Machine Learning per prevedere l'esito degli incontri di tennis professionistico maschile (circuito ATP). 

L'obiettivo è analizzare le performance storiche e individuare i pattern determinanti per la vittoria, confrontando diversi algoritmi ad albero per ottimizzare l'accuratezza predittiva.

## 📊 Dati e Metodologia
Il modello è stato addestrato e validato su un dataset contenente i dati storici dei match ATP dal **2021 al 2025**. Le feature ingegnerizzate includono statistiche di gioco, ranking, superfici e storico degli scontri diretti.

## 🧠 Modelli Sviluppati
Sono stati testati e confrontati i seguenti modelli:
*   **Random Forest:** Per catturare relazioni non lineari complesse con bassa varianza.
*   **LightGBM:** Per un training altamente efficiente e per gestire in modo ottimale il bilanciamento delle feature.

## 🛠️ Tecnologie Utilizzate
*   **Linguaggio:** Python
*   **Librerie ML:** Scikit-learn, LightGBM
*   **Manipolazione Dati:** Pandas, NumPy
*   **Data Visualization:** Matplotlib

## 🚀 Come avviare il progetto in locale
1. Clona il repository:
   ```bash git clone https://github.com/rickycross05/tennis-match-predictor.git```