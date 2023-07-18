import os.path as osp
from soma.train.soma_trainer import create_soma_data_id
from soma.tools.run_soma_multiple import run_soma_on_multiple_settings

soma_expr_id = 'V48_02_SOMA'

soma_work_base_dir = '/scratch/dkj5225/SOMA'    # CHANGE TO FIT LOCAL ENV

support_base_dir = osp.join(soma_work_base_dir, 'support_files')
soma_data_settings = [(5, 3, 0.0, 1.0), ]
soma_data_ids = [create_soma_data_id(*soma_data_setting) for soma_data_setting in soma_data_settings]
mocap_base_dir = osp.join(support_base_dir, 'evaluation_mocaps/original')
soma_mocap_target_ds_name = 'unlabeled_TMM100'
blender_temp_dir = osp.join(soma_work_base_dir, 'blender_temp')

run_soma_on_multiple_settings(
    soma_expr_ids=[soma_expr_id,],
    soma_mocap_target_ds_names=[soma_mocap_target_ds_name,],
    soma_data_ids=soma_data_ids,
    mosh_cfg={
        'moshpp.verbosity': 1, # set to two to visualize the process in psbody.mesh.mesh_viewer
        'moshpp.stagei_frame_picker.type': 'random',
        'dirs.support_base_dir': support_base_dir,
        # 'mocap.end_fidx': 10 # comment in real runs
    },
    mocap_base_dir=mocap_base_dir,
    run_tasks=['mosh'],
    fname_filter=[],    # Add subject name ("Subject1") or sequence file ("MOCAP_MRK_1.mat") to filter sequences
    mocap_ext='.mat',
    soma_work_base_dir=soma_work_base_dir,
    parallel_cfg={
        # 'max_num_jobs': 1, # uncomment to run one sequence
        'randomly_run_jobs': True,
    },
)