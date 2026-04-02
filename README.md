# neural-forge

Every engineer who truly understands deep learning once 
sat down and built it from scratch.

This repo is that process — documented. Starting from a 
single neuron in pure Python, adding one concept at a time, 
and working up through NumPy, PyTorch, and beyond. No 
shortcuts. No black boxes. Every abstraction earned.

---

## The Philosophy

Libraries are tools. Tools are only powerful in the hands 
of someone who understands what they are replacing.

Before touching a framework, the goal here is to know 
exactly what happens inside it — the math, the logic, 
the decisions, and the tradeoffs. That foundation is what 
this repo is built on.

---

## The Journey

### Phase 1 — Pure Python (current)
No libraries. No abstractions. Just math and code.
Build every function by hand. Understand every number.

### Phase 2 — NumPy
Same concepts, vectorized. Feel why NumPy exists by 
having already done it without it.

### Phase 3 — PyTorch
Same concepts, GPU accelerated. Read the source code 
and recognise everything inside it.

### Phase 4 — Full Stack AI
Agents, orchestration, LLMs. Built on a foundation 
that was earned, not installed.

---

## Structure
```
src/
  one_neuron/
    greater_or_less_than/     ← single neuron comparison system
  ten_neurons/                ← coming soon

datasets/
  one_neuron/
    greater_or_less_than/     ← static training dataset
  ten_neurons/                ← coming soon
```

---

## Progress

### One Neuron — Pure Python
- [x] Weighted sum
- [x] Sigmoid activation
- [x] Binary cross entropy loss
- [x] Gradient descent
- [x] Persistent weight storage
- [x] Encoder router — integer and string inputs
- [x] Feature engineering — A minus B difference
- [x] Static JSON dataset
- [x] Epoch shuffling
- [x] Average loss monitoring
- [x] Terminal UI with three-outcome decision logic
- [x] Greater or less than comparison system

### Ten Neurons — Pure Python (Current)
- [ ] Hidden layer architecture
- [ ] Backpropagation
- [ ] Chain rule
- [ ] XOR solved

### NumPy Refactor
- [ ] Vectorized operations
- [ ] Matrix multiplication

### PyTorch
- [ ] Same architecture, autograd
- [ ] GPU acceleration
