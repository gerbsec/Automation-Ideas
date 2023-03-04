while($true)
{
  $process = Get-WmiObject Win32_Process | Select-Object CommandLine
  Start-Sleep 1
  $process2 = Get-WmiObject Win32_Porcess | Select-Object CommandLine
  Compare-Object -ReferenceObject $process -DifferenceObject $process2
}
