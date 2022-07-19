from itertools import product

regions = ["vis ctx", "thal", "hipp", "other ctx", "midbrain", "basal ganglia", "cortical subplate", "other"]
region_colors = ["blue", "red", "green", "darkblue", "violet", "lightblue", "orange", "gray"]
brain_groups = [
    ["VISa", "VISam", "VISl", "VISp", "VISpm", "VISrl"],  # visual cortex
    ["CL", "LD", "LGd", "LH", "LP", "MD", "MG", "PO", "POL", "PT", "RT", "SPF", "TH", "VAL", "VPL", "VPM"],  # thalamus
    ["CA", "CA1", "CA2", "CA3", "DG", "SUB", "POST"],  # hippocampal
    ["ACA", "AUD", "COA", "DP", "ILA", "MOp", "MOs", "OLF", "ORB", "ORBm", "PIR", "PL", "SSp", "SSs", "RSP", "TT"],  # non-visual cortex
    ["APN", "IC", "MB", "MRN", "NB", "PAG", "RN", "SCs", "SCm", "SCig", "SCsg", "ZI"],  # midbrain
    ["ACB", "CP", "GPe", "LS", "LSc", "LSr", "MS", "OT", "SNr", "SI"],  # basal ganglia
    ["BLA", "BMA", "EP", "EPd", "MEA"],  # cortical subplate
]
contrasts = [0.0, 0.25, 0.5, 1.0]
contrast_pairs = list(product(contrasts, contrasts))
