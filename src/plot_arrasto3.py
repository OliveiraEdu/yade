import pandas as pd
import pylab as plt
import seaborn as sns

#sns.set_theme(style="darkgrid")

data = pd.read_csv('dados.csv', delimiter=',', header=None)

sns.set_theme()

#g = sns.relplot(x=0, y=1, sort=False, kind="line", data=data);
#h = sns.relplot(x=0, y=2, sort=False, kind="line", data=data);


sns.relplot(x="timepoint", y="signal", hue="region",
            units="subject", estimator=None,
            kind="line", data=fmri.query("event == 'stim'"));

#g.figure.autofmt_xdate()
#h.figure.autofmt_xdate()

plt.show()
