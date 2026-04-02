import math
import json 
# The scope of this project is to find the difference between to values ranging from 0-9
# or their string representation zero - nine, than difference is then use to tell if inputs
# are greater or less than each other, if not, they are equal.
# Note cases of equal values were not trained and handled in UI 
# The single neuron is then trained with this in mind.

# Dictionary for data relationship
relation = {
    "zero": 0,
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
}
# Neuron memory retrival to set as default data for forward function
def get_neuron_data():
    try:
        with open("neuron_data.json", "r") as d:
            data = json.load(d)
        weights = data["weights"]
        bias = data["bias"]
    except Exception:
        weights = 0.0
        bias = 0.0
    return weights, bias
neuron_data = get_neuron_data()

def encoder_router(input, i = 0):
    # Handling errors to only accept values in relation table or between 0-9
    # Since user inputs from terminal will always be a string 
    # To normalize user input for encoding and fix string input issues, try convert to int
    # if no errors raise value is an int
    # except errors were raised value will be treated as string
    # After normalization is then values are then checked to be within contraints of values
    try:
        nom_input = int(input[i])
        if 0 > nom_input or nom_input > 9:
            raise Exception("Invalid input, values must be between 0-9 or zero-nine")
        else:
            return nom_input
    except ValueError:
        val = input[i].lower()
        if not val in relation:
            raise Exception("Invalid input, values must be between 0-9 or zero-nine")
        else:
            return relation[val]         
        
def weighted_sum(inputs, weights, bias):
    # Weighted sums formula have been simplified through feature engineering for faster and accurate training
    # Since comparison between to values is only ever A - B = C, where C is the difference
    # The new weighted sums then becomes Weights(A - B) + bias as inputs are then differentaited to one
    # We only ever need one weight with our bias
    # Handling edge case errors for invalid argument data types
    if type(inputs) != list:
        raise Exception("Inputs dataset must be a list")
    if type(weights) != int and type(weights) != float:
        raise Exception("Weights must be an Integer or float value")
    if type(bias) != int and type(bias) != float:
        raise Exception("Biases must be an Integer or float value")
    
    # Going through inputs list encoded them and then find their difference
    enc_input1 = encoder_router(inputs, 0)
    enc_input2 = encoder_router(inputs, 1)
    enc_input = enc_input1 - enc_input2
    return weights * (enc_input) + bias

# Add the activation func
def sigmoid(x):
    return 1 / (1 + math.exp(-x)) 

# Adding forward pass
def forward(inputs, weights = neuron_data[0], bias = neuron_data[1]):
    return sigmoid(weighted_sum(inputs, weights, bias))

# Adding loss function, where y is excpected guess and p is actual guess
def loss(y, p):
    p = max(1e-10, min(1 - 1e-10, p))
    return -(y * math.log(p) + (1 - y) * math.log(1 - p))

# Adding trainer, where y is excpected guess and p is actual guess
def train(inputs,  y, learning_rate, weights = neuron_data[0], bias = neuron_data[1]):
    input1 = encoder_router(inputs, 0)
    input2 = encoder_router(inputs, 1)
    p = forward(inputs, weights, bias)
    error = p - y
    # Difference of inputs feature also implemented here
    new_weights = weights - learning_rate * error * (input1 - input2)
    bias = bias - learning_rate * error
    return new_weights, bias
