from spinup.utils.run_utils import ExperimentGrid
from spinup import vpg
import tensorflow as tf

if __name__ == '__main__':
     import argparse
     parser = argparse.ArgumentParser()
     parser.add_argument('--cpu', type=int, default=4)
     parser.add_argument('--num_runs', type=int, default=5)
     # parser.add_argument('--clip_ratio', type=int, )
     args = parser.parse_args()

     def runExperiment(someEnv,someOptimizer, someActivation, someSize, someEpoch):
          env = ExperimentGrid(name='vpg-once')
          env.add('env_name', someEnv, '', True)
           # eg.add('clip_ratio', [0.1,0.2])
          env.add('seed', [10*i for i in range(args.num_runs)])
          env.add('epochs', someEpoch)
          env.add('steps_per_epoch', [4000])
          #someOptimizer should be list
          env.add('optimizer',[someOptimizer])
          env.add('ac_kwargs:hidden_sizes', someSize, 'hid')
          env.add('ac_kwargs:activation', [someActivation], '')
          env.run(vpg, num_cpu=args.cpu)
          #, 'ProximalAdagradOptimizer', 'ProximalGradientDescentOptimizer', 'RMSPropOptimizer', 'AdaMaxOptimizer', 'AdamGSOptimizer', 'AdamWOptimizer', 'AddSignOptimizer', 'GGTOptimizer', 'LARSOptimizer', 'LazyAdamGSOptimizer', 'LazyAdamOptimizer', 'MomentumWOptimizer', 'NadamOptimizer', 'PowerSignOptimizer', 'RegAdagradOptimizer', 'ShampooOptimizer'
          # , , tf.nn.crelu, tf.nn.elu, tf.nn.selu, tf.nn.softplus, tf.nn.softsign, tf.sigmoid, tf.tanh

     allEnvs = ['BipedalWalkerHardcore-v2', 'LunarLanderContinuous-v2', 'MontezumaRevenge-ram-v0', 'Enduro-ram-v0', 'MsPacman-ram-v0']
     optList = ['AdadeltaOptimizer', 'AdagradOptimizer', 'AdamOptimizer', 'FtrlOptimizer', 'GradientDescentOptimizer', 'MomentumOptimizer', 'ProximalAdagradOptimizer', 'ProximalGradientDescentOptimizer', 'RMSPropOptimizer', 'AdaMaxOptimizer', 'AdamGSOptimizer', 'AdamWOptimizer', 'AddSignOptimizer', 'GGTOptimizer', 'LARSOptimizer', 'LazyAdamGSOptimizer', 'LazyAdamOptimizer', 'MomentumWOptimizer', 'NadamOptimizer', 'PowerSignOptimizer', 'RegAdagradOptimizer', 'ShampooOptimizer']
     actList = ['tf.nn.relu', 'tf.nn.relu6', 'tf.nn.crelu', 'tf.nn.elu', 'tf.nn.selu', 'tf.nn.softplus', 'tf.nn.softsign', 'tf.sigmoid', 'tf.tanh']
     tfList = [tf.nn.relu, tf.nn.relu6, tf.nn.crelu, tf.nn.elu, tf.nn.selu, tf.nn.softplus, tf.nn.softsign, tf.sigmoid, tf.tanh]
     hidSize = [(32,), (64,64)]
     bigSize = [(300,), (128,128)]
     sz = [hidSize,bigSize]
     epochList = [10,100,200]
     f = open('readme.md', 'w')
     for envi in allEnvs:
          f.write("# %s\n| Optimizer  |"%envi)
          for tact in actList:
               f.write(" %s |"%tact)
          f.write("\n|----|")
          for a in range(len(actList)):
               f.write("--|")
          f.write("\n")
          for opt in optList:
               f.write("| %s |"%opt)
               for act in tfList:
                    for siz in sz:
                         for ep in epochList:
                              try:
                                   runExperiment(envi,opt,act,siz,ep)
                                   f.write(" :white_check_mark: |")
                              except:        
                                   f.write(" :red_circle: |")
               f.write("\n")
          f.write("\n\n")
     f.close()

