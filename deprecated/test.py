import matplotlib.pyplot as plt
from matplotlib.widgets import Button

fig = plt.figure()
def next(event, text):
    print(text)
    pass


axnext = plt.axes([0.81, 0.05, 0.1, 0.075])
bnext = Button(axnext, 'Next')
bnext.on_clicked(lambda x: next(x, bnext.label.get_text()))
plt.show()