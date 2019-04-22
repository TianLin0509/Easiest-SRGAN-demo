# Easiest-SRGAN-demo
最简单的基于SRGAN网络的实现， 附带已训练好的模型及GIF生成代码， 更适合作为Demo展示。

# Demo效果
![image](https://github.com/TianLin0509/Easiest-SRGAN-demo/blob/master/result.png)

上图就是训练了2000次后的模型的效果，只需要输入一张左边的低精度的图片， 就可以生成右边的高精度的图片。肉眼看上去效果还是非常不错的！

![image](https://github.com/TianLin0509/Easiest-SRGAN-demo/blob/master/demo.gif)

(由于GIF较大可能加载不出来)

这张GIF则展示了整个训练过程的变化， **左边的图是由神经网络生成的， 中间的是原始的高精度的图片， 右边的是输入到神经网络的低分辨率图片**， ==神经网络在整个生成过程中是没有得到高精度图片信息的，这里给出高精度图片只是为了对比体现生成的效果==。可以看到在100次epoch迭代之后，性能已经非常不错了。 
# 环境要求
***
## 训练模型
tensorflow or tensorflow-gpu > 1.10.0 

keras = 2.2.4

## 生成自己的GIF图片
imageio ```pip install imageio```

# 代码使用
***
## 直接使用训练好的模型恢复高精度图片
* 下载训练好的模型权重

我给出了自己这边训练了2000次后的模型权重，可以从[链接](https://pan.baidu.com/s/1RWd8-fyF-2pHUJWqWmoKaw )下载
提取码：su92 
下载完成后，将.h5文件保存在saved_model文件夹下
运行**srgan.py**, (将gan.train这一句注释掉).

* 自己训练模型

先去下载数据集[数据集地址](http://mmlab.ie.cuhk.edu.hk/projects/CelebA.html) ，推荐使用百度云盘下载，很快。
将代码中self.dataset_name改为本地的数据集地址。
运行**srgan.py**.

* 生成自己的GIF
（必须是自己训练模型后才能使用）
运行**generate_GIF.py**

* 所有测试数据默认存放在test_images文件夹下

# 参考
这个代码主要基于https://github.com/eriklindernoren/Keras-GAN)的实现，做了一些小小的修改更有demo效果。

论文地址 [Photo-Realistic Single Image Super-Resolution Using a Generative Adversarial Network](https://arxiv.org/abs/1609.04802)。

博客地址 [深度学习：用生成对抗网络（GAN）来恢复高分辨率（高精度）图片 （附源码，模型与数据集）](https://blog.csdn.net/weixin_39274659/article/details/89459262)
