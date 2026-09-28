import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def plot_raw(file_csv,file_name,file_title):
    df = pd.read_csv(file_csv)
    t = df["Time (s)"]
    a = df["Absolute acceleration (m/s^2)"]
    plt.plot(t,a)
    plt.xlabel("Time (s)")
    plt.ylabel("Absolute acceleration (m/s^2))")
    plt.title(file_title)
    plt.savefig(file_name)
    plt.close()

plot_raw("run.csv","run.png","running-raw")
plot_raw("walk.csv","walk.png","walk-raw")

df=pd.read_csv("run.csv")
y=df["Absolute acceleration (m/s^2)"].to_numpy()
#滤波函数
def moving_average(y,window=5):
    half = window//2
    result = []
    for i in range(half,len(y)-half):
        result.append(np.mean(y[i-half:i+half+1]))
    return np.array(result)
#run滤波
smooth = moving_average(y,5)
t=df["Time (s)"].to_numpy()
t_smooth = t[2:2+len(smooth)]
plt.plot(t,y,alpha = 0.4,label="Raw")
plt.plot(t_smooth,smooth,linewidth = 2,label="filtered")
plt.xlabel("Time (s)")
plt.ylabel("Absolute acceleration (m/s^2)")
plt.legend()
plt.savefig("run_filtered.png")
plt.close()
#run窗口51滤波
smooth_big = moving_average(y,51)
t=df["Time (s)"].to_numpy()
t_smooth = t[25:25+len(smooth_big)]
plt.plot(t,y,alpha = 0.4,label="Raw")
plt.plot(t_smooth,smooth_big,linewidth = 2,label="filtered")
plt.xlabel("Time (s)")
plt.ylabel("Absolute acceleration (m/s^2)")
plt.legend()
plt.savefig("run_filtered_big.png")
plt.close()
#walk滤波
df1=pd.read_csv("walk.csv")
t_walk = df1["Time (s)"].to_numpy()
y_walk = df1["Absolute acceleration (m/s^2)"].to_numpy()
smooth_walk = moving_average(y_walk,5)
plt.plot(t_walk,y_walk,linewidth = 0.5,label="Raw")
t_walk_smooth = t_walk[2:2+len(smooth_walk)]
plt.plot(t_walk_smooth,smooth_walk,linewidth = 2,label="filtered")
plt.xlabel("Time (s)")
plt.ylabel("Absolute acceleration (m/s^2)")
plt.legend()
plt.savefig("walk_filtered.png")
plt.close()

print(f"run:均值{smooth.mean():.2f},标准差{smooth.std():.2f}")
print(f"walk:均值{smooth_walk.mean():.2f},标准差{smooth_walk.std():.2f}")
