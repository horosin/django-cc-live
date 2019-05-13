FROM node:10-alpine

WORKDIR /usr/src/app

# install and cache app dependencies
COPY package.json .
RUN npm install --silent

# copy app files
COPY . . 

# start app
CMD ["npm", "start"]
