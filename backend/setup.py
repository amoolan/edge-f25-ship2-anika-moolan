from setuptools import setup, find_packages

setup(
    name="backend",
    version="0.0.1",
    packages=find_packages(),
    install_requires=[
        "fastapi",
        "uvicorn[standard]",
        "pydantic"
    ],
    extras_require={
        "dev": ["pytest", "httpx"]
    },
)