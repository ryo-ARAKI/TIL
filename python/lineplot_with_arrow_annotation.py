########################################################################
#
#  Matplotlibのplt.plotに矢印のアノーテーションをつける
#  https://stackoverflow.com/a/19102353
#
########################################################################
import numpy as np
import matplotlib.pyplot as plt


def arrowplot(
    axes, x, y, narrs=30, dspace=0.5,
    hl=0.3, hw=6, c='black'
):
    '''
    narrs  :  Number of arrows that will be drawn along the curve

    dspace :  Shift the position of the arrows along the curve.
              Should be between 0. and 1.

    hl     :  length of the arrow head

    hw     :  width of the arrow head

    c      :  color of the edge and face of the arrow head
    '''

    # r is the distance spanned between pairs of points
    r = [0]
    for i in range(1, len(x)):
        dx = x[i]-x[i-1]
        dy = y[i]-y[i-1]
        r.append(np.sqrt(dx*dx+dy*dy))
    r = np.array(r)

    # rtot is a cumulative sum of r, it's used to save time
    rtot = []
    for i in range(len(r)):
        rtot.append(r[0:i].sum())
    rtot.append(r.sum())

    # based on narrs set the arrow spacing
    aspace = r.sum() / narrs

    arrowData = []  # will hold tuples of x,y,theta for each arrow
    arrowPos = aspace*(dspace)  # current point on walk along data
    # could set arrowPos to 0 if you want
    # an arrow at the beginning of the curve

    ndrawn = 0
    rcount = 1
    while arrowPos < r.sum() and ndrawn < narrs:
        x1, x2 = x[rcount-1], x[rcount]
        y1, y2 = y[rcount-1], y[rcount]
        da = arrowPos-rtot[rcount]
        theta = np.arctan2((x2-x1), (y2-y1))
        ax = np.sin(theta)*da+x1
        ay = np.cos(theta)*da+y1
        arrowData.append((ax, ay, theta))
        ndrawn += 1
        arrowPos += aspace
        while arrowPos > rtot[rcount+1]:
            rcount += 1
            if arrowPos > rtot[-1]:
                break

    # could be done in above block if you want
    for ax, ay, theta in arrowData:
        # use aspace as a guide for size and length of things
        # scaling factors were chosen by experimenting a bit

        dx0 = np.sin(theta)*hl/2. + ax
        dy0 = np.cos(theta)*hl/2. + ay
        dx1 = -1.*np.sin(theta)*hl/2. + ax
        dy1 = -1.*np.cos(theta)*hl/2. + ay

        ax0 = dx1
        ay0 = dy1
        ax1 = dx0
        ay1 = dy0

        axes.annotate(
            '',
            xy=(ax0, ay0), xycoords='data',
            xytext=(ax1, ay1), textcoords='data',
            arrowprops=dict(headwidth=hw, frac=1., ec=c, fc=c)
        )

    axes.plot(x, y, color=c)
    axes.set_xlim(x.min()*1.1, x.max()*1.1)
    axes.set_ylim(y.min()*1.1, y.max()*1.1)


if __name__ == '__main__':
    fig = plt.figure()
    axes = fig.add_subplot(111)

    # my random data
    l = np.linspace(0.0, 4.0*np.pi, 100)
    x = l * np.sin(l)
    y = l * np.cos(l)
    arrowplot(axes, x, y)

    plt.show()
