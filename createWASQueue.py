#  
#  This script can be included in the wsadmin command invocation like this:
#     
#     /opt/IBM/WebSphere/AppServer/bin/wsadmin.sh -lang jython -user x_user_x1 -password xxxxxx -f /opt/IBM/WebSphere/xxxx/build/install/jython/configuration/sit3/createDcs2Queue.py
#
import sys
import java

def queue( name, jndiName, baseQueueName ):
  
   #--------------------------------------------------------------
   # set up globals
   #--------------------------------------------------------------
   global AdminConfig
   global template
   global mqjmsp
   
   #--------------------------------------------------------------
   # set up attributes
   #--------------------------------------------------------------   
   name = ['name', name]
   jndi = ['jndiName', jndiName]
   baseQN = ['baseQueueName', baseQueueName]   
   targetClient = ['targetClient', 'MQ']
   mqqAttrs = [name, jndi, baseQN, targetClient]
   print AdminConfig.createUsingTemplate('MQQueue', mqjmsp, mqqAttrs, template)

   #--------------------------------------------------------------
   # Save all the changes 
   #--------------------------------------------------------------



#-----------------------------------------------------------------
# Main
#-----------------------------------------------------------------

lineseparator = java.lang.System.getProperty('line.separator')
template = AdminConfig.listTemplates('MQQueue').split(lineseparator)[0]
print template

#mqjmsp = AdminConfig.getid('/ServerCluster:DCSCluster3/JMSProvider:WebSphere MQ JMS Provider')
mqjmsp = AdminConfig.getid('/ServerCluster:AutoDCSCluster3/JMSProvider:WebSphere MQ JMS Provider')
print mqjmsp


print "Start creating queue..."

#queue( 'CrossShipmentRequestSearchData', 'jms/CrossShipmentRequestSearchData', 'LQ.DCS.MCPE.PARTS.DPCA.DATA' )
queue( 'CrossShipmentRequestSearchData', 'jms/CrossShipmentRequestSearchData', 'LQ.DCS.AUTO.PARTS.EPCA.DATA' )


print "Finish creating queue..."

print "queue: saving the configuration"
AdminConfig.save()

print "script ended"

