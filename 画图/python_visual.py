#-*- coding:utf-8 -*-

import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
# 要显示3d图像，必须加上此句
from mpl_toolkits.mplot3d import Axes3D
myfont=fm.FontProperties(fname='/Library/Fonts/Songti.ttc',size=14)
# 简单曲线图
def simple_plot():
    # 生成测试数据
    x=np.linspace(-np.pi,np.pi,256,endpoint=True)
    y_cos,y_sin=np.cos(x),np.sin(x)

    # 生成画布，并设定标题
    plt.figure(figsize=(8,6),dpi=80)
    plt.title('简单曲线图',fontproperties=myfont)
    plt.grid(True)

    # 设置X轴
    plt.xlabel('X轴',fontproperties=myfont)
    plt.xlim(-4.0,4.0)
    plt.xticks(np.linspace(-4,4,9,endpoint=True))

    # 设置Y轴
    plt.ylabel('Y轴',fontproperties=myfont)
    plt.ylim(-1.0,1.0)
    plt.yticks(np.linspace(-1,1,9,endpoint=True))

    # 画两条曲线
    plt.plot(x,y_cos,'b--',linewidth=2.0,label='cos示例')
    plt.plot(x,y_sin,'g-',linewidth=2.0,label='sin示例')

    # 设置图例位置,loc可以为[upper,lower,left,right,center]
    plt.legend(loc='upper left',prop=myfont,shadow=True)

    # 图形显示
    plt.show()
    return

# 复杂曲线图
def simple_advanced_plot():
    # 生成测试数据
    x=np.linspace(-np.pi,np.pi,256,endpoint=True)
    y_cos,y_sin=np.cos(x),np.sin(x)

    # 生成画布，并设定标题
    plt.figure(figsize=(8,6),dpi=80)
    plt.title("复杂曲线图",fontproperties=myfont)
    plt.grid(True)

    # 画图的另外一种方式
    ax_1=plt.subplot(111)
    ax_1.plot(x,y_cos,color='blue',linewidth=2.0,linestyle='--',label='左cos')
    ax_1.legend(loc='upper left',prop=myfont,shadow=True)

    # 设置Y轴(左边)
    ax_1.set_ylabel('左cos的Y轴',fontproperties=myfont)
    ax_1.set_ylim(-1.0,1.0)
    ax_1.set_yticks(np.linspace(-1,1,9,endpoint=True))

    # 画图的另外一种方式
    ax_2=ax_1.twinx()
    ax_2.plot(x,y_sin,color='green',linewidth=2.0,linestyle='-',label='右sin')
    ax_2.legend(loc='upper right',prop=myfont,shadow=True)

    # 设置Y轴(右边)
    ax_2.set_ylabel('右sin的y轴',fontproperties=myfont)
    ax_2.set_ylim(-2.0,2.0)
    ax_2.set_yticks(np.linspace(-2,2,9,endpoint=True))

    # 设置X轴(共同)
    ax_1.set_xlabel('x轴',fontproperties=myfont)
    ax_1.set_xlim(-4.0,4.0)
    ax_1.set_xticks(np.linspace(-4,4,9,endpoint=True))

    # 图形显示
    plt.show()
    return
# 生成子图
def subplot_plot():
    style_list=['g+-','r*-','b.-','yo-']
    # 依次画图
    for num in range(4):
        # 生成测试数据
        x=np.linspace(0.0,2+num,num=10*(num+1))
        y=np.sin((5-num)*np.pi*x)
        # 子图的生成方式
        plt.subplot(2,2,num+1)
        plt.title("子图 %d"%(num+1),fontproperties=myfont)
        plt.plot(x,y,style_list[num])

    # 图形显示
    plt.show()
    return

# subplot_plot()
def bar_plot():
    # 生成测试数据
    means_men=(20,35,30,35,27)
    means_women=(25,32,34,20,25)

    # 设置标题
    plt.title('柱状图',fontproperties=myfont)

    # 设置相关参数
    index=np.arange(len(means_men))
    bar_width=0.35

    # 画柱状图,alpha表示透明度
    plt.bar(index,means_men,width=bar_width,alpha=0.2,color='b',label='男生')
    plt.bar(index+bar_width,means_women,width=bar_width,alpha=0.8,color='r',label='女生')
    plt.legend(loc='upper right',prop=myfont,shadow=True)

    # 设置柱状图标示
    for x,y in zip(index,means_men):
        plt.text(x,y+0.3,y,ha='center',va='bottom')
    for x,y in zip(index,means_women):
        plt.text(x+bar_width,y+0.3,y,ha='center',va='bottom')

    # 设置刻度范围/坐标轴名称等
    plt.ylim(0,45)
    plt.xlabel('分组Group',fontproperties=myfont)
    plt.ylabel('得分Scores',fontproperties=myfont)
    plt.xticks(index+(bar_width/2),('A组','B组','C组','D组','E组'),fontproperties=myfont)

    plt.show()
    return

# 横向柱状图
def barh_plot():
    means_men=(20,35,30,35,27)
    means_women=(25,32,34,20,25)
    # 设置标题
    plt.title('横向柱状图',fontproperties=myfont)
    # 设置相关参数
    index=np.arange(len(means_men))
    bar_height=0.35
    # 画柱状图(水平方向),alpha表示透明度
    plt.barh(index,means_men,height=bar_height,alpha=0.2,color='b',label='男生')
    plt.barh(index+bar_height,means_women,height=bar_height,alpha=0.8,color='r',label='女生')
    plt.legend(loc='upper right',prop=myfont,shadow=True)
    # 设置柱状图标示
    for x,y in zip(index,means_men):
        plt.text(y+0.3,x,y,ha='left',va='center')
    for x,y in zip(index,means_women):
        plt.text(y+0.3,x+bar_height,y,ha='left',va='center')

    # 设置刻度范围/坐标轴名称等
    plt.xlim(0,45)
    plt.xlabel('Scores')
    plt.ylabel('Group')
    plt.yticks(index+(bar_height/2),('A组','B组','C组','D组','E组'),fontproperties=myfont)

    plt.show()
    return
# barh_plot()

# 柱状和折线
def bar_advanced_plot():
    means_men = np.array((20, 35, 30, 35, 27, 25, 32, 34, 20, 25))
    means_women = np.array((25, 32, 34, 20, 25, 20, 35, 30, 35, 27))
    #设置标题
    plt.title('高级柱状图',fontproperties=myfont)
    # 设置相关参数
    index=np.arange(len(means_men))
    bar_width=0.8

    # 画柱状图(两种：X轴以上和X轴以下)
    plt.bar(index,means_men,width=bar_width,alpha=0.4,color='b',label='Men')
    plt.bar(index,-means_women,width=bar_width,alpha=0.4,color='r',label='Women')

    #画折线图(两种，和柱状图对应)
    plt.plot(index,means_men,marker='o',linestyle='-',color='r',label='Men line')
    plt.plot(index,-means_women,marker='.',linestyle='--',color='b',label='Women line')

    #设置图形标示(两种，和柱状图对应)
    for x,y in zip(index,means_men):
        plt.text(x,y+1,y,ha='center',va='bottom')
    for x,y in zip(index,means_women):
        plt.text(x,-y-1,y,ha='center',va='top')

    # 设置Y轴和图例位置
    plt.ylim(-45,80)
    plt.legend(loc='upper left',shadow=True)

    plt.show()
    return
# bar_advanced_plot()
# 层次柱状图
def table_plot():
    # 生成测试数据
    data=np.array([
        [1,4,2,5,2],
        [2,1,1,3,6],
        [5,3,6,4,1]
    ])

    # 设置标题
    plt.title('层次柱状图',fontproperties=myfont)

    # 设置相关参数
    index=np.arange(len(data[0]))
    color_index=['r','g','b']
    # 声明底部位置
    bottom=np.array([0,0,0,0,0])
    # 依次画图，并更新底部位置
    for i in range(len(data)):
        plt.bar(index,data[i],width=0.5,color=color_index[i],bottom=bottom,alpha=0.7,label='标签 %d'%i)
        bottom+=data[i]

    # 设置图例位置
    plt.legend(loc='upper left',prop=myfont,shadow=True)

    plt.show()
    return

# 直方图
def histograms_plot():
    # 生成测试数据
    mu,sigma=100,15
    x=mu+sigma*np.random.randn(10000)
    # 设置标题
    plt.title('直方图',fontproperties=myfont)
    # 画直方图，并返回相关结果
    n,bins,patches=plt.hist(x,bins=50,normed=1,cumulative=False,color='green',alpha=0.6,label='直方图')
    # 根据直方图返回的结果，画折线图
    y=mlab.normpdf(bins,mu,sigma)
    plt.plot(bins,y,'r--',label='线条')
    # 设置图例位置
    plt.legend(loc='upper left',prop=myfont,shadow=True)

    plt.show()
    return

# 饼图
def pie_plot():
    # 生成测试数据
    sizes=[15,30,45,10]
    labels = ["Frogs", "中文", "Dogs", "Logs"]
    colors = ["yellowgreen", "gold", "lightskyblue", "lightcoral"]

    # 设置标题
    plt.title('饼图',fontproperties=myfont)
    # 设置突出参数
    explode=[0,0.05,0,0]
    # 画饼状图
    patches,l_text,p_text=plt.pie(sizes,explode=explode,labels=labels,colors=colors,autopct='%1.1f%%',shadow=True,startangle=90)
    for text in l_text:
        text.set_fontproperties(myfont)
    plt.axis('equal')

    plt.show()
    return
# 散点图
def scatter_plot():
    # 生成测试数据
    point_count=1000
    x_index=np.random.random(point_count)
    y_index=np.random.random(point_count)

    # 设置标题
    plt.title('散点图',fontproperties=myfont)
    # 设置相关参数
    color_list=np.random.random(point_count)
    scale_list=np.random.random(point_count)*100
    # 画散点图
    plt.scatter(x_index,y_index,s=scale_list,c=color_list,marker='o')

    plt.show()
    return

# 填充图
def fill_plot():
    # 生成测试数据
    x=np.linspace(-2*np.pi,2*np.pi,1000,endpoint=True)
    y=np.sin(x)
    # 设置标题
    plt.title('填充图',fontproperties=myfont)
    # 画图
    plt.plot(x,y,color='blue',alpha=1.0)
    # 填充图形
    plt.fill_between(x,0,y,where=(y>0),color='blue',alpha=0.25)
    plt.fill_between(x,0,y,where=(y<0),color='red',alpha=0.25)

    plt.show()
    return

# 雷达图
def radar_plot():
    # 生成测试数据
    labels = np.array(["A组", "B组", "C组", "D组", "E组", "F组"])
    data=np.array([68,83,90,77,89,73])
    theta=np.linspace(0,2*np.pi,len(data),endpoint=False)
    # 数据预处理
    data=np.concatenate((data,[data[0]]))
    theta=np.concatenate((theta,[theta[0]]))

    # 画图方式
    plt.subplot(111,polar=True)
    plt.title('雷达图',fontproperties=myfont)
    # 设置'theta grid/radar gird
    plt.thetagrids(theta*(180/np.pi),labels=labels,fontproperties=myfont)
    plt.rgrids(np.arange(20,100,20),labels=np.arange(20,100,20),angle=0)
    plt.ylim(0,100)

    # 画雷达图，并填充雷达图内部区域
    plt.plot(theta,data,'bo-',linewidth=2)
    plt.fill(theta,data,color='red',alpha=0.25)

    plt.show()
    return

# 三维散点图，运行不成功
def three_dimension_scatter():
    # 生成测试数据
    x=np.random.random(100)
    y=np.random.random(100)
    z=np.random.random(100)
    color=np.random.random(100)
    scale=np.random.random(100)*100
    # 生成画布(两种形式)
    fig=plt.figure()
    fig.suptitle('三维散点图',fontproperties=myfont)

    ax=fig.add_subplot(111,projection='3d')

    # 画三维散点图
    ax.scatter(x,y,z,s=scale,c=color,marker='.')
    # 设置坐标轴图标
    ax.set_xlabel('X Label')
    ax.set_ylabel('Y Label')
    ax.set_zlabel('X label')

    # 设置坐标轴范围
    ax.set_xlim(0,1)
    ax.set_ylim(0,1)
    ax.set_zlim(0,1)

    plt.show()

# 三维折线图
def three_dimension_line():
    # 生成测试数据
    x=np.linspace(0,1,1000)
    y=np.linspace(0,1,1000)
    z=np.sin(x*2*np.pi)/(y+0.1)
    # 生成画布(两种形式)
    fig=plt.figure()
    ax=fig.gca(projection='3d',title='plot title')
    # 画三维折线图
    ax.plot(x,y,z,color='red',linestyle='-')
    # 设置坐标轴图标
    ax.set_xlabel('X Label')
    ax.set_ylabel('Y Label')
    ax.set_zlabel('Z label')

    plt.show()

# 三维柱状图
def three_dimension_bar():
    # 生成测试数据(位置数据)
    xpos = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    ypos = [2, 3, 4, 5, 1, 6, 2, 1, 7, 2]
    zpos = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    # 生成测试数据(柱形参数)
    dx = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    dy = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    dz = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    # 生成画布
    fig=plt.figure()
    ax=fig.gca(projection='3d',title='plot title')
    # 画三维柱状图
    ax.bar3d(xpos,ypos,zpos,dx,dy,dz,alpha=0.5)
    # 设置坐标轴图标
    ax.set_xlabel('X Label')
    ax.set_ylabel('Y Label')
    ax.set_zlabel('Z label')

    plt.show()

three_dimension_bar()