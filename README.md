这是优达学城毕业项目的开题报告

做的是“[猫狗大战](https://www.kaggle.com/c/dogs-vs-cats-redux-kernels-edition)”的项目



项目报告详见project_report.pdf

结果存储于：prediction/pred_test.csv


运行环境：Ubuntu 16.04.3 

opencv					3.3.0  (conda-forge )

h5py					2.7.1 

Keras					2.1.2 

matplotlib				2.1.0  

numpy					1.13.3 

pandas					0.21.0 

python					3.6.3 

scikit-learn				0.19.1                    

scipy					1.0.0

sklearn					0.0 

tensorflow-gpu			1.4.0              

tensorflow-tensorboard	0.4.0rc3



执行文件：

以阿拉伯数字开头的jupyter notebook文件为项目需要执行的文件：

1_img_split_and_move.ipynb

2_abnormal_img_detection.ipynb

3_delete_abnormal_img.ipynb

4_data_turbo_boost.ipynb

5_feature_extract.ipynb

6_features_train.ipynb

7_prediction_and_unload.ipynb



以report为开头的jupyter notebook文件为项目报告作图及过程中验证算法的辅助文件，不必执行

report_1_show_CNN.ipynb

report_2_change_brightness.ipynb



问题，数据处理时，异常值去除：

​	猫：

​	['cat.10700.jpg', 'cat.2150.jpg', 'cat.10636.jpg', 'cat.5351.jpg', 'cat.9090.jpg', 
	'cat.7968.jpg', 'cat.7564.jpg', 'cat.9290.jpg', 'cat.6345.jpg', 'cat.2939.jpg', 
	'cat.3672.jpg',   'cat.10536.jpg', 'cat.10365.jpg', 
	'cat.2663.jpg',  'cat.12227.jpg', 
	'cat.2520.jpg', 'cat.11184.jpg', 'cat.11565.jpg', 
	'cat.2337.jpg', 'cat.12272.jpg', 
	'cat.5418.jpg', 'cat.4338.jpg',  'cat.5583.jpg', 
	'cat.8921.jpg', 'cat.7377.jpg', 'cat.5820.jpg', 'cat.372.jpg', 
	'cat.10712.jpg', 'cat.9552.jpg', 'cat.9171.jpg', 'cat.2457.jpg', 'cat.4986.jpg', 
	'cat.4308.jpg', 'cat.8456.jpg']

​	狗：

​	['dog.11299.jpg', 'dog.9681.jpg',  'dog.1043.jpg', 'dog.5336.jpg', 
	'dog.8736.jpg', 'dog.11437.jpg', 'dog.4367.jpg', 'dog.1259.jpg', 
	'dog.5604.jpg',  'dog.10190.jpg', 'dog.10161.jpg', 'dog.4507.jpg', 
	'dog.3035.jpg', 'dog.6725.jpg', 'dog.9418.jpg', 'dog.729.jpg', 'dog.59.jpg', 
	'dog.1773.jpg', 'dog.7076.jpg', 'dog.4218.jpg', 'dog.1194.jpg', 
	'dog.2422.jpg', 'dog.9517.jpg', 'dog.1895.jpg', 'dog.10801.jpg', 'dog.12376.jpg', 
	'dog.6405.jpg', 'dog.10747.jpg', 'dog.6475.jpg',  'dog.2614.jpg', 
	'dog.10237.jpg',  'dog.3497.jpg', 'dog.11266.jpg']







