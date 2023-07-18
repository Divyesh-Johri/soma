% TMMdir: (String) location of TMM100 marker folder
% label: (bool) true if labeling markers, false if unlabeled
function save_markers(TMMdir, label)
    takes = [9, 11, 9, 11, 8, 10, 9, 10, 13, 10];
    sex = ["female", "male", "female", "male", "female", "female", "male", "male", "female", "male"];
    
    if(label)
        dataset = "labeled_TMM100";
    else
        dataset = "unlabeled_TMM100";
    end
    
    for subject = 1:10

        % Create new directory
        mkdir(sprintf("%s/Subject%d", dataset, subject));

        % Create settings json
        settings = struct('gender', sex(subject));
        fileID = fopen(sprintf("%s/Subject%d/settings.json", dataset, subject), 'w');
        fprintf(fileID, '%s', jsonencode(settings));
        fclose(fileID);

        for take = 1:takes(subject)
            % Filenames for joints and markers
            mocapmarkerfile = sprintf('%s/Mocap_Markers/Subject%d/MOCAP_MRK_%d.mat', TMMdir, subject, take);
            
            % Marker order is as follows: 
            % LFHD, RFHD, LBHD, RBHD, C7, T10, CLAV, STRN, RBAK, LSHO, LUPA, LELB, 
            % LFRM, LWRA, LWRB, LFIN, RSHO, RUPA, RELB, RFRM, RWRA, RWRB, RFIN, 
            % LASI, RASI, LPSI, RPSI, LTHI, LKNE, LTIB, LANK, LHEE, LTOE, RTHI, 
            % RKNE, RTIB, RANK, RHEE, RTOE.
            
            % Mocap marker data
            tmp = load(mocapmarkerfile);
            markers = tmp.mcMarkers();
            Markers = markers(:,:,1:3);

            if(label)
                monames = tmm_monames();
                m = size(markers, 1);
                Labels = repmat(monames, [m,1]);
                save(sprintf("%s/Subject%d/MOCAP_MRK_%d.mat", dataset, subject, take), ...
                "Markers", "Labels")
            else
                save(sprintf("%s/Subject%d/MOCAP_MRK_%d.mat", dataset, subject, take), ...
                "Markers")
            end
        end
    end
end



