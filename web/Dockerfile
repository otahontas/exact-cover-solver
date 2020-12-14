# Build frontend
FROM node:14.15.1-alpine3.12 as build

WORKDIR /app

COPY ui/package.json ./
COPY ui/yarn.lock ./

RUN yarn install --frozen-lockfile

COPY ui/src/ ./src
COPY ui/public/ ./public

RUN yarn run build
















#  # Install python and pip
#  RUN apk add --no-cache --update python3 py3-pip bash
#  ADD ./webapp/requirements.txt /tmp/requirements.txt
#  
#  # Install dependencies
#  RUN pip3 install --no-cache-dir -q -r /tmp/requirements.txt
#  
#  # Add our code
#  ADD ./webapp /opt/webapp/
#  WORKDIR /opt/webapp
#  
#  # Expose is NOT supported by Heroku
#  # EXPOSE 5000 		
#  
#  # Run the image as a non-root user
#  RUN adduser -D myuser
#  USER myuser
#  
#  # Run the app.  CMD is required to run on Heroku
#  # $PORT is set by Heroku			
#  CMD gunicorn --bind 0.0.0.0:$PORT wsgi 
#  
