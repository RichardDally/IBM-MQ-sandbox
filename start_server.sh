docker run \
  --env LICENSE=accept \
  --env MQ_QMGR_NAME=QM1 \
  --network mq-demo-network \
  --publish 1414:1414 \
  --publish 9443:9443 \
  ibmcom/mq

#  --detach \
#  --volume qm1data:/mnt/mqm \
