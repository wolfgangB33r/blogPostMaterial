import tensorflow as tf
from tensorflow import keras

import requests

# Custom TensorFlow Keras callback receiver that sends the logged metrics
# to a Dynatrace monitoring environment.
# Read more about writing your own callback receiver here:
# https://www.tensorflow.org/guide/keras/custom_callback
class DynatraceKerasCallback(keras.callbacks.Callback):
    metricprefix = ''
    modelname = ''
    url = ''
    apitoken = ''

    batch = ''

    # Constructor that takes a metric prefix, the name of the current model that is used, 
    # the Dynatrace metric ingest API endpoint (e.g.: https://your.live.dynatrace.com/api/v2/metrics/ingest)
    # and the Dynatrace API token (with metric ingest scope enabled)
    def __init__(self, metricprefix='tensorflow.', modelname='', url='', apitoken=''):
        self.metricprefix = metricprefix
        self.modelname = modelname
        self.url = url
        self.apitoken = apitoken

    def send_metric(self, name, value, tags):
      tags_str = ''
      for tag_key in tags:
        tags_str = tags_str + ',{key}={value}'.format(key=tag_key, value=tags[tag_key])
      line = '{prefix}.{name}{tags} {value}\n'.format(prefix=self.metricprefix, tags=tags_str, model=self.modelname, name=name, value=value)
      self.batch = self.batch + line

    def flush(self):
      print(self.batch)
      r = requests.post(self.url, headers={'Content-Type': 'text/plain', 'Authorization' : 'Api-Token ' + self.apitoken}, data=self.batch)
      self.batch = ''

    def on_train_end(self, logs=None):
        keys = list(logs.keys())
        for m in keys:
          self.send_metric(m, logs[m], { 'model' : self.modelname, 'stage' : 'train' })
        self.flush()

    def on_epoch_end(self, epoch, logs=None):
        keys = list(logs.keys())
        for m in keys:
          self.send_metric(m, logs[m], { 'model' : self.modelname, 'stage' : 'train' })
        self.flush()

    def on_test_end(self, logs=None):
        keys = list(logs.keys())
        for m in keys:
          self.send_metric(m, logs[m], { 'model' : self.modelname, 'stage' : 'test' })
        self.flush()

    def on_predict_end(self, logs=None):
        keys = list(logs.keys())
        for m in keys:
          self.send_metric(m, logs[m], { 'model' : self.modelname, 'stage' : 'predict' })
        self.flush()
