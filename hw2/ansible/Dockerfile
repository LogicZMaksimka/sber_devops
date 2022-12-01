FROM alpine:3.11
RUN apk add --no-cache bash openssh-client ansible git sshpass
RUN mkdir -p /root/.ssh
RUN echo "HOST *" > /root/.ssh/config && echo " StrictHostKeyChecking no" >> /root/.ssh/config
WORKDIR /ansible
COPY . .
CMD [ "" ]