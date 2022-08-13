import os
import tempfile

import numpy as np
import tensorflow as tf

loaded_model = tf.saved_model.load('one_step/')


states = None
next_char = tf.constant([str(input("what should i write about: "))])
result = [next_char]

for n in range(1000):
  next_char, states = loaded_model.generate_one_step(next_char, states=states)
  result.append(next_char)

x = tf.strings.join(result)[0].numpy().decode("utf-8")
print(x)


