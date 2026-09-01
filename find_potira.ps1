[System.Reflection.Assembly]::LoadFrom("C:\Users\dantas.jonatha\.gemini\antigravity\scratch\mysqldata8\lib\net48\MySql.Data.dll") | Out-Null

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
    }
)

foreach ($s in $servers) {
    Write-Host "========================================"
    Write-Host "Connecting to $($s.Name)..."
    $connStr = "Server=$($s.Host);Port=$($s.Port);Uid=$($s.User);Pwd=$($s.Pass);Connection Timeout=10;SslMode=None;CharacterSet=utf8mb4;"
    try {
        $conn = New-Object MySql.Data.MySqlClient.MySqlConnection($connStr)
        $conn.Open()
        Write-Host "Connected successfully to $($s.Name)!"
        
        $cmd = $conn.CreateCommand()
        $cmd.CommandText = "SHOW DATABASES LIKE '%potira%';"
        $reader = $cmd.ExecuteReader()
        $found = 0
        while ($reader.Read()) {
            $found++
            Write-Host "  -> DB Match (potira): $($reader.GetString(0))"
        }
        $reader.Close()

        $cmd2 = $conn.CreateCommand()
        $cmd2.CommandText = "SHOW DATABASES LIKE '%lanchonete%';"
        $reader2 = $cmd2.ExecuteReader()
        while ($reader2.Read()) {
            $found++
            Write-Host "  -> DB Match (lanchonete): $($reader2.GetString(0))"
        }
        $reader2.Close()

        if ($found -eq 0) {
            Write-Host "  No matching database found."
        }
        
        $conn.Close()
    } catch {
        Write-Host "Error on $($s.Name): $_"
    }
}
