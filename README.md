# IBM-MQ-sandbox

- How to build containers
   - `build_ibm_mq_server.sh` image tweaked from official IBM MQ Server (to add additional user)
   - `build_ibm_mq_client.sh` image based on [pymqi](https://github.com/RichardDally/pymqi)

- How to publish to Docker Hub
   - Select the right image to tag `docker images`
   - Tag image `docker tag <IMAGE ID> richarddally/ibm_mq_client:latest`
   - Publish `docker push richarddally/ibm_mq_client`

- How to start IBM MQ Server within Docker `start_ibm_mq_server.sh`

- How to access server command line directly from live container:
   - Grab container id with `docker ps`
   - Connect with `docker exec -ti <your container id> /bin/bash`
   - Useful commands within shell:
       - Display MQ version `dspmqver`
       - Display your running queue managers `dspmq`
       - Display rights `dmpmqaut`
            - Example: `dspmqaut -m QM1 -t qmgr -p admin`

- How to debug your container from bash within:
   - `docker run -it --entrypoint /bin/bash richarddally/ibm_mq_client:latest -s`

- How to connect to web console:
   - url: https://localhost:9443/ibmmq/console/
   - username: admin
   - password: passw0rd

- How to connect client to server `start_ibm_mq_client.sh`
   - Type the host name or IP address for your queue manager: qmgr

Interesting stuff:
- https://developer.ibm.com/messaging/learn-mq/mq-tutorials/mq-connect-to-queue-manager/#docker
- https://github.com/ibm-messaging/mq-container
- https://bencane.com/2013/04/22/websphere-mq-cheat-sheet-for-system-administrators/
