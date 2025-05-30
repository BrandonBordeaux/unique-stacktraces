# Unique Stacks Project

Finds Java stack traces in logs and reports on unique stacks and the number of them found.

Usage:

```bash
python main.py -h
usage: main.py [-h] [-f FILE] [-d]

Finds unique Java stack traces in a log file and counts their occurrences.

options:
  -h, --help            show this help message and exit
  -f FILE, --file FILE  log file
  -d, --debug           enable debug output
```


Sample output:
```
======================================================
Count: 1255
Stack:
org.apache.cassandra.exceptions.UnavailableException: Cannot achieve consistency level ONE
        at org.apache.cassandra.exceptions.UnavailableException.create(UnavailableException.java:37)
        at org.apache.cassandra.locator.ReplicaPlans.assureSufficientLiveReplicas(ReplicaPlans.java:169)
        at org.apache.cassandra.locator.ReplicaPlans.assureSufficientLiveReplicasForWrite(ReplicaPlans.java:112)
        at org.apache.cassandra.locator.ReplicaPlans.forWrite(ReplicaPlans.java:353)
        at org.apache.cassandra.locator.ReplicaPlans.forWrite(ReplicaPlans.java:344)
        at org.apache.cassandra.locator.ReplicaPlans.forWrite(ReplicaPlans.java:338)
        at org.apache.cassandra.service.StorageProxy.wrapViewBatchResponseHandler(StorageProxy.java:1417)
        at org.apache.cassandra.service.StorageProxy.mutateMV(StorageProxy.java:1077)
        at org.apache.cassandra.db.view.TableViews.pushViewReplicaUpdates(TableViews.java:169)
        at org.apache.cassandra.db.Keyspace.applyInternal(Keyspace.java:645)
        at org.apache.cassandra.db.Keyspace.applyFuture(Keyspace.java:476)
        at org.apache.cassandra.db.Mutation.applyFuture(Mutation.java:223)
        at org.apache.cassandra.hints.Hint.applyFuture(Hint.java:109)
        at org.apache.cassandra.hints.HintVerbHandler.doVerb(HintVerbHandler.java:97)
        at org.apache.cassandra.net.InboundSink.lambda$new$0(InboundSink.java:78)
        at org.apache.cassandra.net.InboundSink.accept(InboundSink.java:97)
        at org.apache.cassandra.net.InboundSink.accept(InboundSink.java:45)
        at org.apache.cassandra.net.InboundMessageHandler$ProcessMessage.run(InboundMessageHandler.java:430)
        at org.apache.cassandra.concurrent.ExecutionFailure$1.run(ExecutionFailure.java:133)
        at org.apache.cassandra.concurrent.SEPWorker.run(SEPWorker.java:142)
        at io.netty.util.concurrent.FastThreadLocalRunnable.run(FastThreadLocalRunnable.java:30)
        at java.base/java.lang.Thread.run(Unknown Source)
======================================================
Count: 461
Stack:
org.apache.cassandra.exceptions.UnavailableException: Cannot achieve consistency level ONE
        at org.apache.cassandra.exceptions.UnavailableException.create(UnavailableException.java:37)
        at org.apache.cassandra.locator.ReplicaPlans.assureSufficientLiveReplicas(ReplicaPlans.java:169)
        at org.apache.cassandra.locator.ReplicaPlans.assureSufficientLiveReplicasForWrite(ReplicaPlans.java:112)
        at org.apache.cassandra.locator.ReplicaPlans.forWrite(ReplicaPlans.java:353)
        at org.apache.cassandra.locator.ReplicaPlans.forWrite(ReplicaPlans.java:344)
        at org.apache.cassandra.locator.ReplicaPlans.forWrite(ReplicaPlans.java:338)
        at org.apache.cassandra.service.StorageProxy.wrapViewBatchResponseHandler(StorageProxy.java:1417)
        at org.apache.cassandra.service.StorageProxy.mutateMV(StorageProxy.java:1077)
        at org.apache.cassandra.db.view.TableViews.pushViewReplicaUpdates(TableViews.java:169)
        at org.apache.cassandra.db.Keyspace.applyInternal(Keyspace.java:645)
        at org.apache.cassandra.db.Keyspace.applyFuture(Keyspace.java:476)
        at org.apache.cassandra.db.Mutation.applyFuture(Mutation.java:223)
        at org.apache.cassandra.db.MutationVerbHandler.doVerb(MutationVerbHandler.java:54)
        at org.apache.cassandra.net.InboundSink.lambda$new$0(InboundSink.java:78)
        at org.apache.cassandra.net.InboundSink.accept(InboundSink.java:97)
        at org.apache.cassandra.net.InboundSink.accept(InboundSink.java:45)
        at org.apache.cassandra.net.InboundMessageHandler$ProcessMessage.run(InboundMessageHandler.java:430)
        at org.apache.cassandra.concurrent.ExecutionFailure$1.run(ExecutionFailure.java:133)
        at org.apache.cassandra.concurrent.SEPWorker.run(SEPWorker.java:142)
        at io.netty.util.concurrent.FastThreadLocalRunnable.run(FastThreadLocalRunnable.java:30)

```
