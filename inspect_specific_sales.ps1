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

Write-Host "=== Detalhes das Parcelas das Vendas 57, 58, 59 ==="
$cmd = $conn.CreateCommand()
$cmd.CommandText = "SELECT * FROM financeiro_parcela WHERE venda_id IN (57, 58, 59);"
$reader = $cmd.ExecuteReader()
$dt = New-Object System.Data.DataTable
$dt.Load($reader)
$dt | Format-Table -AutoSize id, venda_id, empresa_id, parcela, valor_parcela, valor_pago, vencimento, data_pagamento, forma_pagamento_id, cancelada, deleted_at | Out-String | Write-Host

Write-Host "=== Detalhes das Notas Fiscais das Vendas 57, 58, 59 ==="
$cmd.CommandText = "SELECT id, empresa_id, numero_nfe, serie, total_nota_valor, recibo_situacao, mensagem_erro, data_hora_emissao FROM nota_fiscal_eletronica WHERE id IN (SELECT nfe_id FROM venda WHERE id IN (57, 58, 59));"
$reader2 = $cmd.ExecuteReader()
$dt2 = New-Object System.Data.DataTable
$dt2.Load($reader2)
$dt2 | Format-Table -AutoSize | Out-String | Write-Host

Write-Host "=== Detalhes das Vendas 57, 58, 59 ==="
$cmd.CommandText = "SELECT id, empresa_id, valor_total, total_pagamento, total_desconto, total_acrescimo, api_data_hora_venda, nfe_id FROM venda WHERE id IN (57, 58, 59);"
$reader3 = $cmd.ExecuteReader()
$dt3 = New-Object System.Data.DataTable
$dt3.Load($reader3)
$dt3 | Format-Table -AutoSize | Out-String | Write-Host

$conn.Close()
