import torch
from common import *

inputs = torch.tensor(
  [[0.43, 0.15, 0.89],          # Your     (x^1)
   [0.55, 0.87, 0.66],          # journey  (x^2)
   [0.57, 0.85, 0.64],          # starts   (x^3)
   [0.22, 0.58, 0.33],          # with     (x^4)
   [0.77, 0.25, 0.10],          # one      (x^5)
   [0.05, 0.80, 0.55]]          # step     (x^6)
)

x_2 = inputs[1]
d_in = inputs.shape[1]
d_out = 2

#Initialize the weight matrix
w_query = torch.nn.Parameter(torch.rand(d_in, d_out), requires_grad=False)
w_key = torch.nn.Parameter(torch.rand(d_in, d_out), requires_grad=False)
w_value = torch.nn.Parameter(torch.rand(d_in, d_out), requires_grad=False)

print(f"Query weight matrix: {w_query}")
print(f"Key weight matrix: {w_key}")
print(f"Value weight matrix: {w_value}")

query_2 = x_2 @ w_query
key_2 = x_2 @ w_key
value_2 = x_2 @ w_value

print(f"Query for input 2: {query_2}")
print(f"Key for input 2: {key_2}")
print(f"Value for input 2: {value_2}")


