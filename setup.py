from setuptools import setup, Extension

setup(
    ext_modules=[
        Extension(
            'example',
            sources=['video-encoder/cpp/main.cpp'],
            include_dirs=[
                '/venv/Lib/pybind11',
            ],  # Укажите путь к pybind11
            # library_dirs=[
            #     'C:/Users/user/opencv2/opencv/build/x64/vc16/lib'  # Путь к библиотекам OpenCV на Windows
            # ],
            # libraries=[
            #     'opencv_world420',  # Проверьте версию и название вашей библиотеки
            # ],
            language='c++'
        ),
    ],
)
