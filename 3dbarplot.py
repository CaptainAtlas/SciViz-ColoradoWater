from mpl_toolkits.mplot3d import Axes3D
import matplotlib.colors as colors
import matplotlib.cm as cmx

jet = cm = plt.get_cmap('jet') 
cNorm  = colors.Normalize(vmin=0, vmax=max(data))
scalarMap = cmx.ScalarMappable(norm=cNorm, cmap=jet)

fig=plt.figure(figsize=(10,8))

ax = Axes3D(fig)
ax.add_collection3d(map.drawcoastlines(linewidth=0.25))
ax.add_collection3d(map.drawcountries(linewidth=0.35))
ax.azim = 250
ax.dist = 8

m = Basemap(llcrnrlon=-110.0,llcrnrlat=36.0,\
            urcrnrlon=-101.0,urcrnrlat=42.0)

ax.add_collection3d(m.drawcoastlines(linewidth=0.25))
ax.add_collection3d(m.drawstates(linewidth=1))
#ax.add_collection3d(m.fillcontinents(color='lightgrey',lake_color='aqua'))
ax.add_collection3d(m.drawrivers(color='blue'))

b = ax.bar3d(x, y, np.zeros(len(x)), 0.15, 0.15, data, color=scalarMap.to_rgba(data), alpha=0.5)
