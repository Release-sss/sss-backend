FROM node:14-alpine

WORKDIR /streaming

COPY package*.json ./
RUN yarn

COPY . .

EXPOSE 3030

CMD ["yarn", "start"]
