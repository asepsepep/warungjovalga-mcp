from setuptools import setup, find_packages

setup(
    name="warungjovalga-mcp",
    version="1.0.0",
    description="Official Model Context Protocol (MCP) server & LangChain tool for Warung Jovalga x402 AI micro-services on Base L2",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    author="PapiJo Corporation",
    url="https://github.com/asepsepep/warungjovalga-mcp",
    packages=find_packages(),
    install_requires=[],
    extras_require={
        "langchain": ["langchain>=0.1.0", "pydantic>=2.0.0"]
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
)
