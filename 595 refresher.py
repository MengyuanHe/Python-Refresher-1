
import numpy as np
import matplotlib.pyplot as plt

def plotsc():
    x=np.linspace(-np.pi,np.pi,1024)
    s=np.sin(x)
    c=np.cos(x)
    plt.plot(x,s)
    plt.plot(x,c)
    plt.plot(np.linspace(0, 0.5 * np.pi),
             np.tan(np.linspace(0, 0.5 * np.pi)),
             label='Tangent',
             color='red')  # Added by Mengyuan He

    plt.plot(np.linspace(0.5 * np.pi + 1e-10, 1.5 * np.pi),
             np.tan(np.linspace(0.5 * np.pi + 1e-10, 1.5 * np.pi)),
             color='red')  # Added by Mengyuan He

    plt.plot(np.linspace(1.5 * np.pi + 1e-10, 2 * np.pi),
             np.tan(np.linspace(1.5 * np.pi + 1e-10, 2 * np.pi)),
             color='red')  # Added by Mengyuan He

    plt.axhline(y=0.0, color='black')  # Added by Mengyuan He

    plt.ylim(-1.00, 1.00)  # The original scale is from -1.0 to 1.0, # Added by Mengyuan He
    plt.xlabel('x - axis')
    plt.ylabel('y-axis')
    plt.title('My lines')
    plt.legend()

    plt.show()

if __name__ == "__main__":
    plotsc()

