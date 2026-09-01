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

Write-Host "=== nota_fiscal_eletronica_forma_pagamento ==="
$cmd = $conn.CreateCommand()
$cmd.CommandText = "SELECT * FROM nota_fiscal_eletronica_forma_pagamento WHERE nota_fiscal_eletronica_id IN (57, 58, 59);"
$r = $cmd.ExecuteReader()
while ($r.Read()) {
    Write-Host "ID: $($r['id']) | NFe_ID: $($r['nota_fiscal_eletronica_id']) | FormaPagamentoID: $($r['forma_pagamento_id']) | Valor: $($r['valor'])"
}
$r.Close()

Write-Host "`n=== financeiro_parcela_pagamento ==="
$cmd.CommandText = "SELECT * FROM financeiro_parcela_pagamento WHERE financeiro_parcela_id IN (121, 122, 123);"
$r2 = $cmd.ExecuteReader()
$foundFpp = $false
while ($r2.Read()) {
    $foundFpp = $true
    Write-Host "ID: $($r2['id']) | ParcelaID: $($r2['financeiro_parcela_id']) | ValorPago: $($r2['valor_pago'])"
}
$r2.Close()
if (-not $foundFpp) {
    Write-Host "Nenhum registro em financeiro_parcela_pagamento para essas parcelas."
}

Write-Host "`n=== Venda vs Parcela vs NFe detalhado ==="
$cmd.CommandText = @"
SELECT 
    v.id AS venda_id,
    v.valor_total AS venda_valor_total,
    v.total_pagamento AS venda_total_pagamento,
    fp.id AS parcela_id,
    fp.valor_parcela,
    fp.valor_pago,
    nfe.id AS nfe_id,
    nfe.numero_nfe,
    nfe.total_nota_valor,
    nfe.recibo_situacao,
    nfe.mensagem_erro
FROM venda v
INNER JOIN nota_fiscal_eletronica nfe ON v.nfe_id = nfe.id
INNER JOIN financeiro_parcela fp ON fp.venda_id = v.id
WHERE v.id IN (57, 58, 59);
"@
$r3 = $cmd.ExecuteReader()
while ($r3.Read()) {
    Write-Host "--------------------------------------------------"
    Write-Host "Venda ID: $($r3['venda_id']) | NFe Nº: $($r3['numero_nfe']) (ID: $($r3['nfe_id']))"
    Write-Host "  Venda Valor Total: $($r3['venda_valor_total']) | Venda Total Pagamento: $($r3['venda_total_pagamento'])"
    Write-Host "  Parcela ID: $($r3['parcela_id']) | Valor Parcela: $($r3['valor_parcela']) | Valor Pago: $($r3['valor_pago'])"
    Write-Host "  NFe Total: $($r3['total_nota_valor']) | Situacao: $($r3['recibo_situacao'])"
    Write-Host "  Mensagem Erro: $($r3['mensagem_erro'])"
}
$r3.Close()

$conn.Close()
