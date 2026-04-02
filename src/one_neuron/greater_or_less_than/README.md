## Files

greater_or_less_than.py         → neuron engine
train_greater_or_less_than.py   → trainer, loads dataset from JSON
greater_or_less_than_ui.py      → terminal interface
neuron_data.json                → persistent trained weights
dataset.json                    → static training dataset (18 samples)

---

## Trained Weights

weights:  5.336155456996256
bias:     -0.0005995581191612629

Weight of 5.34 produces sigmoid(5.34) ≈ 0.9952 for a 
difference of 1 — highly confident even on the smallest 
non-equal comparison. Bias of essentially zero confirms 
a perfectly symmetric learned boundary.

---

## Dataset

18 static examples stored in dataset.json.
9 greater-than cases and 9 less-than cases, perfectly balanced.
No equal cases — equal inputs are detected in the UI before
the neuron is called and return 0.5 directly.

All training examples compare against 0 as the second value.
Feature engineering (A - B) ensures the neuron generalises
correctly to all value pairs regardless of this pattern.

---

## Architecture Notes

Equal case handling was deliberately moved out of the neuron
engine and into the UI. The neuron itself is a pure binary
classifier — it only ever sees strictly greater-than and
strictly less-than cases. This keeps the neuron's job clean
and the bias near zero.
