import os.path as osp
from glob import glob

import numpy as np
from loguru import logger

from soma.amass.mosh_manual import mosh_manual

soma_work_base_dir = '/scratch/dkj5225/SOMA'
support_base_dir = osp.join(soma_work_base_dir, 'support_files')

mocap_base_dir = osp.join(support_base_dir, 'evaluation_mocaps/mosh')

work_base_dir = osp.join(soma_work_base_dir, 'running_just_mosh')

blender_temp_dir = osp.join(soma_work_base_dir, 'blender_temp_gt')

target_ds_names = ['labeled_TMM100',]

for ds_name in target_ds_names:
    # mocap_fnames = glob(osp.join(mocap_base_dir, ds_name,  '.mat'))
    mocap_fnames = [
        osp.join(soma_work_base_dir, 'support_files/evaluation_mocaps/original/labeled_TMM100/Subject1/MOCAP_MRK_1.mat'),
        osp.join(soma_work_base_dir, 'support_files/evaluation_mocaps/original/labeled_TMM100/Subject2/MOCAP_MRK_1.mat'),
        osp.join(soma_work_base_dir, 'support_files/evaluation_mocaps/original/labeled_TMM100/Subject3/MOCAP_MRK_1.mat'),
        osp.join(soma_work_base_dir, 'support_files/evaluation_mocaps/original/labeled_TMM100/Subject4/MOCAP_MRK_1.mat'),
        osp.join(soma_work_base_dir, 'support_files/evaluation_mocaps/original/labeled_TMM100/Subject5/MOCAP_MRK_1.mat'),
        osp.join(soma_work_base_dir, 'support_files/evaluation_mocaps/original/labeled_TMM100/Subject6/MOCAP_MRK_1.mat'),
        osp.join(soma_work_base_dir, 'support_files/evaluation_mocaps/original/labeled_TMM100/Subject7/MOCAP_MRK_1.mat'),
        osp.join(soma_work_base_dir, 'support_files/evaluation_mocaps/original/labeled_TMM100/Subject8/MOCAP_MRK_1.mat'),
        osp.join(soma_work_base_dir, 'support_files/evaluation_mocaps/original/labeled_TMM100/Subject9/MOCAP_MRK_1.mat'),
        osp.join(soma_work_base_dir, 'support_files/evaluation_mocaps/original/labeled_TMM100/Subject10/MOCAP_MRK_1.mat')
    ]

    logger.info(f'#mocaps found for {ds_name}: {len(mocap_fnames)}')

    mosh_manual(
        mocap_fnames,
        mosh_cfg={
            'moshpp.verbosity': 1, # set to 2 to visulaize the process in meshviewer
            'dirs.work_base_dir': osp.join(work_base_dir, 'mosh_results'),
            'dirs.support_base_dir': support_base_dir,
        },
        parallel_cfg={
            'pool_size': 1,
            # 'max_num_jobs': 3,
            'randomly_run_jobs': True,
        },
        run_tasks=[
            'mosh',
        ],
    )
