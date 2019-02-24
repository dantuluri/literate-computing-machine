# optList = ['GradientDescentOptimizer', 'MomentumOptimizer', 'ProximalAdagradOptimizer', 'ProximalGradientDescentOptimizer', 'RMSPropOptimizer', 'AdaMaxOptimizer', 'AdamGSOptimizer', 'AdamWOptimizer', 'AddSignOptimizer', 'GGTOptimizer', 'LARSOptimizer', 'LazyAdamGSOptimizer', 'LazyAdamOptimizer', 'MomentumWOptimizer', 'NadamOptimizer', 'PowerSignOptimizer', 'RegAdagradOptimizer', 'ShampooOptimizer']
# actList = ['tf.nn.relu', 'tf.nn.relu6', 'tf.nn.crelu', 'tf.nn.elu', 'tf.nn.selu', 'tf.nn.softplus', 'tf.nn.softsign', 'tf.sigmoid', 'tf.tanh']
# with open('areadme.md', 'w') as f:
# 	f.write("# VPG\n| Optimizer  |")
# 	for act in actList:
# 		f.write(" %s |"%act)
# 	f.write("\n|----|")
# 	for a in range(len(actList)):
# 		f.write("--|")
# 	f.write("\n")
# 	for opt in optList:
# 		f.write("| %s |"%opt)
# 		for act in actList:
# 			f.write(" :red_circle: |")
# 		f.write("\n")
allEnvs = ['BipedalWalkerHardcore-v2', 'LunarLanderContinuous-v2', 'MontezumaRevenge-ram-v0', 'Enduro-ram-v0', 'MsPacman-ram-v0']
optList = ['AdadeltaOptimizer', 'AdagradOptimizer', 'AdamOptimizer', 'FtrlOptimizer', 'GradientDescentOptimizer', 'MomentumOptimizer', 'ProximalAdagradOptimizer', 'ProximalGradientDescentOptimizer', 'RMSPropOptimizer', 'AdaMaxOptimizer', 'AdamGSOptimizer', 'AdamWOptimizer', 'AddSignOptimizer', 'GGTOptimizer', 'LARSOptimizer', 'LazyAdamGSOptimizer', 'LazyAdamOptimizer', 'MomentumWOptimizer', 'NadamOptimizer', 'PowerSignOptimizer', 'RegAdagradOptimizer', 'ShampooOptimizer']
actList = ['tf.nn.relu', 'tf.nn.relu6', 'tf.nn.crelu', 'tf.nn.elu', 'tf.nn.selu', 'tf.nn.softplus', 'tf.nn.softsign', 'tf.sigmoid', 'tf.tanh']

f = open('tes.md', 'w')
f.write("# Enduro\n| Optimizer  |")
for tact in actList:
	f.write(" %s |"%tact)
f.write("\n|----|")
for a in range(len(actList)):
	f.write("--|")
f.write("\n")
for opt in optList:
	f.write("| %s |"%opt)
	for act in actList:
		try:
			f.write(" :white_check_mark: |")
		except:        
			f.write(" :red_circle: |")
	f.write("\n")
f.close()