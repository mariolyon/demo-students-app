FROM node:latest

WORKDIR /app

ENV PATH /app/node_modules/.bin:$PATH

RUN yarn global add serve

COPY build /app

EXPOSE 3000
CMD ["serve", "-s", "build", "-l", "3000"]
