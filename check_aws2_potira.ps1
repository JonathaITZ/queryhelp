$depsDir = "C:\Users\dantas.jonatha\.gemini\antigravity\scratch\deps"
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
    if (Test-Path $dll) { [System.Reflection.Assembly]::LoadFrom($dll) | Out-Null }
}

$connStr = "Server=softcomdb-mysql-prd-2-instance-1.cyv0220iwox9.us-east-1.rds.amazonaws.com;Port=3306;Uid=patrick.morais;Pwd=sq6j7dDW53pm;Connection Timeout=10;SslMode=None;CharacterSet=utf8mb4;"
$conn = New-Object MySql.Data.MySqlClient.MySqlConnection($connStr)
$conn.Open()
$cmd = $conn.CreateCommand()
$cmd.CommandText = "SHOW DATABASES LIKE '%potira%';"
$reader = $cmd.ExecuteReader()
while ($reader.Read()) {
    Write-Host "AWS2 Match: $($reader.GetString(0))"
}
$conn.Close()
