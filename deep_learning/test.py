import sys
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("--n_layer", default=2)
parser.add_argument("--n_para", default=2)

args = parser.parse_args()

from omegaconf import OmegaConf
config = OmegaConf.load(r"deep_learning/config.yaml")
def sum_2_digit(n_layer, n_para):
    return n_layer * n_para

if __name__ == "__main__":
    a = int(args.n_layer)
    b = int(args.n_para)
    print(sum_2_digit(config.n_layer, config.n_para))