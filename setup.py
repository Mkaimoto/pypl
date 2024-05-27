from setuptools import setup, find_packages
import os
current_directory = os.path.abspath(os.path.dirname(__file__))

# READMEファイルを読み込む関数
def read_readme():
    with open(os.path.join(current_directory, 'README.md'), encoding='utf-8') as f:
        return f.read()
setup(
    name='maesyorikun',
    version='0.1.3',
    description='This app can interactively preprocess and graph CSV data.',
    long_description=read_readme(),  # ここを追加
    long_description_content_type='text/markdown',  # ここを追加
    author='Makimoto-eita',
    author_email='s2222034@stu.musashino-u.ac.jp',
    packages=find_packages(),
    install_requires=[
        'pandas',
        'matplotlib',
        'seaborn',
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.8',
)


