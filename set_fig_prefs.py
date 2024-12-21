def set_fig_prefs():
    import matplotlib.pyplot as plt
    font_preferences = { 'family':'monospace', 'weight':'bold', 'size': 14, 'family': 'Arial'}
    plt.rc('font', **font_preferences)
    #plt.rc('figure', figsize=[10, 10])
    plt.rc('axes', linewidth=1.5)
    plt.rcParams.update({"xtick.major.width": 1.25, "ytick.major.width": 1.25})

    #update default color palette from coolors.co
    from cycler import cycler
    coolors_color_palette_ = ["#ff0000","#ff8700","#ffd300","#deff0a","#a1ff0a","#0aff99","#0aefff","#147df5","#580aff","#be0aff"] #https://coolors.co/palette/ff0000-ff8700-ffd300-deff0a-a1ff0a-0aff99-0aefff-147df5-580aff-be0aff
    # plt.rcParams.update({"axes.prop_cycle": plt.cycler(color=coolors_color_palette)})
    plt.rcParams.update({"axes.prop_cycle": plt.cycler(color=coolors_color_palette_)})