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

     BipedalWalkerHardcore = ExperimentGrid(name='vpg-ocho')
     BipedalWalkerHardcore.add('env_name', 'BipedalWalkerHardcore-v2', '', True)
     # eg.add('clip_ratio', [0.1,0.2])
     BipedalWalkerHardcore.add('seed', [10*i for i in range(args.num_runs)])
     BipedalWalkerHardcore.add('epochs', 10)
     BipedalWalkerHardcore.add('steps_per_epoch', [4000,100])
     BipedalWalkerHardcore.add('optimizer',['NadamOptimizer', 'PowerSignOptimizer', 'RegAdagradOptimizer', 'ShampooOptimizer'])
     BipedalWalkerHardcore.add('ac_kwargs:hidden_sizes', [(32,), (64,64)], 'hid')
     BipedalWalkerHardcore.add('ac_kwargs:activation', [tf.nn.relu, tf.nn.relu6, tf.nn.crelu, tf.nn.elu, tf.nn.selu, tf.nn.softplus, tf.nn.softsign, tf.sigmoid, tf.tanh], '')
     BipedalWalkerHardcore.run(vpg, num_cpu=args.cpu)

     # 'AdadeltaOptimizer', 'AdagradOptimizer', 'AdamOptimizer', 'FtrlOptimizer', 'GradientDescentOptimizer', 'MomentumOptimizer', 'ProximalAdagradOptimizer', 'ProximalGradientDescentOptimizer', 'RMSPropOptimizer', 'AdaMaxOptimizer', 'AdamGSOptimizer', 'AdamWOptimizer', 'AddSignOptimizer', 'GGTOptimizer', 'LARSOptimizer', 'LazyAdamGSOptimizer', 'LazyAdamOptimizer', 'MomentumWOptimizer', 'NadamOptimizer', 'PowerSignOptimizer', 'RegAdagradOptimizer', 'ShampooOptimizer'

     #Done AdadeltaOptimizer, AdagradOptimizer, AdamOptimizer, FtrlOptimizer, LARSOptimizer, LazyAdamGSOptimizer
     #Run 'NadamOptimizer', 'PowerSignOptimizer', 'RegAdagradOptimizer', 'ShampooOptimizer'

     # GradientDescentOptimizer does not work with 1 or 2 or 4 CPUs on Enduro, Pacman, Montezuma
     # GradientDescentOptimizer works on Walker and Lunar

     # MomentumOptimizer, ProximalAdagradOptimizer, ProximalGradientDescentOptimizer, RMSPropOptimizer, AdamGSOptimizer, AdamWOptimizer, AddSignOptimizer, MomentumWOptimizer same as GradDescent
     # GGTOptimizer only works on lunar

     #RN: LARSOptimizer,LazyAdamGSOptimizer, rest
