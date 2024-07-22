## Reservoir
$h_t = (1 - lr) \times h_{t-1} + lr \times tanh(W^{in} x_t + W^{res} h_{t-1})$ 
## Readout
$\tilde{h}_t = PCA(h_t) \space \rightarrow \space y_t = W^{out}\tilde{h}_t + b$
