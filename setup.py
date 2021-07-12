from setuptools import setup, find_packages

setup(
    name='yolov3_gh',
    version='1.0.0',
    url='https://github.com/Ghazali-telecom/yoylov3.git',
    author='ghazali',
    author_email='ghazali.yfm@gmail.com',
    description='Description of my package',
    packages=find_packages(),    
    install_requires=['numpy >=1.21.0','torch>=1.0','torchvision==0.10.0','matplotlib >=3.4.2','tensorflow==1.15','tensorboard>=2.5.0','terminaltables>=3.1.0'
    ,'pillow>=8.3.1','tqdm>=4.61.2'],
)