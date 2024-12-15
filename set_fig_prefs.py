def set_fig_prefs():
    import matplotlib.pyplot as plt
    font_preferences = { 'family':'monospace', 'weight':'bold', 'size': 14, 'family': 'Arial'}
    plt.rc('font', **font_preferences)
    #plt.rc('figure', figsize=[10, 10])
    plt.rc('axes', linewidth=1.5)
    plt.rcParams.update({"xtick.major.width": 1.25, "ytick.major.width": 1.25})