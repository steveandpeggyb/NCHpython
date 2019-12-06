import sys
import psutil
import win32service
import win32serviceutil

STOPPED = 1

target = 'ReportServer$DEVSERVER'
def getService(name): 
        service = None
        try:
            service = psutil.win_service_get(name)
            service = service.as_dict()
        except Exception as ex:
            print(str(ex))
        return service

# In Windows Services, double-click the service. In the dialog box, use the "Service name:"
service = getService(target)

print('\r\nThe "' + target + '" service is ' +  service['status'] + '.')

# if service['status'] == 'stopped':
#     win32serviceutil.RestartService(target)
# service = getService(target)
# print('\r\nAfter trying to restart, the "' + target + '" service is ' +  service['status'] + '.')
