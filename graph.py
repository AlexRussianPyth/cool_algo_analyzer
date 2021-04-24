import matplotlib.pyplot as plt

# class ProgramGui:



class Graph:

    def __init__(self, DataClass):
        self.func_data = DataClass.func_array
        self.labels = ["Constant '1'", "Linear 'n'", "Quadratic 'n**2'", "Qubic 'n**3'", "Exponential '2**n'", "Factorial 'n!'"]

        # Construct graph
        plt.figure(figsize=(8,6))
        plt.style.use("dark_background")


        for i in range(len(self.func_data)):
            plt.plot(DataClass.x_axis, self.func_data[i], label=self.labels[i])

        # Graph Exterior
        
        plt.title("Big O Graph")
        # plt.yscale("log")
        plt.ylim(0, DataClass.range[1]**2)
        plt.xlabel("N's")
        plt.ylabel("Operations")
        plt.tick_params(axis='x', colors='black')
        plt.tick_params(axis='y', colors='black')

        plt.legend()

        plt.show()
