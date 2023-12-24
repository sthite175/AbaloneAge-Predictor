FROM continuumio/anaconda3:latest
# Copy from current directory to home folder
COPY . /home  
# Now home is our working directory     
WORKDIR /home

# If you need to upgrade pip, you can uncomment the following line
RUN pip install --upgrade pip
RUN conda install --file requirements.txt

EXPOSE 8888

CMD ["python", "app.py"]

