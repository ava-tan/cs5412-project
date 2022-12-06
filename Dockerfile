# pull down the most recent docker image
FROM python:3.8.0 

# creating our active directory
WORKDIR /user/src/app

# copying over requirements necessary for this file to run from venv
COPY './requirements.txt' .
RUN pip install -r requirements.txt

# copy over the app (app.py) and run
COPY . . 
ENTRYPOINT [ "python", "app.py"]