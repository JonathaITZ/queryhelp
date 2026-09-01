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

$connStr = "Server=softcomdb-mysql-hml.cluster-cyv0220iwox9.us-east-1.rds.amazonaws.com;Port=3306;Database=softcoms_softcomshop_lanchoneteerestaurantepotira;Uid=patrick.morais;Pwd=sq6j7dDW53pm;Connection Timeout=30;SslMode=None;CharacterSet=utf8mb4;Convert Zero Datetime=True;Allow Zero Datetime=True;"
$conn = New-Object MySql.Data.MySqlClient.MySqlConnection($connStr)
$conn.Open()
Write-Host "Conectado ao banco para mapeamento completo do schema..."

$schemaDir = "C:\Users\dantas.jonatha\.gemini\antigravity\scratch\schema"
if (-not (Test-Path $schemaDir)) { New-Item -ItemType Directory -Path $schemaDir -Force | Out-Null }

# 1. Buscar todas as tabelas
Write-Host "Carregando metadados de tabelas..."
$cmdTables = $conn.CreateCommand()
$cmdTables.CommandText = "SELECT TABLE_NAME, TABLE_TYPE, ENGINE, TABLE_ROWS, DATA_LENGTH, TABLE_COMMENT FROM information_schema.TABLES WHERE TABLE_SCHEMA = 'softcoms_softcomshop_lanchoneteerestaurantepotira' ORDER BY TABLE_NAME;"

$tables = @()
$rTables = $cmdTables.ExecuteReader()
while ($rTables.Read()) {
    $tables += [PSCustomObject]@{
        Name = $rTables["TABLE_NAME"].ToString()
        Type = $rTables["TABLE_TYPE"].ToString()
        Engine = if ($rTables.IsDBNull(2)) { "" } else { $rTables["ENGINE"].ToString() }
        Rows = if ($rTables.IsDBNull(3)) { 0 } else { [int64]$rTables["TABLE_ROWS"] }
        DataLength = if ($rTables.IsDBNull(4)) { 0 } else { [int64]$rTables["DATA_LENGTH"] }
        Comment = if ($rTables.IsDBNull(5)) { "" } else { $rTables["TABLE_COMMENT"].ToString() }
        Columns = @()
    }
}
$rTables.Close()
Write-Host "Total de tabelas mapeadas: $($tables.Count)"

# 2. Buscar todas as colunas
Write-Host "Carregando metadados de colunas..."
$cmdCols = $conn.CreateCommand()
$cmdCols.CommandText = "SELECT TABLE_NAME, COLUMN_NAME, ORDINAL_POSITION, COLUMN_DEFAULT, IS_NULLABLE, DATA_TYPE, COLUMN_TYPE, COLUMN_KEY, EXTRA, COLUMN_COMMENT FROM information_schema.COLUMNS WHERE TABLE_SCHEMA = 'softcoms_softcomshop_lanchoneteerestaurantepotira' ORDER BY TABLE_NAME, ORDINAL_POSITION;"

$tableDict = @{}
foreach ($t in $tables) {
    $tableDict[$t.Name] = $t
}

$rCols = $cmdCols.ExecuteReader()
$totalCols = 0
while ($rCols.Read()) {
    $tName = $rCols["TABLE_NAME"].ToString()
    if ($tableDict.ContainsKey($tName)) {
        $colObj = [PSCustomObject]@{
            Name = $rCols["COLUMN_NAME"].ToString()
            Position = [int]$rCols["ORDINAL_POSITION"]
            Default = if ($rCols.IsDBNull(3)) { $null } else { $rCols["COLUMN_DEFAULT"].ToString() }
            Nullable = ($rCols["IS_NULLABLE"].ToString() -eq "YES")
            DataType = $rCols["DATA_TYPE"].ToString()
            FullType = $rCols["COLUMN_TYPE"].ToString()
            Key = $rCols["COLUMN_KEY"].ToString()
            Extra = $rCols["EXTRA"].ToString()
            Comment = if ($rCols.IsDBNull(9)) { "" } else { $rCols["COLUMN_COMMENT"].ToString() }
        }
        $tableDict[$tName].Columns += $colObj
        $totalCols++
    }
}
$rCols.Close()
Write-Host "Total de colunas mapeadas: $totalCols"

# 3. Buscar Chaves Estrangeiras (Foreign Keys)
Write-Host "Carregando chaves estrangeiras (Foreign Keys)..."
$cmdFk = $conn.CreateCommand()
$cmdFk.CommandText = "SELECT TABLE_NAME, COLUMN_NAME, CONSTRAINT_NAME, REFERENCED_TABLE_NAME, REFERENCED_COLUMN_NAME FROM information_schema.KEY_COLUMN_USAGE WHERE TABLE_SCHEMA = 'softcoms_softcomshop_lanchoneteerestaurantepotira' AND REFERENCED_TABLE_NAME IS NOT NULL ORDER BY TABLE_NAME, COLUMN_NAME;"

$fks = @()
$rFk = $cmdFk.ExecuteReader()
while ($rFk.Read()) {
    $fks += [PSCustomObject]@{
        Table = $rFk["TABLE_NAME"].ToString()
        Column = $rFk["COLUMN_NAME"].ToString()
        Constraint = $rFk["CONSTRAINT_NAME"].ToString()
        RefTable = $rFk["REFERENCED_TABLE_NAME"].ToString()
        RefColumn = $rFk["REFERENCED_COLUMN_NAME"].ToString()
    }
}
$rFk.Close()
Write-Host "Total de FKs mapeadas: $($fks.Count)"

$conn.Close()

# 4. Salvar JSON Estruturado
$jsonFile = "$schemaDir\schema.json"
$schemaData = [PSCustomObject]@{
    Database = "softcoms_softcomshop_lanchoneteerestaurantepotira"
    Host = "softcomdb-mysql-hml.cluster-cyv0220iwox9.us-east-1.rds.amazonaws.com"
    MappedAt = (Get-Date -Format "yyyy-MM-dd HH:mm:ss")
    TotalTables = $tables.Count
    TotalColumns = $totalCols
    TotalForeignKeys = $fks.Count
    Tables = $tables
    ForeignKeys = $fks
}
$jsonContent = $schemaData | ConvertTo-Json -Depth 5
[System.IO.File]::WriteAllText($jsonFile, $jsonContent, [System.Text.Encoding]::UTF8)
Write-Host "Schema JSON salvo com sucesso em: $jsonFile"

# 5. Salvar Markdown com Indice Rapido de Tabelas e Colunas
$mdFile = "$schemaDir\schema_quick_reference.md"
$sb = New-Object System.Text.StringBuilder
[void]$sb.AppendLine("# Mapeamento Completo do Banco de Dados: softcoms_softcomshop_lanchoneteerestaurantepotira")
[void]$sb.AppendLine("**Gerado em:** $(Get-Date -Format 'yyyy-MM-dd HH:mm:ss') | **Tabelas:** $($tables.Count) | **Colunas:** $totalCols | **FKs:** $($fks.Count)")
[void]$sb.AppendLine()
[void]$sb.AppendLine("## Indice de Tabelas")
[void]$sb.AppendLine("| Tabela | Tipo | Registros Aprox. | Colunas | Chave Primaria |")
[void]$sb.AppendLine("| :--- | :--- | :--- | :--- | :--- |")

foreach ($t in $tables) {
    $pkList = @()
    foreach ($c in $t.Columns) {
        if ($c.Key -eq "PRI") { $pkList += $c.Name }
    }
    $pk = $pkList -join ", "
    if (-not $pk) { $pk = "-" }
    [void]$sb.AppendLine("| $($t.Name) | $($t.Type) | $($t.Rows) | $($t.Columns.Count) | $pk |")
}

[void]$sb.AppendLine()
[void]$sb.AppendLine("---")
[void]$sb.AppendLine("## Estrutura Detalhada das Tabelas")
[void]$sb.AppendLine()

foreach ($t in $tables) {
    [void]$sb.AppendLine("### Tabela: $($t.Name) ($($t.Type))")
    if ($t.Comment) { [void]$sb.AppendLine("**Comentario:** $($t.Comment)") }
    [void]$sb.AppendLine("**Linhas aprox:** $($t.Rows) | **Colunas:** $($t.Columns.Count)")
    [void]$sb.AppendLine()
    [void]$sb.AppendLine("| # | Coluna | Tipo | Nulo | Chave | Padrao | Extra |")
    [void]$sb.AppendLine("| :--- | :--- | :--- | :---: | :---: | :--- | :--- |")
    foreach ($c in $t.Columns) {
        $nullStr = if ($c.Nullable) { "SIM" } else { "NAO" }
        $keyStr = if ($c.Key) { $c.Key } else { "-" }
        $defStr = if ($null -ne $c.Default) { $c.Default } else { "NULL" }
        $extraStr = if ($c.Extra) { $c.Extra } else { "-" }
        [void]$sb.AppendLine("| $($c.Position) | $($c.Name) | $($c.FullType) | $nullStr | $keyStr | $defStr | $extraStr |")
    }
    [void]$sb.AppendLine()
}

[System.IO.File]::WriteAllText($mdFile, $sb.ToString(), [System.Text.Encoding]::UTF8)
Write-Host "Schema Markdown salvo com sucesso em: $mdFile"
