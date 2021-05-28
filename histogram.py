from random import randint
import matplotlib.pyplot as plt


def compute_histogram_bins(data=[], bins=[]):
    """
        Question 1:
        Given:
            - data, a list of numbers you want to plot a histogram from,
            - bins, a list of sorted numbers that represents your histogram
              bin thresdholds,
        return a data structure that can be used as input for plot_histogram
        to plot a histogram of data with buckets bins.
        You are not allowed to use external libraries other than those already
        imported.
    """
    bin_ranges = []
    range_tuple = zip(bins[:-1], bins[1:])
    for bin_left_range, bin_right_range in range_tuple:
        bin_ranges.append(str(bin_left_range) + "-" + str(bin_right_range))
    bin_ranges.append(str(bins[-1])+"-+")

    count_bins = [0 for bin in bins]
    for x in data:
        bin_number = 0
        for y in bins:
            if x >= y:
                bin_number = bins.index(y)
        count_bins[bin_number] += 1

    return bin_ranges, count_bins


def plot_histogram(bins_count):
    """
        Question 1:
        Implement this function that plots a histogram from the data
        structure you returned from compute_histogram_bins. We recommend using
        matplotlib.pyplot but you are free to use whatever package you prefer.
        You are also free to provide any graphical representation enhancements
        to your output.
    """
    plt.bar(x=bins_count[0], height=bins_count[1])
    plt.title("Distribution of Something")
    plt.xlabel("some metric bins")
    plt.ylabel("count")
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    # EXAMPLE:

    # inputs
    data = [randint(0, 100) for x in range(200)]
    bins = [0, 10, 20, 30, 40, 70, 100]
    print(data)

    # compute the bins count
    histogram_bins = compute_histogram_bins(data=data, bins=bins)
    print(histogram_bins)

    # plot the histogram given the bins count above
    plot_histogram(histogram_bins)
