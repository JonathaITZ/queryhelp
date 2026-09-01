try {
    [System.Reflection.Assembly]::LoadFrom("C:\Users\dantas.jonatha\.gemini\antigravity\scratch\mysqldata8\lib\net48\MySql.Data.dll")
    Write-Host "Loaded successfully!"
} catch [System.Reflection.ReflectionTypeLoadException] {
    Write-Host "TypeLoadException:"
    $_.Exception.LoaderExceptions | ForEach-Object { Write-Host " - " $_.Message }
} catch {
    Write-Host "Other exception:" $_.Exception.Message
}
