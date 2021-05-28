"""
    The idea to improve the backend processing time is to call the compute_histogram_bins method before
    in the send_data_to_backend, and send directly the bin counts array to backend_database. And then we
    can just calculate the sum of all tha bin counts array to have the global distribution.
"""
import random
import numpy as np

from peer import Peer
from simulation import Simulation, BINS
from histogram import compute_histogram_bins, plot_histogram

class PeerQ4(Peer):

    def send_data_to_backend(self):
        """
            Question 4:
            receive the peer's connection durations and calculate the bin counts then return the bin counts array
        """
        _, bin_counts = compute_histogram_bins(list(self.peer_pool.values()), BINS)
        return bin_counts

class SimulationQ4(Simulation):

    def generate_network(self):
        self.network = [PeerQ4() for _ in range(self.number_of_peers)]

    def process_backend_data(self):
        """
            Question 4:
            sum up the bin counts array, here we use the numpy library to facilitate the calculation for 2D dimension
            array
        """
        bin_counts_array = np.array(self.backend_database)
        bin_counts_remove_duplicate = list(np.sum(bin_counts_array, axis=0)//2)
        #print(bin_counts_remove_duplicate)
        return bin_counts_remove_duplicate


if __name__ == "__main__":

    s = SimulationQ4(number_of_peers=10, max_peer_pool_size=2)
    s.run()
    s.report_result()

    s = SimulationQ4(number_of_peers=1000, max_peer_pool_size=10)
    s.run()
    s.report_result()

    s = SimulationQ4(number_of_peers=1000, max_peer_pool_size=100)
    s.run()
    s.report_result()

    s = SimulationQ4(number_of_peers=1000, max_peer_pool_size=1000)
    s.run()
    s.report_result()

    s = SimulationQ4(number_of_peers=10000, max_peer_pool_size=10)
    s.run()
    s.report_result()

    s = SimulationQ4(number_of_peers=10000, max_peer_pool_size=100)
    s.run()
    s.report_result()
