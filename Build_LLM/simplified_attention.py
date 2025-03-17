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

Query = inputs[1]
print(f"query selected as input 2={Query}")

Attn_scores_2 = torch.empty(inputs.shape[0])
print(f"Attention_scores_2={Attn_scores_2}")

for i, x_i in enumerate(inputs):
    print(f"i={i} and x_i={x_i} and query={Query}")
    Attn_scores_2[i] = torch.dot(x_i, Query)

print(f"Attention_scores_2={Attn_scores_2}") # Attention scores for input 2 (inputs[1])

#normalization attention weights that sum up to 1
attn_weights_2_tmp = Attn_scores_2/Attn_scores_2.sum()
print(f"attn_weights_2_tmp={attn_weights_2_tmp}")

#using the softmax function to normalize the attention weights
attn_weights_2_naive = softmax_naive(Attn_scores_2)
print(f"Normalized scores using softmax function {attn_weights_2_naive}")

#using pytroch's built-in softmax function
attn_weights_2 = torch.softmax(Attn_scores_2, dim=0)
print(f"Normalized scores using pytorch's softmax function {attn_weights_2}")
print(f"Sum: {attn_weights_2.sum()}")


# calculate the context vector z is the weighted sum of all input vectors, obtained by multipying each input vector by its corresponding attention weight and summing the results
print(inputs)
query = inputs[1]
print(f"query selected as input 2={query}")
context_vec_2= torch.zeros(query.shape[0])

for i, x_i in enumerate(inputs):
    print(f"i={i} and x_i={x_i} and query={query}")
    context_vec_2 += attn_weights_2[i] * x_i
print(f"Context vector for input 2: {context_vec_2}")

## attention scores of all queries(each input is a query at some point) and all inputsm, so total size would be inpus size by input size
attn_scores = torch.empty(6,6)
for i, x_i in enumerate(inputs):
    for j,x_j in enumerate(inputs):
        attn_scores[i,j] = torch.dot(x_i, x_j)
print(f"Attention scores for all inputs: {attn_scores}")

#5. Why is dim=-1 Used?
#Generalization – It automatically refers to the last axis, regardless of how many dimensions the matrix/tensor has.
#Avoids Hardcoding – If we had a 3D or 4D tensor, dim=-1 would still correctly apply across the last axis.
#Consistent Behavior – In deep learning (e.g., attention mechanisms), applying softmax along dim=-1 ensures each row normalizes independently, which is what we want when working with probability distributions.
attn_weights = torch.softmax(attn_scores, dim=-1) # dim -1
print(f"Attention weights for all inputs: {attn_weights}")

all_context_vecs = attn_weights @ inputs # matrix multiplication similar to context_vec_2
print(f"Context vectors for all inputs: {all_context_vecs}")

