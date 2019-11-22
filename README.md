# PyB8ZS


<b>Scrambling</b> is a technique that does not increase the number of bits and does provide synchronization. Problem with technique like Bipolar AMI(Alternate Mark Inversion) is that continuous sequence of zero’s create synchronization problems one solution to this is Scrambling.

<b>B8ZS(Bipolar with 8-zero substitution) –</b>
This technique is similar to Bipolar AMI except when eight consecutive zero-level voltages are encountered they are replaced by the sequence,”000VB0VB”.

- V(Violation), is a non-zero voltage which means signal have same polarity as the previous non-zero voltage. Thus it is violation of general AMI technique.

- B(Bipolar), also non-zero voltage level which is in accordance with the AMI rule (i.e.,opposite polarity from the previous non-zero voltage).

## How to Run
```bash
$  python main.py
Enter the 10 bit data stream: 10000000001
Enter the last symbol (1 for +ve pulse and -1 for -ve pulse): 1
  ```

## Output Plot

This should be the Output

![Plot](https://github.com/PotatoSpudowski/PyB8ZS/blob/master/Images/sample_plot.png)
