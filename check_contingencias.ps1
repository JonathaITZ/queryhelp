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

Write-Host "--- Estrutura e dados de Contingencia ---"
$cmd = $conn.CreateCommand()
$cmd.CommandText = @"
SELECT 
    v.id AS venda_id,
    v.empresa_id,
    v.api_data_hora_venda,
    v.total_venda,
    nfe.id AS nfe_id,
    nfe.numero_nfe,
    nfe.recibo_situacao,
    nfe.mensagem_erro,
    COUNT(fp.id) AS qtd_parcelas,
    COALESCE(SUM(fp.valor_parcela), 0) AS total_parcelas,
    ROUND(v.total_venda - COALESCE(SUM(fp.valor_parcela), 0), 4) AS diferenca
FROM venda v
INNER JOIN nota_fiscal_eletronica nfe ON v.nfe_id = nfe.id
LEFT JOIN financeiro_parcela fp ON fp.venda_id = v.id AND fp.empresa_id = v.empresa_id AND (fp.deleted_at IS NULL)
WHERE nfe.recibo_situacao LIKE '%CONTING%'
GROUP BY v.id, v.empresa_id, v.api_data_hora_venda, v.total_venda, nfe.id, nfe.numero_nfe, nfe.recibo_situacao, nfe.mensagem_erro
ORDER BY v.id DESC;
"@

$reader = $cmd.ExecuteReader()
$contingencias = @()
while ($reader.Read()) {
    $row = [PSCustomObject]@{
        VendaId = $reader["venda_id"]
        EmpresaId = $reader["empresa_id"]
        DataVenda = $reader["api_data_hora_venda"]
        TotalVenda = $reader["total_venda"]
        NfeId = $reader["nfe_id"]
        NumeroNfe = $reader["numero_nfe"]
        ReciboSituacao = $reader["recibo_situacao"]
        QtdParcelas = $reader["qtd_parcelas"]
        TotalParcelas = $reader["total_parcelas"]
        Diferenca = $reader["diferenca"]
        MensagemErro = $reader["mensagem_erro"]
    }
    $contingencias += $row
}
$reader.Close()

Write-Host "Total de notas em contingência encontradas: $($contingencias.Count)"
$contingencias | Format-Table -AutoSize | Out-String | Write-Host

# Also let's check columns of financeiro_parcela
Write-Host "`n--- Colunas de financeiro_parcela ---"
$cmd2 = $conn.CreateCommand()
$cmd2.CommandText = "DESCRIBE financeiro_parcela;"
$r2 = $cmd2.ExecuteReader()
while ($r2.Read()) {
    Write-Host "$($r2['Field']) ($($r2['Type']))"
}
$r2.Close()

# Also let's check columns of venda
Write-Host "`n--- Colunas principais de venda ---"
$cmd3 = $conn.CreateCommand()
$cmd3.CommandText = "DESCRIBE venda;"
$r3 = $cmd3.ExecuteReader()
while ($r3.Read()) {
    if ($r3['Field'] -match 'total|valor|preco|desconto|acrescimo') {
        Write-Host "$($r3['Field']) ($($r3['Type']))"
    }
}
$r3.Close()

$conn.Close()
