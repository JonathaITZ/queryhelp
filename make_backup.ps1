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

$connStr = "Server=softcomdb-mysql-hml.cluster-cyv0220iwox9.us-east-1.rds.amazonaws.com;Port=3306;Database=softcoms_softcomshop_lanchoneteerestaurantepotira;Uid=patrick.morais;Pwd=sq6j7dDW53pm;Connection Timeout=10;SslMode=None;CharacterSet=utf8mb4;Convert Zero Datetime=True;Allow Zero Datetime=True;"
$conn = New-Object MySql.Data.MySqlClient.MySqlConnection($connStr)
$conn.Open()

$backupFile = "C:\Users\dantas.jonatha\.gemini\antigravity\scratch\backup_potira_contingencias_$(Get-Date -Format 'yyyyMMdd_HHmmss').sql"
$sb = New-Object System.Text.StringBuilder
[void]$sb.AppendLine('-- BACKUP DE SEGURANCA ANTES DO AJUSTE DAS VENDAS EM CONTINGENCIA')
[void]$sb.AppendLine("-- Data/Hora: $(Get-Date -Format 'yyyy-MM-dd HH:mm:ss')")
[void]$sb.AppendLine('-- Banco: softcoms_softcomshop_lanchoneteerestaurantepotira')
[void]$sb.AppendLine('')

$tablesToBackup = @(
    @{ Table = "financeiro_parcela"; Query = "SELECT * FROM financeiro_parcela WHERE venda_id IN (57, 58, 59);" },
    @{ Table = "financeiro_parcela_pagamento"; Query = "SELECT * FROM financeiro_parcela_pagamento WHERE financeiro_parcela_id IN (121, 122, 123);" },
    @{ Table = "venda"; Query = "SELECT * FROM venda WHERE id IN (57, 58, 59);" },
    @{ Table = "nota_fiscal_eletronica"; Query = "SELECT * FROM nota_fiscal_eletronica WHERE id IN (57, 58, 59);" }
)

foreach ($t in $tablesToBackup) {
    $tbl = $t.Table
    [void]$sb.AppendLine('-- ===================================================')
    [void]$sb.AppendLine("-- Tabela: $tbl")
    [void]$sb.AppendLine('-- ===================================================')
    $cmd = $conn.CreateCommand()
    $cmd.CommandText = $t.Query
    $reader = $cmd.ExecuteReader()
    
    $cols = @()
    for ($i = 0; $i -lt $reader.FieldCount; $i++) {
        $colName = $reader.GetName($i)
        $cols += ('`' + $colName + '`')
    }
    $colList = $cols -join ', '
    
    while ($reader.Read()) {
        $vals = @()
        for ($i = 0; $i -lt $reader.FieldCount; $i++) {
            if ($reader.IsDBNull($i)) {
                $vals += 'NULL'
            } else {
                $val = $reader.GetValue($i).ToString()
                $valEscaped = $val.Replace("'", "''")
                $vals += ("'" + $valEscaped + "'")
            }
        }
        $valList = $vals -join ', '
        $insertLine = [string]::Format('INSERT INTO `{0}` ({1}) VALUES ({2});', $tbl, $colList, $valList)
        [void]$sb.AppendLine($insertLine)
    }
    $reader.Close()
    [void]$sb.AppendLine('')
}

[System.IO.File]::WriteAllText($backupFile, $sb.ToString(), [System.Text.Encoding]::UTF8)
Write-Host "Backup gerado com sucesso em: $backupFile"

$conn.Close()
