# Data Science Exercises

## Introduction

Welcome to this test! This file should come with a zip archive (**test.zip**), in which you should find the following:

* A folder `connections`, with the files needed for the **Connections** exercise:
  - `histogram.py`
  - `histogram_example.png`
  - `peer.py`
  - `question2.py`
  - `question4.py`
  - `simulation.py`

* A folder `dataMining`, with the files needed for the **Data Mining** exercise:
  - `dstest.zip`

Contact us if any is missing.

During this test you will be asked to code in `python3`, make sure you have it installed on your machine.
**Please, also follow the privacy instructions that have been given to you in the email we sent you.**

## Exercise 1 : Connections

There are two types of question in this exercise :
- some in which you must fill some missing parts of code. The files you need to fill will be mentioned in the questions.
- some in which you must write an answer in English, which you will do directly under the question in the file `questions.md`.

You can import any external modules you deem relevant to answer the questions unless asked not to.

You can read and modify any parts of the code for debugging purpose (we strongly recommend that you create a "sandbox" file on the side where you can experiment and explore the mechanisms of the classes and functions present in this code base, or use the `main` part of `histogram.py`, `question2.py` and `question4.py`) but **don't change any logic where you are not asked to do so**. Your answers to the exercise will be run against the version of the code as you received it: adapting the classes to make your answers work will result in your answers not working once run against the original version of this code.

You will post to https://github.com/ under your account, the following files as an answer to this exercise even if you have not edited the files:
- `histogram.py`
- `question2.py`
- `question4.py`
- `questions.md`
You can also post any other custom relevant python file(s) of images(s) if you want to, but **don't post the files `peer.py`, `simulation.py`,`instructions.md` and `histogram_example.png`**.
**Please, also follow the privacy instructions that have been given to you in the email we sent you.**

Some context is given below with the assumptions you will make for the exercise, questions are in `questions.md`.

Have a nice exercise!

### Context

Let's imagine a network of peers. A peer is able to connect and disconnect to other peers according to rules that are out of the scope of this test. We can assume that the connection duration between two peers is random. Say such a network is initialized at time `t=0`. Peers connect and disconnect randomly and at time `t=delta_t`, we take a snapshot of the network. For instance this one:

```
    +---+          600s          +---+
    | 1 +------------------------+ 2 |
    +-+-+                        +-+-+
      | |                          |
      | |                          |
      | |                          | 459s
      | |                          |
1200s | |        34s         +---+ |
      | +--------------------+ 4 +-+
      |                      +---+
      |     +---+
      +-----+ 3 |
            +---+
```

There are 4 peers in this network:
- peer 1 is connected to peer 1, 2, and 4
- peer 2 is connected to peer 1 and 4
- peer 3 is connected to peer 1
- peer 4 is connected to peer 1 and 2

At the moment we took the snapshot:
- peer 1 had been connected to peer 2 for 600s
- peer 1 had been connected to peer 4 for 34s
...

We would like to build a nice **visualization of the distribution of the connection durations** of any given peer network. In particular we would like to plot a **histogram** of the connection durations between peers. For the above network, the result would look like this:

```
   connection count
   ^
   |
   |
2  |               +---------------+
   |               |               |
   |               |               |
   |               |               |
   |               |               |
1  +---------------+               |               +---------------+
   |               |               |               |               |
   |               |               |               |               |
   |               |               |               |               |
   |               |               |               |               |
   |               |               |               |               |
0  +---------------+---------------+---------------+---------------+---> connection duration (s)

   0               400             800            1200
```

Let's assume that:
- peers know to which peers they are connected to at the moment of the snapshot, and they also know the connection durations between them and the peers they are connected to.
- we have a server to which the peers can send any type of data at the moment we take the snapshot of the network. We will refer to this server as the _backend_. The _backend_ server is able to store the data it receives from the peers and do any kind of processing on the data in order to plot a histogram.

The python files that come with this file represent the situation described above:
- the file `histogram.py` which has two functions, `compute_histogram_bins` that computes a histogram bins count given a list of numbers and a list of bins thresholds and `plot_histogram` that plots the histogram given the result of the first function. This corresponds to the operations the _backend_ server will carry on once data is retrieved from peers.
- the file `peer.py` has a class `Peer` that describes a peer: a peer has an `id` and a `peer_pool` i.e. the group of peers it is connected to. For each peer, you can `add_peers_to_peer_pool`; when adding a new peer to its peer pool, a random connection duration associated with this connection is generated. When taking a snapshot of the network, a peer will send data to our _backend_ server with `send_data_to_backend`.
- the file `simulation.py` has a class `Simulation` whose purpose is to create a peer network simulation. It takes the number of peers you want in the network (`number_of_peers`) and the maximum number of peers there can be in a peer pool (`max_peer_pool_size`). When calling `Simulation`'s `run`:
    - we generate a network with `number_of_peers` peers,
    - we connect them randomly to at most `max_peer_pool_size` peers, with random connection durations,
    - we call `send_data_to_backend` on each peer and keep it in `Simulation`'s `backend_database` attribute, our _backend_ server database, which is merely a list.
    - we finally call `process_backend_data` which represents the operations done on our _backend_ server in order to plot the histogram.

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
>> _answer here_

#### Question 4

Go to the file `question4.py`:
Propose new implementations of `send_data_to_backend` and `process_backend_data` that can deal with millions of peers _and_ still provide a good representation of the _distribution_ of the connection duration. You are free to add any written comments, add pictures etc. to enhance your answer.
>> _answer here_

## Exercise 2 : Data Mining

### Instructions

The questions in this exercise can be answered separately, meaning they are independent from each other, apart from the Question 1, in which you define a performance measure that is used in some other questions.

You will write your answers to the questions below in a [Jupyter notebook](https://jupyter.org/). For each question, please provide the appropriate explanations in _English_, the `python3` code you wrote to answer the question and finally any graphical representation.

You will post the notebook to https://github.com/ under your account.
**Please, also follow the privacy instructions that have been given to you in the email we sent you.**

### Context

We develop a technology that allows a viewer watching a video online to download the video data either from the broadcaster's Content Delivery Network ('CDN') or from a Peer to Peer Network, using other viewers on the same stream as sources.

During their session, each viewer sends payloads **every two minutes**, containing some metrics collected by our P2P client. The dataset attached to this file (**dstest.zip**) is a sample of those payloads. Each row is a payload sent by a viewer, and has the following columns:

* **company** : The name of the company providing the stream being watched by the user that sent the payload
* **live** : A string indicating if the video being watched is a live stream or a VOD stream
* **content** : The name of the content being watched by the viewer sending the payload
* **p2p** : The volume of data (in bytes) **downloaded through the P2P network** from other viewers during the payload timespan (2 minutes)
* **cdn** : The volume of data (in bytes) **downloaded the CDN** during the payload timespan (2 minutes)
* **upload** : The volume of data (in bytes) **uploaded to other viewers** on the P2P network during the payload timespan (2 minutes)
* **peers_count** : Average number of peers connected to the users during the payload timespan
* **timestamp** : Unix timestamp (UTC) of the moment the payload was sent
* **sessionDuration** : **Total time** elapsed since the beginning of the video session (in milliseconds)
* **playbackErrorCount** : Number of playback errors that occurred during the payload timespan
* **totalPlaybackErrorCount** : Number of playback errors that have occurred since the beginning of the viewer's session

### Questions

#### Question 1

Knowing the goal of the our technology, define a metric to measure our performance. Calculate that performance score for each of the companies in the dataset.

#### Question 2

##### 2.1
How can we know whether a payload is the first payload of a viewer's session?

##### 2.2
Add a column `isFirstPayload` to the dataset, that must be `True` if the row represents a payload that was **the first payload** sent by a viewer, and `False` otherwise.

##### 2.3
Use that column to calculate the **number of distinct viewers** that sent payloads for each company.

#### Question 3

##### 3.1
Let's consider a viewer A who starts a video at T=0, then has a playback error at **T = 2 minutes 30 seconds**, and then another one at **T=6 minutes 20 seconds**. What will be the values of the fields `playbackErrorCount` and `totalPlaybackErrorCount` in the first 5 payloads sent by viewer A?

##### 3.2
Calculate the **number of distinct viewers** that had **at least 1** playback error during their session.

#### Question 4

In this question, we only focus on customer **Streamr\*\*\*\* TV**.

We define the _concurrency_ as the number of viewers connected simustaneously on the **same content**, i.e the number of payloads we received during a given 2 minutes window on a given content.

##### 4.1
Add a column "readableDate" to the dataset that will be the beginning of the 2 minutes window during which the payload was sent. For example, if a payload was sent at 11:35, the column "readableDate" should be 11:33.

##### 4.2
Plot the concurrency time series for the content `content-05335`.

##### 4.3
What is the average performance measured when the concurrency is lower than 10?

##### 4.4
Starting from which concurrency can we say there is a 75% chance that the performance on a content is higher than 80%?
