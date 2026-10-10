# Wake word "Alis" per openWakeWord

Modello pronto all'uso che riconosce la parola **«Alis»** (pronuncia italiana).
Allenato con openWakeWord su 10.000 campioni + 1.000 di validazione, con
riverbero simulato e decine di frasi confondibili come negativi
(alice, alias, elisa, alzati, almeno, ascolta…). Esito misurato: recall 99%,
precisione 92%, falsi positivi 9%.

## Installazione

```bash
pip install openwakeword
python install_model.py
```

Copia `alis.onnx` nella cartella dei modelli di openWakeWord. Niente cloud:
tutto gira in locale.

## Uso

```python
from openwakeword.model import Model

model = Model(wakeword_models=["alis"], inference_framework="onnx")
# oppure col percorso completo del file:
# model = Model(wakeword_models=["/percorso/a/alis.onnx"], inference_framework="onnx")

# frame audio: int16 mono a 16 kHz, a blocchi (es. 1280 campioni)
scores = model.predict(frame_int16)
if scores.get("alis", 0) >= 0.5:
    print("Alis!")
```

Soglia consigliata: `0.5`. Alzala se scatta troppo spesso, abbassala se a
volte non ti sente.

## File

| File | Cosa è |
|---|---|
| `alis.onnx` | il modello (849 KB) |
| `install_model.py` | lo copia al posto giusto |
| `alis.yaml` | la configurazione usata per l'addestramento (riferimento / riallenamento) |
| `LICENSE` | CC BY-NC 4.0 (solo uso non commerciale) |
