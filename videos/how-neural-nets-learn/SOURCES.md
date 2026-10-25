# Sources (all pages opened via fetch)

- https://www.3blue1brown.com/lessons/gradient-descent
  - "this network has 13,002 weights and biases that we can adjust." (two hidden layers of 16 neurons)
  - "we mean changing the weights and biases to minimize a cost function."
  - "add up the squares of the differences between each of these trash output activations"; "the average cost over all the tens of thousands of training examples."
- https://www.3blue1brown.com/lessons/backpropagation
  - "Backpropagation, the topic of this lesson, is an algorithm for computing that negative gradient."
  - "To get the most bang for your buck, adjust the weights in proportion to their associated activations."
  - "the process of gradient descent looks more like a drunk man stumbling aimlessly down a hill."
- https://cs231n.github.io/optimization-1/
  - "start with random weights and iteratively refine them over time to get lower loss."
  - "will become one of the most important (and most headache-inducing) hyperparameter settings"; "if it is too low the progress is steady but slow. If it is too high the progress can be faster, but more risky."
  - "hiking on a hilly terrain with a blindfold on, and trying to reach the bottom."
- https://cs231n.github.io/optimization-2/
  - "computing gradients of expressions through recursive application of chain rule"; "a beautifully local process"; "gates communicating to each other (through the gradient signal) whether they want their outputs to increase or decrease."
- https://developers.google.com/machine-learning/crash-course/linear-regression/gradient-descent
  - "Calculate the loss with the current weight and bias." / "Move the weight and bias values a small amount in the direction that reduces loss." / "When a model converges, additional iterations don't reduce loss more."
- https://developers.google.com/machine-learning/crash-course/neural-networks/backpropagation
  - "makes gradient descent feasible for multi-layer neural networks"; "Layers with vanishing gradients train very slowly, or not at all."
- https://en.wikipedia.org/wiki/Backpropagation
  - "It is an efficient application of the chain rule to neural networks." (per-layer gradients computed once and reused)
- https://d2l.ai/chapter_optimization/sgd.html
  - "is an unbiased estimate of the full gradient." (page states this for a single sampled example; script says "small batch... errors cancel on average", matching the outline claim; minibatch detail is on the next d2l section, not opened)

Illustrative: squared error 0.81 for guess 0.1 vs answer 1.0 is arithmetic, marked "for example" in the script.
