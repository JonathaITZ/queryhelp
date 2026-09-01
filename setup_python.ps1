[Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::Tls12
$pyDir = 'C:\Users\dantas.jonatha\.gemini\antigravity\scratch\python'
if (-not (Test-Path $pyDir)) { New-Item -ItemType Directory -Path $pyDir -Force | Out-Null }

$zipPath = 'C:\Users\dantas.jonatha\.gemini\antigravity\scratch\python_embed.zip'
if (-not (Test-Path "$pyDir\python.exe")) {
    Write-Host 'Downloading Python Embeddable 3.11.9...'
    Invoke-WebRequest -Uri 'https://www.python.org/ftp/python/3.11.9/python-3.11.9-embed-amd64.zip' -OutFile $zipPath
    Expand-Archive -Path $zipPath -DestinationPath $pyDir -Force
}

$pthFile = Get-ChildItem -Path $pyDir -Filter '*._pth' | Select-Object -First 1
if ($pthFile) {
    $content = Get-Content $pthFile.FullName
    $content = $content -replace '#import site', 'import site'
    Set-Content -Path $pthFile.FullName -Value $content
}

$getPip = "$pyDir\get-pip.py"
if (-not (Test-Path $getPip)) {
    Write-Host 'Downloading get-pip.py...'
    Invoke-WebRequest -Uri 'https://bootstrap.pypa.io/get-pip.py' -OutFile $getPip
    Write-Host 'Installing pip...'
    & "$pyDir\python.exe" $getPip --no-warn-script-location
}

Write-Host 'Installing PyMySQL, cryptography, tabulate...'
& "$pyDir\python.exe" -m pip install pymysql cryptography tabulate --no-warn-script-location

Write-Host 'Testing Python + PyMySQL...'
& "$pyDir\python.exe" -c "import pymysql; print('Python + PyMySQL ready and working!')"
