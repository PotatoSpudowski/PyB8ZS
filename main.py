import numpy as np
import matplotlib.pyplot as plt
import utils

inputStream = str(input("Enter the 10 bit data stream: "))
lastSymbol = int(input("Enter the last symbol (1 for +ve pulse and -1 for -ve pulse): "))

BipolarAMI = utils.ToBipolarAmi(inputStream, lastSymbol)

b8zsScrambled = utils.B8ZS_Scrambler(BipolarAMI, lastSymbol)

inputStream = list(inputStream)
inputStream = [int(i) for i in inputStream]

fig, axs = plt.subplots(3)

fig.suptitle('B8ZS scrambling technique for 10 bit data stream')
axs[0].plot(inputStream, drawstyle='steps-pre')
axs[0].set_title("Input data stream")
axs[1].plot(BipolarAMI, drawstyle='steps-pre')
axs[1].set_title("Bipolar AMI plot")
axs[2].plot(b8zsScrambled, drawstyle='steps-pre')
axs[2].set_title("B8ZS scrambled plot")

for ax in axs.flat:
    ax.label_outer()
    
plt.show()