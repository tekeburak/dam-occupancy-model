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
train_df = df[0:int(n*0.85)]
val_df = df[int(n*0.85):int(n*0.95)]
test_df = df[int(n*0.95):]

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


# def windowed_dataset(dataFrame, window_size, batch_size):
  
#   dataset = tf.data.Dataset.from_tensor_slices(dataFrame.values)
#   dataset = dataset.window(window_size + 1, shift=window_size, drop_remainder=True)
#   dataset = dataset.flat_map(lambda window: window.batch(window_size + 1))
#   dataset = dataset.map(lambda window: (window[1::], window[0]))
#   dataset = dataset.batch(batch_size).prefetch(1)
  
#   return dataset

# def parse_samples(x):
#     return tf.data.Dataset.from_tensor_slices(x)\
#         .window(size=30, shift=1, drop_remainder=True)\
#         .flat_map(lambda window: window.batch(30))\
#         .map(lambda window: (window[1::], window[0]))

train_np = train_df.to_numpy()
val_np = val_df.to_numpy()
test_np = test_df.to_numpy()

train_np = np.concatenate((train_np[:, 1::], train_np[:, 0, None]), axis=1)
val_np = np.concatenate((val_np[:, 1::], val_np[:, 0, None]), axis=1)
test_np = np.concatenate((test_np[:, 1::], test_np[:, 0, None]), axis=1)

LABEL_WINDOW_SIZE = 7

modified_train_np = train_np[0:-LABEL_WINDOW_SIZE]
modified_val_np = val_np[0:-LABEL_WINDOW_SIZE]
modified_test_np = test_np[0:-LABEL_WINDOW_SIZE]

for i in range(LABEL_WINDOW_SIZE-1):

  columns_to_append_train = train_np[i+1:-LABEL_WINDOW_SIZE+i+1, -1]
  columns_to_append_val = val_np[i+1:-LABEL_WINDOW_SIZE+i+1, -1]
  columns_to_append_test = test_np[i+1:-LABEL_WINDOW_SIZE+i+1, -1]

  modified_train_np = np.append(modified_train_np, columns_to_append_train[:, None], 1)
  modified_val_np = np.append(modified_val_np, columns_to_append_val[:, None], 1)
  modified_test_np = np.append(modified_test_np, columns_to_append_test[:, None], 1)


train_dataset = tf.keras.preprocessing.timeseries_dataset_from_array(
    modified_train_np[:, :-LABEL_WINDOW_SIZE], modified_train_np[:, -LABEL_WINDOW_SIZE:], sequence_length=7, batch_size=128)

val_dataset = tf.keras.preprocessing.timeseries_dataset_from_array(
    modified_val_np[:, :-LABEL_WINDOW_SIZE], modified_val_np[:, -LABEL_WINDOW_SIZE:], sequence_length=7, batch_size=128)

test_dataset = tf.keras.preprocessing.timeseries_dataset_from_array(
    modified_test_np[:, :-LABEL_WINDOW_SIZE], modified_test_np[:, -LABEL_WINDOW_SIZE:], sequence_length=7, batch_size=128)

# for batch in train_dataset:
#   inputs, targets = batch
#   print("Input shape:", inputs.shape, "Target shape:", targets.shape)


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
  tf.keras.layers.Conv1D(filters=256, kernel_size=5,
  strides=1, padding="causal",
  activation="relu",
  input_shape=[7, 6]),
  tf.keras.layers.LSTM(128, return_sequences=True),
  tf.keras.layers.LSTM(64, return_sequences=True),
  tf.keras.layers.LSTM(32, return_sequences=True),
  tf.keras.layers.Dense(32, activation="relu"),
  tf.keras.layers.Dense(16, activation="relu"),
  tf.keras.layers.Dense(1),
  ])
elif model_name == 'CNN':
  model = tf.keras.models.Sequential([
  tf.keras.layers.Conv1D(filters=512, kernel_size=5,
  strides=1, padding="causal",
  activation="relu",
  input_shape=[7, 6]),
  tf.keras.layers.Conv1D(256, kernel_size=5, strides=1, padding="causal",activation="relu",),
  tf.keras.layers.Conv1D(128, kernel_size=5, strides=1, padding="causal",activation="relu",),
  tf.keras.layers.Conv1D(64, kernel_size=5, strides=1, padding="causal",activation="relu",),
  tf.keras.layers.Dense(32, activation="relu"),
  tf.keras.layers.Dense(16, activation="relu"),
  tf.keras.layers.Dense(1),
  ])

history = compile_and_fit(model, train_dataset, val_dataset)


# multi_val_performance[model_name] = model.evaluate(val_dataset)
# multi_performance[model_name] = model.evaluate(test_dataset, verbose=0)

model.load_weights(model_ckpt_name)

model.save(model_saved_name, save_format='h5')