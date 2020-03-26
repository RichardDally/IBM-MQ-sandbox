# IBM-MQ-sandbox

- How to start server `start_server.sh`

- How to access server command line directly from live container:
   - Grab container id with `docker ps`
   - Connect with `docker exec -ti <your container id> /bin/bash`
   - Useful commands within shell:
       - Display MQ version `dspmqver`
       - Display your running queue managers `dspmq`
       - Display rights `dmpmqaut`
            - Example: `dspmqaut -m QM1 -t qmgr -p admin`

- How to connect to web console:
   - url: https://localhost:9443/ibmmq/console/
   - username: admin
   - password: passw0rd
   
- How to connect client to server `start_client.sh`
   - Type the host name or IP address for your queue manager: qmgr

Interesting stuff:
- https://developer.ibm.com/messaging/learn-mq/mq-tutorials/mq-connect-to-queue-manager/#docker
- https://github.com/ibm-messaging/mq-container
- https://bencane.com/2013/04/22/websphere-mq-cheat-sheet-for-system-administrators/
