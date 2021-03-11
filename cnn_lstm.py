import pandas as pd
import tensorflow as tf
import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt

mpl.rcParams['figure.figsize'] = (8, 6)
mpl.rcParams['axes.grid'] = False

# use_col_list = ['DATE', 'GENERAL_DAM_OCCUPANCY_RATE', 'DateTime', 'Rain', 'MaxTemp', 'MinTemp', 'AvgWind', 'AvgHumidity', 'AvgPressure']
use_col_list = ['GENERAL_DAM_OCCUPANCY_RATE', 'Rain', 'MaxTemp', 'MinTemp', 'AvgWind', 'AvgHumidity', 'AvgPressure']
df = pd.read_csv("dam_istanbul_weather.csv", usecols=use_col_list)

# print(df['GENERAL_DAM_OCCUPANCY_RATE'].mean())
# print(df['GENERAL_DAM_OCCUPANCY_RATE'].std())

column_indices = {name: i for i, name in enumerate(df.columns)}

n = len(df)
train_df = df[0:int(n*0.7)]
val_df = df[int(n*0.7):int(n*0.9)]
test_df = df[int(n*0.9):]

train_min = train_df.min()
train_max = train_df.max()

# Min-Max Scale
train_df = (train_df - train_min) / (train_max - train_min)
val_df = (val_df - train_min) / (train_max - train_min)
test_df = (test_df - train_min) / (train_max - train_min)

model_name = 'LSTM' # 'LSTM' or 'CNN'
model_ckpt_name = model_name + '_ckpt.h5'
model_saved_name = model_name + '_model.h5'

MAX_EPOCHS = 1000
PATIENCE = 200


def windowed_dataset(dataFrame, window_size, batch_size, shuffle_buffer):
  
  dataset = tf.data.Dataset.from_tensor_slices(dataFrame.values)
  dataset = dataset.window(window_size + 1, shift=1, drop_remainder=True)
  dataset = dataset.flat_map(lambda window: window.batch(window_size + 1))
  dataset = dataset.shuffle(shuffle_buffer).map(lambda window: (window[1:], window[0]))
  dataset = dataset.batch(batch_size).prefetch(1)
  
  return dataset

train_dataset = windowed_dataset(train_df, 7, 64, 1000)
val_dataset = windowed_dataset(val_df, 7, 64, 1000)
test_dataset = windowed_dataset(test_df, 7, 64, 1000)

def plot(self, model=None, plot_col='GENERAL_DAM_OCCUPANCY_RATE', max_subplots=3):
  inputs, labels = self.example
  plt.figure(figsize=(12, 8))
  plot_col_index = self.column_indices[plot_col]
  max_n = min(max_subplots, len(inputs))
  for n in range(max_n):
    plt.subplot(3, 1, n+1)
    plt.ylabel(f'{plot_col} [normed]')
    plt.plot(self.input_indices, inputs[n, :, plot_col_index],
             label='Inputs', marker='.', zorder=-10)

    if self.label_columns:
      label_col_index = self.label_columns_indices.get(plot_col, None)
    else:
      label_col_index = plot_col_index

    if label_col_index is None:
      continue

    plt.scatter(self.label_indices, labels[n, :, label_col_index],
                edgecolors='k', label='Labels', c='#2ca02c', s=64)
    if model is not None:
      predictions = model(inputs)
      plt.scatter(self.label_indices, predictions[n, :, label_col_index],
                  marker='X', edgecolors='k', label='Predictions',
                  c='#ff7f0e', s=64)

    if n == 0:
      plt.legend()

  plt.xlabel('Time [h]')


def compile_and_fit(model, train_dataset, val_dataset, patience=PATIENCE):
  early_stopping = tf.keras.callbacks.EarlyStopping(monitor='val_loss',
                                                    patience=patience,
                                                    mode='min')

  model.compile(loss=tf.losses.MeanSquaredError(),
                optimizer=tf.optimizers.Adam(),
                metrics=[tf.metrics.MeanAbsoluteError()])

  checkpoint_filepath = model_ckpt_name
  model_checkpoint_callback = tf.keras.callbacks.ModelCheckpoint(
      filepath=checkpoint_filepath,
      save_weights_only=True,
      monitor='val_loss',
      mode='min',
      save_best_only=True)

# Model weights are saved at the end of every epoch, if it's the best seen
# so far.

  history = model.fit(train_dataset, epochs=MAX_EPOCHS,
                      validation_data=val_dataset,
                      callbacks=[early_stopping, model_checkpoint_callback])
  return history


multi_val_performance = {}
multi_performance = {}

if model_name == 'LSTM':
  model = tf.keras.models.Sequential([
  tf.keras.layers.Conv1D(filters=60, kernel_size=5,
  strides=1, padding="causal",
  activation="relu",
  input_shape=[None, 7]),
  tf.keras.layers.LSTM(60, return_sequences=True),
  tf.keras.layers.LSTM(60, return_sequences=True),
  tf.keras.layers.Dense(30, activation="relu"),
  tf.keras.layers.Dense(10, activation="relu"),
  tf.keras.layers.Dense(1),
  ])
elif model_name == 'CNN':
  model = tf.keras.models.Sequential([
  tf.keras.layers.Conv1D(filters=60, kernel_size=5,
  strides=1, padding="causal",
  activation="relu",
  input_shape=[None, 7]),
  tf.keras.layers.Conv1D(256, kernel_size=5, strides=1, padding="causal",activation="relu",),
  tf.keras.layers.Conv1D(128, kernel_size=5, strides=1, padding="causal",activation="relu",),
  tf.keras.layers.Conv1D(64, kernel_size=5, strides=1, padding="causal",activation="relu",),
  tf.keras.layers.Dense(30, activation="relu"),
  tf.keras.layers.Dense(10, activation="relu"),
  tf.keras.layers.Dense(1),
  ])

history = compile_and_fit(model, train_dataset, val_dataset)


multi_val_performance[model_name] = model.evaluate(val_dataset)
multi_performance[model_name] = model.evaluate(test_dataset, verbose=0)

model.load_weights(model_ckpt_name)

model.save(model_saved_name, save_format='h5')