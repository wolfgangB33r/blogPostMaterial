# Example Keras model training with TensorFlow and evaluation use along with a Dynatrace TensorFlow 
# callback receiver for AI Observability.
import tensorflow as tf
print("TensorFlow version:", tf.__version__)

import time

# load the Dynatrace callback receiver
from dynatrace import DynatraceKerasCallback

# load a sample data set
mnist = tf.keras.datasets.mnist

(x_train, y_train), (x_test, y_test) = mnist.load_data()
x_train, x_test = x_train / 255.0, x_test / 255.0

# define a model
model = tf.keras.models.Sequential([
  tf.keras.layers.Flatten(input_shape=(28, 28)),
  tf.keras.layers.Dense(128, activation='relu'),
  tf.keras.layers.Dropout(0.2),
  tf.keras.layers.Dense(10)
])

# define a loss function
loss_fn = tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True)

# compile the model
model.compile(optimizer='adam',
              loss=loss_fn,
              metrics=['accuracy'])

# define the tensor board callbacks
dt_callback = DynatraceKerasCallback(metricprefix='tensorflow', modelname='mnist-classifier', url='https://<YOUR_ENV>.live.dynatrace.com/api/v2/metrics/ingest', apitoken='<YOUR_TOKEN>') 

# train the model
model.fit(x_train, y_train, epochs=5, callbacks=[dt_callback])

# use the model in production
while True:
    model.evaluate(x_test,  y_test, verbose=2, callbacks=[dt_callback])
    time.sleep(60)
    