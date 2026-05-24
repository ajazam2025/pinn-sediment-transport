import tensorflow as tf
from tensorflow.keras import layers

def build_pinn(input_dim):

    model = tf.keras.Sequential([

        layers.Dense(
            64,
            activation='relu'
        ),

        layers.Dense(
            64,
            activation='relu'
        ),

        layers.Dense(1)

    ])

    model.compile(
        optimizer='adam',
        loss='mse'
    )

    return model
