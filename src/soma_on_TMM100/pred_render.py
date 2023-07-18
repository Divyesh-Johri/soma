import os.path as osp
from soma.train.soma_trainer import create_soma_data_id
from soma.tools.run_soma_multiple import run_soma_on_multiple_settings

soma_expr_id = 'V48_02_SOMA'

soma_work_base_dir = '/scratch/dkj5225/SOMA'     # CHANGE TO FIT LOCAL ENV

support_base_dir = osp.join(soma_work_base_dir, 'support_files')
soma_data_settings = [(5, 3, 0.0, 1.0), ]
soma_data_ids = [create_soma_data_id(*soma_data_setting) for soma_data_setting in soma_data_settings]
mocap_base_dir = osp.join(support_base_dir, 'evaluation_mocaps/original')
soma_mocap_target_ds_name = 'unlabeled_TMM100'
blender_temp_dir = osp.join(soma_work_base_dir, 'blender_temp')

run_soma_on_multiple_settings(
        soma_expr_ids=[soma_expr_id],
        soma_mocap_target_ds_names=[
            soma_mocap_target_ds_name,
        ],
        soma_data_ids=soma_data_ids,
        render_cfg={
            # 'moshpp.verbosity': 1,
            # 'render.render_only_one_image': True, # uncomment for initial testing of the pipeline
            'render.show_markers': True,
            # 'render.video_fps': 15,
            # 'render.save_final_blend_file': True, # uncomment to save blend files and image files
            'render.resolution.default': [1600, 1600],  # [x,y]
            'mesh.ds_rate': 5,
            'render.render_engine': 'cycles',  # eevee / cycles,
            'dirs.temp_base_dir': blender_temp_dir,
            'dirs.support_base_dir': support_base_dir,

        },
        mocap_base_dir=mocap_base_dir,
        run_tasks=['render'],
        fname_filter=[],    # Add subject name ("Subject1") or sequence file ("MOCAP_MRK_1.mat") to filter sequences
        mocap_ext='.mat',
        soma_work_base_dir=soma_work_base_dir,
        parallel_cfg = {
            # 'max_num_jobs': 1, # uncomment to run one sequence
            'randomly_run_jobs': True,
        },
    )