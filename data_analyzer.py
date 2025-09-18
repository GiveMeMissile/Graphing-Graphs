import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import os
import math

class DataAnalyzer:
    # A class which is used to graph and collect data from csv files.

    def __init__(self, folders=None):
        if not folders is None:
            self.folder = ["RL_LSTM_Progress_Data"]

    def get_csv_data(self, filename):
        # This reads a csv file and appends the data to the dictionary.

        for folder in self.folder:
            if not os.path.isfile(folder + "/" + filename):
                print("File does not exist.")
                return
        
        df = pd.read_csv(self.folder + "/" + filename)
        csv_data = df.to_dict(orient="list")
        for key in self.data.keys():
            if key in csv_data:
                self.data[key] = csv_data[key]
            else:
                print(f"Key {key} not found in CSV file.")

        return self.data

    def append(self, item, location):
        try:
            self.data[location].append(item)
        except Exception:
            print("Invalid location, please input a valid location.")
    
    def __len__(self):
        return len(self.data["Episodes"])
    
    def calculate_sd(self, data, mean):
        # Calculate the Standard Deviation of the Data: sd^2 = (∑((value - mean)^2))/total

        sd = 0

        for value in data:
            sd += (value - mean)**2
        
        sd /= len(data)
        sd = math.sqrt(sd)
        return sd

    def calculate_mean(self, data):
        return sum(data)/len(data)
    
    def calculate_range(self, data):
        return max(data) - min(data)
    
    def calculate_mad(self, data, mean):
        # Calculate the Mean Absolute Diviation of the Data: mad = (∑|value - mean|)/total

        mad = 0

        for value in data:
            mad += abs(value - mean)
        
        mad /= len(data)
        return mad
    
    def calculate_median(self, data):
        # Calculate the median of the data

        sorted_data = sorted(data)
        length = len(data)

        if length % 2 == 0:
            median = (sorted_data[length//2 - 1] + sorted_data[length//2]) / 2
        else:
            median = sorted_data[length//2]
        
        return median

    def calculate_z_scores(self, data, mean, sd):
        # Calculate the z_scores of the data, equation: z_score = (value - mean_of_data)/standard deviation

        z_scores = []
        for value in data:
            try:
                z_score = (value-mean)/sd
            except ZeroDivisionError:
                z_score = 0
            z_scores.append(z_score)

        return z_scores
    
    def calculate_lsrl(self, x, y):
        # Calculates the lsrl of the data, which is the linear best fit line for the data.
        # The equation is ŷ = mx + b, where ŷ is the predicted y value, m is the slope, and b is the y-int.
        # m = r(sdy/sdx) where r = (1/total)∑(((x_mean - x)/sdx)*(y_mean - y)/sdy))
        # b = y_mean - m*x_mean

        y_mean = self.calculate_mean(y)
        x_mean = self.calculate_mean(x)
        sdy = self.calculate_sd(y, y_mean)
        sdx = self.calculate_sd(x, x_mean)
        total_sum = sum([((yi - y_mean)/sdy)*((xi - x_mean)/sdx) for xi, yi in zip(x, y)])
        r = (1/len(x)) * total_sum
        m = r * (sdy/sdx)
        b = y_mean - m*x_mean
        print(f"y_mean: {y_mean}, x_mean: {x_mean}, sdy: {sdy}, sdx: {sdx}, sum: {total_sum}, r: {r}, m: {m}, b: {b}")
        return m, b, r
    
    def graph_scatter(self, x, y, x_name, y_name):
        # Takes in a list of data from two different variables and graphs all of the data vs the episodes

        plt.figure(figsize=(10, 6))
        plt.scatter(x, y, label = f"{y_name} vs {x_name}")
        
        plt.xlabel(x_name)
        plt.ylabel(y_name)
        plt.title(f"{x_name} vs {y_name} Scatter Plot")
        plt.legend()
        plt.grid(True)
        plt.show()

    def graph_lsrl(self, x, y, x_name, y_name, scatter=False):
        # Takes in two lists, x and y, and calculates and graphs the lsrl for the graph.

        if len(x) != len(y):
            print(f"List size Error: y_list: {len(x)}, x_list = {len(y)}. Please input correct list sizes")
            return

        m, b, r = self.calculate_lsrl(x, y)
        pred_y = [m*xi + b for xi in x]
        if scatter:
            plt.scatter(x, y, color='blue', label="Original Values")
        plt.plot(x, pred_y, color='red', label=f"LSRL: y = {m:.2f}x + {b:.2f}, r = {r:.2f}")
        plt.xlabel(x_name)
        plt.ylabel(y_name)
        plt.title(f"{x_name} vs {y_name} with LSRL")
        plt.legend()
        plt.grid(True)
        plt.show()

    def graph(self, x, data, names, x_name):
        # Takes in a list of data from different variables and graphs all of the data vs the episodes

        if type(data) != list:
            data = np.array([data])
        if type(names) != list:
            names = [names]
        
        print(len(data))

        plt.figure(figsize=(10, 6))
        for name, values in zip(names, data):
            values = np.array(values)
            plt.plot(x, values, label = name)
        
        plt.xlabel(x_name)
        plt.ylabel("Value")
        plt.title(f"{x_name} vs {", ".join([label for label in names])} Graph")
        plt.legend()
        plt.grid(True)
        plt.show()
    
    def graph_box_plot(self, data, name):
        # Takes in a list of data from a single variable and graphs all of the data vs the episodes

        fig, ax = plt.subplots()
        data = np.array(data).reshape(-1, 1)
        bp = ax.boxplot(data)

        ax.set_xticklabels([name])
        plt.ylabel("Value")
        plt.title(f"{name} Box Plot")

        plt.show()

    def graph_histogram(self, data, name, bins=10):
        # Takes in a list of data from a single variable and graphs all of the data vs the episodes

        data = np.array(data)
        plt.hist(data, bins=bins, label=[name])
        plt.legend()
        plt.title(f"{name} Histogram")
        plt.show()

    def get_info(self, data):
        mean = self.calculate_mean(data)
        sd = self.calculate_sd(data, mean)
        z_scores = self.calculate_z_scores(data, mean, sd)
        return mean, sd, z_scores
