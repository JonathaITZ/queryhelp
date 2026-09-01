$depsDir = "C:\Users\dantas.jonatha\.gemini\antigravity\scratch\deps"

# Load dependencies in proper order
$dlls = @(
    "$depsDir\System.Runtime.CompilerServices.Unsafe\lib\net462\System.Runtime.CompilerServices.Unsafe.dll",
    "$depsDir\System.Buffers\lib\net461\System.Buffers.dll",
    "$depsDir\System.Numerics.Vectors\lib\net46\System.Numerics.Vectors.dll",
    "$depsDir\System.Memory\lib\net461\System.Memory.dll",
    "$depsDir\System.Threading.Tasks.Extensions\lib\net461\System.Threading.Tasks.Extensions.dll",
    "$depsDir\Microsoft.Bcl.AsyncInterfaces\lib\net462\Microsoft.Bcl.AsyncInterfaces.dll",
    "$depsDir\System.Diagnostics.DiagnosticSource\lib\net462\System.Diagnostics.DiagnosticSource.dll",
    "$depsDir\Google.Protobuf\lib\net45\Google.Protobuf.dll",
    "$depsDir\K4os.Hash.xxHash\lib\net462\K4os.Hash.xxHash.dll",
    "$depsDir\K4os.Compression.LZ4\lib\net462\K4os.Compression.LZ4.dll",
    "$depsDir\K4os.Compression.LZ4.Streams\lib\net462\K4os.Compression.LZ4.Streams.dll",
    "$depsDir\BouncyCastle.Cryptography\lib\net461\BouncyCastle.Cryptography.dll",
    "C:\Users\dantas.jonatha\.gemini\antigravity\scratch\mysqldata8\lib\net48\MySql.Data.dll"
)

foreach ($dll in $dlls) {
    if (Test-Path $dll) {
        [System.Reflection.Assembly]::LoadFrom($dll) | Out-Null
    } else {
        Write-Host "Not found: $dll"
    }
}

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
    Write-Host "Connecting to $($s.Name) at $($s.Host)..."
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
