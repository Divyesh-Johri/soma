import os.path as osp
from soma.train.soma_trainer import create_soma_data_id
# from soma.run_soma.paper_plots.mosh_soma_dataset import gen_stagei_mocap_fnames
from soma.tools.run_soma_multiple import run_soma_on_multiple_settings

soma_expr_id = 'V48_02_SOMA'
soma_work_base_dir = '/scratch/dkj5225/SOMA'
support_base_dir = osp.join(soma_work_base_dir, 'support_files')
soma_data_settings = [(5, 3, 0.0, 1.0), ] # upto 5 occlusions, upto 3 ghost points, 0.0% real data, 100. % synthetic data
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
            'render.render_only_one_image': False, # uncomment for initial testing of the pipeline
            'render.show_markers': True,
            # 'render.video_fps': 15,  # 25,
            # 'mesh.ds_rate': 10,
            # 'render.save_final_blend_file': False,
            # 'render.resolution.change_from_blend': True,
            'render.resolution.default': [1600, 1600],  # [x,y]
            'mesh.ds_rate': 5,
            'render.render_engine': 'cycles',  # eevee / cycles,
            # 'render.render_only_one_image': True, # uncomment for initial testing of the pipeline,
            'dirs.temp_base_dir': blender_temp_dir,
            'dirs.support_base_dir': support_base_dir,

        },
        mocap_base_dir=mocap_base_dir,
        run_tasks=['render'],
        fname_filter=[
            osp.join(soma_work_base_dir, 'support_files/evaluation_mocaps/original/unlabeled_TMM100/Subject1/MOCAP_MRK_1.mat'),
            osp.join(soma_work_base_dir, 'support_files/evaluation_mocaps/original/unlabeled_TMM100/Subject2/MOCAP_MRK_1.mat'),
            osp.join(soma_work_base_dir, 'support_files/evaluation_mocaps/original/unlabeled_TMM100/Subject3/MOCAP_MRK_1.mat'),
            osp.join(soma_work_base_dir, 'support_files/evaluation_mocaps/original/unlabeled_TMM100/Subject4/MOCAP_MRK_1.mat'),
            osp.join(soma_work_base_dir, 'support_files/evaluation_mocaps/original/unlabeled_TMM100/Subject5/MOCAP_MRK_1.mat'),],
        parallel_cfg = {
            # 'max_num_jobs': 1, # comment to run on all mocaps
            'randomly_run_jobs': True,
        },

        mocap_ext='.mat',
        soma_work_base_dir=soma_work_base_dir
    )