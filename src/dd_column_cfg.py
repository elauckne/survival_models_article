id_col = 'regime_id'
drop_cols = ['ctryname', 'cowcode2', 'politycode', 'ehead', 'leaderspellreg', 'start_year']
cat_cols = ['un_region_name', 'un_continent_name', 'democracy', 'regime']
num_cols = []

duration_col = 'duration'
event_col = 'observed'
target_cols = [duration_col, event_col]