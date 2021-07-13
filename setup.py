from setuptools import setup, find_packages

setup(
    name='yolov3_gh',
    version='1.0.0',
    url='https://github.com/Ghazali-telecom/yoylov3.git',
    author='ghazali',
    author_email='ghazali.yfm@gmail.com',
    description='Description of my package',
    packages=find_packages(),    
    install_requires=['numpy >=1.21.0','torch==1.9.0','torchvision==0.10.0','matplotlib ==3.4.2','tensorboard>=1.5.0','terminaltables==3.1.0'
    ,'pillow==8.3.1','tqdm==4.61.2','tensorflow-probability==0.13.0','tensorflow-gpu==2.4.1','pytorch-lightning==1.3.8'],
)