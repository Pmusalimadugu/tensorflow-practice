
import tensorflow as tf


def main():
    # tf.ones() creates a shape [1,2,3] tensor full of ones
    tensor1 = tf.ones([1, 2, 3])
    # reshape existing data to shape [2,3,1]
    tensor2 = tf.reshape(tensor1, [2, 3, 1])
    # -1 tells the tensor to calculate the size of the dimension in that place
    tensor3 = tf.reshape(tensor2, [3, -1])
    # this will reshape the tensor to [3,3]
    print(tensor1)
    # The numer of elements in the reshaped tensor MUST match the number in the original


if __name__ == "__main__":
    main()
