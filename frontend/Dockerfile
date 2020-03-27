FROM alpine

RUN apk add --update nodejs
RUN apk add --update yarn

RUN yarn global add serve

WORKDIR /app
COPY build ./build

EXPOSE 3000
CMD ["serve", "-s", "/app/build", "-l", "3000"]
