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

$connStr = "Server=softcomdb-mysql-hml.cluster-cyv0220iwox9.us-east-1.rds.amazonaws.com;Port=3306;Database=softcoms_softcomshop_lanchoneteerestaurantepotira;Uid=patrick.morais;Pwd=sq6j7dDW53pm;Connection Timeout=10;SslMode=None;CharacterSet=utf8mb4;"
$conn = New-Object MySql.Data.MySqlClient.MySqlConnection($connStr)
$conn.Open()

# Check tables with pagamento or nfe
$cmd = $conn.CreateCommand()
$cmd.CommandText = "SHOW TABLES LIKE '%pagamento%';"
$r = $cmd.ExecuteReader()
Write-Host "Tabelas de pagamento:"
while ($r.Read()) {
    Write-Host " - $($r.GetString(0))"
}
$r.Close()

$cmd.CommandText = "SHOW TABLES LIKE '%venda%';"
$r2 = $cmd.ExecuteReader()
Write-Host "`nTabelas de venda:"
while ($r2.Read()) {
    Write-Host " - $($r2.GetString(0))"
}
$r2.Close()

# Check nota_fiscal_eletronica_forma_pagamento
$cmd.CommandText = "SELECT * FROM information_schema.tables WHERE table_schema = 'softcoms_softcomshop_lanchoneteerestaurantepotira' AND table_name = 'nota_fiscal_eletronica_forma_pagamento';"
$hasNfeFp = ($cmd.ExecuteScalar() -ne $null)
if ($hasNfeFp) {
    Write-Host "`nRegistros em nota_fiscal_eletronica_forma_pagamento para NFe 57, 58, 59:"
    $cmd.CommandText = "SELECT * FROM nota_fiscal_eletronica_forma_pagamento WHERE nota_fiscal_eletronica_id IN (57, 58, 59);"
    $r3 = $cmd.ExecuteReader()
    $dt = New-Object System.Data.DataTable
    $dt.Load($r3)
    $dt | Format-Table -AutoSize | Out-String | Write-Host
}

# Check financeiro_parcela_pagamento
$cmd.CommandText = "SELECT * FROM information_schema.tables WHERE table_schema = 'softcoms_softcomshop_lanchoneteerestaurantepotira' AND table_name = 'financeiro_parcela_pagamento';"
$hasFpp = ($cmd.ExecuteScalar() -ne $null)
if ($hasFpp) {
    Write-Host "`nRegistros em financeiro_parcela_pagamento para parcelas 121, 122, 123:"
    $cmd.CommandText = "SELECT * FROM financeiro_parcela_pagamento WHERE financeiro_parcela_id IN (121, 122, 123);"
    $r4 = $cmd.ExecuteReader()
    $dt2 = New-Object System.Data.DataTable
    $dt2.Load($r4)
    $dt2 | Format-Table -AutoSize | Out-String | Write-Host
}

$conn.Close()
