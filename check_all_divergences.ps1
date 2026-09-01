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

Write-Host "=== Todas as vendas com divergencia de valor na base ==="
$cmd = $conn.CreateCommand()
$cmd.CommandText = @"
SELECT 
    v.id AS venda_id,
    v.valor_total AS venda_valor_total,
    v.total_pagamento AS venda_total_pagamento,
    COALESCE(SUM(fp.valor_parcela), 0) AS total_parcelas,
    ROUND(v.valor_total - COALESCE(SUM(fp.valor_parcela), 0), 4) AS dif_parcela,
    nfe.id AS nfe_id,
    nfe.numero_nfe,
    nfe.recibo_situacao,
    nfe.mensagem_erro
FROM venda v
LEFT JOIN nota_fiscal_eletronica nfe ON v.nfe_id = nfe.id
LEFT JOIN financeiro_parcela fp ON fp.venda_id = v.id AND (fp.deleted_at IS NULL)
WHERE v.deleted_at IS NULL
GROUP BY v.id, v.valor_total, v.total_pagamento, nfe.id, nfe.numero_nfe, nfe.recibo_situacao, nfe.mensagem_erro
HAVING ABS(v.valor_total - COALESCE(SUM(fp.valor_parcela), 0)) > 0.001
   OR ABS(v.valor_total - v.total_pagamento) > 0.001;
"@

$r = $cmd.ExecuteReader()
$divergencias = @()
while ($r.Read()) {
    $divergencias += [PSCustomObject]@{
        VendaId = $r['venda_id']
        VendaTotal = $r['venda_valor_total']
        VendaTotalPagamento = $r['venda_total_pagamento']
        TotalParcelas = $r['total_parcelas']
        DifParcela = $r['dif_parcela']
        NfeNumero = $r['numero_nfe']
        NfeSituacao = $r['recibo_situacao']
        NfeErro = $r['mensagem_erro']
    }
}
$r.Close()

Write-Host "Total de vendas com divergência: $($divergencias.Count)"
$divergencias | Format-Table -AutoSize | Out-String | Write-Host

$conn.Close()
