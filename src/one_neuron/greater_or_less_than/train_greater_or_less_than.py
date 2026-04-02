import greater_or_less_than as neuron
import json
import random

# Get data set
with open("dataset.json", "r") as f:
    dataset = json.load(f)

print(f"Dataset loaded: {len(dataset)} samples")

# Dynamically Initializing trainig data memory
try:
    with open("neuron_data.json", "r") as d:
        data = json.load(d)
    weights = data["weights"]
    bias = data["bias"]
except Exception:
    weights = 0
    bias = 0.0
learning_rate = 0.1

# Main training loop
for i in range(0, 1000):
    # Shuffle dataset each epoch to prevent learning order-specific patterns
    random.shuffle(dataset)
# Example loop
    for j in range(len(dataset)):
        # Train function takes input, weight, bias, answer and learning rate
        # And it returns weights and bias in that order.
        weights, bias = neuron.train(dataset[j][0], dataset[j][1], learning_rate, weights, bias) 
    if ((i + 1) % 100) == 0:
        # Every 100 epochs print the current epoch and the loss on each example.
        print(f"Current epoch: {i + 1}")  
        # Loss function takes answer and prediction and returns loss
        # Forward function takes input, weight and bias and returns prediction
        # using sigmoid.   
        # Here we represent averege loss for each epoch
        avg_loss = 0
        for inx in range(len(dataset)):
            avg_loss += neuron.loss(dataset[inx][1], neuron.forward(dataset[inx][0], weights, bias))
        print(f"Current average loss across dataset: {avg_loss / len(dataset)}")   
# Save training data at the end of loop
data = {
    "weights": weights,
    "bias": bias,
}
with open("neuron_data.json", "w") as d:
    json.dump(data, d)     




                 