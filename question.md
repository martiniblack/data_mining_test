
## Exercise 1 : Connections


### Questions

#### Question 1

Fill in the two functions `compute_histogram_bins` and `plot_histogram` in `histogram.py`. As an example, we would like to be able to plot something similar to `histogram_example.png` as a minimum result.

#### Question 2

Go to the file `question2.py`:
1. fill in `send_data_to_backend` so that it returns an _array_ of the peer's connection durations.
2. fill in `process_backend_data` which must do all necessary processing to return the connection durations histogram bins counts. **Don't call `plot_histogram` in this method, we just want to compute the histogram bins counts**.

#### Question 3

With peers sending such datastructure and our _backend_ server making such operations, we retrieve exactly **all** the connection durations on the network at the moment of the snapshot and we are able to plot the _exact distribution_ of the connection durations.
`question2.py` main has several simulations with increasing numbers of peers and peer pool size. Run the simulations with your implementation. What do you see? Can you explain the limitations of the implementations of question 2 taking into account that a _real_ peer network can have _millions_ of peers? (answer below in this file)
>> With the increasing of the numbers of perrs and peer pool size, the backen processing time also increases significantly (eg. 2.17s for 10 000 number of peers and pool size of 100, which is too long. the limitation of the implementation is that the backend database contain a very large list that need to be counted by `the compute_histogram_bins` method. This is not a optimal way.

#### Question 4

Go to the file `question4.py`: 
Propose new implementations of `send_data_to_backend` and `process_backend_data` that can deal with millions of peers _and_ still provide a good representation of the _distribution_ of the connection duration. You are free to add any written comments, add pictures etc. to enhance your answer.
>> Following the analysis above, we can perform each time the `the compute_histogram_bins` method with a small list before and send the result to the backend database instead of the raw data. And for the process step, we can just take a sum of the result for each list, which is very fast to run. Throughout the simulation, it takes 0.00979s to run the 10 000 number of peers and pool size of 100. even with 100 000 peers and 100 pool size, it takes 0.1366s, this is a more optimal way.


