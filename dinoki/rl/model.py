"""
Reinforcement learning model for the dino game.
"""

import tensorflow as tf
import trfl


# DUMMY CODE!

class DinoRl(object):
    def __init__(self, learning_rate=0.1):
        self.learning_rate = learning_rate

        self.setup_model()
        self.setup_loss()
        self.setup_optimizer()

    def setup_model(self):
        # Q-values for the previous and next timesteps, shape [batch_size,
        # num_actions].
        self.q_tm1 = tf.get_variable(
            "q_tm1", initializer=[[1., 1., 0.], [1., 2., 0.]], dtype=tf.float32)
        self.q_t = tf.get_variable(
            "q_t", initializer=[[0., 1., 0.], [1., 2., 0.]], dtype=tf.float32)

        # Action indices, discounts and rewards, shape [batch_size].
        self.a_tm1 = tf.constant([0, 1], dtype=tf.int32)
        self.r_t = tf.constant([1, 1], dtype=tf.float32)
        self.pcont_t = tf.constant([0, 1],
                                   dtype=tf.float32)  # the discount factor

    def setup_loss(self):
        # Q-learning loss, and auxiliary data.
        self.loss, self.q_learning = trfl.qlearning(self.q_tm1, self.a_tm1,
                                                    self.r_t, self.pcont_t,
                                                    self.q_t)
        self.reduced_loss = tf.reduce_mean(self.loss)

    def setup_optimizer(self):
        self.optimizer = tf.train.AdamOptimizer(self.learning_rate)
        self.train_op = self.optimizer.minimize(self.reduced_loss)
