from rhel8/python-36
RUN yum install python3 python3-pip \
    && pip3 install --upgrade pip --trusted-host pypi.python.org --trusted-host pypi.org --trusted-host files.pythonhosted.org --index-url https://pypi.python.org/simple

WORKDIR /app
COPY . /app

RUN pip3 --no-cache-dir install -r requirements.txt --trusted-host pypi.python.org --trusted-host pypi.org --trusted-host files.pythonhosted.org --index-url https://pypi.python.org/simple

EXPOSE 5000

ENTRYPOINT ["python3"]
CMD ["helloworld.py"]
