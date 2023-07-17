import os.path as osp
from moshpp.mosh_head import MoSh

soma_work_base_dir = '/scratch/dkj5225/SOMA'

mosh_results_dir = 'training_experiments/V48_02_SOMA/OC_05_G_03_real_000_synt_100/evaluations/mosh_results_tracklet/unlabeled_TMM100'
sequence = 2
ds = "pred" # Or "pred" for autolabeled MoSh results

for subject in range(1,11):
    # npz_dir describes where the npz should be saved (and with what name)
    npz_dir = osp.join(
        soma_work_base_dir,
        f'amass_npzs/{ds}',
        f'Subject{subject}/Subject{subject}_MOCAP_MRK_{sequence}_{ds}_stageii.npz'
    )

    # mosh_stageii_pkl_fname provides the MoSh data to convert
    mosh_stageii_pkl_fname = osp.join(
        soma_work_base_dir,
        mosh_results_dir,
        f'Subject{subject}/MOCAP_MRK_{sequence}_stageii.pkl'
    )

    MoSh.load_as_amass_npz(
        stageii_pkl_data_or_fname = mosh_stageii_pkl_fname,
        stageii_npz_fname = npz_dir,
        include_markers = True
    )