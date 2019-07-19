# -*- coding : utf-8 -*-

import os
import sys
import argparse

import NRAJ_Config as nc

class NRAM_Results():
    def __init__(self):
        pass

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description = '日ラ報告用フォーマットを出力')
    parser.add_argument('--version', '-v', action='version',
                        version=os.path.basename(__file__) + ' ver.0.1')
    args = parser.parse_args()
    
    nraj = NRAJ_Results()
