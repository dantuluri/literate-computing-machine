from spinup.utils.run_utils import ExperimentGrid
from spinup import vpg
import tensorflow as tf
     # ENVS
     # BipedalWalkerHardcore-v2
     # LunarLanderContinuous-v2
     # MontezumaRevenge-ram-v0
     # Enduro-ram-v0
     # MsPacman-ram-v0
     # Ant-v2
     # HumanoidStandup-v2

if __name__ == '__main__':
     import argparse
     parser = argparse.ArgumentParser()
     parser.add_argument('--cpu', type=int, default=4)
     parser.add_argument('--num_runs', type=int, default=10)
     # parser.add_argument('--clip_ratio', type=int, )
     args = parser.parse_args()

     MontezumaRevenge = ExperimentGrid(name='vpg-siete')
     MontezumaRevenge.add('env_name', 'MontezumaRevenge-ram-v0', '', True)
     # eg.add('clip_ratio', [0.1,0.2])
     MontezumaRevenge.add('seed', [10*i for i in range(args.num_runs)])
     MontezumaRevenge.add('epochs', 10)
     MontezumaRevenge.add('steps_per_epoch', [4000,100])
     MontezumaRevenge.add('optimizer',['AdadeltaOptimizer', 'AdagradOptimizer', 'AdamOptimizer', 'FtrlOptimizer', 'GradientDescentOptimizer', 'MomentumOptimizer', 'ProximalAdagradOptimizer', 'ProximalGradientDescentOptimizer', 'RMSPropOptimizer', 'AdaMaxOptimizer', 'AdamGSOptimizer', 'AdamWOptimizer', 'AddSignOptimizer', 'GGTOptimizer', 'LARSOptimizer', 'LazyAdamGSOptimizer', 'LazyAdamOptimizer', 'MomentumWOptimizer', 'NadamOptimizer', 'PowerSignOptimizer', 'RegAdagradOptimizer', 'ShampooOptimizer'])
     MontezumaRevenge.add('ac_kwargs:hidden_sizes', [(32,), (64,64)], 'hid')
     MontezumaRevenge.add('ac_kwargs:activation', [tf.nn.relu, tf.nn.relu6, tf.nn.crelu, tf.nn.elu, tf.nn.selu, tf.nn.softplus, tf.nn.softsign, tf.sigmoid, tf.tanh], '')
     MontezumaRevenge.run(vpg, num_cpu=args.cpu)