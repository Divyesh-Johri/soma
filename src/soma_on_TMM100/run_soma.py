import os.path as osp
from soma.train.soma_trainer import create_soma_data_id
from soma.tools.run_soma_multiple import run_soma_on_multiple_settings
soma_expr_id = 'V48_02_SOMA'

soma_work_base_dir = '/home/divyeshjohri/Documents/SOMA'    # CHANGE TO FIT LOCAL ENV

support_base_dir = osp.join(soma_work_base_dir, 'support_files')
soma_data_settings = [(5, 3, 0.0, 1.0), ]
soma_data_ids = [create_soma_data_id(*soma_data_setting) for soma_data_setting
in soma_data_settings]
mocap_base_dir = osp.join(support_base_dir, 'evaluation_mocaps/original')
soma_mocap_target_ds_name = 'unlabeled_TMM100' # Unlabeled dataset
soma_mocap_ds_name_gt = 'labeled_TMM100' # Ground-truth dataset

run_soma_on_multiple_settings(
    soma_expr_ids=[soma_expr_id],
    soma_mocap_target_ds_names=[soma_mocap_target_ds_name],
    soma_data_ids=soma_data_ids,
    soma_cfg={
        'soma.batch_size': 512,
        'dirs.support_base_dir': support_base_dir,
        'mocap.unit': 'mm',
        'save_c3d': True,
        'keep_nan_points': True, # required for labeling evaluation
        'remove_zero_trajectories': False # required for labeling evaluation
    },
    mocap_base_dir=mocap_base_dir,
    run_tasks=['soma'],
    mocap_ext='.mat',
    soma_work_base_dir = soma_work_base_dir,
    parallel_cfg = {
        'randomly_run_jobs': True,
    },
)