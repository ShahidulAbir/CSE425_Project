import os
import pandas as pd
from matplotlib import pyplot as plt

mapping_dictionary = {
    "cpuUtilization": "CPU Utilization",
    "peakMemoryUsage": "Peak Memory Usage",
    "runtimes": "Runtimes",

    "ConvexHull": "Convex Hull Algorithm",
    "PrimsAlgorithm": "Prim's Algorithm",
    "CoinChange": "Coin Change Algorithm",
    "FloydWarshall": "Floyd Warshall Algorithm",

    "Python": "red",
    "Java": "blue",
    "C": "green",
    "CPP": "purple",
}

for algorithm in os.listdir("./algorithms"):
    for resource in os.listdir(f"./algorithms/{algorithm}"):
        df_csvs = []
        for csv_file in os.listdir(f"./algorithms/{algorithm}/{resource}"):
            filename = os.path.splitext(csv_file)[0]
            print(filename)

            df_csvs.append([pd.read_csv(f"algorithms/{algorithm}/{resource}/{csv_file}"), filename])

        cpp_filename_parts = df_csvs[0][1].split("_")
        c_filename_parts = df_csvs[1][1].split("_")
        java_filename_parts = df_csvs[2][1].split("_")
        python_filename_parts = df_csvs[3][1].split("_")

        plt.figure(figsize=(10, 5))
        plt.xlabel("Number of Datapoints")
        plt.ylabel(mapping_dictionary[java_filename_parts[1]])
        plt.title(f"Implementation of {mapping_dictionary[java_filename_parts[2]]}\n{mapping_dictionary[java_filename_parts[1]]} vs Number of Datapoints")
        plt.plot(list(range(1, len(df_csvs[0][0].index) + 1)), df_csvs[0][0], color=f"{mapping_dictionary['CPP']}", label="CPP")
        plt.plot(list(range(1, len(df_csvs[1][0].index) + 1)), df_csvs[1][0], color=f"{mapping_dictionary['C']}", label="C")
        plt.plot(list(range(1, len(df_csvs[2][0].index) + 1)), df_csvs[2][0], color=f"{mapping_dictionary['Java']}", label="Java")
        plt.plot(list(range(1, len(df_csvs[3][0].index) + 1)), df_csvs[3][0], color=f"{mapping_dictionary['Python']}", label="Python")
        plt.legend()
        plt.grid()
        plt.savefig(f"graphs/{algorithm}/{resource}/{java_filename_parts[1]}_{java_filename_parts[2]}.jpg")
        plt.show()
