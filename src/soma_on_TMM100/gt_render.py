import os.path as osp
from glob import glob
from loguru import logger
from soma.amass.mosh_manual import mosh_manual

soma_work_base_dir = '/scratch/dkj5225/SOMA'    # CHANGE TO FIT LOCAL ENV

support_base_dir = osp.join(soma_work_base_dir, 'support_files')
mocap_base_dir = osp.join(support_base_dir, 'evaluation_mocaps/mosh')
work_base_dir = osp.join(soma_work_base_dir, 'running_just_mosh')
blender_temp_dir = osp.join(soma_work_base_dir, 'blender_temp_gt')

target_ds_names = ['labeled_TMM100',]

for ds_name in target_ds_names:
    mocap_fnames = glob(osp.join(mocap_base_dir, ds_name,  '.mat'))
    # mocap_fnames = [
    #     osp.join(soma_work_base_dir, 'support_files/evaluation_mocaps/original/labeled_TMM100/Subject1/MOCAP_MRK_1.mat'),
    # ]

    logger.info(f'#mocaps found for {ds_name}: {len(mocap_fnames)}')

    mosh_manual(
        mocap_fnames,
        mosh_cfg={
            'moshpp.verbosity': 1, # set to 2 to visulaize the process in meshviewer
            'dirs.work_base_dir': osp.join(work_base_dir, 'mosh_results'),
            'dirs.support_base_dir': support_base_dir,
        },
        render_cfg={
            'dirs.work_base_dir': osp.join(work_base_dir, 'mp4_renders'),
            'render.resolution.default': [1600, 1600],  # [x,y]
            'mesh.ds_rate': 5,
            'render.render_engine': 'cycles',  # eevee / cycles,
            'render.show_markers': True,
            # 'render.save_final_blend_file': True, # uncomment to save blend files and image files
            # 'render.render_only_one_image': True, # uncomment for initial testing of the pipeline,
            'dirs.support_base_dir': support_base_dir,
            'dirs.temp_base_dir': blender_temp_dir,
        },
        parallel_cfg={
            'pool_size': 1,
            # 'max_num_jobs': 1,     # uncomment to run one sequence
            'randomly_run_jobs': True,
        },
        run_tasks=[
            'render',
        ],
    )
