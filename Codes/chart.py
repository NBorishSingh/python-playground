import matplotlib.pyplot as plt

data = [0.1181487, 0.478338462, 0.740936292, 0.268400321, 0.29961619,
        0.510991897, 0.615811983, 0.769641636, 0.518611831, 0.980015585,
        0.649746521, 0.61747247, 0.849586809, 0.099743726, 0.844934572,
        0.412569259, 0.099277675, 0.453938393, 0.083287168, 0.213453331]

# Wrap in a list to treat it as one dataset in a stacked bar histogram
plt.hist([data], bins=10, histtype='barstacked', color='skyblue', edgecolor='black')

plt.title("Histogram with barstacked type")
plt.xlabel("Value Range")
plt.ylabel("Frequency")
plt.grid(True)

plt.show()
