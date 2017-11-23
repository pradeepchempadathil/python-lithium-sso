from setuptools import setup


setup(
   name="python-lithium-sso",
   version="0.1",
   description="Python Client for Lithium SSO Integration",
   author="Pradeep Chempadathil",
   author_email="pradeepchempadathil@gmail.com",
   package_dir={"": "src"},
   packages = ["pylithium"],
   py_modules=["pylithium.client"],
   url="",
   install_requires=["pycryptodomex==3.4.7"]
)