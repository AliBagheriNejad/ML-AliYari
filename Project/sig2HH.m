clc, clear all, close all;
%%
% Read file
path = 'SplitData\Target.csv';
df = readtable(path,'ReadRowNames',true, 'ReadVariableNames',true);

i = 1;
for i = 1:size(df,1)
% for i = 1:5
    % Read Signal
    sig = df(i,2:end);
    sig = sig.Variables;
    
    % EMD on signal
    emd_sig = emd(sig);

    fig = figure('Visible', 'off');
    hht(emd_sig,25000,'FrequencyLimits',[0 500]);
    axis([-0.001 0.021 0 500]); % Adjust these values as needed
    set(fig, 'Position', [100, 100, 800, 600]); % [left, bottom, width, height]
    colorbar off
    % Save the plot
    im_name = df.name{i};
    add = ['HH\Target\',im_name,'.png'];
    saveas(gcf, add);
end
 
