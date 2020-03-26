docker run \
  --env LICENSE=accept \
  --env MQ_QMGR_NAME=QM1 \
  --network mq-demo-network \
  --network-alias qmgr \
  --publish 1414:1414 \
  --publish 9443:9443 \
  richarddally/ibmmqclient:latest
  #ibmcom/mq

#  --detach \
#  --volume qm1data:/mnt/mqm \
