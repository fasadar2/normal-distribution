import matplotlib.pyplot as plt


def print_function(x, f, x_name="x", y_name="y", title="График"):
	plt.title(title)
	plt.plot(x, f)
	plt.xlabel(x_name)
	plt.ylabel(y_name)
	plt.show()
