Add-Type -Path "C:\Users\dantas.jonatha\.gemini\antigravity\scratch\mysqldata\lib\net45\MySql.Data.dll"

$servers = @(
    @{
        Name = "AWS2 (RDS PRD 2)"
        Host = "softcomdb-mysql-prd-2-instance-1.cyv0220iwox9.us-east-1.rds.amazonaws.com"
        User = "patrick.morais"
        Pass = "sq6j7dDW53pm"
        Port = 3306
    },
    @{
        Name = "AWS (RDS HML)"
        Host = "softcomdb-mysql-hml.cluster-cyv0220iwox9.us-east-1.rds.amazonaws.com"
        User = "patrick.morais"
        Pass = "sq6j7dDW53pm"
        Port = 3306
    },
    @{
        Name = "Softcomshop"
        Host = "softcomsistemas.com.br"
        User = "n2_gestor"
        Pass = "qMifoz98"
        Port = 3306
    },
    @{
        Name = "GLAÇAI"
        Host = "glacai.com.br"
        User = "especialistas-patrick"
        Pass = "Bz0R870a_OL17qMN"
        Port = 3306
    }
)

foreach ($s in $servers) {
    Write-Host "----------------------------------------"
    Write-Host "Connecting to $($s.Name) at $($s.Host)..."
    $connStr = "Server=$($s.Host);Port=$($s.Port);Uid=$($s.User);Pwd=$($s.Pass);Connection Timeout=10;SslMode=None;"
    try {
        $conn = New-Object MySql.Data.MySqlClient.MySqlConnection($connStr)
        $conn.Open()
        Write-Host "Connected successfully to $($s.Name)!"
        
        $cmd = $conn.CreateCommand()
        $cmd.CommandText = "SHOW DATABASES LIKE '%potira%';"
        $reader = $cmd.ExecuteReader()
        $found = $false
        while ($reader.Read()) {
            $found = $true
            Write-Host "FOUND DATABASE: $($reader.GetString(0))"
        }
        $reader.Close()
        if (-not $found) {
            Write-Host "No database matching '%potira%' found on $($s.Name)."
        }
        $conn.Close()
    } catch {
        Write-Host "Error connecting to $($s.Name): $_"
    }
}
