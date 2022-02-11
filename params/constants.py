SEED = 0

# Dataset params
NB_IMGS_TRAIN_NI = 630
NB_IMGS_TRAIN_CG = 630
NB_IMGS_TEST_PERCLASS = 360
NB_CLASSES = 5 # Natural images and 4 different CG algorithms
BATCH_SIZE = 16

# NICE parameters
INPUT_DIM = 4096 # Don't touch that, not an actual parameter
HIDDEN_DIM = 1000
NUM_LAYERS = 4

# Optimizer params
LR_IMG_MAP = 1e-3
MOMENTUM_IMG_MAP = 0.9
WEIGHT_DECAY_IMG_MAP = 0
LR_FLOW = 1e-3
BETA1 = 0.9
BETA2 = 0.999

# Training params
ID_CG_TRAIN = 1
TRAIN_STEP_IMG_MAP = 100
EPOCHS_IMG_MAP = 3 * TRAIN_STEP_IMG_MAP
EPOCHS_FLOW = 100
K = 2
NU = 0.05

LOG_INTERVAL = 1
