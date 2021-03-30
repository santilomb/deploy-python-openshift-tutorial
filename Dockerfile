from rhel8/python-36
RUN pip3 install --upgrade pip --trusted-host pypi.python.org --trusted-host pypi.org --trusted-host files.pythonhosted.org --index-url https://pypi.python.org/simple

WORKDIR /app
COPY . /app
RUN touch /tmp/chat.txt

RUN pip3 --no-cache-dir install -r requirements.txt --trusted-host pypi.python.org --trusted-host pypi.org --trusted-host files.pythonhosted.org --index-url https://pypi.python.org/simple

EXPOSE 5000

ENTRYPOINT ["python3"]
CMD ["chat-server.py"]
