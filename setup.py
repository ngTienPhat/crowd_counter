import platform

from setuptools import find_packages, setup, find_namespace_packages


def torch_urls(version):
    platform_system = platform.system()
    if platform_system == "Windows":
        return f"torch@https://download.pytorch.org/whl/cu90/torch-{version}-cp36-cp36m-win_amd64.whl#"
    return f"torch>={version}"


setup(
    name="crowd-counter",
    version="v0.0.1",
    description="Backend for final project of Software Design",
    author="Nguyen Tien Phat & Tran Vinh Hung",
    url="https://github.com/ngTienPhat/crowd_counter/",
    packages=find_namespace_packages(
        exclude=["docs", "tests", "experiments", "scripts"]
    ),
    include_package_data=True,
    zip_safe=True,
    python_requires=">=3.6",
    install_requires=["numpy", "Pillow", "opencv-python", "tqdm", "yacs"],
    extras_require={
        "sanet": [
            "keras",
            # "git+https://www.github.com/keras-team/keras-contrib.git",
            "scikit-image",
        ]
    },
)
