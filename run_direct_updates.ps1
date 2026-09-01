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

$sqlStatements = @(
    "UPDATE financeiro_parcela SET valor_parcela = 26.0100, valor_pago = 26.0100 WHERE id = 121 AND venda_id = 57;",
    "UPDATE financeiro_parcela SET valor_parcela = 23.0100, valor_pago = 23.0100 WHERE id = 122 AND venda_id = 58;",
    "UPDATE financeiro_parcela SET valor_parcela = 18.5100, valor_pago = 18.5100 WHERE id = 123 AND venda_id = 59;",

    "UPDATE financeiro_parcela_pagamento SET valor_pago = 26.0100, valor_recebido = 26.0100 WHERE id = 17 AND financeiro_parcela_id = 121;",
    "UPDATE financeiro_parcela_pagamento SET valor_pago = 23.0100, valor_recebido = 23.0100 WHERE id = 18 AND financeiro_parcela_id = 122;",
    "UPDATE financeiro_parcela_pagamento SET valor_pago = 18.5100, valor_recebido = 18.5100 WHERE id = 19 AND financeiro_parcela_id = 123;",

    "UPDATE venda SET total_pagamento = 26.01 WHERE id = 57;",
    "UPDATE venda SET total_pagamento = 23.01 WHERE id = 58;",
    "UPDATE venda SET total_pagamento = 18.51 WHERE id = 59;"
)

foreach ($sql in $sqlStatements) {
    $cmd = $conn.CreateCommand()
    $cmd.CommandText = $sql
    $affected = $cmd.ExecuteNonQuery()
    Write-Host "Executado: $sql (Linhas afetadas: $affected)"
}

Write-Host "`n=== CONFERENCIA FINAL ==="
$cmdCheck = $conn.CreateCommand()
$cmdCheck.CommandText = @"
SELECT 
    v.id AS venda_id,
    v.valor_total AS venda_total,
    v.total_pagamento AS venda_pagamento,
    fp.id AS parcela_id,
    fp.valor_parcela,
    fp.valor_pago AS parcela_pago,
    fpp.id AS fpp_id,
    fpp.valor_pago AS fpp_pago,
    ROUND(v.valor_total - fp.valor_parcela, 4) AS dif_parcela,
    ROUND(v.valor_total - v.total_pagamento, 4) AS dif_pagto
FROM venda v
INNER JOIN financeiro_parcela fp ON fp.venda_id = v.id
INNER JOIN financeiro_parcela_pagamento fpp ON fpp.financeiro_parcela_id = fp.id
WHERE v.id IN (57, 58, 59)
ORDER BY v.id;
"@

$r = $cmdCheck.ExecuteReader()
$results = @()
while ($r.Read()) {
    $results += [PSCustomObject]@{
        VendaID = $r["venda_id"]
        ValorTotalVenda = $r["venda_total"]
        TotalPagamentoVenda = $r["venda_pagamento"]
        ParcelaID = $r["parcela_id"]
        ValorParcela = $r["valor_parcela"]
        ValorPagoParcela = $r["parcela_pago"]
        PagamentoID = $r["fpp_id"]
        ValorPagoPagamento = $r["fpp_pago"]
        DifParcela = $r["dif_parcela"]
        DifPagto = $r["dif_pagto"]
    }
}
$r.Close()

$results | Format-Table -AutoSize | Out-String | Write-Host

$conn.Close()
